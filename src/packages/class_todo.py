import os
import pandas as pd


class ToDo:
    """ Methods Refactored """
    def __init__(self, path: str) -> None:
        self.path_to_data = path
        """
        Init class

        :param path: path to data
        :type path: str
        :rtype: None
        """

    def data_path(self) -> str:
        """
        Return path to data

        :return: string with path to data
        :rtype: str
        """
        return self.path_to_data

    def update_task_in_list(self,
                            list_name: str,
                            task_id: str,
                            field: str,
                            change: str
                            ) -> None:
        """
        Update data in the list

        :param list_name: name of the list
        :type list_name: str
        :param task_id: id from the tsk list
        :type task_id: str
        :param field: parameter to update
        :type field: str
        :param change: data to update
        :type change: str
        :rtype: None
        """
        df = self.load_list(list_name)
        df.loc[task_id, field] = change
        self.store_list(df, list_name)

    def create_list(self, name: str) -> None:
        """
        Create a new list

        :param name: name to new list
        :type name: str
        :rtype: None
        """
        df = pd.DataFrame(columns=["created", "task",
                                   "summary", "status", "owner"])
        self.store_list(df, name)

    def get_existing_lists(self) -> str:
        """
        Get existing lists

        :return: list directory
        :rtype: str
        """
        return os.listdir(self.path_to_data)

    def check_list_exists(self, name: str) -> bool:
        """
        Verify if list exists

        :param name: name of the list
        :type name: str
        :return: True if the list exists, False if not exists
        :rtype: bool
        """
        return self.get_list_filename(name) in self.get_existing_lists()

    def get_list_filename(self, name: str) -> str:
        """
        Get list filename

        :param name: name of the list
        :type name: str
        :return: name list and .csv
        :rtype: str
        """
        return f"{name}.csv"

    def load_list(self, name: str) -> object:
        """
        Load dataframe of the list

        :param name: name of the list
        :type name: str
        return: dataframe fo the list
        :rtype: object
        """
        return pd.read_csv(self.get_list_path(name))

    def store_list(self, df: object, name: str) -> None:
        """
        Save list to csv

        :param df: dataframe name
        :type df: object
        :param name: name of the list
        :type name: str
        :rtype: None
        """
        df.to_csv(self.get_list_path(name), index=False)

    def get_list_path(self, name: str) -> str:
        """
        Get list path

        :param name: name of the list
        :type name: str
        :return: complete path list
        :rtype: str
        """
        return f"{self.path_to_data}{self.get_list_filename(name)}"

    def add_to_list(self, list_name: str, new_row: str) -> None:
        """
        Add element to list

        :param list_name: name of the list
        :type list_name: str
        :param new_row: data of the new row
        :type new_row: str
        :rtype: None
        """
        df = self.load_list(list_name)
        df.loc[len(df.index)] = new_row
        self.store_list(df, list_name)


if __name__ == "__main__":
    pass
