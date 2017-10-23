import uno
from com.sun.star.ui.dialogs.TemplateDescription import FILEOPEN_SIMPLE


class DataExtractor():
    """Class, that represents implementation of dialog for BOM-file selection."""
    @staticmethod
    def get_file_name(path=None, mode=1):
        """Get name of BOM-file.

        Returns:
            :return Absolute path of selected BOM-file.

        """
        context = uno.getComponentContext()
        service_manager = context.getServiceManager()
        file_picker = service_manager.createInstanceWithArgumentsAndContext('com.sun.star.ui.dialogs.FilePicker',
                                                                            (FILEOPEN_SIMPLE,), context)
        if path:
            file_picker.setDisplayDirectory(path)
        file_picker.initialize((mode,))
        if file_picker.execute():
            return file_picker.getFiles()[0]
