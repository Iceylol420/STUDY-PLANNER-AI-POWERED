# STUDY-PLANNER-AI-POWERED
A Python-based Study Planner with both CLI and GUI interfaces. It allows users to create, save, load, and manage study schedules in multiple formats (JSON, Excel, CSV). The application includes logging functionality to track user actions and provides an option to download logs for review. 


# Study Planner GUI Project

## **Project Overview**
This project involves creating a comprehensive study planner application with both a CLI (Command Line Interface) and a GUI (Graphical User Interface) version. The planner allows users to generate study schedules, save them in multiple formats (JSON, Excel, CSV), load existing schedules, and manage saved schedules. Additionally, it includes features for logging user actions and generating downloadable log files.

---

## **Current Functionalities**

### **CLI Features**
1. **Generate Study Schedule**
   - Takes user input for subjects, total study hours per day, and number of days.
   - Generates a balanced study schedule.
2. **Save Schedule**
   - Saves the schedule in JSON, Excel, or CSV format.
3. **Load Schedule**
   - Loads a previously saved schedule from a selected file.
4. **Delete Schedule**
   - Deletes a selected saved schedule.
5. **Help Command**
   - Lists available commands.
6. **Error Handling**
   - Provides appropriate error messages for invalid inputs and file operations.

### **GUI Features**
1. **Main Tab**
   - Input fields for subjects, total study hours, and number of days.
   - Buttons to generate, save, and load schedules.
   - A scrollable text area to display the generated or loaded schedule.

2. **Saved Schedules Tab**
   - Listbox to view saved schedules.
   - Buttons to refresh the list, load a selected schedule, and delete a selected schedule.

3. **Statistics Tab**
   - Button to download the log file containing user actions.

4. **Logging**
   - Logs all key user actions (e.g., generating, saving, loading, deleting schedules) to a text file (`statistics_log.txt`).
   - Allows users to download the log file from the Statistics tab.

5. **Exit Prompt**
   - Prompts the user to save the log file before exiting.

---

## **Recent Fixes and Enhancements**
1. **Fixed Load Page Issues**
   - Ensured correct file paths are used when loading schedules.
   - Improved error handling during file loading.
2. **Implemented Logging**
   - Added a `log_action` method to record user actions in a log file.
   - Created a `download_log` method to allow users to download the log file.
3. **Exit Handling**
   - Added an `on_close` method to prompt the user to save the log before exiting.

---

## **Planned Enhancements**

1. **Multi-User Support**
   - Allow multiple users to maintain separate schedules and logs.

2. **Theme Customization**
   - Add options for light and dark modes.

3. **Advanced Statistics**
   - Display statistics such as total study hours per subject and daily workload distribution.

4. **Export and Import Configurations**
   - Allow users to export and import their settings and schedules.

5. **Conversion to Executable**
   - Use `PyInstaller` to create a standalone `.exe` version of the application for easy distribution.

---

## **Instructions for Running the Project**

### **CLI Version**
1. Ensure Python 3.11 or later is installed.
2. Run the CLI script using:
   ```bash
   python CLIPYTHONPY.py
   ```
3. Follow the on-screen instructions to generate, save, load, or delete schedules.

### **GUI Version**
1. Ensure Python 3.11 or later is installed.
2. Install required libraries using:
   ```bash
   pip install tkinter openpyxl cryptography
   ```
3. Run the GUI script using:
   ```bash
   python GUIPYTHONpy.py
   ```
4. Use the GUI to manage study schedules and download logs.

---

## **Requirements**
- Python 3.11 or later
- Libraries: `tkinter`, `openpyxl`, `cryptography`

---

## **Files**
1. `CLIPYTHONPY.py`: CLI version of the study planner.
2. `GUIPYTHONpy.py`: GUI version of the study planner.
3. `core_logic.py`: Core logic for generating schedules.
4. `statistics_log.txt`: Log file for user actions.

---

## **Next Steps**
1. Complete the GUI enhancements (in progress).
2. Add advanced statistics display.
3. Implement multi-user support.
4. Prepare for `.exe` conversion.

---

## **Notes**
- Ensure that all file operations (save, load, delete) are performed in the correct directory.
- Regularly test the application to identify and fix bugs.
- Maintain separate versions of the project for CLI and GUI during development.

