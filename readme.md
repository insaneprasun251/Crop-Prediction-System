# Crop Prediction System

This project is a simple machine‑learning–based web application that predicts the most suitable crop based on user‑provided agricultural parameters. The system uses a trained model (`model.pkl`) and a lightweight web interface built in Python.

## Project Overview
- The model takes numerical inputs such as temperature, humidity, rainfall, and soil details.
- A web form collects user inputs and sends them to the prediction function.
- The model output (best crop) is displayed back on the webpage.

## Repository Contents
```
app.py            - Main web application file
model.py          - Script used for training and preparing the model
model.pkl         - Trained machine learning model
templates/        - HTML templates for the interface
static/           - CSS/JS assets
dataset/          - Dataset used for training
requirements.txt  - Required Python libraries
```

## Installation
```bash
git clone https://github.com/insaneprasun251/Crop-Prediction-System.git
cd Crop-Prediction-System
pip install -r requirements.txt
```

## Usage
Run the application using:
```bash
python app.py
```
Open the browser and visit:
```
http://127.0.0.1:5000
```
Enter the required parameter values in the form and submit to get the predicted crop.

## Model Information
- The model is trained on the dataset provided in the repository.
- `model.py` handles loading the dataset, preprocessing, training the model, and exporting it as `model.pkl`.
- The web app loads `model.pkl` at startup and uses it to generate predictions.

## File Responsibilities
- **app.py**: Reads user inputs, loads the trained model, and returns the prediction.
- **model.py**: Reads dataset, trains the model, and saves it.
- **templates/**: Contains frontend HTML files.
- **static/**: Contains stylesheets, scripts, and images.

## Running Notes
- Ensure `model.pkl` remains in the project root.
- All input values must be numerical.

## Summary
This repository provides a straightforward crop prediction system combining a trained ML model with a web interface. Fill in the parameters, submit the form, and the system returns the predicted suitable crop.

