"""
======================================
Pigment Data Source (dictionary) for red pigments
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
red_pigments = [

    {
        "name": "Vermilion (cinnabar)",#HgS mercuric sulphide
        "family": "Red",
        "era_since": "Antiquity",
        "use_period": [-3000, 1900],
        "type": "Mineral/synthetic"
    },
    {
        "name": "Cadmium red",#CdS(Se) cadmium sulpho-selenide
        "family": "Red",
        "era_since": "Contemporary",
        "use_period": [1900, 5000],#from beginning of 20th#
        # 5000 means until now
        "type": "Synthetic"
    },
    {
        "name": "Cadmium red lithopone",#CdS(Se) +BaSO4
        "family": "Red",
        "era_since": "Contemporary",
        "use_period": [1926, 5000],#5000 means until now
        "type": "Synthetic"
    },
    {
        "name": "Red lead (minium)",#Pb3O4 lead oxide
        "family": "Red",
        "era_since": "Antiquity",
        "use_period": [-3000, 1900],#No longer manufactured for artists due its toxic nature and its colour change upon ageing
        "type": "Synthetic (lead oxide)"
    },
    {
        "name": "Red ochre",#silica&clay
        # anhydrous ferric oxide Fe2O3
        "family": "Red",
        "era_since": "Prehistoric",
        "use_period": [-40000, 5000],#5000 means until now
        "type": "Mineral natural/synthetic"
    },
    {
        "name": "Haematite",#anhydrous ferric oxide
        "family": "Red",
        "era_since": "Prehistoric",
        "use_period": [-40000, 5000],#5000 means until now
        "type": "Mineral natural"
    },
    {
        "name": "Venetian red",#particially hydrated ferric oxide
        "family": "Red",
        "era_since": "Medieval Age",
        "use_period": [500, 5000],#5000 means until now
        "type": "Mineral natural"
    },
    {
        "name": "Madder lake",#1,2-dihydroxyantraquinone
        "family": "Red",
        "era_since": "Antiquity",
        "use_period": [-3000, 1900],#since Egyptians times
        "type": "Natural plant"
    },
    {
        "name": "Alizarin crimson",#same as madder lake
        "family": "Red",
        "era_since": "Industrialization",
        "use_period": [1868, 5000],
        "type": "Synthetic"
    },
    {
        "name": "Cochineal",
        "family": "Red",
        "era_since": "Baroque",
        "use_period": [1550, 1900],#introduced to Europe SINCE THE MID 16TH
        "type": "Natural animal(insect dye)"
    },
    {
        "name": "Kermes",#kermesic acid C18H22O9
        "family": "Red",
        "era_since": "Antiquity",
        "use_period": [-3000, 5000],  #REPLACED BY OTHER LAKES
        "type": "Natural animal"
    },
    {
        "name": "Lake",  #Laccaic acid C20H14O11
        "family": "Red",
        "era_since": "Antiquity",
        "use_period": [-3000, 5000],  #ancients in INDIA, introduced to the WEST after 7th
        "type": "Natural animal"#shellac
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