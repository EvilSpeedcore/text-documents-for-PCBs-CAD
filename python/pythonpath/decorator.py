# coding: utf8
import uno
from com.sun.star.awt.FontSlant import ITALIC as FS_ITALIC
from com.sun.star.style.ParagraphAdjust import CENTER, LEFT


class DataDecorator():
    """Class to set style of imported data in document table."""
    def __init__(self, data, document):
        """

        Args:
            :param data: Instance of Data class, which stores imported data from BOM-file.
            :param document: Instance of Specification/ListOfComponents class which represents document model.

        """
        self.data = data
        self.document = document
        self.colons = self.document.colons
        self.first_row_index = self.document.first_row_index
        self.last_row_index = self.first_row_index + len(self.data.list_of_components) - 1

    def set_optimal_row_height(self):
        """Set optimal height property of table row."""
        for index, item in enumerate(self.data.designator):
            cell_name = ''.join([self.colons["designator"], str(index + self.first_row_index)])
            cell = self.document.table.getCellByName(cell_name)
            cell_text = cell.getString()
            if cell_text:
                row = self.document.rows.getByIndex(index + self.first_row_index - 1)
                row.OptimalHeight = True

    def calculate_cell_range(self):
        """Calculate cell range in document table for formatting."""
        range_list = []
        for value in self.colons.values():
            start = ''.join([value, str(self.first_row_index)])
            finish = ''.join([value, str(self.last_row_index)])
            complete_range = ':'.join([start, finish])
            range_list.append(complete_range)
        return range_list

    def set_style(self):
        """Set style of table which contains converted data from BOM-file."""
        list_of_components_range, quantity_range, designator_range = self.calculate_cell_range()
        _range1 = self.document.table.getCellRangeByName(list_of_components_range)
        _range2 = self.document.table.getCellRangeByName(quantity_range)
        _range3 = self.document.table.getCellRangeByName(designator_range)
        _range1.CharPosture, _range2.CharPosture, _range3.CharPosture = (FS_ITALIC, FS_ITALIC, FS_ITALIC)
        _range1.ParaAdjust, _range2.ParaAdjust, _range3.ParaAdjust = (LEFT, CENTER, CENTER)
