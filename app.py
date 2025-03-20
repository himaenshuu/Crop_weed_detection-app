from flask import Flask, request, render_template, send_from_directory, redirect, url_for
from ultralytics import YOLO
import os
import cv2

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained YOLO model
model = YOLO('best.pt')  # Replace 'best.pt' with your model path 

# Define the directory to save uploaded files 
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER): 
    os.makedirs(UPLOAD_FOLDER) 

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/') 
def home(): 
    return render_template('index.html')  # Use relative path for the template 

@app.route('/upload', methods=['POST']) 
def upload_file(): 
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file', 400
    
    if file:
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        try:
            # Run inference on the uploaded image
            results = model(file_path)  # YOLO model inference
            
            # Get the image with predictions
            result_image = results[0].plot()  
            
            # Save the result image
            result_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_' + file.filename) 
            cv2.imwrite(result_image_path, result_image)
            
            # Redirect to the result page
            return redirect(url_for('result', filename='result_' + file.filename)) 

        except Exception as e:
            return str(e), 500

@app.route('/result/<filename>')
def result(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__': 
    app.run(debug=True) 