# I don't have a square image and in current tutorial
# I don't have a scope of doing that . This is a breaking
# code
from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np

laveena = ndimage.imread('./laveena.jpg')
yLen = laveena.shape[1]
xLen = laveena.shape[0]
arr = np.arange(xLen)

laveena[range(xLen), range(yLen)] = 0

# laveena[range(xLen)][range(yLen - 1, -1, -1)] = 0

plt.title('I check you once and I check you twice-Aha haa-Look what you made me do')
plt.imshow(laveena)
plt.axis("off")
plt.show()
