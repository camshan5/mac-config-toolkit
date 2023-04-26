import json
import subprocess
from contextlib import contextmanager
from pathlib import Path


class DirTools:
    def __init__(self, path):
        self.path = Path(path)

    def get_directory_names(self):
        # get list of directories in given path
        dir_list = [d for d in self.path.iterdir() if d.is_dir()]

        # get names of directories
        dir_names = [d.name for d in dir_list]

        return sorted(dir_names)


class FileTools:
    def __init__(self, path):
        self.path = Path(path)

    def get_file_names(self):
        # get list of files in given path
        file_list = [f for f in self.path.iterdir() if f.is_file()]

        # get names of files
        file_names = [f.name for f in file_list]

        return sorted(file_names)

    @contextmanager
    def json_file_manager(self, file_name):
        file = self.path / file_name
        try:
            with open(file, "r") as f:
                data = json.load(f)
            yield data

        except Exception as e:
            print(f"Error: {e}")
            yield None
        finally:
            print("File closed...")
            pass


class UseSubprocess:
    def __init__(self, command: list):
        self.command = command

    def run_command(self):
        result = subprocess.run(self.command, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Error running {self.command}: {result.stderr}")

        return result.stdout
