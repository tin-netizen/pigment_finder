"""
======================================
Pigment Data Source (dictionary) for BLUE pigments
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


blue_pigments = [
    {
        "name": "Azurite",#copper(II)-carbonate
        #2 CuCO3 · Cu(OH)2
        "family": "Blue",
        "era_since": "Antiquity",
        "use_period": [-3000, 1700],#since antiquity until the 17th century
        #minus number=B.C.
        "type": "Mineral natural"
    },
    {
        "name": "Lapis Lazuli(Ultramarine)",#Lazurite, is a tectosilicate mineral with sulfate, sulfur and chloride
        #Na7Ca(Al6Si6O24)(SO4)(S3) ·H2O
        "family": "Blue",
        "era_since": "Antiquity",
        "use_period": [-3000, 1800],#since antiquity until the 18th century
        #minus number=B.C.
        "type": "Mineral natural"
    },
    {
        "name": "Artificial Ultramarine",#A complex sulfur-containing sodium aluminum silicate
        #Na8-10Al6Si6O24S2-4
        "family": "Blue",
        "era_since": "Industrialization",
        "use_period": [1826, 5000],#since 1826 in France by Jean-Baptiste
        #5000 means until now (big number= until NOW)
        "type": "Synthetic"
    },
    {   "name": "Smalt",#potassium glass containing cobalt
        #SiO2(65%) + K20 (15%) + Al2O3 (5%) + CoO (10%)
        "family": "Blue",
        "era_since": "Renaissance",
        "use_period": [1400, 1900],#between the 15th and the 18th century, around 1540 by Christian Schiirrer
        "type": "Synthetic"
    },
    {   "name": "Cobalt Blue",#Cobalt(II) oxide-aluminum oxide
        #CoO · Al2O3
        "family": "Blue",
        "era_since": "Industrialization",
        "use_period": [1807, 5000],#Production began in France in 1807
        #5000 means until now (big number= until NOW)
        "type": "Synthetic"
    },
    {   "name": "Cerulean Blue",#Cobalt(II)-stannate,Formula:CoO · n SnO2
        "family": "Blue",
        "era_since": "Industrialization",
        "use_period": [1860, 5000],#widely available until its reintroduction in 1860 by George Rowney in England.
        #5000 means until now (big number= until NOW)
        "type": "Synthetic"
    },
    {   "name": "Prussian Blue",#Iron(III)-hexacyanoferrate(II), Fe[Fe3+Fe2+(CN)6]3
        "family": "Blue",
        "era_since": "Early Modern",
        "use_period": [1724, 5000],#available to artists by 1724
        #5000 means until now (big number= until NOW)
        "type": "Synthetic"
    },
    {   "name": "Indigo",
        "family": "Blue",
        "era_since": "Antiquity",
        "use_period": [-3000, 5000],
        # #minus number=B.C.
        #5000 means until now (big number= until NOW)
        #(Since 19th century it has been manufactured synthetically)
        "type": "Natural Plant"
    },
    {   "name": "Blue Verditer(Blue Bice)",#Indigotin (2,2'-Biindolinyliden-3,3'-dion)
        #C16H10 N2O2
        "family": "Blue",
        "era_since": "Medieval Age",
        "use_period": [500, 1900],#from medieval times until 19th century
        "type": "Synthetic" #similar chemical composition to mineral azurite
    },
    {   "name": "Egyptian Blue",#Calcium copper silicate, CaCuSi4O10
        "family": "Blue",
        "era_since": "Antiquity",
        "use_period": [-2600, 1500],#until late middle ages#
        #minus number=B.C.
        "type": "Synthetic"
    },
    {   "name": "Han Blue",#barium copper silicate, BaCuSi4O10
        "family": "Blue",
        "era_since": "Antiquity",
        "use_period": [-1200, 220],  #ancient China
        "type": "Synthetic"
     },
    {   "name": "Manganese Blue",#barium manganate fixed on barium sulphate base
        #BaMnO4 +BaSO4
        "family": "Blue",
        "era_since": "Contemporary",
        "use_period": [1935, 5000],
        #5000 means until now (big number= until NOW)
        "type": "Synthetic"
     },
    {   "name": "Turnsole",
        "family": "Blue",
        "era_since": "Medieval Age",
        "use_period": [500, 1600],#medival and renaissance Italian Manuscripts
        "type": "Natural Plant(Organic Dye)"#
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