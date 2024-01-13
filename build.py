import PyInstaller.__main__

# Replace "your_script.py" with the actual filename of your Python script
script = 'main.py'

# Use PyInstaller to create the executable
PyInstaller.__main__.run([
    '--onefile',     # Create a single executable file
    script           # Path to your Python script
])
