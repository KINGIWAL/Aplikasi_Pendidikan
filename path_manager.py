import os
import sys

def get_folder_catatan():
    if getattr(sys, 'frozen', False):
        base_folder = os.path.dirname(sys.executable)
    else:
        base_folder = os.path.dirname(__file__)

    folder_catatan = os.path.join(base_folder, "catatan")

    if not os.path.exists(folder_catatan):
        os.makedirs(folder_catatan)
        print("Folder 'catatan' berhasil dibuat.")
    else:
        print("Folder 'catatan' sudah ada.")

    return folder_catatan
