import os
import sys
import pandas as pd
import pytest
import shutil
from pathlib import Path

sys.path.append(os.path.abspath(os.path.dirname("class_todo.py")) + "/src/packages")
import class_todo


PATH = str(Path(__file__).parent)
PATH_TO_DATA = f"{PATH}/data/"

todos = class_todo.ToDo(PATH_TO_DATA)


@pytest.fixture(scope="function")
def tmp_dir(tmpdir_factory):
    my_tmpdir = tmpdir_factory.mktemp("pytestdata")
    PATH_TO_DATA = my_tmpdir
    yield my_tmpdir
    shutil.rmtree(str(my_tmpdir))


@pytest.fixture(scope="session")
def df_empty():
    return pd.DataFrame(columns=["created", "task", "summary", "status", "owner"])


@pytest.fixture(scope="function")
def df_empty_stored(tmp_dir, df_empty):
    df_empty.to_csv(f"{tmp_dir}/todos.csv")
    return df_empty


def test_get_list_path_filename():
    assert (todos.get_list_path("todos") == PATH_TO_DATA + "todos.csv") \
            & (todos.get_list_filename("data") == "data.csv")


def test_create_check_list_exists(df_empty):
    todos.create_list("todos")
    df1 = todos.load_list("todos")
    if pd.testing.assert_frame_equal(df1, df_empty) == True:
        assert todos.check_list_exists("todos") == True


def test_load_store_list(df_empty, df_empty_stored):
    todos.store_list(df_empty, "todos")
    df1 = todos.load_list("todos")
    if pd.testing.assert_frame_equal(df_empty, df1) == True:
        pd.testing.assert_frame_equal(df_empty_stored, df1)

