from typing import Optional

import pandas as pd

_BASE_URL = (
    "https://github.com/cezary986/clalassification_tabular_datasets/raw/refs/heads/main"
)
_LABEL_COLUMN = "class"
AVAILABLE_DATASETS: list[str] = [
    "adult",
    "anneal",
    "audiology",
    "auto-mpg",
    "autos",
    "balance-scale",
    "breast-cancer",
    "bupa-liver-disorders",
    "car",
    "churn",
    "cleveland",
    "connect-4",
    "covertype",
    "credit-a",
    "credit-g",
    "cylinder-bands",
    "diabetes",
    "echocardiogram",
    "ecoli",
    "flag",
    "glass",
    "haberman",
    "hayes-roth",
    "heart-c",
    "heart-statlog",
    "hepatitis",
    "horse-colic",
    "hr-evaluation",
    "hungarian-heart-disease",
    "iris",
    "lymphography",
    "magic",
    "monk-1",
    "monk-2",
    "monk-3",
    "mushroom",
    "nursery",
    "phoneme",
    "poker-hand",
    "segment",
    "seismic-bumps",
    "sonar",
    "soybean",
    "tic-tac-toe",
    "titanic",
    "vote",
    "wilt",
    "wine",
    "zoo",
]


def read_full_dataset(dataset_name: str) -> tuple[pd.DataFrame, pd.Series]:
    """Reads full dataset and returns a tuple of X and y, where X is data and y are
    labels.

    Args:
        dataset_name (str): name of the dataset (to get list of available datasets use
            clfdatasets.DATASETS_NAME)

    Raises:
        ValueError: for invalid dataset_name

    Returns:
        tuple[pd.DataFrame, pd.Series]: X and y

    Example:
        >>> X, y = read_full_dataset("iris")
    """
    if dataset_name not in AVAILABLE_DATASETS:
        raise ValueError(
            f"dataset_name must be one of [{', '.join(AVAILABLE_DATASETS)}]"
        )
    df = pd.read_parquet(f"{_BASE_URL}/{dataset_name}/{dataset_name}.parquet")
    X, y = df.drop(_LABEL_COLUMN, axis=1), df[_LABEL_COLUMN]
    return X, y


def read_dataset_train_test(
    dataset_name: str, cv_fold: Optional[int] = None
) -> tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    """Reads dataset splitted into train and test parts. and returns a tuple containing
    X_train, y_train, X_test, y_test, where X is data and y are labels.

    Args:
        dataset_name (str): name of the dataset (to get list of available datasets use
            clfdatasets.DATASETS_NAME)
        cv_fold (Optional[int], optional): cv fold number. If none is provided it will
            read default train and test split.

    Raises:
        ValueError: for invalid dataset_name

    Returns:
        tuple[pd.DataFrame, pd.Series]: tuple containing X_train, y_train, X_test,
            y_test

    Example:
        >>> Reads default train and test split
        >>> X_train, y_train, X_test, y_test = read_dataset_train_test("iris")
        >>> Reads given cv fold train and test parts
        >>> X_train, y_train, X_test, y_test = read_dataset_train_test(
        >>>    "iris", cv_fold=3
        >>> )
    """
    if dataset_name not in AVAILABLE_DATASETS:
        raise ValueError(
            f"dataset_name must be one of [{', '.join(AVAILABLE_DATASETS)}]"
        )
    if cv_fold is None:
        df_train = pd.read_parquet(
            f"{_BASE_URL}/{dataset_name}/train_test/train.parquet"
        )
        X_train, y_train = df_train.drop(_LABEL_COLUMN, axis=1), df_train[_LABEL_COLUMN]
        df_test = pd.read_parquet(f"{_BASE_URL}/{dataset_name}/train_test/test.parquet")
        X_test, y_test = df_test.drop(_LABEL_COLUMN, axis=1), df_test[_LABEL_COLUMN]
        return X_train, y_train, X_test, y_test
    if cv_fold is not None and cv_fold < 1 or cv_fold > 10:
        raise ValueError("cv_fold must be in range 1-10")
    df_train = pd.read_parquet(
        f"{_BASE_URL}/{dataset_name}/cv/{str(cv_fold)}/train.parquet"
    )
    X_train, y_train = df_train.drop(_LABEL_COLUMN, axis=1), df_train[_LABEL_COLUMN]
    df_test = pd.read_parquet(
        f"{_BASE_URL}/{dataset_name}/cv/{str(cv_fold)}/test.parquet"
    )
    X_test, y_test = df_test.drop(_LABEL_COLUMN, axis=1), df_test[_LABEL_COLUMN]
    return X_train, y_train, X_test, y_test
