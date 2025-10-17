"""
============================================================
Pigment Dictionary Search & Compare Tool
============================================================

<pigment_finder>.py - for finding pigments by the year of completion of an artwork。

Author: Ting-shiuan Su
Created Date: 01-10-2025
Contact Email: tingshiuan.su@gmail.com
Version: 1.0.0

"""


# pigment_finder.py
# This file contains the core logic for finding pigments.



#Importing modules and defining functions
from pigment_data import pigments_db, era_order
#pigments_db：the list that store pigments information
#era_order: This is the dictionary we use to determine the order of eras

#Function definition and variable initialization
def find_pigments(artwork_input, color_family):
    """
    Finds pigments based on artwork year or historical era.

    Args:
        artwork_input (str): The year (e.g., "1850") or a historical era (e.g., "Baroque").
        color_family (str): The color family (e.g., "Red", "Blue").
    """
    possible_pigments = []
    impossible_pigments = []

    # the initialization of found_any_pigment here
    #Incase the color is not in database:
    found_any_pigment = False

    # Step 1: Check if the input is a year or a period
    is_year_input = False
    try:
        artwork_year = int(artwork_input)
        #If the user enters a numeric string (e.g. "1850"), this line will successfully convert it to the number 1850.
        is_year_input = True
    except ValueError:
        #If the conversion fails (for example, if the user enters "Baroque"), the program will jump to this block.
        artwork_era = artwork_input
        if artwork_era not in era_order:
            print("Invalid year input. Please enter a valid year or period.")
            return

    # Step 2: Query the database based on the input type
    # Core Decision Loop
    for pigment in pigments_db:
        # Only process user-specified color families
        if pigment["family"].lower() == color_family.lower():
            # If we enter this block, it means we found at least one pigment of the specified color
            found_any_pigment = True
            is_possible = False


            if is_year_input:
                # Case 1: The user provides a year and uses a numeric range to determine
                start_year, end_year = pigment["use_period"]
                if start_year <= artwork_year <= end_year:
                    is_possible = True
            else:
                # Case 2: User provides the era, and uses era_order to determine
                pigment_era_level = era_order.get(pigment["era_since"])
                artwork_era_level = era_order.get(artwork_era)
                #Get the numeric order of the pigment and artwork from the era_order dictionary.
                # .get() avoids errors if the key is not found.

                if pigment_era_level is not None and artwork_era_level is not None:
                    if pigment_era_level <= artwork_era_level:
                        is_possible = True

            if is_possible:
                possible_pigments.append(pigment)
            else:
                # If the conditions are not met, add it to the impossible pigment list
                impossible_pigments.append(pigment)

    # Step 3: Display the results
    print(f"\n--- Artwork Age：{artwork_input} | Color：{color_family} ---")

    # if any matching pigments are found
    # Correct logic for handling colors not in the database
    if not found_any_pigment:
        print(f"\nSorry! There is no color associated with {color_family} in the database.")
        return

    #for possible pigments:
    print("\nPossible pigments:")
    if possible_pigments:
        for p in possible_pigments:
            # Determines the text displayed

            start_year, end_year = p['use_period']

            # 將 5000 替換為 "now"
            end_year_text = "now" if end_year == 5000 else end_year
            display_text = f"{p['era_since']} (about {start_year} till {end_year_text} )"

            ## Display more precise years for Industrialization

            if 'Industrialization' in p['era_since']:
                display_text = f"Industrialization period (about {start_year} CE)"

            print(f"- {p['name']} (used period: {display_text})")
    else:
        print("No matching pigments found for this age.")

    #for impossible pigments:
    print("\nImpossible pigments:")
    if impossible_pigments:
        for p in impossible_pigments:
            # show the full period and usage period
            start_year, end_year = p['use_period']
            # 將 5000 替換為 "now"
            end_year_text = "now" if end_year == 5000 else end_year

            display_text = f"{p['era_since']} (about {start_year} till {end_year_text} )"

            print(f"- {p['name']} (used period: {display_text})")
    else:
        print("All the pigments are possible!")

#Differences between Two Logic Decisions

#the if is_year_input: statement to distinguish between these two inputs:
#When "1920" is entered:
#The program executes the if is_year_input: block
#and uses the numeric range to determine whether the pigment is possible:
# start_year <= 1920 <= end_year.
#Paints with a rank of [1826, 5000] will qualify, but paints with a rank of [1550, 1700] will not,
#even though their era_since rank is less than Contemporary.

#When "Contemporary" is entered:
#The program executes the else: block
#and uses the era_order level to determine the pigment:
# pigment_era_level <= artwork_era_level.
#This means that any pigment that existed before Contemporary era
# will be considered "possible."



