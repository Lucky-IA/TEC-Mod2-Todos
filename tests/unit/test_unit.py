import os
import sys
import pandas as pd
import pytest
import shutil
from pathlib import Path
from datetime import datetime

sys.path.append(os.path.abspath(os.path.dirname("class_todo.py")) + "/src/packages")
import class_todo


PATH = str(Path(__file__).parent)
PATH_TO_DATA = f"{PATH}/data/"

todos = class_todo.ToDo(PATH_TO_DATA)


@pytest.fixture(scope="function")
def tmp_dir(tmpdir_factory):

    """Generate temp directory"""

    my_tmpdir = tmpdir_factory.mktemp("pytestdata")
    PATH_TO_DATA = my_tmpdir
    yield my_tmpdir
    shutil.rmtree(str(my_tmpdir))


@pytest.fixture(scope="session")
def df_empty():

    """Return dataframe columns"""
    
    return pd.DataFrame(columns=["created", "task", "summary", "status", "owner"])


@pytest.fixture(scope="session")
def df_full(new_row):

    """Return dataframe new row"""
    
    return pd.DataFrame(
        [new_row], columns=["created", "task", "summary", "status", "owner"]
    )


@pytest.fixture(scope="function")
def df_full_stored(tmp_dir, df_full):
    
    """Return dataframe full stored"""
    
    df_full.to_csv(f"{tmp_dir}/todos.csv")
    return df_full


@pytest.fixture(scope="function")
def df_empty_stored(tmp_dir, df_empty):
   
    """Return dataframe empty stored"""
    
    df_empty.to_csv(f"{tmp_dir}/todos.csv")
    return df_empty


@pytest.fixture(scope="session")
def new_row():
    
    """Return default new task"""
    
    return {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": "cocinar",
        "summary": "Cocinar algo rico",
        "status": "todo",
        "owner": "Andre",
    }



def test_get_list_path_1():
    """ Test get list path """
    assert todos.get_list_path("todos") == PATH_TO_DATA + "todos.csv"


def test_get_list_path_2():
    """ Test get list path """
    assert todos.get_list_path("test") == PATH_TO_DATA + "test.csv"


def test_get_filename_1():
    """ Test get filename """
    assert todos.get_list_filename("data") == "data.csv"


def test_get_filename_2():
    """ Test get filename """
    assert (todos.get_list_filename("data_1") == "data_1.csv") \
            & (todos.get_list_filename("data_2") == "data_2.csv")


def test_create_list(tmp_dir, df_empty):
    """ Test create list """
    todos.create_list("todos")
    df1 = todos.load_list("todos")
    pd.testing.assert_frame_equal(df1, df_empty)


def test_store_list(tmp_dir, df_empty):
    """ Test store list """
    todos.store_list(df_empty, "todos")
    df2 = todos.load_list("todos")
    pd.testing.assert_frame_equal(df_empty, df2)


def test_check_list_exists_1(df_empty_stored):
    """ Test check list exists """
    assert todos.check_list_exists("todos") == True


def test_check_list_exists_2(tmp_dir):
    """ Test check list exists """
    assert not todos.check_list_exists("todos") == False


def test_load_list(df_empty_stored, tmp_dir):
    """ Test load list """
    df = todos.load_list("todos")
    pd.testing.assert_frame_equal(df_empty_stored, df)


def test_add_to_list(new_row, df_full, tmp_dir):
    """ Test add to list """
    todos.add_to_list("todos", new_row)
    df1 = todos.load_list("todos")
    pd.testing.assert_frame_equal(df1, df_full)


def test_update_list_1(df_full_stored):
    """ Test update list """
    df_full_stored.loc[0, "owner"] = "Ivan"
    todos.update_task_in_list("todos", 0, "owner", "Ivan")
    df = todos.load_list("todos")
    pd.testing.assert_frame_equal(df, df_full_stored)


def test_update_list_2(df_full_stored):
    """ Test update list """
    df_full_stored.loc[0, "task"] = "TEC-Modulo-2"
    todos.update_task_in_list("todos", 0, "task", "TEC-Modulo-2")
    df = todos.load_list("todos")
    pd.testing.assert_frame_equal(df, df_full_stored)


def test_update_list_3(df_full_stored):
    """ Test update list """
    df_full_stored.loc[0, "summary"] = "Entregable"
    todos.update_task_in_list("todos", 0, "summary", "Entregable")
    df = todos.load_list("todos")
    pd.testing.assert_frame_equal(df, df_full_stored)
