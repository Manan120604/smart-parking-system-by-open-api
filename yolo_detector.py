from ultralytics import YOLO
import cv2
import os
from datetime import datetime

model = YOLO("yolov8n.pt")
os.makedirs("assets", exist_ok=True)

def capture_image(camera_id=0, zone="entry"):
    cap = cv2.VideoCapture(camera_id)
    ret, frame = cap.read()
    cap.release()
    if not ret: return None

    results = model(frame)
    for r in results:
        for box in r.boxes:
            cls = r.names[int(box.cls[0])]
            if cls.lower() in ['car', 'motorbike', 'truck']:
                filename = f"{zone}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                path = os.path.join("assets", filename)
                cv2.imwrite(path, frame)
                return path
    return None
