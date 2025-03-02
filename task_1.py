import numpy as np
import matplotlib.pyplot as plt



#arrays
black_image = np.zeros((29, 29), dtype=np.uint8)
gray_image = np.full((29, 29), 128, dtype=np.uint8)

plt.figure(figsize=(10, 5))

# black box
plt.subplot(1, 2, 1)
plt.imshow(black_image, cmap='gray', vmin=0, vmax=255)
plt.title('Black Image')
plt.axis('off')

# grey box
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray', vmin=0, vmax=255)
plt.title('Gray Image')
plt.axis('off')

plt.show()

# vertical white line
black_image[:, 14] = 255
# black box
plt.subplot(1, 2, 1)
plt.imshow(black_image, cmap='gray', vmin=0, vmax=255)
plt.title('Black Image with White Line')
plt.axis('off')

# vertical black line
gray_image[:, 14] = 0
# grey box
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray', vmin=0, vmax=255)
plt.title('Gray Image with Black Line')
plt.axis('off')

plt.show()
