from yolo_detector import capture_image
from openai_processor import classify_vehicle
from ocr_reader import extract_plate
from db import init_db, insert_event
from slot_manager import get_available_slots
from known_vehicles import is_known_vehicle

def process(zone: str):
    image = capture_image(zone=zone)
    if not image:
        print("No vehicle detected.")
        return

    vehicle = classify_vehicle(image)
    plate = extract_plate(image)
    print(f"Plate: {plate}, Vehicle: {vehicle}")

    vehicle["license_plate"] = plate
    vehicle["image_path"] = image
    vehicle["entry"] = True if zone == "entry" else False
    vehicle["occupied_slots"] = 2 if vehicle["vehicle_type"].lower() == "car" else 1

    insert_event(vehicle)
    print(f"Remaining Slots: {get_available_slots()}")
    if plate and is_known_vehicle(plate):
        print(f"Known Vehicle: {is_known_vehicle(plate)}")

if __name__ == "__main__":
    init_db()
    while True:
        zone = input("Enter zone (entry/exit): ")
        process(zone)
