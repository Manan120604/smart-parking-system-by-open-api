import sqlite3

def get_available_slots():
    conn = sqlite3.connect("parking.db")
    rows = conn.execute("SELECT entry, occupied_slots FROM parking_events").fetchall()
    conn.close()
    current = sum(s if e else -s for e, s in rows)
    return 20 - current  # 10 cars (2 slots each), 20 bikes (1 slot each)
