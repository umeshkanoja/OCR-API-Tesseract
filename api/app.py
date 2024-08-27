from fastapi import FastAPI, File, UploadFile
from typing import List
import time
import asyncio
import ocr
import utils

app = FastAPI()

@app.get("/", response_model=dict[str, str])
def home() -> dict[str, str]:
    """
    Endpoint: /

    This function returns a message indicating the endpoint to visit to perform OCR.

    Returns:
        dict[str, str]: A dictionary containing a message indicating the endpoint to visit for OCR.
    """
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}

@app.post("/api/v1/extract_text", response_model=dict[str, str | float])
async def extract_text(
    images: List[UploadFile] = File(...),
) -> dict[str, str | float]:
    """
    Extract text from uploaded images.

    Args:
        images (List[UploadFile]): List of images to extract text from.

    Returns:
        dict[str, Union[str, float]]: A dictionary containing the extracted text
            for each image and the time taken to process the images.
    """
    response = {}
    s = time.time()
    tasks = []
    for img in images:
        print("Images Uploaded: ", img.filename)
        temp_file = utils._save_file_to_server(img, path="./", save_as=img.filename)
        tasks.append(asyncio.create_task(ocr.read_image(temp_file)))
    text = await asyncio.gather(*tasks)
    for i, text_content in enumerate(text):
        response[images[i].filename] = text_content
    response["Time Taken"] = round((time.time() - s),2)
    return response
