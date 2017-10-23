# coding: cp1251


class DataConverter():
    """Class for conversion of imported data from BOM-file. """
    def __init__(self, data):
        """Initializes data converter.

        Args:
            :param data: Instance of Data class, which stores imported data from BOM-file.

        """
        self.data = data

    def first_step_of_converting_for_specification(self):
        """Define quantity of identical elements and group their conventions from PCB
        for specification document."""
        for this_index, this_item in enumerate(self.data.list_of_components):
            number_of_elements = 1
            for next_index in range(this_index + 1, len(self.data.list_of_components)):
                next_item = self.data.list_of_components[next_index]
                if this_item == next_item:
                    self.data.list_of_components[next_index] = ""
                    self.data.quantity[next_index] = ""
                    if this_item:
                        number_of_elements += 1
                        self.data.designator[this_index] += ", " + self.data.designator[next_index]
                        self.data.designator[next_index] = ""
                        self.data.quantity[this_index] = number_of_elements

    def first_step_of_converting_for_list_of_elements(self):
        """Define quantity of identical elements and group their conventions from PCB
        for list of elements document."""
        for this_index, this_item in enumerate(self.data.list_of_components):
            number_of_elements = 1
            for next_index, next_item in enumerate(self.data.list_of_components):
                last_character_1 = self.data.designator[this_index][-1:]
                last_character_2 = self.data.designator[next_index][-1:]
                if this_item and next_item:
                    if this_item == next_item and int(last_character_2) - int(last_character_1) == 1:
                        self.data.list_of_components[next_index] = ""
                        self.data.quantity[next_index] = ""
                        if this_item:
                            number_of_elements += 1
                            self.data.designator[this_index] += ", " + self.data.designator[next_index]
                            self.data.designator[next_index] = ""
                            self.data.quantity[this_index] = number_of_elements
            if self.data.quantity[this_index] and int(self.data.quantity[this_index]) > 2:
                first_designator = self.data.designator[this_index][:2]
                last_designator = self.data.designator[this_index][-2:]
                self.data.designator[this_index] = first_designator + "..." + last_designator

    def remove_empty_elements(self):
        """Delete empty elements from lists with data."""
        self.data.list_of_components = list(filter(None, self.data.list_of_components))
        self.data.quantity = list(filter(None, self.data.quantity))
        self.data.designator = list(filter(None, self.data.designator))

    def group_elements(self):
        """Distribute elements into groups."""
        for index, item in enumerate(self.data.list_of_components):
            this_item = item
            next_item = self.data.list_of_components[(index + 1) % len(self.data.list_of_components)]
            if this_item and next_item and self.data.list_of_components.index(next_item) != 0:
                if this_item.split()[0] != next_item.split()[0]:
                    for _list in [self.data.list_of_components, self.data.quantity, self.data.designator]:
                        for repeat in range(2):
                            _list.insert(index + 1, "")
        for _list in [self.data.list_of_components, self.data.designator, self.data.quantity]:
            for repeat in range(1):
                _list.insert(0, "")

    def name_groups_of_elements(self):
        """Name groups of elements."""
        for index, item in enumerate(self.data.list_of_components):
            this_item = item
            next_item = self.data.list_of_components[(index + 1) % len(self.data.list_of_components)]
            if next_item and not this_item:
                name_of_component = next_item.split()[0] + "û"
                self.data.list_of_components[index] = name_of_component

    def convert_data_for_specification(self):
        """Convert imported data from BOM-file to form specification document."""
        self.first_step_of_converting_for_specification()
        self.remove_empty_elements()
        self.group_elements()
        self.name_groups_of_elements()
        for repeat in range(2):
            for _list in [self.data.list_of_components, self.data.quantity, self.data.designator]:
                _list.insert(0, "")
        self.data.list_of_components[0] = "Ïðî÷èå èçäåëèÿ"

    def convert_data_for_list_of_elements(self):
        """Convert imported data from BOM-file to form list of elements."""
        self.first_step_of_converting_for_list_of_elements()
        self.remove_empty_elements()
        self.group_elements()
        self.name_groups_of_elements()
