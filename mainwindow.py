# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form_Admin.ui -o ui_form_Admin.py, or
#     pyside2-uic form.ui -o ui_form.py
# This Python file uses the following encoding: utf-8
import sys
import os
import mysql.connector
import globals
import pandas as pd


from path_manager import get_folder_catatan
from DB_Connection import get_mysql_connection,get_mongo_collections
from logic_Login import loginUser
from logic_Register import simpanData
from logic_Materi import loadlistMateri,inputDataMateri
from logic_Catatan import loadListCatatan,TambahCatatan,onSimpanCatatanBaru
from logic_Student import pindahHalamanStudent,loadListStudent
from globals import ui
from ui_form_Admin import Ui_MainWindow

from datetime import datetime
from functools import  partial
from PySide6.QtWidgets import QFileDialog,QApplication, QMainWindow, QPushButton, QMessageBox,QWidget, QVBoxLayout, QLabel,QHBoxLayout,QLineEdit,QButtonGroup,QComboBox,QRadioButton
from PySide6.QtCore import Qt
from pymongo import MongoClient


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_instance = Ui_MainWindow()
        ui_instance.setupUi(self)
        globals.set_main_window(self)

        self.ui = ui_instance
        globals.ui = ui_instance

        self.folder_catatan = get_folder_catatan()

        # Koneksi MySQL
        self.conn = get_mysql_connection()
        globals.set_conn(self.conn)
        # Koneksi MongoDB
        mongo = get_mongo_collections()
        self.koleksi_Materi = mongo["materi"]
        self.koleksi_Soal = mongo["soal"]

        self.DropdownFolder()

        # Halaman yang pertama kali dibuka pertama
        self.ui.stackedWidget_Utama.setCurrentWidget(self.ui.page_Login)

        # Membuka Halaman
        self.ui.btnBeranda.clicked.connect(partial(self.bukaPage,"Beranda"))
        self.ui.btnMateri.clicked.connect(self.aksiPageMateri)
        self.ui.btnCatatan.clicked.connect(self.aksiPageCatatan)
        self.ui.btnStudent.clicked.connect(self.aksiPageStudent)
        self.ui.btnQuis.clicked.connect(self.aksiPageQuis)

        # Membuka Halaman input_pages
        self.ui.btnTambah_Materi.clicked.connect(partial(self.bukaPageInputMateri))
        self.ui.btnTambah_Catatan.clicked.connect(partial(TambahCatatan,self))
        self.ui.btnTambah_Quis.clicked.connect(partial(self.TambahSoal))
        #Input jumlah soal
        self.ui.btn_JumlahSoal.clicked.connect(partial(self.JumlahSoal))
        #Simpan semua soal
        self.ui.btn_SimpanSoal.clicked.connect(partial(self.simpanSemuaSoal))
        #Input catatan
        self.ui.btn_Simpan_Catatan_dan_edit.clicked.connect(partial(onSimpanCatatanBaru,self))

        #Input data Materi
        self.ui.btnSimpan_Materi.clicked.connect(partial(inputDataMateri, self.ui, self.koleksi_Materi))

        #Pindahan ke halaman daftar
        self.ui.btnDaftar.clicked.connect(self.bukaPageDaftar)

        #kembali kehalaman login
        self.ui.btnKembali.clicked.connect(self.kembaliPageLogin)

        #Input ke database
        self.ui.btnRegister.clicked.connect(partial(simpanData, self.ui, self.conn))

        #Login
        self.ui.btnLogin.clicked.connect(partial(loginUser,self, self.ui, self.conn))

        #Logout
        self.ui.btnLogout.clicked.connect(self.Logout)

        # Edit Student
        # self.ui.btnSimpan_Student.clicked.connect(editDetailDataMain)

        #Tambah Student
        self.ui.btnTambah_Student.clicked.connect(pindahHalamanStudent)

        # Ekspor Student
        self.ui.btnEkspor_Student.clicked.connect(partial(self.export_students_to_excel))

# BAGIAN METHOD UNTUK MENGGABUNGKAN METHOD


    #Menggabungkan 2 method


    def aksiPageMateri(self):
        self.bukaPage("Materi")
        loadlistMateri(self,self.ui,self.koleksi_Materi)

    def aksiPageCatatan(self):
        self.bukaPage("Catatan")
        loadListCatatan(self)

    def aksiPageStudent(self):
        self.bukaPage("Student")
        loadListStudent()

    def aksiPageQuis(self):
        self.bukaPage("Quis")
        self.loadListQuis()

