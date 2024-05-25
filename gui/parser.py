import subprocess
import sys

input_ui_file = "mainWindow.ui"
output_py_file = "output.py"
#
subprocess.call(["pyuic5", input_ui_file, "-o", output_py_file])