import globals
import mysql.connector
from PySide6.QtWidgets import QMessageBox

def simpanData(ui,conn):
    window = globals.get_main_window()

    fields = {
        "nama": ui.lineEdit_NamaLengkap,
        "email": ui.lineEdit_Email,
        "username": ui.lineEdit_Username,
        "password": ui.lineEdit_Password
    }

    for label, field in fields.items():
        if not field.text().strip():
            QMessageBox.warning(window, "Input Kosong", f"{label} belum diisi.")
            return


        # Ambil nilai dari QLineEdit
    nama = ui.lineEdit_NamaLengkap.text()
    email = ui.lineEdit_Email.text()
    username = ui.lineEdit_Username.text()
    password = ui.lineEdit_Password.text()

    try:
        cursor = conn.cursor()
        query = "INSERT INTO admin (nama, email, username, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nama, email, username, password,))
        conn.commit()
        cursor.close()

        ui.stackedWidget_Utama.setCurrentWidget(ui.page_Main)
        ui.stackedWidget_Sidebar.setCurrentWidget(ui.page_Sidebar_Beranda)
        ui.stackedWidget_Main.setCurrentWidget(ui.page_Main_Beranda)

        for field in fields.values():
            field.clear()
    except mysql.connector.Error as err:
        QMessageBox.critical(window, "Gagal", f"Gagal menyimpan data:\n{err}")


