import sys
import os
import globals

from PySide6.QtWidgets import QMessageBox, QHBoxLayout,QWidget,QPushButton
from path_manager import get_folder_catatan
from functools import partial
from PySide6.QtCore import Qt


# masalah yang terjadi
# path kd jelas
# self pina aneh
# parameter pertama di QMessageBox   (Parent)




def get_ui():
    if globals.ui is None:
        raise Exception("UI belum diinisialisasi!")
    return globals.ui

#Hapus file catatan
def HapusFileCatatan(window,path):
    #Untuk mengambil nama file dari path
    nama_file = os.path.basename(path)

    if os.path.exists(path):
        asking = QMessageBox.question(window,"konfirmasi",f"Yakin ingin menghapus'{nama_file}'",QMessageBox.Yes|QMessageBox.No)
        if asking == QMessageBox.Yes:
            try:
                os.remove(path)
                # Digunakan untuk reload Page_Catatan
                loadListCatatan(window)
                TambahCatatan(window)
                # # Untuk mengosongkan field ketika filenya dihapus
                # self.HapusCatatan()
            except Exception as e:
                QMessageBox.critical(window, "Gagal", f"Error saat menghapus: {str(e)}")
        else:
            QMessageBox.information(window, "Dibatalkan", "Penghapusan dibatalkan oleh pengguna.")
    else:
        QMessageBox.warning(window, "Gagal", "File tidak ditemukan.")



def onSimpanCatatanBaru(window):
    ui = get_ui()
    judul = ui.judul_input.text()
    isi = ui.editor.toPlainText()
    SimpanCatatanBaru(window,judul, isi)

#Simpan Catatan
def SimpanCatatanBaru(window,judul_baru, isi_baru):
    ui = get_ui()
    folder_catatan = get_folder_catatan()
    # Buat path dulu
    path = os.path.join(folder_catatan, f"{judul_baru}.txt")

    #Judul tidak boleh kosong
    if not judul_baru.strip():
        QMessageBox.warning(window, "Gagal", "Judul tidak boleh kosong.")
        return

    # Baru cek apakah file sudah ada
    if os.path.exists(path):
        QMessageBox.warning(window, "Gagal", "Nama file sudah ada, ganti dengan nama lain.")
        return

    # Simpan isi ke file
    with open(path, "w", encoding="utf-8") as file:
        file.write(isi_baru)
    #Untuk mengclear field
    ui.judul_input.clear()
    ui.editor.clear()
    #Alternatif untuk mereload sidebar
    loadListCatatan(window)

    QMessageBox.information(window, "Berhasil", "Catatan berhasil disimpan.")


#Menampilkan List Catatan
def loadListCatatan(window):
    ui = get_ui()
    folder_catatan = get_folder_catatan()

    layout = ui.verticalLayout_Sidebar_Catatan

    # Bersihkan layout dulu
    for i in reversed(range(layout.count())):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.setParent(None)


    # Loop semua file .txt
    for nama_file in os.listdir(folder_catatan):
        if nama_file.endswith(".txt"):
            nama_catatan = os.path.splitext(nama_file)[0]  # hapus .txt
            path_file = os.path.join(folder_catatan, nama_file)
            # Buat tombol untuk tiap catatan

            row_layout = QHBoxLayout()
            row_widget = QWidget()
            row_widget.setLayout(row_layout)

            btn_catatan = QPushButton(nama_catatan)
            btn_catatan.setStyleSheet("""
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
            btn_catatan.clicked.connect(partial(BukaCatatan,window, path_file))

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
            btn_delete.clicked.connect(partial(HapusFileCatatan,window,path_file))

            # Tambahkan ke layout baris
            row_layout.addWidget(btn_catatan)
            row_layout.addWidget(btn_delete)

            # Tambahkan ke layout utama
            layout.addWidget(row_widget)
            layout.setAlignment(Qt.AlignTop)


# button + di klik
def TambahCatatan(window):
    ui = get_ui()
    ui.judul_input.clear()
    ui.editor.clear()
    ui.btn_Simpan_Catatan_dan_edit.setText("Simpan")
    ui.btn_Simpan_Catatan_dan_edit.clicked.disconnect()
    ui.btn_Simpan_Catatan_dan_edit.clicked.connect(partial(onSimpanCatatanBaru,window))


def BukaCatatan(window,path):
    ui = get_ui()
    with open(path, "r", encoding="utf-8") as file:
        isi = file.read()

    #Yang bagian ini digunakan untuk menampilkan isi file ke text edit-nya
    ui.editor.setPlainText(isi)

    nama_file= os.path.splitext(os.path.basename(path))[0]
    ui.judul_input.setText(nama_file)

    ui.btn_Simpan_Catatan_dan_edit.setText("Edit")
    #Memutuskan event sebelumnya
    ui.btn_Simpan_Catatan_dan_edit.clicked.disconnect()
    ui.btn_Simpan_Catatan_dan_edit.clicked.connect(partial(SimpanPerubahanCatatan,window,path))

def SimpanPerubahanCatatan(window, path):
    ui = get_ui()
    if not path or not os.path.exists(path):
          QMessageBox.warning(window, "Gagal", "Tidak ada file yang sedang dibuka.")
          return

    isi_baru = ui.editor.toPlainText()
    try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(isi_baru)

            QMessageBox.information(window, "Berhasil", "Perubahan berhasil disimpan.")
    except Exception as e:
            QMessageBox.critical(window, "Gagal", f"Error saat menyimpan: {str(e)}")



