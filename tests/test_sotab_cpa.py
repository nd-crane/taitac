from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from taitac import mapper

DATA_ROOT = Path("./data")
TRAIN_ROOT = DATA_ROOT / "Train"


def small_dataset():
    result = {}

    data = pd.read_csv(DATA_ROOT / "sotab_v2_cpa_training_set_small.csv")
    for _, row in data.iterrows():
        if row["table_name"] not in result:
            result[row["table_name"]] = {}
        result[row["table_name"]][row["column_index"]] = row["label"]

    return result


def small_dataset_paramterize():
    for table in small_dataset():
        marks = []
        if not TRAIN_ROOT.joinpath(table).exists():
            marks.append(pytest.mark.xfail(reason="data file is missing"))
        yield pytest.param(str(table), marks=marks)


@pytest.fixture(scope="session")
def expected_small():
    result = {}

    data = pd.read_csv(DATA_ROOT / "sotab_v2_cpa_training_set_small.csv")
    for _, row in data.iterrows():
        if row["table_name"] not in result:
            result[row["table_name"]] = {}
        result[row["table_name"]][row["column_index"]] = row["label"]

    return result


@pytest.mark.parametrize(("path"), small_dataset_paramterize())
def test_cpa_small(path: str, expected_small: dict):
    result = mapper.map_headers(str(TRAIN_ROOT.joinpath(path).absolute()))
    for key, value in expected_small[path].items():
        assert key in result, result
        assert result[value] == value, result
