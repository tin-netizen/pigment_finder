"""
======================================
Pigment Data Source (dictionary) for white pigments
======================================

Purpose (or Functionality):
  Defines and stores the main pigment data dictionary used by the project.
Data Source:
  [Reference]
  [1]Pigments through the Ages: https://www.webexhibits.org/pigments/
  [2]M. Matteini, R. Mazzeo, and A. Moles, Chemistry for Restoration: Painting and Restoration Materials. Nardini Editore, 2016.

Author: Ting-shiuan Su
Contact Email: tingshiuan.su@gmail.com
"""

white_pigments = [
    {
        "name": "Lead white",#Basic lead(II)-carbonate, 2 PbCO3· Pb(OH)2
        "family": "White",
        "era_since": "Antiquity",
        "use_period": [-400, 1900],#since antiquity as early as 400 B.C, up to 19th
        "type": "Synthetic"
    },
    {
        "name": "Lime white",#(chalk, bianco di San Giovanni)
        #calcium carbonate, CaCO3 (chalk)
        #calcium carbonate + calcium hydroxide, CaCO3 + Ca(OH)2 (bianco di San Giovanni)
        "family": "White",
        "era_since": "Antiquity",
        "use_period": [-3000, 5000],#today, as an inert filler
        # #5000 means until now
        "type": "Mineral natural/ synthetic"
    },
    {
        "name": "Zinc white",#(zinc oxide, ZnO)
        "family": "White",
        "era_since": "Industrialization",
        "use_period": [1782, 5000],#Historians agreed, that in 1782, zinc oxide was suggested as a white pigment.
         #5000 means until now
        "type": "Synthetic"
    },
    {
        "name": "Titanium white",#Titanium dioxide, TiO2
        "family": "White",
        "era_since": "Contemporary",
        "use_period": [1920, 5000],# The titanium pigment, titanium dioxide was discovered in 1821
        #but, it was not until 1921 that a titanium white oil color suitable for artistic purposes was introduced by an American manufacturer.
        "type": "Synthetic (titanium dioxide)"
    },
    {
        "name": "Lithopone",#Zns + BaSO4
        "family": "White",
        "era_since": "Contemporary",
        "use_period": [1950, 5000],#from the end of 19th
        # #5000 means until now
        "type": "Synthetic (titanium dioxide)"
    },
    {
        "name": "Barium white",#Barium sulphate, BaSO4
        "family": "White",
        "era_since": "Industrialization",
        "use_period": [1800, 5000],#manufactured from the beginning of 19th
        # #5000 means until now
        "type": "Natural(barite)/Synthetic (blanc fixe"
    },
    {
        "name": "Gypsum", #hydrated calcium sulphate, CaSO4·2H2O
        "family": "White",
        "era_since": "Antiquity",
        "use_period": [-3000, 5000],#5000 means until now
        "type": "Natural/ synthetic"
    },


]
#era_order＝definition the order of time sequence
#Prehistoric (c. 40,000 BCE – c. 4,000 BCE)
#Antiquity (c. 3,000 BCE – c. 500 CE)
#Medieval Age (c. 500 CE – c. 1400 CE)
#Renaissance (c. 1400 CE – c. 1600 CE)
#Baroque (c. 1600 CE – c. 1700 CE)
#Early Modern (1700s), ready-made paints,watercolor
#Industrialization (1800s),The development of synthetic pigments
#Contemporary(1900-now)

#data from the website: https://www.webexhibits.org/pigments/
#and the book
#M. Matteini, R. Mazzeo, and A. Moles, Chemistry for Restoration: Painting and Restoration Materials. Nardini Editore, 2016.