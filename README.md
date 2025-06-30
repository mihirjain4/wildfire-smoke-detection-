# 🔥 Wildfire Smoke Detection Using YOLOv8

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-red)](https://github.com/ultralytics/ultralytics)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

### 🌲 Project Overview

Wildfires pose a severe threat to forests, wildlife, and human communities, causing extensive damage that is difficult to control using traditional methods due to **delayed detection and response**.

This project leverages **YOLOv8**, a cutting-edge object detection model, to build a robust **AI system for early wildfire smoke detection** in forest surveillance images and videos. It includes a real-time **Streamlit web app** to provide instant alerts and visual predictions.

---

### ⚙️ Features

- 🔍 Real-time **smoke detection** in forest images/videos
- 🧠 YOLOv8 trained on smoke datasets (custom/Roboflow)
- ☁️ Handles interference from clouds and fog
- 🖥️ Web interface using **Streamlit**
- 💾 Easy model integration and deployment

---

### 🧠 Tech Stack

| Component        | Library/Tool            |
|------------------|-------------------------|
| Object Detection | [YOLOv8 - Ultralytics](https://github.com/ultralytics/ultralytics) |
| Programming Lang | Python 3.10+            |
| Web UI           | Streamlit               |
| DL Framework     | PyTorch, OpenCV         |
| Dataset Format   | Images/Videos           |

---

### 📁 Folder Structure

```bash
wildfire-smoke-detection-/
├── yolov8-model/          # Trained YOLOv8 weights (.pt)
├── streamlit-app/         # Streamlit web app for detection
├── data/                  # Optional: input images/videos
├── outputs/               # Detection results
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
