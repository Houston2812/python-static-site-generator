from copy import copy
from typing import List
from pathlib import Path
import shutil

class Parser:
    def __init__(self) -> None:
        self.extensions: List[str] = List()

    def valid_extension(self, extension: str) -> bool:
        if extension in self.extensions:
            return True
        else:
            return False

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError
    
    def read(self, path: Path):
        with open(path) as file:
            return file.read()

    def write(self, path: Path, dest: Path, content: str, ext: str = ".html"):
        full_path = dest / path.with_suffix(ext).name

        with open(full_path) as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))

class ResourceParser(Parser):
    def __init__(self) -> None:
        self.extensions = List(".jpg", ".png", ".gif", ".css", ".html")

        super().__init__()

    def parse(self, path: Path, source: Path, dest: Path):
        super().copy(path, source, dest)
