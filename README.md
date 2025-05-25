# 🖥️🔥 Flask YOLO 🏷️ Detection App

This is a 🏗️ Flask-based 🌐 web app that lets users 📤 upload 🖼️ images and 🏷️ detect objects using a pre-trained YOLO 🧠 model. The app 📊 processes the uploaded 🖼️, runs YOLO 🔍 inference, and returns the 🎯 result with 🏷️ boxes drawn on detected objects.

## 🌟 Features
- 📤 Upload 🖼️ via a web 🖥️ interface.
- 🏷️ Detect objects using YOLO (`best.pt` 🧠).
- 🖼️ Display the processed 🏷️ 🖼️.
- 🚀 Simple & 🛠️ user-friendly Flask framework.

## ✅ Prerequisites
Make sure you have these installed:

- 🐍 Python 3.8+
- 🏗️ Flask
- 📷 OpenCV (`cv2`)
- 🚀 Ultralytics YOLO (`ultralytics`)

## 📥 Installation
1. **📂 Clone the repo**
   ```bash
   git clone https://github.com/himaenshuu/Crop_weed_detection-app.git
   cd Crop_weed_detection-app
   ```

2. **🔧 Create Conda env (optional)**
   ```bash
   conda create --name yolo-env python=3.9 -y
   conda activate yolo-env
   ```

3. **📦 Install dependencies**
   ```bash
   pip install flask ultralytics opencv-python
   ```

4. **📌 Add YOLO model**
   - Place your trained YOLO model (`best.pt` 🧠) in the project 📁 directory.

## 🚀 Usage
1. **▶️ Run the Flask app**
   ```bash
   python app.py
   ```

2. **🌐 Open web app**
   Open your 🔍 browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

3. **🖼️ Upload image**
   - Select & 📤 upload a 🖼️.
   - The app will process and return the detected 🏷️ objects.

## 📂 Project Structure
```
flask-yolo-app/
│── 📁 uploads/                  # 📤 Uploaded & processed 🖼️
│── 📁 templates/
│   └── 📝 index.html            # 🌐 Web UI
│── 🖥️ app.py                    # 🎯 Main Flask app
│── 🧠 best.pt                   # Pre-trained YOLO 🏷️ model
│── 📄 README.md                 # 📖 Project docs
```

## 📝 Notes
- `UPLOAD_FOLDER` is auto-created if it doesn’t exist.
- Ensure your `best.pt` 🧠 is 🏗️ compatible with `ultralytics`.
- Modify `index.html` 🎨 to customize the UI.

## 📜 License
This project is open-source 🔓. Modify & use it as needed.
