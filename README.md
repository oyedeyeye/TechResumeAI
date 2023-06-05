# <<<<<<< HEAD

TechResumeAI

> > > > > > > ffe3daf03c37556f1bb21c9fa70ff9331a758a71

# TechResumeAI

The scope of this project is to develop a web application that assists ALX software engineering internship graduates in creating powerful, captivating, and ATS-compliant resumes. The application will utilize GPT's API to rewrite and transform user responses to specific resume questionnaires, generating job-winning content based on Certified Professional Resume Writer (CPRW) writing guide and Google's XYZ resume formula.

# Development Environment Setup

The project uses `python3`, `python3-pip`, `MySQL`

# Virtual environment setup

A virtual environment allows you to isolate the dependencies for your project, preventing conflicts between different projects on your machine. You can create a new virtual environment using the venv module that comes with Python.

Create the project directory

```
mkdir TechResumeAI/
cd TechResumeAI/
```

create a new virtual environment:

`python3 -m venv venv`

Activate the virtual environment:

`source venv/bin/activate`

# Install Flask and SQLAlchemy

You can install Flask and Flask-SQLAlchemy, which provides additional utilities for working with SQLAlchemy in Flask:

`pip install Flask SQLAlchemy Flask-SQLAlchemy`

# Install the necessary Python libraries and packages

Install other packages and libraries
PyPDF2 : Python module for pdf conversion
python-docx: Python module for docx
openai: OpenAI Python client

`pip install PyPDF2 python-docx openai`

# Install MySQL Connector for Python

To connect your Python application to MySQL, you'll need a connector. You can install it with the following command:

`pip install mysql-connector-python`

To run the application:

`python app.py`
