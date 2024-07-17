# Fish Species Predictor

This project is a Flask web application that predicts the species of a fish based on its physical measurements. The model is trained using the Fish Market dataset from Kaggle.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [License](#license)

## Introduction

The Fish Species Predictor uses a machine learning model to predict the species of a fish based on its weight, length, height, and width. The model is built using scikit-learn and deployed using Flask.

## Features

- Input fish measurements (weight, length, height, width) through a web form.
- Predict the species of the fish using a pre-trained model.
- Display the prediction on the web page.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/fish_species_predictor.git
    cd fish_species_predictor
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv fishapp_venv
    fishapp_venv\Scripts\activate  # On Windows
    source fishapp_venv/bin/activate  # On macOS/Linux
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Train the model and save it:**

    Ensure the dataset (`Fish.csv`) is in the project directory and run the following script to train and save the model:

    ```sh
    python train_model.py
    ```

2. **Run the Flask application:**

    Set the Flask app environment variable and run the application:

    ```sh
    set FLASK_APP=app.py
    flask run
    ```

    Or on PowerShell:

    ```sh
    $env:FLASK_APP="app.py"
    flask run
    ```

3. **Access the web application:**

    Open your web browser and go to `http://127.0.0.1:5000/`.
