# definition the order of time sequence
#Prehistoric (c. 40,000 BCE – c. 4,000 BCE)
#Antiquity (c. 3,000 BCE – c. 500 CE)
#Medieval Age (c. 500 CE – c. 1400 CE)
#Renaissance (c. 1400 CE – c. 1600 CE)
#Baroque (c. 1600 CE – c. 1700 CE)
#Modern age (1700s), ready-made paints,watercolor
#Industrialization (1800s),The development of synthetic pigments
#Contemporary(1900-now)
era_order = {
    "Prehistoric": 1,
    "Antiquity": 2,
    "Medieval Age": 3,
    "Renaissance": 4,
    "Baroque": 5,
    "Early Modern": 6,
    "Industrialization": 7,
    "Contemporary": 8,
    }

# Pigment Database
from red_pigments import red_pigments
from yellow_pigments import yellow_pigments
from blue_pigments import blue_pigments
from black_pigments import black_pigments
from white_pigments import white_pigments
from green_pigments import green_pigments
from orange_pigments import orange_pigments
from brown_pigments import brown_pigments
from purple_pigments import purple_pigments


# a TOTAL database for all color families
#pigments_db = red_pigments + blue_pigments + yellow_pigments
pigments_db = blue_pigments + red_pigments + yellow_pigments +black_pigments +white_pigments +green_pigments + orange_pigments + brown_pigments + purple_pigments


#data from the website: https://www.webexhibits.org/pigments/
#and the book
#M. Matteini, R. Mazzeo, and A. Moles, Chemistry for Restoration: Painting and Restoration Materials. Nardini Editore, 2016.