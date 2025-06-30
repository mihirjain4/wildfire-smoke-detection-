import streamlit as st
import requests
from PIL import Image
import tempfile
import cv2
import numpy as np
from io import BytesIO

# Main page heading
st.title("Object Detection using YOLOv8")

# Select media type
media_type = st.radio("Select Media Type", ["Image", "Video"])

# Upload media
uploaded_file = st.file_uploader(f"Choose a {media_type.lower()}...", type=["jpg", "jpeg", "png", "mp4"])

# Confidence slider
confidence = st.slider("Select Model Confidence", min_value=0.0, max_value=1.0, value=0.4, step=0.05)

# Display media and detected objects
if uploaded_file is not None:
    if media_type == "Image":
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Detect objects on the image
        if st.button("Detect Objects"):
            # Make a POST request to the FastAPI backend
            response = requests.post("http://localhost:8000/detect/image", files={"file": uploaded_file}, data={"confidence": confidence})

            if response.status_code == 200:
                # Display the detected image
                detected_image = Image.open(BytesIO(response.content))
                st.image(detected_image, caption="Detected Image", use_column_width=True)
            else:
                st.error("Error occurred during object detection. Please try again.")

    elif media_type == "Video":
        # Display uploaded video
        st.video(uploaded_file, format="video/mp4", start_time=0)

        # Detect objects in the video
        if st.button("Detect Objects"):
            # Temporarily save the uploaded video
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_path = temp_file.name

            # Read the video file
            cap = cv2.VideoCapture(temp_file_path)
            frames = []

            # Process each frame for object detection
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                # Encode the frame as bytes
                _, encoded_frame = cv2.imencode('.jpg', frame)
                file_bytes = BytesIO(encoded_frame.tobytes())

                # Make a POST request to the FastAPI backend for each frame
                response = requests.post("http://localhost:8000/detect/video", files={"file": file_bytes}, data={"confidence": confidence})

                if response.status_code == 200:
                    # Convert the response content (annotated frame) to a numpy array
                    annotated_frame = np.array(Image.open(BytesIO(response.content)))

                    # Append the annotated frame to the list of frames
                    frames.append(annotated_frame)
                else:
                    st.error("Error occurred during object detection. Please try again.")

            # Release the video capture object
            cap.release()

            # Display the processed video frames
            st.image(frames, use_column_width=True)
