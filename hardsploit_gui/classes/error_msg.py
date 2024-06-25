"""error_msg.py"""

import time
from pathlib import Path

from PySide6.QtWidgets import QMessageBox


class ErrorMsg:

	@staticmethod
	def hardsploit_not_found():
		QMessageBox(
			QMessageBox.Critical,
			'Hardsploit Connectivity',
			'Hardsploit not detected. Please check the USB connection'
		).exec_()
		return True

	@staticmethod
	def usb_error():
		QMessageBox(
			QMessageBox.Critical,
			'Hardsploit USB error',
			'USB error occurred'
		).exec_()

	@staticmethod
	def no_chip_loaded():
		QMessageBox(
			QMessageBox.Information,
			"Wire chip",
			"You need to load a chip first"
		).exec_()()
		return True

	@staticmethod
	def invalid_pin_nbr():
		QMessageBox(
			QMessageBox.Warning,
			'Invalid pin number value',
			'Pin number needs to be between 4 and 144'
		).exec_()

	@staticmethod
	def invalid_values():
		QMessageBox(
			QMessageBox.Warning,
			'Error',
			'Invalid value(s) in field(s)',
		).exec_()

	class FileSizeError(Exception):
		pass


	class InvalidBaudRateValue(Exception):
		pass

	@staticmethod
	def filesize_error():
		QMessageBox(
			QMessageBox.Critical,
			'Error',
			'Dump error: The file size does not match with the given parameters'
		).exec_()
	

	@staticmethod
	def swd_not_found():
		QMessageBox(
			QMessageBox.Information,
			'SWD Action',
			'No return from the SWD'
		).exec_()
	

	@staticmethod
	def swd_error():
		QMessageBox(
			QMessageBox.Critical,
			'SWD Action',
			'An error occurred while processing the SWD scan'
		).exec_()
		return False
	

	@staticmethod
	def spi_error():
		QMessageBox(
			QMessageBox.Critical,
			'SPI Action',
			'An error occurred while processing the SPI command'
		).exec_()
	

	@staticmethod
	def spi_mode_missing():
		QMessageBox(
			QMessageBox.Warning,
			'SPI mode missing',
			'Mode setting is missing for this chip'
			).exec_()
		return False
	

	@staticmethod
	def spi_cmd_too_long():
		QMessageBox(
			QMessageBox.Warning,
			'SPI command invalid',
			'SPI command size is to big (> 4000)'
			).exec_()
		return False


	@staticmethod
	def i2c_error():
		QMessageBox(
			QMessageBox.Critical,
			'I²C Action',
			'An error occurred while processing the I²C command (I²C wrong speed)'
		).exec_()
		return False
	
	# Commands
	@staticmethod
	def no_cmd_selected():
		QMessageBox(
			QMessageBox.Warning,
			'Missing command',
			'Select a command in the array first'
		).exec_()
		return True
	
	@staticmethod
	def concat_nbr():
		QMessageBox(
			QMessageBox.Warning,
			'Wrong selection',
			'Select two commands in the table to concatenate them'
		).exec_()
		return True
	
	@staticmethod
	def concat_disallow():
		QMessageBox(
			QMessageBox.Warning,
			'Concatenation option',
			'This option can be used only with I2C bus commands'
		).exec_()
		return False
	
	@staticmethod
	def lowbyte_missing():
		QMessageBox(
			QMessageBox.Critical,
			'Command error',
			'Payload size invalid or payload size (low) missing'
		).exec_()
		return False
	
	@staticmethod
	def highbyte_missing():
		QMessageBox(
			QMessageBox.Critical,
			'Command error',
			'Payload size invalid or payload size (high) missing'
		).exec_()
		return False
	
	@staticmethod
	def mode_missing():
		QMessageBox(
			QMessageBox.Critical,
			'Command error',
			'Payload size invalid or Read / Write address missing'
		).exec_()
		return False
	
	@staticmethod
	def size_neq_row_number():
		QMessageBox(
			QMessageBox.Critical,
			'Command error',
			'The payload size does not match with the row number'
		).exec_()
		return False
	
	@staticmethod
	def i2c_cmd_too_long():
		QMessageBox(
			QMessageBox.Critical,
			'I2C command invalid',
			'Your payload is too big (> 2000)'
		).exec_()
		return False
	
	@staticmethod
	def positive_cell_value():
		QMessageBox(
			QMessageBox.Warning,
			'Wrong data',
			'Only positive values are accepted in this cell'
		).exec_()
	
	@staticmethod
	def hexa_cell_value():
		QMessageBox(
			QMessageBox.Warning,
			'Wrong data',
			'Only hexadecimal values are accepted in this cell'
		).exec_()
	
	@staticmethod
	def char_cell_value():
		QMessageBox(
			QMessageBox.Warning,
			'Wrong data',
			'Wrong characters in this cell'
		).exec_()

	@staticmethod
	def int_cell_value():
		QMessageBox(
			QMessageBox.Warning,
			'Wrong data',
			'Wrong characters in this cell'
		).exec_()
	
	@staticmethod
	def ascii_only():
		QMessageBox(
			QMessageBox.Warning,
			'String error',
			'Only ASCII characters can be specified'
		).exec_()
		return False

	@staticmethod
	def wrong_syntax():
		QMessageBox(
			QMessageBox.Warning,
			'Syntax error',
			'A syntax error has been detected'
		).exec_()
		return False

	# Global Settings
	@staticmethod
	def settings_missing():
		QMessageBox(
			QMessageBox.Warning,
			'Missing settings',
			'No settings saved for this chip'
		).exec_()
		return False
	
	@staticmethod
	def frequency_missing():
		QMessageBox(
			QMessageBox.Warning,
			'Missing settings',
			'Frequency setting missing'
		).exec_()
		return False
	
	@staticmethod
	def i2c_mode_missing():
		QMessageBox(
			QMessageBox.Warning,
			'Missing settings',
			'Missing write base address (I²C) or read command (SPI)'
		).exec_()
		return False
	
	@staticmethod
	def full_size_error():
		QMessageBox(
			QMessageBox.Warning,
			'Empty field',
			'Full size setting missing or equal 0'
		).exec_()
		return False
	
	@staticmethod
	def start_stop_missing():
		QMessageBox(
			QMessageBox.Warning,
			'Empty field',
			'Start and stop address must be filled'
		).exec_()
		return False
	
	@staticmethod
	def start_neq_stop():
		QMessageBox(
			QMessageBox.Warning,
			'Wrong value',
			'Start address must not be equal to the stop address'
		).exec_()
		return False
	
	@staticmethod
	def start_inf_to_stop():
		QMessageBox(
			QMessageBox.Warning,
			'Wrong value',
			'Start address must be inferior to the stop address'
		).exec_()
		return False
	
	@staticmethod
	def inf_to_total_size():
		QMessageBox(
			QMessageBox.Warning,
			'Wrong value',
			'Start and stop address must be inferior to the chip total size'
		).exec_()
		return False
	
	@staticmethod
	def para_read_latency():
		QMessageBox(
			QMessageBox.Warning,
			'Missing parallel settings',
			'Read latency setting missing'
		).exec_()
		return False
	
	@staticmethod
	def para_word_size():
		QMessageBox(
			QMessageBox.Warning,
			'Missing parallel settings',
			'Word size setting missing'
		).exec_()
		return False
	@staticmethod
	def repetition_value(index):
		QMessageBox(
			QMessageBox.Warning,
			f"Invalid value line {index}",
			'Value must be > 0'
		).exec_()
		return False

	# Unknown

	@staticmethod
	def unknown(msg):

		f = open(str(Path(__file__).parent.resolve()) + "/../logs/error.log", "a")
		# Logger.new($logFilePath).error(msg)
		f.write(str(time.ctime()) + ": " + str(msg) + "\n")
		QMessageBox(
			QMessageBox.Critical,
			'Hardsploit unknown error',
			'An unknown error has been detected. Check the log for more details.'
		).exec_()

	@staticmethod
	def custom(title, msg):
		QMessageBox(
			QMessageBox.Critical,
			f'{title}',
			f'{msg}'
		).exec_()
