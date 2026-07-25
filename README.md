# 🌸 Flower Species Recognition using VGG16 Transfer Learning

A deep learning-based flower species recognition system that classifies flower images into five different species using **Transfer Learning with VGG16**. The model is built using **TensorFlow/Keras** and deployed as an interactive **Streamlit** web application.

---

## 📌 Project Overview

This project demonstrates an end-to-end computer vision workflow for image classification using transfer learning. Instead of training a convolutional neural network from scratch, a pre-trained **VGG16** model is used as the feature extractor, allowing efficient learning with improved performance.

The system is capable of identifying five flower species from uploaded images through an interactive web interface.

---

## 🎯 Objectives

- Build an accurate flower image classification model.
- Apply Transfer Learning using VGG16.
- Improve model generalization using data augmentation.
- Evaluate model performance using multiple classification metrics.
- Deploy the trained model as a Streamlit web application.

---

## 🌼 Supported Flower Classes

- 🌼 Daisy
- 🌼 Dandelion
- 🌹 Roses
- 🌻 Sunflowers
- 🌷 Tulips

---

## 🧠 Model Architecture

**Base Model**

- VGG16 (Pre-trained on ImageNet)

**Transfer Learning Strategy**

- Frozen convolutional base
- Global Average Pooling
- Dense Layer (128 neurons)
- Dropout (0.5)
- Softmax Output Layer (5 Classes)

**Framework**

- TensorFlow / Keras

---

## 📂 Dataset

Dataset Source:

**Kaggle Flower Recognition Dataset**

Dataset Structure

```
train/
validation/
test/
sample/
```

Each class contains images belonging to one of the five flower species.

---

## 🔄 Data Preprocessing

The following preprocessing techniques were applied:

- Image resizing (180 × 180)
- Pixel normalization (1/255)
- Data augmentation
  - Rotation
  - Zoom
  - Horizontal Flip

---

## 🚀 Model Training

Training Configuration

| Parameter | Value |
|-----------|------:|
| Image Size | 180 × 180 |
| Batch Size | 32 |
| Epochs | 10 |
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Early Stopping | Enabled |

---

## 📊 Model Performance

### Overall Accuracy

**81% Validation Accuracy**

### Classification Report

| Flower | Precision | Recall | F1 Score |
|---------|----------:|--------:|---------:|
| Daisy | 0.88 | 0.88 | 0.88 |
| Dandelion | 0.93 | 0.88 | 0.90 |
| Roses | 0.92 | 0.69 | 0.79 |
| Sunflowers | 0.70 | 0.94 | 0.80 |
| Tulips | 0.73 | 0.69 | 0.71 |

**Overall Accuracy:** **81%**

---

## 📈 Evaluation Methods

The trained model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

Training and validation accuracy/loss curves were also generated during training.

---

## 💻 Streamlit Web Application

The project includes a fully functional Streamlit application where users can:

- Upload a flower image
- Predict the flower species
- View prediction confidence
- Receive real-time inference results

---

## 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- VGG16 Transfer Learning
- NumPy
- Matplotlib
- Scikit-learn
- Seaborn
- Pillow
- Streamlit

---

## 📁 Project Structure

```
flower-recognition-model/
│
├── app.py
├── Flower_Recognition_Model.ipynb
├── Flower_Recog_Model.keras
├── README.md
├── requirements.txt
├── LICENSE
│
├── sample/
├── train/
├── validation/
└── test/
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/PramishSubedi/flower-recognition-model.git
```

Move into the project

```bash
cd flower-recognition-model
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Streamlit App

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📦 Requirements

Main libraries used

```
streamlit
tensorflow
numpy
matplotlib
Pillow
scikit-learn
seaborn
```

---

## 🔮 Future Improvements

- Fine-tune the VGG16 model
- Support additional flower species
- Mobile-friendly interface
- Cloud deployment
- Real-time camera prediction
- Improve classification accuracy beyond 90%

---

## 👨‍💻 Author

**Pramish Subedi**

BSc (Hons) Computer Systems Engineering

Interested in:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Computer Vision
- Data Science

---

## ⭐ If you found this project useful

Please consider giving the repository a **Star ⭐**.
