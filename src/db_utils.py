import sqlite3

def init_db(path='data/supply_chain.db'):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS sales (order_id INTEGER PRIMARY KEY, date TEXT, location_id TEXT, item_id TEXT, qty INTEGER, unit_price REAL)''')
    conn.commit()
    conn.close()
