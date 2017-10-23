import csv


class DataImporter():
    """Class for importing data from BOM-files"""
    def __init__(self, data):
        """Initialize data importer.
        Args:
            :param data: Instance of Data class, which stores imported data from BOM-file.
        """
        self.data = data

    def import_data_from_csv_to_lists(self, file):
        """Import data form BOM-file to corresponding lists for further conversion.

        Args:
            file(str): Absolute path to BOM-file.

        """
        with open(file) as filename:
            reader = csv.reader(filename, delimiter="\t")
            next(filename)
            for row in reader:
                if row:
                    self.data.designator.append(row[0])
                    self.data.list_of_components.append(row[1])
                    self.data.quantity.append(row[2])
