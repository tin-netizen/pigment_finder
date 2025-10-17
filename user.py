"""
======================================
MODULE: User Interface (Main Entry)
======================================

Purpose (or Functionality):
  Handles the command-line interface (CLI) for the Pigment Data Finder.
  This module manages all user input, orchestrates the core logic module
  for data retrieval and comparison, and displays the final results to the user.

Dependencies:
  - pigment_finder.py (for data processing functions)
  - pigment_data.py (for the data dictionary)

Author: Ting-shiuan Su
Contact Email: tingshiuan.su@gmail.com
Date Created: 06/10/2025
"""

#This file serves as the user interface and entry point.

from pigment_finder import find_pigments

# Here begins the code that interacts with the user.
if __name__ == '__main__':

    # Use the input() function to allow the user to enter the year
    artwork_input = input("Please enter the year or the period of the artwork \n(example：1850 or Baroque, but the  year will give a more accurate result): ")

    # Use the input() function to allow the user to enter a color
    color_family = input("Please enter the color (example：Red, Blue): ")
    # the find_pigments function to perform the query
    find_pigments(artwork_input, color_family)

# definition of the time period
#Prehistoric (c. 40,000 BCE – c. 4,000 BCE)
#Antiquity (c. 3,000 BCE – c. 500 CE)
#Medieval Age (c. 500 CE – c. 1400 CE)
#Renaissance (c. 1400 CE – c. 1600 CE)
#Baroque (c. 1600 CE – c. 1700 CE)
#Early Modern (1700s)
#Industrialization (1800s)
#Contemporary(1900-now)

# Pigment color families:
#red
#yellow
#blue
#black
#white
#green
#orange
#brown
#purple