"""generic_commands.py"""

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMenu, QMainWindow, QMessageBox, QTableWidgetItem

from hardsploit_gui.classes.command_editor import CommandEditor
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.export_manager import ExportManager
from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.db.models import Bus, Command, Byte
from hardsploit_gui.gui.gui_generic_commands import Ui_Generic_commands
from hardsploit.core import HardsploitUtils


class GenericCommands(QMainWindow):

    def __init__(self, chip, bus_name, hardsploit_api):
        super().__init__()

        # Set up the ui
        self.view = Ui_Generic_commands()
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)
        self.view.lbl_search.setPixmap(QPixmap('images/search.png'))
        input_restrict(self.view.lie_search, 2)

        # Setup attributes
        self.chip = chip
        self.bus_name = bus_name
        self.bus_id = Bus.get(Bus.name == bus_name).id
        self._api = hardsploit_api
        self.chip_settings = None

        # Load the commands from the db
        self.feed_cmd_array()

        self.export_manager = None
        self.cmd_editor = None

    def _get_context_actions(self):
        """Return an iterable of the actions that should be included in the
        context menu.
        """
        return (self.view.actionExecute,
                self.view.actionEdit,
                self.view.actionTemplate,
                self.view.actionDelete,
                )

    def contextMenuEvent(self, event):
        """Display the context menu when the user clicks on a command.
        It uses the actions provided by the '_get_context_actions' method.
        """
        if not self.view.tbl_cmd.currentItem():
            return False
        elif self.view.tbl_cmd.currentItem().column() == 1:
            return False
        else:
            menu = QMenu(self)
            for action in self._get_context_actions():
                menu.addAction(action)
            menu.exec_(event.globalPos())

    @Slot()
    def execute(self):
        """Action to execute when the user wants to execute a command."""
        if HardsploitUtils.get_number_of_board_available() < 1:
            return ErrorMsg.hardsploit_not_found()
        if not self.view.tbl_cmd.currentItem():
            return ErrorMsg.no_cmd_selected()

        cmd_array = self.prepare_cmd()
        result = self._exec_cmd(cmd_array)

        if self.view.check_result.isChecked() and result:
            self.export_manager = ExportManager(self.bus_name, result, cmd_array)
            self.export_manager.setWindowModality(Qt.ApplicationModal)
            self.export_manager.show()

    @Slot()
    def execute_n(self):
        """Action to execute when the user wants to execute a command multiple times."""
        if HardsploitUtils.get_number_of_board_available() < 1:
            return ErrorMsg.hardsploit_not_found()
        if not self.view.tbl_cmd.currentItem():
            return ErrorMsg.no_cmd_selected()

        # Ask the user for the number of times to send the frame
        n, ok = QInputDialog.getInt(self, "Execute n times", "Number of times", 10, 1)

        cmd_array = self.prepare_cmd()
        result = self.exec_cmd(cmd_array, n)

        if self.view.check_result.isChecked() and result:
            # TODO: Define the behaviour when sending multiple commands
            # self.export_manager = ExportManager(self.bus_name, result, cmd_array)
            # self.export_manager.setWindowModality(Qt.ApplicationModal)
            # self.export_manager.show()
            pass

    @Slot()
    def create(self):
        """Action to execute when the user wants to create a new command."""
        self.cmd_editor = CommandEditor(0, None, None, self.chip, self.bus_id, self)
        self.cmd_editor.show()

    @Slot()
    def concatenate(self):
        """Action to execute when the user wants to concatenate commands."""
        self._concatenate()

    def _concatenate(self):
        """This function should be overridden to implement desired behaviour
        for supported bus."""
        ErrorMsg.concat_disallow()

    @Slot()
    def edit(self):
        """Action to execute when the user wants to edit an existing command."""
        if not self.view.tbl_cmd.currentItem():
            return ErrorMsg.no_cmd_selected()
        cmd_id = self.view.tbl_cmd.item(self.view.tbl_cmd.currentRow(), 2).text()
        self.cmd_editor = CommandEditor(2, cmd_id, self.view.tbl_cmd.currentItem().text(), self.chip, self.bus_id, self)
        self.cmd_editor.show()

    @Slot()
    def template(self):
        if not self.view.tbl_cmd.currentItem():
            return ErrorMsg.no_cmd_selected()
        cmd_id = self.view.tbl_cmd.item(self.view.tbl_cmd.currentRow(), 2).text()
        self.cmd_editor = CommandEditor(1, cmd_id, self.view.tbl_cmd.currentItem().text(), self.chip, self.bus_id, self)
        self.cmd_editor.show()

    @Slot()
    def delete(self):
        """Action to execute when the user wants to delete a command."""
        current_item = self.view.tbl_cmd.currentItem()
        if not current_item:
            return ErrorMsg.no_cmd_selected()
        confirm = QMessageBox.question(self, "Delete command",
                                       f"Are you sure you want to delete command '{current_item.text()}' ?")
        cmd_id = self.view.tbl_cmd.item(self.view.tbl_cmd.currentRow(), 2).text()
        if confirm == QMessageBox.Yes:
            Command.delete().where(Command.id == cmd_id).execute()
            self.feed_cmd_array()

    @Slot()
    def feed_cmd_array(self):
        """Fills in the table of commands from the database."""
        self.view.tbl_cmd.clearContents()
        cmd = self.chip.commands.where(Command.bus == self.bus_id)
        if self.view.lie_search.text() != "":
            cmd = cmd.where('name LIKE ?', f"%{self.view.lie_search.text()}%")

        # Add a hidden column with the id
        self.view.tbl_cmd.setColumnCount(3)
        self.view.tbl_cmd.hideColumn(2)

        self.view.tbl_cmd.setRowCount(len(cmd))
        for i, c in enumerate(cmd):
            it0 = QTableWidgetItem(c.name)
            it0.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            it1 = QTableWidgetItem(c.description)
            it1.setFlags(Qt.ItemIsEnabled)
            it2 = QTableWidgetItem(str(c.id))
            it0.setFlags(Qt.ItemIsEnabled)
            self.view.tbl_cmd.setItem(i, 0, it0)
            self.view.tbl_cmd.setItem(i, 1, it1)
            self.view.tbl_cmd.setItem(i, 2, it2)

        self.view.tbl_cmd.verticalHeader().setStretchLastSection(False)
        self.view.tbl_cmd.horizontalHeader().setStretchLastSection(True)

    def prepare_cmd(self):
        """Prepare a command before sending it to the hardsploit."""
        command_name = self.view.tbl_cmd.currentItem().text()
        byte_list = Byte.select().where(
                        Byte.command == Command.get(Command.name == command_name)
                    ).order_by(Byte.position)
        packet = []
        for bl in byte_list:
            if not bl.iteration:
                packet.append(int(bl.value, 16))
            else:
                for i in range(1, int(bl.iteration)):
                    packet.append(int(bl.value, 16))
        return packet
