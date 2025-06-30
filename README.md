
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
```

---

### 🛠️ Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/mihirjain4/wildfire-smoke-detection-.git
cd wildfire-smoke-detection-
```

#### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Requirements
```bash
pip install -r requirements.txt
```

#### 4. Add YOLOv8 Model Weights
Download your trained `.pt` model and place it in:
```
yolov8-model/
```

---

### 🚀 Run Streamlit App

```bash
streamlit run streamlit-app/app.py
```

---

### 📷 Sample Input/Output

![Output](https://user-images.githubusercontent.com/61203589/90666480-156de100-e213-11ea-856c-fcf7ee1fae4b.gif)
![Output](https://user-images.githubusercontent.com/61203589/90589985-051f1d00-e1a5-11ea-9f94-a06bb98ad19e.gif)



---

### 🧭 Future Improvements

- 🔁 Live webcam/streaming integration
- 📡 IoT integration with real-time alerts
- 🎯 Add support for fire flame detection
- 💻 Edge device deployment (Jetson Nano, Raspberry Pi)

---

### 🙏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [Roboflow Datasets](https://roboflow.com/)
- [OpenCV](https://opencv.org/), [PyTorch](https://pytorch.org/), [Streamlit](https://streamlit.io/)

---

### 📬 Contact

**Mihir Jain**  
📧 mihirjain@example.com  
🔗 [GitHub](https://github.com/mihirjain4) | [LinkedIn](https://linkedin.com/in/mihirjain4)

---

> ⚠️ *This project is for research and educational purposes only.*
