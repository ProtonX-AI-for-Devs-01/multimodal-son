from flask import Flask, request, jsonify
from PIL import Image
import io
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration, BlipForQuestionAnswering

app = Flask(__name__)

# Load models
captioner = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
qa_model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")

@app.route('/', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    prompt = request.form.get('prompt', '')
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        # Read and process the image
        image = Image.open(io.BytesIO(file.read())).convert('RGB')
        
        # Generate caption
        inputs = processor(image, return_tensors="pt")
        out = captioner.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        
        # Answer question
        inputs = processor(image, prompt, return_tensors="pt")
        out = qa_model.generate(**inputs)
        answer = processor.decode(out[0], skip_special_tokens=True)
        
        return jsonify({
            'caption': caption,
            'answer': answer
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)