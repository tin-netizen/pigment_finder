"""
======================================
Pigment Data Source (dictionary) for orange pigments
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
orange_pigments = [

    {
        "name": "Realgar",#Red orange natural pigment closely related to the yellow orpiment.
        #As4S4 or AsS(arsenic sulfide)
        "family": "Orange",
        "era_since": "Antiquity",
        "use_period": [-3000, 1900],
        "type": "Mineral natural"
    },
    {
        "name": "Chrome orange",# lead chromate variants
        #[PbCrO4 · Pb(OH)2] Basic lead(II)-chromate
        "family": "Orange",
        "era_since": "Industrialization",
        "use_period": [1809, 2000],
        "type": "Synthetic"
    },
    {
        "name": "Antimony vermilion",#Sb2S3 antimony sulphide
        "family": "Orange",
        "era_since": "Industrialization",
        "use_period": [1800, 1950],#replaced by cadmium
        "type": "Synthetic"
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