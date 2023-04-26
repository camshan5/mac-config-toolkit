import os
from pprint import pprint

from dotenv import load_dotenv

from constants import (
    NVM_DIR,
    PYENV_ROOT,
    VS_CODE_EXTENSIONS_PATH,
    VS_CODE_EXTENSIONS_FILE,
)
from utils import DirTools, UseSubprocess, FileTools

load_dotenv()
USER_DIR = os.getenv("USER_DIR")


def get_homebrew_leaves():
    result = UseSubprocess(["brew", "leaves"]).run_command()

    leaves = result.strip().splitlines()

    return {"homebrew_packages": [{"name": p} for p in leaves]}


def get_node_versions_installed():
    node_versions_path = f"{NVM_DIR}/versions/node"
    directory = DirTools(node_versions_path)

    package_dict = {
        "node_versions": [{"version": d} for d in directory.get_directory_names()]
    }

    return package_dict


def get_pipx_venvs():
    result = UseSubprocess(["pipx", "list"]).run_command()

    packages = [
        line.strip()
        for line in result.splitlines()
        if line.strip().startswith("package")
    ]

    pipx_package_dict = {package.split()[1]: package.split()[2] for package in packages}

    return {
        "pipx_packages": [
            {"name": k, "version": v} for k, v in pipx_package_dict.items()
        ]
    }


def get_pyenv_installed_versions():
    pyenv_versions_path = f"{PYENV_ROOT}/versions"
    directory = DirTools(pyenv_versions_path)

    package_dict = {
        "pyenv_versions": [{"version": d} for d in directory.get_directory_names()]
    }

    return package_dict


def get_vscode_extensions():
    file_helper = FileTools(path=VS_CODE_EXTENSIONS_PATH)

    with file_helper.json_file_manager(VS_CODE_EXTENSIONS_FILE) as extensions:
        if extensions is not None:
            extensions_data = {
                "vscode_extensions": [
                    {
                        "name": e["identifier"]["id"].split(".")[1],
                        "identifier": e["identifier"],
                        "version": e["version"],
                    }
                    for e in extensions
                ]
            }

            return extensions_data

        else:
            return {"vscode_extensions": []}


if __name__ == "__main__":
    homebrew_packages_dict = get_homebrew_leaves()
    node_versions_dict = get_node_versions_installed()
    pipx_venvs_dict = get_pipx_venvs()
    pyenv_versions_dict = get_pyenv_installed_versions()
    vscode_extensions = get_vscode_extensions()

    merge_dicts = {
        **pipx_venvs_dict,
        **pyenv_versions_dict,
        **node_versions_dict,
        **homebrew_packages_dict,
        **vscode_extensions,
    }

    pprint(merge_dicts)
