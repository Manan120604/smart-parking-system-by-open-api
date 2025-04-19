import base64
import requests
import json

API_KEY = "your_gemini_api_key"
MODEL_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent?key=" + API_KEY

def classify_vehicle(image_path: str):
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    prompt = "Identify the vehicle type, color, model if visible. Return as JSON like: { 'vehicle_type': '', 'color': '', 'model': '' }"
    
    request_body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                    {"inlineData": {
                        "mimeType": "image/jpeg",
                        "data": image_data
                    }}
                ]
            }
        ]
    }

    response = requests.post(MODEL_URL, json=request_body)
    output = response.json()

    try:
        text = output['candidates'][0]['content']['parts'][0]['text']
        return json.loads(text)
    except Exception as e:
        print("Error parsing response:", e)
        return {}
