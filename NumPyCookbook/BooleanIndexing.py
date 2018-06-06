import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

laveena = ndimage.imread('./laveena.jpg')

copy = laveena.copy()

plt.title('Laveena Filtered')
plt.axis('off')
copy[(laveena > laveena.max() / 4) & (laveena <= (3 * laveena.max() / 4))] = 0
plt.imshow(copy)
plt.show()
