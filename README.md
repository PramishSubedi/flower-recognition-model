# 🌸 Flower Recognition Model

A deep learning-based flower recognition system that classifies flower images into five different species using a Convolutional Neural Network (CNN). This project was developed using Python and TensorFlow/Keras and trained on a Kaggle flower image dataset.

---

## 📖 Project Overview

The objective of this project is to build an image classification model capable of recognizing different flower species from images. The model learns visual patterns from labelled flower images and predicts the correct class for new, unseen images.

This project demonstrates the complete deep learning workflow, including:

- Image preprocessing
- Data augmentation
- CNN model development
- Model training
- Performance evaluation
- Flower image prediction

---

## 🌼 Flower Classes

The model classifies the following flower species:

- 🌼 Daisy
- 🌼 Dandelion
- 🌹 Roses
- 🌻 Sunflowers
- 🌷 Tulips

---

## 🧠 Model Architecture

- Deep Learning Model: Custom Convolutional Neural Network (CNN)
- Framework: TensorFlow / Keras
- Programming Language: Python

---

## 📊 Model Performance

| Metric | Score |
|---------|------:|
| Accuracy | **81%** |
| Precision | **0.83** |
| Recall | **0.81** |
| F1-Score | **0.81** |

### Classification Report

| Flower | Precision | Recall | F1-Score |
|---------|----------:|-------:|---------:|
| Daisy | 0.88 | 0.88 | 0.88 |
| Dandelion | 0.93 | 0.88 | 0.90 |
| Roses | 0.92 | 0.69 | 0.79 |
| Sunflowers | 0.70 | 0.94 | 0.80 |
| Tulips | 0.73 | 0.69 | 0.71 |

---

## 🚀 Features

- Flower species recognition
- Deep learning image classification
- Custom CNN architecture
- Image preprocessing and augmentation
- Model evaluation using Precision, Recall and F1-Score
- Prediction on new flower images

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## 📂 Project Structure

```text
flower-recognition-model/
│
├── app.py
├── Flower_Recognition_Model.ipynb
├── Flower_Recog_Model.keras
├── train/
├── validation/
├── test/
├── sample/
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/PramishSubedi/flower-recognition-model.git
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## 📈 Future Improvements

- Improve accuracy using transfer learning (e.g., EfficientNet or MobileNetV2)
- Expand the dataset with additional flower species
- Deploy the model as a web application
- Optimise the model for faster inference
- Add real-time flower recognition from a webcam

---

## 👨‍💻 Author

**Pramish Subedi**

Computer Systems Engineering Student | Aspiring Data Scientist

---

## 📜 License

This project is licensed under the MIT License.
