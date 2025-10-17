"""
======================================
Pigment Data Source (dictionary) for GREEN pigments
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


green_pigments = [
    {
        "name": "Malachite",#copper(II) carbonate, 2 CuCO3.Cu(OH)2
        "family": "Green",
        "era_since": "Antiquity",
        "use_period": [-3000, 1800],
        "type": "Mineral natural"
    },
    {
        "name": "Verdigris",#Copper acetate, Cu(C2H3O2)2-2Cu(OH)2
        "family": "Green",
        "era_since": "Antiquity",
        "use_period": [-3000, 1900],#ancient greece until 19th century
        "type": "Synthetic"
    },
    {
        "name": "Green earth",#complex aluminosilicate minerals, K[(Al,FeIII),(FeII,Mg](AlSi3,Si4)O10(OH)2
        "family": "Green",
        "era_since": "Antiquity",
        "use_period": [-3000, 1900],#until 19th century
        "type": "Mineral natural"#Glauconite or celadonite
    },
    {
        "name": "Copper resinate",#Cu(C19H29COO)2
        "family": "Green",
        "era_since": "Medieval Age",
        "use_period": [700, 1700],#from 8th to the 16th century
        #In the 15th and 17th centuries artists used copper resinate to add glaze on paintings laying a layer of copper resinate over verdigris to form a deep saturation of green color
        "type": "Synthetic"
    },
    {
        "name": "Green verditer",#Copper hydroxy-acetates, CuCO3·Cu(OH)2
        "family": "Green",
        "era_since": "Renaissance",
        "use_period": [1500, 5000],# first manufactured in the 16th century
        #5000 means until now
        "type": "Synthetic"
    },
    {
        "name": "Viridian",#Chromium(III)-oxide dihydrate, Cr2O3 · 2 H2O
        "family": "Green",
        "era_since": "Industrialization",
        "use_period": [1838, 5000],#5000 means until now
        "type": "Synthetic (hydrated chromium oxide)"
    },
    {
        "name": "Opaque chromium oxide",#chromium oxide,Cr2O3
        "family": "Green",
        "era_since": "Industrialization",
        "use_period": [1800, 5000],#first half of 19th
        # #5000 means until now
        "type": "Synthetic(also minreal natural as eskolaite)"
    },
    {
        "name": "Emerald green",#Copper(II)-acetoarsenite, Cu(CH3COO)2 · 3 Cu(AsO2)2
        "family": "Green",
        "era_since": "Industrialization",
        "use_period": [1814, 1900],#toxic and used only during the 19th
        "type": "Synthetic"
    },

    {
        "name": "Cobalt green",#Cobalt(II)-oxide-zinc(II)-oxide, CoO · ZnO
        "family": "Green",
        "era_since": "Early Modern",
        "use_period": [1780, 5000],#5000 means until now
        "type": "Synthetic "
    },
    {
        "name": "Chrome green",#mixture of Prussian blue and chrome yellow
        #Fe4[Fe(CN)6]3 + PbCrO4
        "family": "Green",
        "era_since": "Industrialization",
        "use_period": [1800, 5000],#from the beginning of 19th
        # #5000 means until now
        "type": "Synthetic "
    },

    {
        "name": "Scheele's green",#copper hydrogen arsenite, CuHAsO3
        "family": "Green",
        "era_since": "Early Modern",
        "use_period": [1700, 1900],  #toxic,from the end of 18th until the beginning of 19th
        "type": "Synthetic "
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

