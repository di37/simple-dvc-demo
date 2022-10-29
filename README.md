1 - Create conda environment.

```bash
conda create -n auto_mpg python=3.8 -y
```

2 - Activate conda environment.

```bash
conda activate auto_mpg
```

3 - Install the requirements.

```bash
pip install --no-cache-dir -r requirements.txt
```
4 - Create `template.py` file and execute.

5 - Download the dataset from
https://www.kaggle.com/datasets/uciml/autompg-dataset

6 - Intialize git and dvc repositories.
```bash
git init
```

```bash
dvc init
```

7 - Adding the dataset file to staging area in dvc.
```bash
dvc add data_given/auto-mpg.csv
```

```bash
git add .
```

```bash
git commit -m "first commit"
```

One liner update

```bash
git add . && git commit -m "Update README.md"
```

```bash
git remote add origin https://github.com/di37/simple-dvc-demo.git
git branch -M main
git push -u origin main
```

Stages included in dvc.yaml file.

```bash
dvc repro
```

It might throw an error. The fix to this issue is downgrade `pathspec` dependency.

```bash
pip install pathspec==0.9.0
```

**Important:** Whenever making changes, always run dvc command before committing to Git otherwise error will be thrown.