#BAGIAN METHOD DENGAN FUNGSI MASING-MASING

    def Logout(self):
        asking = QMessageBox.question(
            self,
            "Konfirmasi",
            "Anda yakin ingin logout?",
            QMessageBox.Yes | QMessageBox.No
        )
        if asking == QMessageBox.Yes:
            self.ui.stackedWidget_Utama.setCurrentWidget(self.ui.page_Login)
            self.ui.lineEdit_LoginPassword.clear()
            self.ui.lineEdit_LoginUsername.clear()
    #KEMBALI KEHALAMAN LOGIN
    def kembaliPageLogin(self):
        self.ui.stackedWidget_Utama.setCurrentWidget(self.ui.page_Login)



#MAIN



    #Membuka Halaman
    def bukaPage(self,nama_halaman):
        sidebar_pages = {
            "Beranda": self.ui.page_Sidebar_Beranda,
            "Materi": self.ui.page_Sidebar_Materi,
            "Catatan": self.ui.page_Sidebar_Catatan,
            "Student": self.ui.page_Sidebar_Student,
            "Quis": self.ui.page_Sidebar_Quis
        }

        main_pages = {
            "Beranda": self.ui.page_Main_Beranda,
            "Materi": self.ui.page_Main_Materi,
            "Catatan": self.ui.page_Main_Catatan,
            # "Student": self.ui.page_Main_Student
            "Student": self.ui.page_Main_Student_2,
            "Quis": self.ui.page_Main_Quis
        }

        if nama_halaman in ["Beranda","Student"]:
            self.ui.stackedWidget_Sidebar.hide()
        else:
            self.ui.stackedWidget_Sidebar.show()

        self.ui.stackedWidget_Main.setCurrentWidget(main_pages.get(nama_halaman))
        self.ui.stackedWidget_Sidebar.setCurrentWidget(sidebar_pages.get(nama_halaman))


    #PINDAH KE HALAMAN MAIN
    def bukaPageDaftar(self):
        self.ui.stackedWidget_Utama.setCurrentWidget(self.ui.page_Daftar)


        #Untuk menyediakan opsi folder yang sudah tersedia
    def DropdownFolder(self):
        data_materi = self.koleksi_Materi.find({}, {"folder": 1, "_id": 0})
        judul_list = list({item["folder"] for item in data_materi})
        self.ui.comboBox_folder_Materi.clear()
        self.ui.comboBox_folder_Materi.addItems(judul_list)
        self.ui.comboBox_Nama_KategoriSoal.clear()
        self.ui.comboBox_Nama_KategoriSoal.addItems(judul_list)

    #Membuka Halaman Input
    def bukaPageInputMateri(self):
        self.ui.stackedWidget_Main.setCurrentWidget(self.ui.page_Main_Input_Materi)
        self.ui.comboBox_folder_Materi.setCurrentText("")
        self.ui.lineEdit_Judul.clear()
        self.ui.textEdit_Materi.clear()
        self.ui.textEdit_Contoh.clear()
        self.ui.textEdit_Peringatan.clear()
        try:
            self.ui.btnSimpan_Materi.clicked.disconnect()
        except Exception:
            pass  # atau log: print("Belum ada koneksi sebelumnya")
        self.ui.btnSimpan_Materi.setText("Simpan")
        self.ui.btnSimpan_Materi.clicked.connect(partial(inputDataMateri,self,self.ui,self.koleksi_Materi))



    #EKSPOR
    def export_students_to_excel(self):
        # ambil data dari DB
        hasil = loadListStudent()  

        if not hasil:
            QMessageBox.warning(self, "Gagal", "Tidak ada data untuk diekspor")
            return

        # buka dialog simpan file
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Simpan Data Siswa",
            "students.xlsx",                 # default nama file
            "Excel Files (*.xlsx)"           # filter hanya file Excel
        )

        if filename:  # kalau user tidak cancel
            df = pd.DataFrame(hasil, columns=["ID", "Nama", "Username", "Email", "Password"])
            df.to_excel(filename, index=False)
            QMessageBox.information(self, "Sukses", f"Data berhasil diekspor ke {filename}")





