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

8 - Include the required information in `params.yaml` file

9 - Create `get_data.py` in src folder -> `touch src/get_data.py`.

10 - Included params and done with coding part in `get_data.py` followed by committing to github.

11 - Create `load_data.py` in src folder -> `touch src/load_data.py`.

12 - Done with coding part in `load_data.py`.

13 - Stage 1 included in `dvc.yaml` file.

```bash
dvc repro
```

It might throw an error. The fix to this issue is downgrade `pathspec` dependency.

```bash
pip install pathspec==0.9.0
```

**Important:** Whenever making changes, always run dvc command before committing to Git otherwise error will be thrown.

14 - Create `split_data.py` in src folder -> `touch src/split_data.py`.

15 - Included stage 2 in `dvc.yaml` file.
