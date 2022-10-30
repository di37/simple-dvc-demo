import os

dirs = [
    "data_given",
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "report",
    "saved_models",
    "src",
    "tests"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py"),
    os.path.join("tests", "__init__.py"),
    os.path.join("tests", "conftest.py"),
    os.path.join("tests", "test_config.py"),
]

for file_ in files:
    with open(file_, "w") as f:
        pass