# Image Classification App with Streamlit 🖼️

A user-friendly web application built with Streamlit that performs real-time image classification using a pre-trained ResNet50 model. Upload any image, and the app will identify objects in it with confidence scores.

![App Demo](assets/demo.png)

## 🌟 Features

- Real-time image classification using ResNet50
- Support for multiple image formats (JPG, JPEG, PNG)
- Interactive web interface built with Streamlit
- Top 5 predictions with confidence scores
- Visual confidence indicators
- Result history tracking
- Error handling and user feedback

## 📋 Prerequisites

Before running this application, make sure you have Python 3.7+ installed on your system. The following packages are required:

```bash
- streamlit
- tensorflow
- pillow
- numpy
```

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/image-classification-app.git
cd image-classification-app
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Upload an image using the file uploader

4. Click the "Predict" button to see the classification results

## 📸 Example Results

Here are some example classifications:

### Cat Image Classification
![Cat Classification](assets/cat_example.png)
- Top prediction: Persian cat (99.2%)
- Other predictions: Tabby, Siamese cat

### Dog Image Classification
![Dog Classification](assets/dog_example.png)
- Top prediction: Golden retriever (98.7%)
- Other predictions: Labrador retriever, Sporting dog

## 📁 Project Structure

```
image-classification-app/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── assets/                # Example images and screenshots
│   ├── demo.png
│   ├── cat_example.png
│   └── dog_example.png
└── output/                # Directory for saving results
```

## 📋 Requirements.txt

```
streamlit==1.31.0
tensorflow==2.15.0
pillow==10.2.0
numpy==1.24.3
```

## 🔧 Customization

You can customize the application by:

1. Changing the model:
   - Replace ResNet50 with other pre-trained models
   - Use your own custom-trained model

2. Modifying the interface:
   - Adjust the number of predictions shown
   - Change the layout and styling
   - Add new features like batch processing

3. Enhancing visualization:
   - Add more detailed analytics
   - Include different types of charts
   - Implement image preprocessing options

