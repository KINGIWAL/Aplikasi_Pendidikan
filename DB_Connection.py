import mysql.connector
import socket
from zeroconf import Zeroconf, ServiceBrowser, ServiceStateChange
from pymongo import MongoClient


def on_service_state_change(zeroconf, service_type, name, state_change):
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            print(f"Service {name} ditemukan di {socket.inet_ntoa(info.addresses[0])}")

zeroconf = Zeroconf()
browser = ServiceBrowser(zeroconf, "_mongodb._tcp.local.", handlers=[on_service_state_change])

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
    ip = socket.gethostbyname("LAPTOP-KINGIWAL.local")
    client = MongoClient(f"mongodb://{ip}:27017/", serverSelectionTimeoutMS=5000)
    db = client["Aplikasi_Pendidikan"]
    return {
        "materi": db["Kumpulan_Materi"],
        "soal": db["Kumpulan_Soal"]
    }

