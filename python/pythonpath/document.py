# coding: utf8


class Specification():
    """Class, which represents specification document model."""
    def __init__(self, model):
        """

        Args:
            :param model: Model of currently opened document.

        """
        self.model = model
        self.tables = self.model.getTextTables()
        self.table = self.tables.getByIndex(0)
        self.rows = self.table.Rows
        self.first_row_index = 2
        self.colons = {"list_of_components": "E", "quantity": "F", "designator": "G"}


class ListOfElements():
    """Class, which represents list of elements document model."""
    def __init__(self, model):
        """

        Args:
            :param model: Model of currently opened document.

        """
        self.model = model
        self.tables = self.model.getTextTables()
        self.table = self.tables.getByIndex(0)
        self.first_row_index = 2
        self.colons = {"list_of_components": "B", "quantity": "C", "designator": "A"}
