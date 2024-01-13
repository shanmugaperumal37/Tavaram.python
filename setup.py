import sys
from cx_Freeze import setup, Executable

# Replace "your_script.py" with the actual filename of your script
script = 'main.py'

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'  # Use this for GUI applications on Windows

# Define the executables and include any additional dependencies
executables = [Executable(script, base=base)]

# Additional options can be added here
options = {}

# Create the setup configuration
setup(name="ANDIAPPAN'S PROJECT",
      version='1.0',
      description='Description of your script',
      executables=executables,
      options=options)
