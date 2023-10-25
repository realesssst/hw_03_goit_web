import os
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

EXTENSIONS = {
    "images": {"jpg", "png", "jpeg", "svg"},
    "videos": {"avi", "mp4", "mov", "mkv"},
    "documents": {"doc", "docx", "txt", "pdf", "xls", "pptx"},
    "music": {"mp3", "ogg", "wav", "amr"},
    "archives": {"zip", "gz", "tar"},
    "unknown": ...,
}

class FileSorter:
    def __init__(self, source_folder):
        self.source_folder = Path(source_folder).resolve()
        self.output_folder = self.source_folder / "sorted"
        self.file_mapping = {}

    def get_file_type(self, file_path):
        extension = file_path.suffix[1:].lower()
        for file_type, extensions in EXTENSIONS.items():
            if extension in extensions:
                return file_type
        return "unknown"

    def create_sorted_folders(self):
        for file_type in EXTENSIONS.keys():
            folder = self.output_folder / file_type
            folder.mkdir(parents=True, exist_ok=True)

    def process_file(self, file_path):
        file_type = self.get_file_type(file_path)
        destination = self.output_folder / file_type / file_path.name
        shutil.move(file_path, destination)

    def sort_files(self):
        self.create_sorted_folders()
        with ThreadPoolExecutor() as executor:
            for item in self.source_folder.iterdir():
                if item.is_file():
                    executor.submit(self.process_file, item)

if __name__ == "__main__":
    source_folder = "your_source_folder_path_here"
    file_sorter = FileSorter(source_folder)
    file_sorter.sort_files()
