class DataInserter():
    """Class for insertion converted data into document tables."""
    def __init__(self, data, document):
        """Initialize data inserter.

        Args:
            :param data: Instance of Data class, which stores imported data from BOM-file.
            :param document: Instance of Specification/ListOfComponents class which represents document model.

        """
        self.data = data
        self.list_of_components = self.data.list_of_components
        self.quantity = self.data.quantity
        self.designator = self.data.designator
        self.document = document
        self.colons = self.document.colons
        self.first_row_index = self.document.first_row_index

    def insert_text_into_cell(self, cell, text):
        """Insert text into cell in table

        Args:
            cell(str): Name of a cell.
            text(str): Text you want to insert into cell.

        """
        cell_text = self.document.table.getCellByName(cell)
        cursor = cell_text.createTextCursor()
        cell_text.setString(text)

    def insert_data_into_document(self):
        """Insert converted data into document tables."""
        for index, (component, quantity, designator) in enumerate(zip(self.list_of_components, self.quantity,
                                                                      self.designator)):
            self.insert_text_into_cell(self.colons["list_of_components"] + str(index + self.first_row_index), component)
            self.insert_text_into_cell(self.colons["quantity"] + str(index + self.first_row_index), quantity)
            self.insert_text_into_cell(self.colons["designator"] + str(index + self.first_row_index), designator)
