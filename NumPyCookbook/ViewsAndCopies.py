import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from scipy import ndimage

laveena = ndimage.imread('./laveena.jpg')

copy = laveena.copy()

aview = copy.view()


