import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import ndimage

laveena = ndimage.imread('./laveena.jpg')
plt.subplot(121)
plt.title("Laveena")
plt.axis("off")
plt.imshow(laveena)
plt.subplot(122)
plt.title("Big-Laveena")
plt.axis("off")
plt.imshow(laveena.repeat(4, axis=0).repeat(4, axis=1))
plt.show()

