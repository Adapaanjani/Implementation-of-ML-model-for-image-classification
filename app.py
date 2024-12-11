import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Set page configuration
st.set_page_config(
    page_title="Image Classifier",
    page_icon="🖼️",
    layout="centered"
)

def load_model():
    """Load pre-trained ResNet50 model"""
    return ResNet50(weights='imagenet')

def preprocess_image(img):
    """Preprocess image for model prediction"""
    # Resize image to 224x224 pixels
    img = img.resize((224, 224))
    # Convert to array and expand dimensions
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    # Preprocess input for ResNet50
    x = preprocess_input(x)
    return x

def predict_image(model, img):
    """Make prediction on preprocessed image"""
    # Get model predictions
    preds = model.predict(img)
    # Decode predictions to human-readable labels
    return decode_predictions(preds, top=5)[0]

def main():
    # Page title
    st.title("📸 Image Classification App")
    st.write("Upload an image and the app will identify what's in it!")
    
    # Load model
    with st.spinner("Loading model... Please wait..."):
        model = load_model()
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        try:
            # Display uploaded image
            img = Image.open(uploaded_file)
            st.image(img, caption="Uploaded Image", use_column_width=True)
            
            # Add prediction button
            if st.button("Predict"):
                with st.spinner("Analyzing image..."):
                    # Preprocess image
                    processed_img = preprocess_image(img)
                    
                    # Make prediction
                    predictions = predict_image(model, processed_img)
                    
                    # Display results
                    st.subheader("Predictions:")
                    for i, (imagenet_id, label, score) in enumerate(predictions):
                        progress_bar = st.progress(0)
                        progress_bar.progress(float(score))
                        st.write(f"{i+1}. {label} ({score:.2%} confidence)")
                        
        except Exception as e:
            st.error(f"Error occurred while processing the image: {e}")
            
    # Add information about the model
    st.sidebar.title("About")
    st.sidebar.info(
        "This app uses ResNet50 pre-trained on ImageNet to classify images. "
        "It can recognize 1000 different categories of objects."
    )
    
    # Add usage instructions
    st.sidebar.title("Instructions")
    st.sidebar.write(
        "1. Upload an image using the file uploader\n"
        "2. Click the 'Predict' button\n"
        "3. View the top 5 predictions with confidence scores"
    )

if __name__ == "__main__":
    main()