import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

laveena = ndimage.imread('./laveena.jpg')
xLen = laveena.shape[0]
yLen = laveena.shape[1]
xIndexes = np.arange(0, xLen)
yIndexes = np.arange(0, yLen)
np.random.shuffle(xIndexes)
np.random.shuffle(yIndexes)

plt.title('Laveena Scrambled')
plt.axis('off')
plt.imshow(laveena[np.ix_(xIndexes, yIndexes)])
plt.show()
