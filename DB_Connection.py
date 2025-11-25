import mysql.connector
from pymongo import MongoClient

#koneksi Mysql
def get_mysql_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="muhammadilham2372005",
            database="myapp"
        )

        if conn.is_connected():
            print(" Koneksi ke database berhasil!")
        return conn
    except mysql.connector.Error as err:
        print(f"Terjadi error: {err}")
        return None




#koneksi mongodb

def get_mongo_collections():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Aplikasi_Pendidikan"]
    return {
        "materi": db["Kumpulan_Materi"],
        "soal": db["Kumpulan_Soal"]
    }

