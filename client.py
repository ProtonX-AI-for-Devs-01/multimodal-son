import streamlit as st
import requests
from PIL import Image
import io

# Streamlit app
def main():
    st.title("Image Captioning and Q&A App")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        user_prompt = st.text_input("Enter a prompt:")

        if st.button("Generate caption"):
            files = {'file': ('image.png', img_byte_arr, 'image/png')}
            data = {'prompt': user_prompt}
            response = requests.post('https://471d-34-16-205-164.ngrok-free.app/', files=files, data=data)

            if response.status_code == 200:
                result = response.json()
                st.markdown("""
                    #### Generated caption:
                   
                """)
                st.code(result['answer'], language='text')
            else:
                st.markdown("""
                #### Generated caption:
                ```
                            st.error("Error: Unable to get a response from the server.")
                ```
                ---
            """)
if __name__ == "__main__":
    main()