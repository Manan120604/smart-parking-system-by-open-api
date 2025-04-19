import sqlite3
from datetime import datetime

DB = "parking.db"

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS parking_events (
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                image_path TEXT,
                vehicle_type TEXT,
                color TEXT,
                model TEXT,
                license_plate TEXT,
                entry BOOLEAN,
                occupied_slots INTEGER
            )
        ''')

def insert_event(data: dict):
    with sqlite3.connect(DB) as conn:
        conn.execute('''
            INSERT INTO parking_events
            (timestamp, image_path, vehicle_type, color, model, license_plate, entry, occupied_slots)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            datetime.now().isoformat(),
            data["image_path"],
            data["vehicle_type"],
            data["color"],
            data["model"],
            data["license_plate"],
            data["entry"],
            data["occupied_slots"]
        ))
