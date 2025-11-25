import mysql.connector
from PySide6.QtWidgets import QMessageBox
#LOGIN

#USER_LOGIN
def loginUser(window,ui,conn):
    username = ui.lineEdit_LoginUsername.text()
    password = ui.lineEdit_LoginPassword.text()

    if not username or not password:
        QMessageBox.warning(window, "Input Kosong", "Username dan Password harus diisi.")
        return

    try:
        cursor = conn.cursor()
        query = "SELECT * FROM student WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        cursor.close()

        if result:
            ui.stackedWidget_Sidebar.hide()
            ui.stackedWidget_Utama.setCurrentWidget(ui.page_Main)
            # ui.stackedWidget_Sidebar.setCurrentWidget(ui.page_Sidebar_Beranda)
            ui.stackedWidget_Main.setCurrentWidget(ui.page_Main_Beranda)
        else:
            QMessageBox.critical(window, "Login Gagal", "Username atau password salah.")

    except mysql.connector.Error as err:
        QMessageBox.critical(window, "Error", f"Gagal mengakses database:\n{err}")
