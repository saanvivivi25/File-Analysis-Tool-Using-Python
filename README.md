 Project: File Analysis Tool

 Description

This Python project analyzes a text file and provides useful statistics such as the number of lines, words, and characters. The program accepts a file path from the user, reads the file safely, and displays the results in a structured format. It demonstrates the use of functions, file handling, exception handling, dictionaries, and user input in Python.

 Features

* Reads any text file specified by the user.
* Counts the total number of lines, words, and characters.
* Uses a context manager (with open) for safe file handling.
* Handles common file-related errors gracefully.
* Returns results in a dictionary format.
* Displays a neatly formatted analysis report.

 Implementation

The project is divided into two main functions:

1. count_file_details()

* Accepts a file path as input.
* Opens and reads the file using a context manager.
* Calculates the number of lines, words, and characters.
* Returns the results as a dictionary.
* Handles exceptions such as FileNotFoundError and PermissionError.

2. display_report()

* Receives the results dictionary.
* Formats and displays the file statistics in a readable report.

 Error Handling

The program includes exception handling to improve reliability:

* FileNotFoundError – Displayed when the specified file does not exist.
* PermissionError – Displayed when the program does not have permission to access the file.


