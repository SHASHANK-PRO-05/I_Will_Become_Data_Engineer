import matplotlib.pyplot as plt
from scipy import ndimage

laveena = ndimage.imread('./laveena.jpg')

plt.subplot(221)
plt.title("Laveena-Orignal")
plt.axis('off')
plt.imshow(laveena)

copy_laveena = laveena.copy()
plt.subplot(2, 2, 2)
plt.title('Laveena-Y-Flipped')
plt.axis('off')
plt.imshow(copy_laveena[:, ::-1])

plt.subplot(2, 2, 3)
plt.title('Laveena-First-Quadrant')
plt.axis('off')
plt.imshow(copy_laveena[:int(copy_laveena.shape[0] / 2), : int(copy_laveena.shape[1] / 2)])

plt.subplot(2, 2, 4)
plt.title("Laveena-Masked")
plt.axis('off')
mask = copy_laveena % 2 == 0
print(mask)
masked_laveena = copy_laveena.copy()
masked_laveena[mask] = 0
plt.imshow(masked_laveena)
plt.show()
