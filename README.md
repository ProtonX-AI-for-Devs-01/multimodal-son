# Image Captioning and Q&A App

This project is a web application that allows users to upload an image and receive an automatically generated caption and answers to questions based on the image. The application uses deep learning models to process the images and generate responses.

## Setup

### Prerequisites

- Python 3.7 or higher

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```sh
     source venv/bin/activate
     ```

4. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Flask server:

   ```sh
   python backend.py
   ```

   The server will run on `http://0.0.0.0:7070`.

2. In a new terminal, start the Streamlit app:

   ```sh
   streamlit run client.py
   ```

   The Streamlit app will run on `http://localhost:8501`.

### Usage

1. Open the Streamlit app in your browser at `http://localhost:8501`.
2. Upload an image using the file uploader.
3. Enter a prompt in the text input field.
4. Click the "Generate caption" button to receive the generated caption and answer.

- Ensure that the Flask server is running before starting the Streamlit app.

### Future Development

- Optimize the models for better performance and accuracy.
- Add more functionalities such as object detection and image classification.
- Deploy the application on cloud platforms like AWS or GCP for better scalability.
