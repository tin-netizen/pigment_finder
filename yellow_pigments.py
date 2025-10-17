"""
======================================
Pigment Data Source (dictionary) for yellow pigments
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

yellow_pigments = [
    {
        "name": "Yellow ochre",#Iron oxyhydroxide, FeO(OH))
        "family": "Yellow",
        "era_since": "Prehistoric",
        "use_period": [-40000, 5000],#5000 means until now
        "type": "Mineral natural"
    },
    {
        "name": "Cadmium yellow",#Cadmium(II)-sulfide, CdS
        "family": "Yellow",
        "era_since": "Industrialization",
        "use_period": [1818, 5000],#5000 means until now
        "type": "Synthetic"
    },
    {
        "name": "Chrome yellow",#lead(II)-chromate, PbCrO4
        "family": "Yellow",
        "era_since": "Industrialization",
        "use_period": [1816, 5000],#not currently widely used
        # #5000 means until now
        "type": "Synthetic"
    },
    {
        "name": "Lead tin yellow",#lead stannate Pb2SnO4(Type I)and lead tin oxide silicate Pb(Sn,Si)O3 (Type II)
        "family": "Yellow",
        "era_since": "Medieval Age",
        "use_period": [1300, 1900],  #Type I:Used between 13th and 18th centuries
        "type": "Synthetic"
    },
    {
        "name": "Orpiment",#Arsenic sulfide, As2S3
        "family": "Yellow",
        "era_since": "Antiquity",
        "use_period": [-3000, 1700],
        "type": "Mineral natural" #synthetically in the 18th
    },
    {
        "name": "Cobalt yellow",#potassium cobaltinitrite,K3[Co(NO2)6] · 3H2O
        "family": "Yellow",
        "era_since": "Industrialization",
        "use_period": [1852, 5000],#5000 means until now
        "type": "Synthetic"
    },
    {
        "name": "Lemon yellow(strontium yellow)",#barium chromate, BaCrO4
        "family": "Yellow",
        "era_since": "Industrialization",
        "use_period": [1830, 5000],#5000 means until now
        "type": "Synthetic"
    },
    {
        "name": "Naples yellow",#(lead antimonate)Pb(SbO3)2 or Pb(SbO4)2
        "family": "Yellow",
        "era_since": "Renaissance",
        "use_period": [1500, 1900],
        "type": "Synthetic"
    },
    {
        "name": "Indian yellow",#magnesium euxanthate, C19H16O11Mg.5H2O
        "family": "Yellow",
        "era_since": "Renaissance",
        "use_period": [1400, 1900],
        "type": "Natural Organic dye"#made from urine of cows fed only on mango leaves and water.
    },
    {
        "name": "Barium yellow",#barium chromate, BaCrO4
        "family": "Yellow",
        "era_since": "Industrialization",
        "use_period": [1800, 5000],#5000 means until now
        "type": "Synthetic"
    },
    {
        "name": "Cadmium lithopone yellow",#cadium suiphide mixed with barium sulphate
        #CdS + BaSO4
        "family": "Yellow",
        "era_since": "Contemporary",
        "use_period": [1927, 5000],#5000 means until now
        "type": "Synthetic"
    },
    {
        "name": "Massicot(lead ochre, Litharge)",#lead monoxide, PbO
        "family": "Yellow",
        "era_since": "Renaissance ",
        "use_period": [1400, 1900],#known since antiquity
        #mainly used from 15th until 19th
        "type": "Synthetic/native mineral"
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