import os
from typing import Tuple
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from joblib import dump
import time

PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(PATH, "../data/diabetes.csv")
MODEL_PATH = os.path.join(PATH, "../models/")


def fetch_data() -> pd.DataFrame:
    csv_data = pd.read_csv(DATA_PATH)
    return csv_data


def prepare_data(
    df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    target = df["Outcome"]
    train_data = df.drop(columns=["Outcome"])

    X_train, X_test, y_train, y_test = train_test_split(
        train_data, target, test_size=0.2, random_state=0
    )
    return X_train, X_test, y_train, y_test


def train_regressor(X_train: pd.DataFrame, y_train: pd.Series):
    reg = LinearRegression().fit(X_train, y_train)

    model_name = f"regressor_{int(time.time())}"

    dump(reg, MODEL_PATH + model_name + ".joblib")

    return reg


def generate_predictions(model, X_test: pd.DataFrame) -> np.ndarray:
    preds = model.predict(X_test)
    return preds


if __name__ == "__main__":
    df = fetch_data()

    X_train, X_test, y_train, y_test = prepare_data(df)

    reg = train_regressor(X_train, y_train)

    preds = generate_predictions(reg, X_test)

    print(
        f"The mean absolute error is:{metrics.mean_absolute_error(y_test, preds): .2f}"
    )
