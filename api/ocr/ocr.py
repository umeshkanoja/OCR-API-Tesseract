import pytesseract
import asyncio

async def read_image(img_path: str, lang: str = 'eng') -> str:
    """
    Asynchronously reads an image using Tesseract OCR and returns the extracted text.

    Args:
        img_path (str): Path to the image file.
        lang (str, optional): Language code for the OCR. Defaults to 'eng'.

    Returns:
        str: The extracted text from the image.

    Raises:
        Exception: If there is an error processing the image.
    """
    try:
        # Use following code to set the path to the Tesseract OCR executable in Windows.
        # This is only needed if you are using Windows and path is not added in environment variables
        # pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        
        text = pytesseract.image_to_string(img_path, lang=lang)
        # Sleep for 2 seconds to simulate server processing time
        await asyncio.sleep(2)
        
        return text
    except Exception as err:
        # Print the error message and return an error string
        print(err)
        return "[ERROR] Unable to process file: {0}".format(img_path)
    