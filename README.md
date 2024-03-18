# Speech Emotion Recognition API - IEMOCAP dataset with good accuracy for realtime use

This FastAPI application provides an endpoint for performing emotion recognition on audio files.

## Installation

1. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    # Windows
    .\env\Scripts\activate
    # Linux/Mac
    source env/bin/activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the FastAPI server, run the following command:
```bash
uvicorn app:app --reload
```

This will start the server, and you can access the API at http://localhost:8000/docs.

## Emotion Recognition Endpoint
You can perform emotion recognition on audio files by sending a POST request to /emotion_recognition. Upload an audio file with the request, and the API will return the detected emotion and its confidence score.

Example:
```bash
curl -X POST -F "audio_file=@/path/to/audio/file.wav" http://localhost:8000/emotion_recognition
```