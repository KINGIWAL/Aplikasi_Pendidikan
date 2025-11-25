ui = None
conn = None
main_window = None

def set_conn(connection):
    global conn
    conn = connection

def get_conn():
    return conn


def set_main_window(window):
    global main_window
    main_window = window

def get_main_window():
    return main_window

