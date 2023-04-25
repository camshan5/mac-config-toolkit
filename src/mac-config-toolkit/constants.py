import os
from pathlib import Path

HOME = Path.home()

DEFAULT_PIPX_HOME = HOME / ".local/pipx"
PIPX_HOME = Path(os.environ.get("PIPX_HOME", DEFAULT_PIPX_HOME)).resolve()

XDG_NVM_PATH = HOME / ".config/nvm"
NVM_DIR = Path(os.environ.get("NVM_DIR", XDG_NVM_PATH)).resolve()

DEFAULT_PYENV_ROOT = HOME / ".local/pyenv"
PYENV_ROOT = Path(os.environ.get("PYENV_ROOT", DEFAULT_PYENV_ROOT)).resolve()
