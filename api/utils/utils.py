import shutil
import os

def _save_file_to_server(
    uploaded_file: UploadFile,
    path: str,
    save_as: str
) -> str:
    """
    Save an uploaded file to the server.

    Args:
        uploaded_file (UploadFile): The uploaded file to save.
        path (str): The path to save the file to.
        save_as (str): The name to save the file as.

    Returns:
        str: The full path to the saved file.
    """
    temp_file = os.path.join(path, save_as)
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    print(f"Temp file path: {temp_file}")
    return temp_file
