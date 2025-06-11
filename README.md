# Classification Tabular Datasets

This repository contains numerous benchmark tabular datasets for testing various classification algorithms.

Check also [Regression Tabular Datasets](https://github.com/cezary986/regression_tabular_datasets) and [Survival Analysis Tabular Datasets](https://github.com/cezary986/survival_tabular_datasets)

All datasets are splitted to train and test parts. If whole unsplitted dataset was accessible it is also splitted into 10-fold cross validation datasets. Each dataset contains target column names **class** for prediction. Files in parquet data format is used which could be easily loaded using pandas Python package.

| Dataset name | Rows | Columns | Missing values | Classes |
|---|---|---|---|---|
| [adult](https://archive.ics.uci.edu/ml/datasets/adult/) | 32561 | 14 (6 numerical and 8 categorical) | yes | 2 |
| [anneal](https://archive.ics.uci.edu/ml/datasets/Annealing) | 898 | 38 (6 numerical and 32 categorical) | no | 5 |
| [audiology](https://archive.ics.uci.edu/ml/datasets/Audiology+%28Standardized%29) | 226 | 69 (0 numerical and 69 categorical) | yes | 24 |
| [auto-mpg](https://archive.ics.uci.edu/ml/datasets/auto+mpg) | 398 | 7 (5 numerical and 2 categorical) | yes | 3 |
| [autos](https://archive.ics.uci.edu/ml/datasets/Automobile) | 205 | 25 (15 numerical and 10 categorical) | yes | 6 |
| [balance-scale](https://archive.ics.uci.edu/ml/datasets/balance+scale) | 625 | 4 (4 numerical and 0 categorical) | no | 3 |
| [breast-cancer](https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+diagnostic>) | 286 | 9 (0 numerical and 9 categorical) | yes | 2 |
| [bupa-liver-disorders](https://archive.ics.uci.edu/ml/datasets/liver+disorders) | 345 | 6 (6 numerical and 0 categorical) | no | 2 |
| [car](https://archive.ics.uci.edu/ml/datasets/Car+Evaluation) | 1728 | 6 (0 numerical and 6 categorical) | no | 4 |
| [churn](https://www.kaggle.com/competitions/customer-churn-prediction-2020/data) | 4250 | 19 (15 numerical and 4 categorical) | no | 2 |
| [cleveland](https://archive.ics.uci.edu/ml/datasets/heart+disease) | 303 | 13 (6 numerical and 7 categorical) | yes | 5 |
| [connect-4](http://archive.ics.uci.edu/ml/datasets/connect-4) | 67557 | 42 (0 numerical and 42 categorical) | no | 3 |
| [covertype](https://archive.ics.uci.edu/ml/datasets/Covertype?ref=datanews.io) | 581011 | 54 (10 numerical and 44 categorical) | no | 7 |
| [credit-a](https://archive.ics.uci.edu/ml/datasets/Credit+Approval) | 690 | 15 (6 numerical and 9 categorical) | yes | 2 |
| [credit-g](https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29) | 1000 | 20 (7 numerical and 13 categorical) | no | 2 |
| [cylinder-bands](https://archive.ics.uci.edu/ml/datasets/Cylinder+Bands) | 540 | 35 (17 numerical and 18 categorical) | yes | 2 |
| [diabetes](https://archive.ics.uci.edu/ml/datasets/Diabetes) | 768 | 8 (8 numerical and 0 categorical) | no | 2 |
| [echocardiogram](https://archive.ics.uci.edu/ml/datasets/Echocardiogram) | 131 | 11 (9 numerical and 2 categorical) | yes | 2 |
| [ecoli](https://archive.ics.uci.edu/ml/datasets/ecoli) | 336 | 7 (7 numerical and 0 categorical) | no | 8 |
| [flag](https://archive.ics.uci.edu/ml/datasets/Flags) | 194 | 28 (10 numerical and 18 categorical) | no | 4 |
| [glass](https://archive.ics.uci.edu/ml/datasets/glass+identification) | 214 | 9 (9 numerical and 0 categorical) | no | 6 |
| [haberman](https://archive.ics.uci.edu/ml/datasets/haberman's+survival) | 306 | 3 (3 numerical and 0 categorical) | no | 2 |
| [hayes-roth](https://archive.ics.uci.edu/ml/datasets/Hayes-Roth) | 132 | 4 (0 numerical and 4 categorical) | no | 3 |
| [heart-c](https://archive.ics.uci.edu/ml/datasets/Heart+Disease) | 303 | 13 (6 numerical and 7 categorical) | yes | 2 |
| [heart-statlog](https://archive.ics.uci.edu/ml/datasets/statlog+heart>) | 270 | 13 (7 numerical and 6 categorical) | no | 2 |
| [hepatitis](https://archive.ics.uci.edu/ml/datasets/hepatitis) | 155 | 19 (6 numerical and 13 categorical) | yes | 2 |
| [horse-colic](https://archive.ics.uci.edu/ml/datasets/Horse+Colic) | 368 | 22 (7 numerical and 15 categorical) | yes | 2 |
| [hr-evaluation](https://www.kaggle.com/datasets/muhammadimran112233/employees-evaluation-for-promotion) | 54808 | 11 (5 numerical and 6 categorical) | yes | 2 |
| [hungarian-heart-disease](https://archive.ics.uci.edu/ml/datasets/Heart+Disease) | 294 | 13 (6 numerical and 7 categorical) | yes | 2 |
| [iris](https://archive.ics.uci.edu/ml/datasets/iris) | 150 | 4 (4 numerical and 0 categorical) | no | 3 |
| [lymphography](https://archive.ics.uci.edu/ml/datasets/Lymphography) | 148 | 18 (3 numerical and 15 categorical) | no | 4 |
| [magic](https://archive.ics.uci.edu/ml/datasets/magic+gamma+telescope) | 19020 | 10 (10 numerical and 0 categorical) | no | 2 |
| [monk-1](https://archive.ics.uci.edu/ml/datasets/MONK's+Problems) | 324 | 6 (0 numerical and 6 categorical) | no | 2 |
| [monk-2](https://archive.ics.uci.edu/ml/datasets/MONK's+Problems) | 369 | 6 (0 numerical and 6 categorical) | no | 2 |
| [monk-3](https://archive.ics.uci.edu/ml/datasets/MONK's+Problems) | 554 | 6 (0 numerical and 6 categorical) | no | 2 |
| [mushroom](https://archive.ics.uci.edu/ml/datasets/mushroom) | 8124 | 22 (0 numerical and 22 categorical) | yes | 2 |
| [nursery](https://archive.ics.uci.edu/ml/datasets/nursery) | 12960 | 8 (0 numerical and 8 categorical) | no | 5 |
| [phoneme](https://www.openml.org/search?type=data&sort=runs&id=1489&status=active) | 5404 | 5 (5 numerical and 0 categorical) | no | 2 |
| [poker-hand](https://archive.ics.uci.edu/ml/datasets/Poker+Hand) | 1025010 | 10 (10 numerical and 0 categorical) | no | 10 |
| [segment](https://archive.ics.uci.edu/ml/datasets/image+segmentation) | 2310 | 19 (19 numerical and 0 categorical) | no | 7 |
| [seismic-bumps](https://archive.ics.uci.edu/ml/datasets/seismic-bumps) | 2584 | 18 (14 numerical and 4 categorical) | no | 2 |
| [sonar](http://archive.ics.uci.edu/ml/datasets/connectionist+bench+sonar,+mines+vs.+rocks>) | 208 | 60 (60 numerical and 0 categorical) | no | 2 |
| [soybean](https://archive.ics.uci.edu/ml/datasets/Soybean+Large>) | 683 | 35 (0 numerical and 35 categorical) | yes | 19 |
| [tic-tac-toe](https://archive.ics.uci.edu/ml/datasets/Tic-Tac-Toe+Endgame) | 958 | 9 (0 numerical and 9 categorical) | no | 2 |
| [titanic](https://www.kaggle.com/c/titanic) | 2201 | 3 (0 numerical and 3 categorical) | no | 2 |
| [vote](https://archive.ics.uci.edu/ml/datasets/congressional+voting+records) | 435 | 16 (0 numerical and 16 categorical) | yes | 2 |
| [wilt](https://archive.ics.uci.edu/ml/datasets/wilt) | 4839 | 5 (5 numerical and 0 categorical) | no | 2 |
| [wine](https://archive.ics.uci.edu/ml/datasets/wine) | 178 | 13 (13 numerical and 0 categorical) | no | 3 |
| [zoo](https://archive.ics.uci.edu/ml/datasets/zoo) | 101 | 16 (1 numerical and 15 categorical) | no | 7 |

Dataset summary is also available in csv file [datasets_summary.csv](https://github.com/cezary986/classification_tabular_datasets/blob/main/datasets_summary.csv) in root repo directory.


## Reading datasets using Python package

This repository also contains a tiny Python package which allows you to use datasets without the need to clone whole repository.
 
 To install it use the following command:

```bash
pip install git+https://github.com/cezary986/classification_tabular_datasets
```

The package exports two functions: `read_full_dataset` and `read_dataset_train_test`.
The first one reads full dataset and returns a tuple of X and y, where X is data and y are labels.
The second one reads dataset splitted to train and test parts and returns a tuple of X_train, y_train, X_test, y_test. 

Example:

```python
import clfdatasets

# print list of all available datasets
print(", ".join(clfdatasets.AVAILABLE_DATASETS))

# reads whole dataset without train/test split
X, y = clfdatasets.read_full_dataset("iris")

# reads dataset splitted into train/test
X_train, y_train, X_test, y_test = clfdatasets.read_dataset_train_test("iris")

# reads given dataset cross-validation fold
X_train, y_train, X_test, y_test = clfdatasets.read_dataset_train_test("iris",  cv_fold=3)
```