from flask import Flask, request, render_template, send_file
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist("file[]")
    if len(uploaded_files) != 9:
        return "Please upload exactly 9 images", 400

    images = []
    for i, file in enumerate(uploaded_files):
        file_path = os.path.join(UPLOAD_FOLDER, f'image_{i}.jpg')
        file.save(file_path)
        images.append(Image.open(file_path))

    target_size = (200, 200)
    resized_images = [img.resize(target_size) for img in images]
    grid_image = Image.new('RGB', (target_size[0] * 3, target_size[1] * 3))

    for i, img in enumerate(resized_images):
        x = (i % 3) * target_size[0]
        y = (i // 3) * target_size[1]
        grid_image.paste(img, (x, y))

    output_path = os.path.join(PROCESSED_FOLDER, 'elmo_grid.jpg')
    grid_image.save(output_path)
    return send_file(output_path, as_attachment=True, download_name='elmo_grid.jpg')

if __name__ == '__main__':
    app.run(debug=True)
