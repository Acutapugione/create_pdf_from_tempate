import os
import glob

def search_files_by_extension(folder_path: str, extension: str) -> list[str]:
    """
    Search for all files with a specified extension in a given folder.

    Args:
        folder_path (str): The path to the folder to search in.
        extension (str): The extension to filter files. (excluding the dot, e.g., "css")

    Returns:
        list: A list of file paths matching the extension.
    """
    # BASE_FOLDER = ".."
    # folder_path = os.path.join(BASE_FOLDER, folder_path)
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Folder {folder_path} not found.")
    
    def _file_generator():
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.' + extension):
                    yield os.path.join(root, file)

    return list(_file_generator())