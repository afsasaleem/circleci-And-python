# Sentiment Analysis Project with CircleCI

This project analyzes the sentiment (positive, negative, or neutral) of a given sentence using the `TextBlob` library. The sentiment score ranges from -1 (most negative) to 1 (most positive).

## Prerequisites

- Python 3.x installed on your machine
- CircleCI account
- `TextBlob` library installed (`pip install textblob`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/afsasaleem/circleci-And-python.git
cd circleci-And-python

2. Install dependencies:
```bash
pip install -r requirements.txt

(Optional) Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

Usage
Run the app:
```bash
python app.py

Testing
To run tests locally:
```bash
python -m unittest discover
CircleCI automatically runs tests on every push to GitHub. The configuration is in .circleci/config.yml.

CI/CD Pipeline
CircleCI is used for continuous integration and deployment.
On each Git push, CircleCI runs automated tests and builds the application.
Configure your pipeline in .circleci/config.yml.

Setting up CircleCI:
Link your GitHub repo with CircleCI.
Push changes to trigger the CI/CD pipeline.
