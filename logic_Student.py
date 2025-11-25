import globals
import mysql.connector
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox,QWidget, QVBoxLayout, QLabel,QHBoxLayout,QScrollArea
from functools import partial
from PySide6.QtCore import Qt
# SISWA

def get_ui():
    if globals.ui is None:
        raise Exception("UI belum diinisialisasi!")
    return globals.ui


#Mengedit data siswa
def editDetailData(id_student, nama_lama, email_lama, username_lama, password_lama):
    ui = get_ui()
    conn = globals.get_conn()
    cursor = conn.cursor()
    window = globals.get_main_window()

    # Ambil data hasil edit dari form
    nama_baru = ui.lineEdit_NamaLengkap_2.text()
    email_baru = ui.lineEdit_Email_2.text()
    username_baru = ui.lineEdit_Username_2.text()
    password_baru = ui.lineEdit_Password_2.text()

    if (
        nama_baru == nama_lama and
        email_baru == email_lama and
        username_baru == username_lama and
        password_baru == password_lama
    ):
        QMessageBox.information(window, "Info", "Data tidak ada yang berubah.")
        return

    # kalau salah satu dari field kosong tidak boleh
    if not nama_baru or not email_baru or not username_baru or not password_baru:
        QMessageBox.warning(window, "Gagal", "Semua field harus diisi.")
        return

    if id_student is None:
        QMessageBox.warning(window, "Gagal", "ID siswa tidak ditemukan.")
        return

    # Update ke database
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE student SET nama=%s, email=%s, username=%s, password=%s WHERE id_Student=%s
    """, (id_student,nama_baru, email_baru, username_baru, password_baru))
    conn.commit()
    cursor.close()

    #Perbarui data lama

    nama_lama = nama_baru
    email_lama = email_baru
    username_lama = username_baru
    password_lama = password_baru


    QMessageBox.information(window, "Berhasil", "Data siswa berhasil diperbarui.")

    # Kembali ke halaman daftar siswa (opsional)
    ui.stackedWidget_Sidebar.setCurrentWidget(ui.page_Sidebar_Student)
    loadListStudent()  # Refresh daftar

# yang bagian ini ada masalah
# ui
#Admin bisa menambahkan Student
def pindahHalamanStudent():
    ui = get_ui()

    ui.stackedWidget_Main.setCurrentWidget(ui.page_Main_Student)
    ui.lineEdit_NamaLengkap_2.clear()
    ui.lineEdit_Email_2.clear()
    ui.lineEdit_Username_2.clear()
    ui.lineEdit_Password_2.clear()
    ui.btnSimpan_Student.clicked.disconnect()
    ui.btnSimpan_Student.clicked.connect(tambahDataStudent)

# yang bagian ini ada masalah
# QMessageBox
# Database Mysql
# ui
def tambahDataStudent():
    ui = get_ui()
    conn = globals.get_conn()
    cursor = conn.cursor()
    window = globals.get_main_window()

    fields = {
        "nama": ui.lineEdit_NamaLengkap_2,
        "email": ui.lineEdit_Email_2,
        "username": ui.lineEdit_Username_2,
        "password": ui.lineEdit_Password_2
    }

    for label, field in fields.items():
        if not field.text().strip():
            QMessageBox.warning(window, "Input Kosong", f"{label} belum diisi.")
            return


        # Ambil nilai dari QLineEdit
    nama = ui.lineEdit_NamaLengkap_2.text()
    email = ui.lineEdit_Email_2.text()
    username = ui.lineEdit_Username_2.text()
    password = ui.lineEdit_Password_2.text()

    try:
        query = "INSERT INTO student (nama, email, username, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nama, email, username, password,))
        conn.commit()
        cursor.close()

        QMessageBox.information(window, "Berhasil", "Data siswa berhasil ditambahkan.")
        # Membersihkan halaman
        ui.lineEdit_NamaLengkap_2.clear()
        ui.lineEdit_Email_2.clear()
        ui.lineEdit_Username_2.clear()
        ui.lineEdit_Password_2.clear()
        loadListStudent()

    except mysql.connector.Error as err:
        QMessageBox.critical(window, "Gagal", f"Gagal menyimpan data:\n{err}")
# yang bagian ini ada masalah
# QMessageBox
# Database Mysql
def onDeleteStudent(id_Student,nama):
    conn = globals.get_conn()
    window = globals.get_main_window()
    # Konfirmasi dulu sebelum menghapus
    reply = QMessageBox.question(
        window,
        "Konfirmasi Hapus",
        f"Yakin ingin menghapus'{nama}'?",
        QMessageBox.Yes | QMessageBox.No
    )

    if reply == QMessageBox.Yes:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM student WHERE id_Student = %s"
            cursor.execute(query, (id_Student,))
            conn.commit()
            print(f"Data student dengan ID {id_Student} berhasil dihapus.")
            loadListStudent()
        except Exception as e:
            print(f"Terjadi error saat menghapus: {e}")
        finally:
            # Tutup koneksi
            if cursor:
                cursor.close()
# yang bagian ini ada masalah
# Database Mysql
# ui
#Membuka detail siswa dan bisa langsung diedit
def bukaDetailSiswa(id):
    ui = get_ui()
    conn = globals.get_conn()
    cursor = conn.cursor()
    window = globals.get_main_window()
    # dictionary=True  supaya bisa menampilakan data berdasarkan nama field
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student WHERE id_Student = %s", (id,))
    data = cursor.fetchone()
    cursor.close()

    if data:
        # untuk menampilkan data dari database berdasarkan nama fieldnya
        ui.lineEdit_NamaLengkap_2.setText(data["nama"])
        ui.lineEdit_Email_2.setText(data["email"])
        ui.lineEdit_Username_2.setText(data["username"])
        ui.lineEdit_Password_2.setText(data["password"])

        #Menyimpan data lama
        id_Student = data["id_Student"]
        nama_lama = data["nama"]
        email_lama = data["email"]
        username_lama = data["username"]
        password_lama = data["password"]
        #Edit Student


        try:
            ui.btnSimpan_Student.clicked.disconnect()
        except TypeError:
            pass  # Tidak ada koneksi sebelumnya, aman diabaikan
        ui.btnSimpan_Student.clicked.connect(partial(editDetailData, id, nama_lama, email_lama, username_lama, password_lama))

        # Pindah ke halaman detail siswa
        ui.stackedWidget_Main.setCurrentWidget(ui.page_Main_Student)

# yang bagian ini ada masalah
# QMessageBox
# Database Mysql
#Menampilkan keseluruhan siswa beserta datanya
def loadListStudent():
    ui = get_ui()
    conn = globals.get_conn()
    cursor = conn.cursor()
    window = globals.get_main_window()

    layout = ui.verticalLayout_Main_Student

    for i in reversed(range(layout.count())):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.setParent(None)

    #Ambil data
    cursor.execute("SELECT * FROM student ")
    hasil = cursor.fetchall()
    cursor.close()

    header_layout = QHBoxLayout()
    header_widget = QWidget()
    header_widget.setLayout(header_layout)

    # Buat label header dengan gaya yang sama
    label_nomor = QLabel("No")
    label_nomor.setFixedSize(40, 40)
    label_nama = QLabel("Nama")
    label_username = QLabel("Username")
    label_email = QLabel("Email")
    label_password = QLabel("Password")
    label_action = QLabel("Action")
    label_action.setFixedSize(90, 40)

    for label in [label_nomor, label_nama, label_username, label_email, label_password,label_action]:
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("""
            QLabel{
                background-color:rgb(19, 76, 53);
                border-radius:3px;
                color :white;
                font-weight:bold;
                font-size:13px;
                padding: 5px;
                border: 2px solid gray;
            }
        """)
        header_layout.addWidget(label)

    # Tambahkan ke layout utama
    layout.addWidget(header_widget)
    layout.setAlignment(Qt.AlignTop)


    nomor_u = 1
    for row in hasil:

        coll_layout = QHBoxLayout()
        coll_widget = QWidget()
        coll_widget.setLayout(coll_layout)

        id_Student= row[0]
        nama = row[1]
        username = row[2]
        email = row [3]
        password = row [4]


        nomor = QLabel(str(nomor_u))
        nomor.setFixedSize(40, 40)
        nomor.setStyleSheet("""
        QLabel{
                background-color:rgb(19, 46, 53);
                border-radius:3px;
                color :White;
                font-weight:bold;
                font-size:13px;
                padding: 10px;
                border: 2px solid Gray;

        }
        """)

        nama_student = QLabel(nama)
        nama_student.setStyleSheet("""
        QLabel{
                background-color:rgb(19, 46, 53);
                border-radius:3px;
                color :White;
                font-weight:bold;
                font-size:13px;
                padding: 10px;
                border: 2px solid Gray;

        }
        """)

        username_student = QLabel(username)
        username_student.setStyleSheet("""
        QLabel{
                background-color:rgb(19, 46, 53);
                border-radius:3px;
                color :White;
                font-weight:bold;
                font-size:13px;
                padding: 10px;
                border: 2px solid Gray;

        }
        """)

        email_student = QLabel(email)
        email_student.setStyleSheet("""
        QLabel{
                background-color:rgb(19, 46, 53);
                border-radius:3px;
                color :White;
                font-weight:bold;
                font-size:13px;
                padding: 10px;
                border: 2px solid Gray;

        }
        """)

        password_student = QLabel(password)
        password_student.setStyleSheet("""
        QLabel{
                background-color:rgb(19, 46, 53);
                border-radius:3px;
                color :White;
                font-weight:bold;
                font-size:13px;
                padding: 10px;
                border: 2px solid Gray;

        }
        """)

        # Tombol edit
        btn_edit= QPushButton("📝")
        btn_edit.setFixedSize(40, 40)
        btn_edit.setStyleSheet("""
            QPushButton{
                background-color:green;
                border-radius:3px;
                color :White;
                font-weight:bold;
                font-size:13px;
                border: 2px solid Gray;
            }
            QPushButton:hover{
                background-color:yellow;
                border-color: rgb(76, 255, 228);
                font-size:18px;
            }

        """)
        btn_edit.clicked.connect(partial(bukaDetailSiswa,id_Student))

        # Tombol delete
        btn_delete = QPushButton("🗑️")
        btn_delete.setFixedSize(40, 40)
        btn_delete.setStyleSheet("""
            QPushButton{
                background-color:rgb(150, 0, 0);
                border-radius:3px;
                color :White;
                font-weight:bold;
                font-size:13px;
                border: 2px solid Gray;
            }
            QPushButton:hover{
                background-color:rgb(200, 0, 0);
                border-color: rgb(76, 255, 228);
                font-size:18px;
            }

        """)
        btn_delete.clicked.connect(partial(onDeleteStudent, id_Student, nama))

        coll_layout.addWidget(nomor)
        coll_layout.addWidget(nama_student)
        coll_layout.addWidget(username_student)
        coll_layout.addWidget(email_student)
        coll_layout.addWidget(password_student)
        coll_layout.addWidget(btn_edit)
        coll_layout.addWidget(btn_delete)

        layout.addWidget(coll_widget)
        layout.setAlignment(Qt.AlignTop)

        nomor_u += 1
    print(hasil)
    print(type(hasil))    
    return hasil
