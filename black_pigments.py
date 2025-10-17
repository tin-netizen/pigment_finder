"""
======================================
Pigment Data Source (dictionary) for BLACK pigments
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


#data from the book "Chemistry for restoration" and
#the web https://www.webexhibits.org/pigments/

black_pigments = [
    {
        "name": "Charcoal black (vine black)",
        "family": "Black",
        "era_since": "Prehistoric",
        "use_period": [-40000, 5000],#5000 means until now
        "type": "Organic plant/artificial"#amorphous carbon
    },
    {
        "name": "Bone black (ivory black)",
        "family": "Black",
        "era_since": "Prehistoric",
        "use_period": [-40000, 5000],#5000 means until now
        "type": "Organic animal(bone)"#amorphous carbon+ high percentage of calcium hydroxyapatite, calcium carbonate
    },
    {
        "name": "Lamp black(carbon black)",#smoke/soot/flame/oil black
        "family": "Black",
        "era_since": "Prehistoric",
        "use_period": [-40000, 5000],#5000 means until now
        "type": "Synthetic"  #nearly pure amorphous carbon
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