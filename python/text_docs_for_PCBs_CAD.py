# coding: cp1251
import uno
import unohelper
from com.sun.star.awt import XActionListener
from data import Data
from extractor import DataExtractor
from importer import DataImporter
from converter import DataConverter
from inserter import DataInserter
from document import Specification, ListOfElements
from decorator import DataDecorator


class MyActionListener1(unohelper.Base, XActionListener):
    """Class, which handles press of a button for opening BOM-file to form specification."""
    def __init__(self):
        pass

    def disposing(self):
        pass

    def actionPerformed(self, actionEvent):
        model = XSCRIPTCONTEXT.getDocument()
        data = Data()
        data_extractor = DataExtractor()
        filename = data_extractor.get_file_name()[8:]
        data_importer = DataImporter(data)
        data_importer.import_data_from_csv_to_lists(filename)
        data_converter = DataConverter(data)
        data_converter.convert_data_for_specification()
        specification = Specification(model)
        data_inserting = DataInserter(data, specification)
        data_inserting.insert_data_into_document()
        data_decorator = DataDecorator(data, specification)
        data_decorator.set_style()


class MyActionListener2(unohelper.Base, XActionListener):
    """Class that handles press of a button for opening BOM-file to form list of components."""
    def __init__(self):
        pass

    def disposing(self):
        pass

    def actionPerformed(self, actionEvent):
        model = XSCRIPTCONTEXT.getDocument()
        data = Data()
        data_extractor = DataExtractor()
        filename = data_extractor.get_file_name()[8:]
        data_importer = DataImporter(data)
        data_importer.import_data_from_csv_to_lists(filename)
        data_converter = DataConverter(data)
        data_converter.convert_data_for_list_of_elements()
        list_of_elements = ListOfElements(model)
        data_inserting = DataInserter(data, list_of_elements)
        data_inserting.insert_data_into_document()
        data_decorator = DataDecorator(data, list_of_elements)
        data_decorator.set_style()


def createDialog():
    """Create main form of application"""
    try:
        context = uno.getComponentContext()
        service_manager = context.ServiceManager

        # Creation of dialog model and setting it's properties.
        dialog_model = service_manager.createInstanceWithContext("com.sun.star.awt.UnoControlDialogModel", context)

        dialog_model.PositionX = 100
        dialog_model.PositionY = 100
        dialog_model.Width = 200
        dialog_model.Height = 140
        dialog_model.Title = "TDSPP"

        # Creation of buttons models and setting their properties.
        button_model1 = dialog_model.createInstance("com.sun.star.awt.UnoControlButtonModel")
        button_model2 = dialog_model.createInstance("com.sun.star.awt.UnoControlButtonModel")
        button_model3 = dialog_model.createInstance("com.sun.star.awt.UnoControlButtonModel")

        button_model1.PositionX = 25
        button_model1.PositionY = 15
        button_model1.Width = 150
        button_model1.Height = 50
        button_model1.Name = "ButtonName1"
        button_model1.TabIndex = 0
        button_model1.Label = "Открыть BOM-файл для оформления спецификации"

        button_model2.PositionX = 25
        button_model2.PositionY = 75
        button_model2.Width = 150
        button_model2.Height = 50
        button_model2.Name = "ButtonName2"
        button_model2.TabIndex = 1
        button_model2.Label = "Открыть BOM-файл для оформления перечня элементов"

        button_model3.PositionX = 50
        button_model3.PositionY = 55
        button_model3.Width = 50
        button_model3.Height = 14
        button_model3.Name = "ButtonName3"
        button_model3.TabIndex = 1
        button_model3.Label = "Click Me"

        # Insertion of buttons models into dialog model.
        dialog_model.insertByName("CommandButton1", button_model1)
        dialog_model.insertByName("CommandButton2", button_model2)

        control_container = service_manager.createInstanceWithContext("com.sun.star.awt.UnoControlDialog", context)
        control_container.setModel(dialog_model)

        # Addition of event handlers.
        control_container.getControl("CommandButton1").addActionListener(MyActionListener1())
        control_container.getControl("CommandButton2").addActionListener(MyActionListener2())

        toolkit = service_manager.createInstanceWithContext("com.sun.star.awt.ExtToolkit", context)

        control_container.setVisible(False)
        control_container.createPeer(toolkit, None)

        control_container.execute()
        control_container.dispose()
    except Exception as e:
        print(e)


g_exportedScripts = createDialog
