# Smart Parking AI System (Gemini Version)

This system detects vehicles using YOLOv8, classifies them with Gemini Vision, reads license plates using OCR, and stores data in a SQLite database.

## Features

- YOLOv8 detection
- Gemini Vision vehicle classification
- EasyOCR for license plate
- SQLite storage
- Streamlit dashboard
- Slot tracking: 10 cars or 20 bikes

## Usage

1. Set your API key in `.env`.
2. Run the main app:
```bash
python main.py
```
3. View dashboard:
```bash
streamlit run dashboard.py
```

## Dependencies

Install with:
```bash
pip install -r requirements.txt
```
