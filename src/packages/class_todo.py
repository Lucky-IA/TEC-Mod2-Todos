import os
import pandas as pd
from pathlib import Path

class ToDo():
    def __init__(self, path):
        self.path_to_data = path
    
    def data_path(self):
        return self.path_to_data

    def update_task_in_list(self, list_name, task_id, field, change):
        df = self.load_list(list_name)
        df.loc[task_id, field] = change
        self.store_list(df, list_name)

    def create_list(self, name):
        df = pd.DataFrame(columns=["created", "task", "summary", "status", "owner"])
        self.store_list(df, name)

    def get_existing_lists(self):
        return os.listdir(self.path_to_data)

    def check_list_exists(self, name):
        return self.get_list_filename(name) in self.get_existing_lists()

    def get_list_filename(self, name):
        return f"{name}.csv"

    def load_list(self, name):
        return pd.read_csv(self.get_list_path(name))

    def store_list(self, df, name):
        df.to_csv(self.get_list_path(name), index=False)

    def get_list_path(self, name):
        return f"{self.path_to_data}{self.get_list_filename(name)}"

    def add_to_list(self, list_name, new_row):
        df = self.load_list(list_name)
        df.loc[len(df.index)] = new_row
        self.store_list(df, list_name)


if __name__ == "__main__":
    pass
