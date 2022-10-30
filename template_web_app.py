import os

dirs = [
    os.path.join("prediction_service", "model"),
    os.path.join("webapp", "static", "css"),
    os.path.join("webapp", "static", "script"),
    os.path.join("webapp", "templates"),
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files = [
    os.path.join("app.py"),
    os.path.join("prediction_service", "__init__.py"),
    os.path.join("prediction_service", "prediction.py"),
    os.path.join("webapp", "static", "css", "main.css"),
    os.path.join("webapp", "static", "script", "index.js"),
    os.path.join("webapp", "templates", "index.html"),
    os.path.join("webapp", "templates", "404.html"),
    os.path.join("webapp", "templates", "base.html"),
]

for file_ in files:
    with open(file_, "w") as f:
        pass
