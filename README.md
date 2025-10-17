# Pigment Data Finding Tool

## Project Overview
This is a personal learning project developed to practice Python modular design. 
The tool allows a user to input the year of completion of an artwork and then searches, extracts, and compares pigment data from an internal dictionary source.
The code will find the possible pigments that the use of the pigment is be in line with the year of completion of an artwork.

##  File Structure
| File Name           | Function Description                                                                     |
|:--------------------|:-----------------------------------------------------------------------------------------|
| `color_pigments.py` | Defines and stores the  pigment data dictionary (Data Source) based on the color family. |
| `pigment_finder.py` | Contains functions for data searching, filtering, and comparison (Core Logic).           |
| `user.py`           | Handles user input and displays the final output (Main Executable).                      |

##  Author & Contact Information
* **Author:** **[Ting-Shiuan Su]** * **Contact Email:** `<tingshiuan.su@gmail.com>`
* **Date Created:** 05/10/2025
* **Version:** 1.0

##  How to Run
1. Ensure you have Python 3.x installed on your system.
2. Open your terminal or command prompt and navigate to the project's root directory.
3. Run the main interface file:
    ```bash
    python user.py
    ```