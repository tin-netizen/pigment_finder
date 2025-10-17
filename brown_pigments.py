"""
======================================
Pigment Data Source (dictionary) for BROWN pigments
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

brown_pigments = [
    {
        "name": "Umber",
        "family": "Brown",
        "era_since": "Antiquity",
        "use_period": [-3000, 5000],#used in Europe since Renaissance
        # #5000 means until now
        "type": "Mineral natural"
        #similar to Sienna, but higher amount of manganese oxide
    },
    {
        "name": "Sienna",
        "family": "Brown",
        "era_since": "Prehistoric",
        "use_period": [-40000, 5000],#5000 means until now
        "type": "Mineral natural "
        #Raw Sienna earth: the earth just mined and ground into a pigment
        #Burnt Sienna earth: the raw earth umber pigment is also calcinated in order to get darker shades.
    },

    {
        "name": "Van Dyke brown",
        "family": "Brown",
        "era_since": "Baroque",
        "use_period": [1600, 1900],
        "type": "Organic natural"
    },

    {
        "name": "Bitumen (asphaltum)",
        "family": "Brown",
        "era_since": "Antiquity",
        "use_period": [-3000, 1900],#mainly used during 18th and 19th
        "type": "Mineral natural"
    },

    {
        "name": "Bistre",#similar to bitumen
        "family": "Brown",
        "era_since": "Renaissance",
        "use_period": [1300, 1900],#from 14th t 19th
        "type": "Synthetic"
    },

    {
        "name": "Sapia",
        "family": "Brown",
        "era_since": "Antiquity",
        "use_period": [-3000, 5000],#since roman times,particularly used during 18th
        "type": "Organic natural (dye)"
    },

    {
        "name": "Mummy(Egyptian brown)",
        "family": "Brown",
        "era_since": "Antiquity",
        "use_period": [-3000, 1900],#since Roman, particularly used during 16th til 19th
        "type": "Natural(egyptian mummy)"
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