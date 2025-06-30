from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from pathlib import Path
import cv2
from io import BytesIO
from ultralytics import YOLO
import tempfile

app = FastAPI()

# Load the YOLO model
model_path = Path("weights/yolov8.pt")
model = YOLO(model_path)

@app.post("/detect/image")
async def detect_objects_image(file: UploadFile = File(...), confidence: float = 0.4):
    # Save the uploaded file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name

    # Read the uploaded image
    image = cv2.imread(temp_file_path)

    # Perform object detection
    results = model.predict(image, conf=confidence)

    # Plot the detected objects on the image
    annotated_image = results[0].plot()
    _, annotated_image_encoded = cv2.imencode('.png', annotated_image)

    return StreamingResponse(BytesIO(annotated_image_encoded.tobytes()), media_type="image/png")

@app.post("/detect/video")
async def detect_objects_video(file: UploadFile = File(...), confidence: float = 0.4):
    # Save the uploaded file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name

    # Read the uploaded video
    cap = cv2.VideoCapture(temp_file_path)
    frames = []

    # Process each frame for object detection
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform object detection on each frame
        results = model.predict(frame, conf=confidence)
        annotated_frame = results[0].plot()

        # Convert the frame to bytes
        _, encoded_frame = cv2.imencode('.png', annotated_frame)
        frames.append(encoded_frame.tobytes())

    # Release the video capture object
    cap.release()

    # Return the processed video frames as a streaming response
    return StreamingResponse(iter(frames), media_type="image/png")