#Quis

    # meload nama kategori soal
    def loadListQuis(self):
        # Tempat untuk menampilkan list
        layout = self.ui.verticalLayout_Sidebar_Quis  # pastikan ini adalah layout yang terpasang di scrollAreaWidget_FolderMateri
    
        #untuk membersihkan widget yang ada lebih dahulu
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # ambil semua nama Soal
        soal_list = self.koleksi_Soal.distinct("Kategori")

        # loop dan tambahkan button
        for kategori_name in soal_list :
            row_layout = QHBoxLayout()
            row_widget = QWidget()
            row_widget.setLayout(row_layout)

                # Tombol folder
            btn_soal = QPushButton(kategori_name)
            btn_soal.setStyleSheet("""
                QPushButton{
                    background-color:rgb(19, 46, 53);
                    border-radius:3px;
                    color :White;
                    font-weight:bold;
                    font-size:13px;
                    padding: 10px;
                    border: 2px solid Gray;
                }
                QPushButton:hover{
                    background-color:#0D1F23;
                    border-color: rgb(76, 255, 228);
                    font-size:18px;
                }
            """)
            btn_soal.clicked.connect(partial(self.loadSoalButtons, kategori_name))

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
            btn_delete.clicked.connect(partial(self.onDeleteKategori, kategori_name))
            # Tambahkan ke layout baris
            row_layout.addWidget(btn_soal)
            row_layout.addWidget(btn_delete)

            # Tambahkan ke layout utama
            layout.addWidget(row_widget)
            layout.setAlignment(Qt.AlignTop)



    
    #Berpindah Halaman
    def TambahSoal(self):
        self.ui.stackedWidget_Main.setCurrentWidget(self.ui.page_Main_Input_Quis)
        self.ui.comboBox_Nama_KategoriSoal.setCurrentText("")
        self.ui.lineEdit_Nama_Soal.clear()
        self.ui.lineEdit_JumlahSoal.clear()
        layout = self.ui.verticalLayout_Quis
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        self.ui.btn_SimpanSoal.setText("Simpan Soal")
        try:
            self.ui.btn_SimpanSoal.clicked.disconnect()
        except TypeError:
            pass  # Jika belum ada koneksi, abaikan error
        self.ui.btn_SimpanSoal.clicked.connect(partial(self.simpanSemuaSoal))


    # merefresh bagian kategori 
    def refrashSoal(self):
        self.ui.comboBox_Nama_KategoriSoal.clear()
        self.ui.lineEdit_Nama_Soal.clear()
        layout = self.ui.verticalLayout_Quis
        
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    # meload nama_soal
    def loadSoalButtons(self,kategori):
        self.ui.stackedWidget_Main.setCurrentWidget(self.ui.page_Main_Quis)
        layout = self.ui.verticalLayout_Soal_Quis

        # Bersihkan dulu kalau ada button lama
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Ambil semua dokumen dari folder tertentu
        hasil = self.koleksi_Soal.find({"Kategori": kategori})
        # Ambil semua judul unik dari hasil tersebut
        judul_set = []
        # mengambil dari dari variabel hasil 
        for data in hasil:
            kategoris = data.get("Kategori")
            soal = data.get("Nama_Soal")
            # validasi data untuk memfilter data
            if soal and soal not in judul_set:
                judul_set.append(soal)


        # Loop dan tambahkan button
        for soal in judul_set:

            row_layout = QHBoxLayout()
            row_widget = QWidget()
            row_widget.setLayout(row_layout)

            # Tombol kategori
            btn_judul = QPushButton(soal)
            btn_judul.setStyleSheet("""
            QPushButton{
                background-color:#4e6a62;
                border-radius:3px;
                color :White;
                font-weight:bold;
                font-size:13px;
                padding: 10px;
                border: 2px solid Gray;
            }
            QPushButton:hover{
                background-color:#0D1F23;
                border-color: rgb(76, 255, 228);
                font-size:18px;
            }
            """)

            btn_judul.clicked.connect(partial(self.onListSoalClicked, soal))
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
            btn_delete.clicked.connect(partial(self.onDeleteSoal, soal))

            # Tombol edit
            btn_edit = QPushButton("📝")
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
            btn_edit.clicked.connect(partial(self.onEditJudul,soal, kategoris))

            # Tambahkan ke layout baris
            row_layout.addWidget(btn_judul)
            row_layout.addWidget(btn_edit)
            row_layout.addWidget(btn_delete)

            layout.addWidget(row_widget)
            layout.setAlignment(Qt.AlignTop)
    # mehtod delete 
    def onDeleteSoal(self, nama_soal):
        reply = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus soal '{nama_soal}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            print(f"Menghapus soal: {nama_soal}")
            self.koleksi_Soal.delete_many({"Nama_Soal": nama_soal})
            self.loadListQuis()
    
    def onDeleteKategori(self, kategori):
        reply = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus kategori soal '{kategori}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            print(f"Menghapus kategori soal: {kategori}")
            self.koleksi_Soal.delete_many({"Kategori": kategori})
            self.loadListQuis()

    def onListSoalClicked(self, soal_name):
        self.ui.stackedWidget_Main.setCurrentWidget(self.ui.page_Main_Quis)
    
        layout = self.ui.verticalLayout_Tanya_Jawab
        # method refresh yang yang menghapus sampai kebagian layoutnya
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                child_layout = item.layout()
                if child_layout:
                    while child_layout.count():
                        sub_item = child_layout.takeAt(0)
                        sub_widget = sub_item.widget()
                        if sub_widget:
                            sub_widget.deleteLater()
                    child_layout.deleteLater()
        hasil = self.koleksi_Soal.find_one({"Nama_Soal": soal_name})
        if not hasil:
            QMessageBox.warning(self, "Tidak Ditemukan", f"Soal '{soal_name}' tidak ditemukan.")
            return
    
        soal_dict = hasil.get("soal", {})
        self.radio_group_list = []  # Simpan semua grup radio untuk evaluasi nanti
        
        no = 1

        for key in sorted(soal_dict.keys()):
            data = soal_dict[key]
            pertanyaan = data["pertanyaan"]
            jawaban_dict = data["jawaban"]
    
            # Label pertanyaan
            label = QLabel(f"{no}. {pertanyaan}")
            label.setWordWrap(True)
            label.setMaximumSize(213123,40)
            label.setStyleSheet("""
            background-color:#202f2f;
            padding:10px;
            font-size:16px;
            font-weight:bold;
            border-radius:4px;
            """)
            layout.addWidget(label)
    
            # Group radio button
            group = QButtonGroup(self)
            opsi_layout = QVBoxLayout()
    
            for opsi in ["A", "B", "C", "D"]:
                radio = QRadioButton(f"{opsi}. {jawaban_dict[opsi]}")
                radio.setStyleSheet("""
                QRadioButton {
                    font-size: 14px;
                    color: white;
                    padding: 5px;
                }
                QRadioButton::indicator {
                    width: 18px;
                    height: 18px;
                    border-radius: 10px;
                    border: 2px solid #999;
                
                }
                QRadioButton::indicator:checked {
                    background-color:rgb(76, 255, 228) ;
                    border: 2px solid #2e8b57;
                }
                QRadioButton::indicator:hover {
                    border: 2px solid #76eec6;
                    background-color:rgb(76, 255, 25) ;
                }
                """)
                group.addButton(radio)
                group.setId(radio, ord(opsi))  # Simpan ID berdasarkan huruf
                opsi_layout.addWidget(radio)
    
            layout.addLayout(opsi_layout)
            self.radio_group_list.append((key, group))  # Simpan dengan key soal

            no += 1 
        btn_simpan = QPushButton("Simpan Jawaban")
        btn_simpan.setFixedHeight(40)
        btn_simpan.setStyleSheet("""
        QPushButton{
            background-color:rgb(19, 46, 53);
            border-radius:6px;
            color :white;
            padding:2px;
            font-weight:bold;
            font-size:17px;
        }
        QPushButton:hover{
            background-color:#0D1F23;
        }
        """)
        btn_simpan.clicked.connect(self.cekJawaban)  # Ganti dengan nama fungsi kamu
        layout.addStretch()
        layout.addWidget(btn_simpan)
    
    #membuat tempat input untuk soal
    def JumlahSoal(self):
        self.soal_list = []

        # tempat widgetnya diletakkan
        layout = self.ui.verticalLayout_Quis
        
        #mengambil input
        text = self.ui.lineEdit_JumlahSoal.text()
        
        # pengecekkan nilai 
        if not text.isdigit():
            QMessageBox.warning(self, "Input Salah", "Masukkan jumlah soal yang valid.")
            return
        
        jumlah_soal = int(text)

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()



        for i in range(1, jumlah_soal + 1):

            # Buat widget container untuk baris ini
            baris = QWidget()
            layout_baris = QVBoxLayout()
            layout_baris.setContentsMargins(0, 0, 0, 0)

            # Buat label dengan style
            label_Pertanyaan = QLabel(f"Soal {i}")
            label_Pertanyaan.setStyleSheet("""
                QLabel {
                        background-color: rgba(0,0,0,0);
                        color:white;
                    border-radius: 15px;
                        font-weight:bold;
                        font-size:20px;
                }
            """)

            # Buat input
            input_Pertanyaan = QLineEdit()
            input_Pertanyaan.setPlaceholderText("isi soal ....")
            input_Pertanyaan.setStyleSheet("""
                QLineEdit{
                        background-color:#06141D;
                    font-size: 25px;
                        border-radius: 10px;
                        color:white;
                        Padding:10px;
                }
                QLineEdit:focus{
                    border: 2px solid rgb(25, 201, 255);
                    background-color: #253745;
                }
            """)

            # Tambahkan ke layout vertical
            layout_baris.addWidget(label_Pertanyaan)
            layout_baris.addWidget(input_Pertanyaan)

            # Buat label dengan style
            label_Jawaban = QLabel(f"Kunci Soal {i}")
            label_Jawaban.setStyleSheet("""
                QLabel {
                        background-color: rgba(0,0,0,0);
                        color:white;
                    border-radius: 15px;
                        font-weight:bold;
                        font-size:20px;
                }
            """)

            combo_Jawaban = QComboBox()
            combo_Jawaban.addItems(["A", "B", "C", "D"])
            combo_Jawaban.setEditable(False)  # Non-editable, hanya bisa pilih dari daftar
            combo_Jawaban.setStyleSheet("""
                QComboBox {
                    background-color: #06141D;
                    font-size: 25px;
                    border-radius: 10px;
                    color: white;
                    padding: 10px;
                }
                QComboBox::drop-down {
                    border: none;
                }
                QComboBox::down-arrow {
                    image: url(:/icons/down-arrow.png);  /* opsional jika kamu punya ikon */
                }
                QComboBox QAbstractItemView {
                    background-color: #253745;
                    selection-background-color: rgb(76, 255, 228);
                    color: white;
                }
            """)



            # Tambahkan ke layout vertical
            layout_baris.addWidget(label_Jawaban)
            layout_baris.addWidget(combo_Jawaban)


            # Layout vertical untuk opsi jawaban
            opsi_pilhanGanda_layout = QVBoxLayout()
            opsi_pilhanGanda_layout.setSpacing(10)
            
            input_opsi_dict = {}
            # Tambahkan input A, B, C, D,Jawaban Benar
            for opsi in ["A", "B", "C", "D"]:
                container_opsi = QWidget()
                layout_opsi = QVBoxLayout(container_opsi)
                layout_opsi.setContentsMargins(0, 0, 0, 0)

                label_opsi = QLabel(f"Jawaban {opsi}")
                label_opsi.setStyleSheet("""
                    QLabel {
                        color: white;
                        font-weight: bold;
                        font-size: 16px;
                    }
                """)

                input_opsi = QLineEdit()
                input_opsi.setPlaceholderText(f"Isi jawaban {opsi}")
                input_opsi.setStyleSheet("""
                    QLineEdit {
                        background-color: #06141D;
                        font-size: 18px;
                        border-radius: 8px;
                        color: white;
                        padding: 8px;
                    }
                    QLineEdit:focus {
                        border: 2px solid rgb(25, 201, 255);
                        background-color: #253745;
                    }
                """)
                

                input_opsi_dict[opsi] = input_opsi
                layout_opsi.addWidget(label_opsi)
                layout_opsi.addWidget(input_opsi)
                opsi_pilhanGanda_layout.addWidget(container_opsi)

            # memasukkan data soal dan opsi ke dalam list
            self.soal_list.append({
            "pertanyaan": input_Pertanyaan,
            "opsi": input_opsi_dict,
            "jawaban_benar": combo_Jawaban
            })

            # Tambahkan layout opsi ke layout utama
            layout_baris.addLayout(opsi_pilhanGanda_layout)
            baris.setLayout(layout_baris)
            layout.addWidget(baris)

    def cekJawaban(self):
        total_soal = len(self.radio_group_list)
        benar = 0
        jawaban_user = {}

        for key, group in self.radio_group_list:
            selected_id = group.checkedId()
            huruf = chr(selected_id) if selected_id != -1 else "-"
            jawaban_user[key] = huruf

            # Ambil jawaban benar dari database
            dokumen = self.koleksi_Soal.find_one({f"soal.{key}": {"$exists": True}})
            if dokumen:
                jawaban_benar = dokumen["soal"][key]["jawaban_benar"]
                if huruf == jawaban_benar:
                    benar += 1

        # Hitung skor 0–100
        skor = round((benar / total_soal) * 100)

        # Tampilkan hasil
        QMessageBox.information(self, "Hasil", f"Skor kamu: {skor} dari 100\nBenar: {benar} dari {total_soal}")

    # menyimpan semua soal ke database
    def simpanSemuaSoal(self):
        
        # mengambil koleksinya
        koleksi = self.koleksi_Soal
        kategori = self.ui.comboBox_Nama_KategoriSoal.currentText().strip()
        nama_soal = self.ui.lineEdit_Nama_Soal.text().strip()
        
        semua_soal = {} #tempat penampungan semua soal

        # validasi apakah nilainya ada 
        if not nama_soal.strip() or not kategori.strip():
            QMessageBox.warning(self, "Gagal", "Nama soal dan kategori harus diisi.")
            return
        # validasi apakah datanya sudah ada di database
        if koleksi.find_one({"Nama_Soal": nama_soal, "Kategori": kategori}):
            QMessageBox.warning(self, "Gagal", "Soal dengan nama dan kategori ini sudah ada.")
            return
        # Loop semua soal
        try:
            for index, soal in enumerate(self.soal_list, start=1):
                pertanyaan = soal["pertanyaan"].text()
                jawaban_benar = soal["jawaban_benar"].currentText().strip()
                opsi_dict = {}

                for opsi, widget in soal["opsi"].items():
                    isi_jawaban = widget.text().strip()
                    opsi_dict[opsi] = isi_jawaban
                # Validasi minimal
                if (
                    not pertanyaan
                    or jawaban_benar not in opsi_dict
                    or len(opsi_dict) < 4 or any(not v for v in opsi_dict.values())
                ):
                    continue
                
                # Tambahkan ke semua_soal dengan key dinamis
                semua_soal[f"pertanyaan_{index}"] = {
                    "pertanyaan": pertanyaan,
                    "jawaban": opsi_dict,
                    "jawaban_benar": jawaban_benar
                }

            # Buat dokumen soal
            if semua_soal:
                dokumen = {
                    "Kategori": kategori,
                    "Nama_Soal": nama_soal,
                    "jumlah_soal": len(semua_soal),
                    "soal": semua_soal
                }
                if len(semua_soal) < 1:
                    QMessageBox.warning(self, "Gagal", "Minimal 1 soal harus diisi dengan lengkap.")
                    return
                # Simpan ke MongoDB
                koleksi.insert_one(dokumen)
                QMessageBox.information(self, "Berhasil", "Semua soal berhasil disimpan ke MongoDB.")
                self.refrashSoal()
                self.loadListQuis()
            else:
                QMessageBox.warning(self, "Gagal", "Tidak ada soal yang valid untuk disimpan.")
        except Exception as e:
                    QMessageBox.critical(self, "Gagal", f"Gagal menyimpan soal: {str(e)}")

    # Bagian ini digunakan untuk mengambil data dari database
    def onEditJudul(self,nama_soal,kategori):
        self.ui.stackedWidget_Main.setCurrentWidget(self.ui.page_Main_Input_Quis)
        # mengambil data dari database
        data = self.koleksi_Soal.find_one({"Nama_Soal": nama_soal, "Kategori": kategori})
        
        try:
            self.ui.btn_SimpanSoal.clicked.disconnect()
        except TypeError:
            pass  # Jika belum ada koneksi, abaikan error
        self.ui.btn_SimpanSoal.setText("Simpan Perubahan")
        self.ui.btn_SimpanSoal.clicked.connect(partial(self.editJudul,nama_soal,kategori))

        if data:
            self.ui.comboBox_Nama_KategoriSoal.setCurrentText(data["Kategori"])
            self.ui.lineEdit_Nama_Soal.setText(data["Nama_Soal"])
            # Mengisi soal yang sudah ada
            soal_dict = data.get("soal", {})
            jumlah_soal = data.get("jumlah_soal", 0)
            self.ui.lineEdit_JumlahSoal.setText(str(jumlah_soal))
            self.JumlahSoal()  # Membuat input soal sesuai jumlah

            for index, soal in enumerate(self.soal_list, start=1):
                key = f"pertanyaan_{index}"
                if key in soal_dict:
                    data_soal = soal_dict[key]
                    soal["pertanyaan"].setText(data_soal["pertanyaan"])
                    soal["jawaban_benar"].setCurrentText(data_soal["jawaban_benar"])
                    for opsi, widget in soal["opsi"].items():
                        widget.setText(data_soal["jawaban"].get(opsi, ""))
        else:
            QMessageBox.warning( self, "Data Tidak Ditemukan", f"Soal dengan nama '{nama_soal}' dengan kategori '{kategori}' tidak ditemukan.")

    #Bagian ini digunakan untuk memasukkan nilainya
    def editJudul(self,nama_soal,kategori):
        # mengambil data dari UI 
        kategori_baru = self.ui.comboBox_Nama_KategoriSoal.currentText().strip()
        nama_soal_baru = self.ui.lineEdit_Nama_Soal.text().strip()
        jumlah_soal_baru = self.ui.lineEdit_JumlahSoal.text().strip()
        
        self.nama_soal_lama = nama_soal
        self.kategori_lama = kategori
        
        # Validasi dasar
        if not nama_soal_baru or not jumlah_soal_baru.isdigit():
            QMessageBox.warning(self, "Gagal", "Nama soal dan jumlah soal harus diisi dengan benar.")
            return
        # konfersi jumlah soal ke integer
        jumlah_soal_baru = int(jumlah_soal_baru)
        # dictionary untuk menampung soal baru

        soal_baru = {}
        # looping soal 
        for index, soal in enumerate(self.soal_list, start=1):
            key = f"pertanyaan_{index}"
            pertanyaan = soal["pertanyaan"].text().strip()
            jawaban_benar = soal["jawaban_benar"].currentText().strip()
            # dictionery untuk menampung opsi jawaban
            jawaban_opsi = {}

            for opsi, widget in soal["opsi"].items():
                jawaban_opsi[opsi] = widget.text().strip()

            # Validasi isi soal
            if not pertanyaan or not all(jawaban_opsi.values()):
                QMessageBox.warning(self, "Gagal", f"Pertanyaan {index} belum lengkap.")
                return

            soal_baru[key] = {
                "pertanyaan": pertanyaan,
                "jawaban": jawaban_opsi,
                "jawaban_benar": jawaban_benar
            }

        # Simpan ke database
        result = self.koleksi_Soal.update_one(
            {"Nama_Soal": self.nama_soal_lama, "Kategori": self.kategori_lama},
            {"$set": {
                "Nama_Soal": nama_soal_baru,
                "Kategori": kategori_baru,
                "jumlah_soal": jumlah_soal_baru,
                "soal": soal_baru
            }}
        )
        # menampilkan pesan berhasil atau gagal
        if result.modified_count > 0:
            QMessageBox.information(self, "Berhasil", "Soal berhasil diperbarui.")
            self.ui.stackedWidget_Main.setCurrentWidget(self.ui.page_Main_Quis)
            self.ui.stackedWidget_Sidebar.setCurrentWidget(self.ui.page_Sidebar_Quis)
            self.loadListQuis()
            self.refrashSoal()
        else:
            QMessageBox.warning(self, "Gagal", "Tidak ada perubahan atau soal tidak ditemukan.")



# MALAM TADI BAGIAN EDIT SUDAH SELESAI 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
