from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox,QWidget, QVBoxLayout, QLabel,QHBoxLayout,QScrollArea
from pymongo import MongoClient
from datetime import datetime
from functools import partial
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox

#Menampilkan List Materi disidebar materi
def loadlistMateri(window,ui,koleksi):
    # Tempat untuk menampilkan list
    layout = ui.verticalLayout_Sidebar_Materi  # pastikan ini adalah layout yang terpasang di scrollAreaWidget_FolderMateri

    #untuk membersihkan widget yang ada lebih dahulu
    for i in reversed(range(layout.count())):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.setParent(None)

    # ambil semua nama folder unik
    folder_list = koleksi.distinct("folder")

    # loop dan tambahkan button
    for folder_name in folder_list:
        row_layout = QHBoxLayout()
        row_widget = QWidget()
        row_widget.setLayout(row_layout)

            # Tombol folder
        btn_folder = QPushButton(folder_name)
        btn_folder.setStyleSheet("""
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
        btn_folder.clicked.connect(partial(onFolderClicked,window, ui,koleksi,folder_name))

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
        btn_delete.clicked.connect(partial(onDeleteFolder, window,koleksi,ui,folder_name))

        # Tambahkan ke layout baris
        row_layout.addWidget(btn_folder)
        row_layout.addWidget(btn_delete)

        # Tambahkan ke layout utama
        layout.addWidget(row_widget)

        layout.setAlignment(Qt.AlignTop)

def onDeleteFolder( window,koleksi,ui, folder_name):
    # Konfirmasi dulu sebelum menghapus
    reply = QMessageBox.question( window,
        "Konfirmasi Hapus",
        f"Yakin ingin menghapus folder '{folder_name}'?",
        QMessageBox.Yes | QMessageBox.No
    )

    if reply == QMessageBox.Yes:
        print(f"Menghapus folder: {folder_name}")
        koleksi.delete_many({"folder": folder_name})
        loadlistMateri(window,ui,koleksi)


#Menampilkan materi di stackedWidget_Main
def onFolderClicked(window,ui,koleksi,folder_name):
    #Membuka Halaman
    ui.stackedWidget_Main.setCurrentWidget(ui.page_Main_Materi)

    # Bersihkan layout sebelum menambahkan halaman baru
    for i in reversed(range(ui.verticalLayout_Materi.count())):
        widget = ui.verticalLayout_Materi.itemAt(i).widget()
        if widget:
            widget.setParent(None)

    # Buat halaman baru
    page = QWidget()
    page.setStyleSheet("""
    background-color: rgba(0,0,0,0);
    padding:18px;
    border-radius:8px;
    color:white;
    """)
    layout = QVBoxLayout(page)

    # Scroll area agar konten panjang bisa digulir
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll_content = QWidget()
    scroll_layout = QVBoxLayout(scroll_content)

    # Ambil semua data dari MongoDB berdasarkan folder
    hasil = koleksi.find({"folder": folder_name}).sort("Time", 1)
    for i, data in enumerate(hasil):
        if i >= 1:
            break
        # Judul
        judul = QLabel(f"{data.get('judul', '-')}")
        judul.setStyleSheet("""
        qproperty-alignment: AlignCenter;
        background-color:#202f2f;
        padding:10px;
        font-size:15px;
        font-weight:bold;
        border-radius:15px;
        """)
        judul.setMaximumHeight(50)
        scroll_layout.addWidget(judul)

        isi = QLabel(f"{data.get('materi', '-')}")
        isi.setStyleSheet("""
        background-color: rgba(0,0,0,90);
        padding:15px;
        font-size:16px;
        border-radius:8px;
        color:white;
        """)
        isi.adjustSize()
        scroll_layout.addWidget(isi)

        # Contoh
        contoh_text = data.get("contoh")
        if contoh_text:
            contoh = QLabel(f"Contoh:\n{contoh_text}")
            contoh.setWordWrap(True)
            contoh.setStyleSheet("""
            background-color:#1a3935;
            padding:18px;
            font-size:15px;
            border-radius:3px;
            """)
            scroll_layout.addWidget(contoh)

        # Peringatan
        peringatan_text = data.get("peringatan")
        if peringatan_text:
            peringatan = QLabel(f"Peringatan:\n{peringatan_text}")
            peringatan.setWordWrap(True)
            peringatan.setStyleSheet("""
            background-color: #6f7e81;
            padding: 18px;
            font-size: 15px;
            border-radius: 15px;
            border: solid 9px white;
            color: black;
            """)
            scroll_layout.addWidget(peringatan)

    # Gabungkan layout scroll ke halaman
    scroll.setWidget(scroll_content)
    layout.addWidget(scroll)

    # Tambahkan halaman ke stackedWidget dan tampilkan
    ui.verticalLayout_Materi.addWidget(page)
    #Menampilkan nama judul di sidebar kanan
    loadJudulButtons(window,ui,koleksi,folder_name)

# Menampilkan list judul
def loadJudulButtons(window, ui,koleksi,folder_name):
    layout = ui.verticalLayout_JudulMateri

    # Bersihkan dulu kalau ada button lama
    for i in reversed(range(layout.count())):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.setParent(None)

    # Ambil semua dokumen dari folder tertentu
    hasil = koleksi.find({"folder": folder_name}).sort("Time",1)

    # Ambil semua judul unik dari hasil tersebut
    judul_set = []
    for data in hasil:
        folder = data.get("folder")
        judul = data.get("judul")
        if judul and judul not in judul_set:
            judul_set.append(judul)


    # Loop dan tambahkan button
    for judul in judul_set:

        row_layout = QHBoxLayout()
        row_widget = QWidget()
        row_widget.setLayout(row_layout)

        # Tombol folder
        btn_judul = QPushButton(judul)
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
        btn_judul.clicked.connect(partial(onJudulClicked, ui,koleksi,judul, folder))
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
        btn_delete.clicked.connect(partial(onDeleteJudul, window,ui,koleksi, judul, folder))

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
        btn_edit.clicked.connect(partial(onEditJudul, window,ui,koleksi,judul, folder))

        # Tambahkan ke layout baris
        row_layout.addWidget(btn_judul)
        row_layout.addWidget(btn_edit)
        row_layout.addWidget(btn_delete)

        layout.addWidget(row_widget)
        layout.setAlignment(Qt.AlignTop)
# Bagian ini digunakan untuk mengambil data dari database
def onEditJudul( window,ui,koleksi,judul,folder):
    ui.stackedWidget_Main.setCurrentWidget(ui.page_Main_Input_Materi)
    data = koleksi.find_one({"judul": judul,"folder": folder})
    try:
        ui.btnSimpan_Materi.clicked.disconnect()
    except TypeError:
        pass  # Jika belum ada koneksi, abaikan error
    ui.btnSimpan_Materi.setText("Simpan Perubahan")
    ui.btnSimpan_Materi.clicked.connect(partial(editJudul,window, ui,koleksi,judul,folder))

    if data:
        ui.comboBox_folder_Materi.setCurrentText(data["folder"])
        ui.lineEdit_Judul.setText(data["judul"])
        ui.textEdit_Materi.setPlainText(data["materi"])
        ui.textEdit_Contoh.setPlainText(data["contoh"])
        ui.textEdit_Peringatan.setPlainText(data["peringatan"])
    else:
        QMessageBox.warning( window, "Data Tidak Ditemukan", f"Materi dengan judul '{judul}' di folder '{folder}' tidak ditemukan.")

#Bagian ini digunakan untuk memasukkan nilainya
def editJudul( window, ui,koleksi,judul, folder):
    # Ambil data baru dari form
    folder_baru = ui.comboBox_folder_Materi.currentText()
    judul_baru = ui.lineEdit_Judul.text()
    materi_baru = ui.textEdit_Materi.toPlainText()
    contoh_baru = ui.textEdit_Contoh.toPlainText()
    peringatan_baru = ui.textEdit_Peringatan.toPlainText()

    # Update data di MongoDB
    result = koleksi.update_one(
        {"judul": judul, "folder": folder},  # filter data lama
        {"$set": {
            "folder": folder_baru,
            "judul": judul_baru,
            "materi": materi_baru,
            "contoh": contoh_baru,
            "peringatan": peringatan_baru
        }}
    )

    # Tampilkan notifikasi
    if result.modified_count > 0:
        QMessageBox.information( window, "Berhasil", "Materi berhasil diperbarui.")

        # digunakan untuk merefresh
        ui.stackedWidget_Main.setCurrentWidget(ui.page_Main_Materi)
        ui.stackedWidget_Sidebar.setCurrentWidget(ui.page_Sidebar_Materi)

    else:
        QMessageBox.warning( window, "Gagal", "Tidak ada perubahan atau data tidak ditemukan.")
    

def onDeleteJudul(window, ui,koleksi,judul_name,folder_name):
    # Konfirmasi dulu sebelum menghapus
    reply = QMessageBox.question( window,
        "Konfirmasi Hapus",
        f"Yakin ingin menghapus judul '{judul_name}'?",
        QMessageBox.Yes | QMessageBox.No
    )

    if reply == QMessageBox.Yes:
        print(f"Menghapus judul: {judul_name}")
        koleksi.delete_many({"judul": judul_name})
        loadJudulButtons(window, ui,koleksi,judul_name,folder_name)


# Menampilkan materi berdasarkan judul ketika diklik
def onJudulClicked( ui,koleksi,judul, folder):
    for i in reversed(range(ui.verticalLayout_Materi.count())):
        widget = ui.verticalLayout_Materi.itemAt(i).widget()
        if widget:
            widget.setParent(None)

    # Buat halaman baru
    page = QWidget()
    page.setStyleSheet("""
    background-color: rgba(0,0,0,0);
    padding:18px;
    border-radius:8px;
    color:white;
    """)
    layout = QVBoxLayout(page)

    # Scroll area agar konten panjang bisa digulir
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll_content = QWidget()
    scroll_layout = QVBoxLayout(scroll_content)

    # Ambil semua data dari MongoDB berdasarkan judul
    hasil = koleksi.find({"folder":folder,"judul": judul}).sort("Time", 1)
    for i, data in enumerate(hasil):
        if i >= 1:
            break

         # Judul
        judul = QLabel(f"{data.get('judul', '-')}")
        judul.setWordWrap(True)
        judul.setStyleSheet("""
        qproperty-alignment: AlignCenter;
        background-color:#202f2f;
        padding:10px;
        font-size:16px;
        font-weight:bold;
        border-radius:15px;
        """)
        judul.setMaximumHeight(50)
        scroll_layout.addWidget(judul)

        isi = QLabel(f"{data.get('materi', '-')}")
        isi.setWordWrap(True)
        isi.setStyleSheet("""
        background-color: rgba(0,0,0,90);
        font-size:16px;
        border-radius:8px;
        color:white;
        """)
        isi.adjustSize()
        scroll_layout.addWidget(isi)

         # Contoh
        contoh_text = data.get("contoh")
        if contoh_text:
            contoh = QLabel(f"Contoh:\n{contoh_text}")
            contoh.setWordWrap(True)
            contoh.setStyleSheet("""
            background-color:#1a3935;
            padding:18px;
            font-size:15px;
            border-radius:3px;
            """)
            scroll_layout.addWidget(contoh)

         # Peringatan
        peringatan_text = data.get("peringatan")
        if peringatan_text:
            peringatan = QLabel(f"Peringatan:\n{peringatan_text}")
            peringatan.setWordWrap(True)
            peringatan.setStyleSheet("""
            background-color: #6f7e81;
            padding: 18px;
            font-size: 15px;
            border-radius: 15px;
            border: solid 9px white;
            color: black;
            """)
            scroll_layout.addWidget(peringatan)

     # Gabungkan layout scroll ke halaman
    scroll.setWidget(scroll_content)
    layout.addWidget(scroll)

     # Tambahkan halaman ke stackedWidget dan tampilkan
    ui.verticalLayout_Materi.addWidget(page)


#Memasukkan data materi
def inputDataMateri(window,ui,koleksi):
    folder = ui.comboBox_folder_Materi.currentText()
    judul = ui.lineEdit_Judul.text()
    materi = ui.textEdit_Materi.toPlainText()
    contoh = ui.textEdit_Contoh.toPlainText()
    peringatan = ui.textEdit_Peringatan.toPlainText()
    data_materi = {
        "folder": folder,
        "judul": judul,
        "materi": materi,
        "contoh": contoh,
        "peringatan": peringatan,
        "Time": datetime.now().isoformat()
    }
    try:
        koleksi.insert_one(data_materi)
        QMessageBox.information( window, "Berhasil", "Data materi berhasil disimpan ke database.")
        ui.comboBox_folder_Materi.setCurrentText("")
        ui.lineEdit_Judul.clear()
        ui.textEdit_Materi.clear()
        ui.textEdit_Contoh.clear()
        ui.textEdit_Peringatan.clear()
        loadlistMateri(window,ui,koleksi)
    except Exception as e:
        QMessageBox.critical( window, "Gagal", f"Gagal menyimpan data: {str(e)}")

