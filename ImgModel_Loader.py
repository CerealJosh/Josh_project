import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
import os

# Define the path to your trained model and the directory of images you want to classify
model_path = 'C:/Users/Josh/source/repos/ProjectServer/Josh-main/VGG16_image_classifier.h5'
image_dir = 'C:/Users/Josh/source/repos/ProjectServer/Josh-main/Fire.png'

# Load the trained model
model = tf.keras.models.load_model(model_path)
model.class_names = ['blue', 'green', 'orange', 'white']  # Define the class names

# Define image dimensions (must match the dimensions used during training)
img_height = 224
img_width = 224


def load_and_preprocess_image(img_path):
    """
    Load and preprocess a single image for the model.
    """
    img = image.load_img(img_path, target_size=(img_height, img_width))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess for MobileNetV2
    return img_array

def predict_image(img_path):
    """
    Predict the class of a single image using the trained model.
    """
    img_array = load_and_preprocess_image(img_path)
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    predicted_class = model.class_names[predicted_index]
    return predicted_class

def classify_images(image_dir):
    """
    Classify all images in the given directory.
    """
    image_files = image_dir

    predicted_class = predict_image(image_dir)
    print(f"Predicted Class: {predicted_class}")

# Run the classification
classify_images(image_dir)