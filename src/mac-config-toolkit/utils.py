import subprocess
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


class UseSubprocess:
    def __init__(self, command: list):
        self.command = command

    def run_command(self):
        result = subprocess.run(self.command, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Error running {self.command}: {result.stderr}")

        return result.stdout
