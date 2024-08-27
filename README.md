
# OCR API using Tesseract and FastAPI

## Introduction

This project is a simple OCR (Optical Character Recognition) API built using FastAPI (a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints). We're using Tesseract OCR for extracting text from images.

The API is built with FastAPI. It has a single endpoint `/api/v1/extract_text` for extracting text from uploaded images. The endpoint accepts a list of images in form-data format. The extracted text for each image is returned in the response.

The API also has a home endpoint `/` which returns a message indicating the endpoint to visit for OCR.

## Setup

### Install Dependent packages

1. `py -m pip install fastapi`
2. `py -m pip install pytesseract`
1. `py -m pip install python-multipart`
1. `py -m pip install uvicorn`

### Run server

1. `cd api`
1. build project: `py .\app.py`
1. run server using: `py -m uvicorn app:app --reload`
1. open http://127.0.0.1:8000/docs
    * Please verify port from run server command and update here as required.
