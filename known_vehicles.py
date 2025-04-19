KNOWN_PLATES = {"KA01AB1234": "VIP", "DL05XY9999": "Resident"}

def is_known_vehicle(plate: str):
    return KNOWN_PLATES.get(plate)
