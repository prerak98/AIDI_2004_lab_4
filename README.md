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

## Deployment

To deploy the application on a platform like PythonAnywhere or Heroku, follow these steps:

### PythonAnywhere

1. **Upload the project files to PythonAnywhere.**

2. **Create a virtual environment on PythonAnywhere:**

    ```sh
    mkvirtualenv --python=/usr/bin/python3.10 fishapp_venv
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r /home/yourusername/fish_species_predictor/requirements.txt
    ```

4. **Configure the WSGI file:**

    Edit the WSGI configuration file to include the following:

    ```python
    import sys
    import os

    # add your project directory to the sys.path
    project_home = '/home/yourusername/fish_species_predictor'
    if project_home not in sys.path:
        sys.path = [project_home] + sys.path

    # activate your virtual environment
    activate_this = '/home/yourusername/.virtualenvs/fishapp_venv/bin/activate_this.py'
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

    # set the working directory so relative paths (and template lookup) work
    os.chdir(project_home)

    # import flask app but need to call it "application" for WSGI to work
    from app import app as application  # noqa
    ```

5. **Reload the web app on PythonAnywhere.**

### Heroku

1. **Create a `Procfile` for Heroku:**

    ```sh
    web: gunicorn app:app
    ```

2. **Commit and push the changes to GitHub:**

    ```sh
    git add .
    git commit -m "Initial commit"
    git push origin main
    ```

3. **Deploy to Heroku:**

    ```sh
    heroku create
    git push heroku main
    heroku open
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
