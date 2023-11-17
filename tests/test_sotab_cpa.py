from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from taitac import mapper

DATA_ROOT = Path("./data")
TRAIN_ROOT = DATA_ROOT / "Train"


def cpa_small_mapping():
    result = {}

    data = pd.read_csv(DATA_ROOT / "sotab_v2_cpa_training_set_small.csv")
    for _, row in data.iterrows():
        if row["table_name"] not in result:
            result[row["table_name"]] = {}
        result[row["table_name"]][row["column_index"]] = row["label"]

    return result


def cpa_small_parameterize():
    for table, data in cpa_small_mapping().items():
        marks = []
        if not TRAIN_ROOT.joinpath(table).exists():
            marks.append(pytest.mark.xfail(reason="data file is missing"))
        yield pytest.param(str(table), data, marks=marks, id=str(table))


@pytest.mark.parametrize(("path", "expected"), cpa_small_parameterize())
def test_cpa_small(path: str, expected: dict):
    result = mapper.map_headers(str(TRAIN_ROOT.joinpath(path).absolute()))
    for key, value in expected.items():
        assert key in result, expected
        assert result[key] == value, expected
