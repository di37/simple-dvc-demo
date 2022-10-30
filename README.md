## Environment Creation Phase

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

## Data Gathering and Preprocessing Phase

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

9 - Create `get_data.py` in src folder.

```bash
touch src/get_data.py
```

10 - Create `load_data.py` in src folder.

```bash
touch src/load_data.py
```

11 - Stage 1 included in `dvc.yaml` file.

```bash
dvc repro
```

It might throw an error. The fix to this issue is downgrade `pathspec` dependency.

```bash
pip install pathspec==0.9.0
```

**Important:** Whenever making changes, always run dvc command before committing to Git otherwise error will be thrown.

12 - Create `split_data.py` in src folder.

```bash
touch src/split_data.py
```

13 - Included stage 2 in `dvc.yaml` file.

## Modelling and Evaluation Phase

14 - Create `train_and_evaluate.py` in src folder.

```bash
touch src/train_and_evaluate.py
```

15 - Check for changes in the params.

```bash
dvc params diff
```

16 - Check for changes in the metrics.

```bash
dvc metrics diff
```

17 - Checking the metrics using dvc command.

```bash
dvc metrics show
```

## Testing Phase

18 - Install `pytest` and `tox` packages.

19 - Create `tox.ini` file and include required details.

20 - Create new folder `tests` and then create following files inside newly created folder.

```bash
touch tests/__init__.py tests/conftest.py tests/test_config.py
```

21 - To perform tests

```bash
pytest -v
```

22 - Create temporary environment for testing.

```bash
tox
```

23 - If `requirements.txt` file is updated.

```bash
tox -r
```

24 - Create file `setup.py` which will allow us to create custom package based on the folder name we pass as name parameter. Then we install our custom package.

```bash
pip install -e .
```

Optional - To create a sharable distribution package.

```bash
python setup.py sdist bdist_wheel
```

25 - Certain cases are required to be handled. Therefore, `handle_cases.ipynb` is created. These all are solved at Exploratory Data Analysis stage.

26 - In `test_config.py` file, we will include code for raising `NotInRange` error. Then run `pytest -v` for testing.

27 - For testing cases, always start the function name with `test_` otherwise pytest library will not consider of taking the functions for testing.
