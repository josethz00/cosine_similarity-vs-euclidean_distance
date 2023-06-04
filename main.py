import matplotlib.pyplot as plt
import numpy as np

# Your vectors
np.random.seed(0)  # for reproducibility
v1 = np.random.rand(10)
v2 = np.random.rand(10)
v3 = np.random.rand(10)

# Calculate Euclidean distances
euclidean_distance12 = np.linalg.norm(v1 - v2)
euclidean_distance13 = np.linalg.norm(v1 - v3)

# Calculate cosine similarities
cosine_similarity12 = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
cosine_similarity13 = np.dot(v1, v3) / (np.linalg.norm(v1) * np.linalg.norm(v3))

# Plot Euclidean distances
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(['v1-v2', 'v1-v3'], [euclidean_distance12, euclidean_distance13])
plt.title('Euclidean Distance')

# Plot cosine similarities
plt.subplot(1, 2, 2)
plt.bar(['v1-v2', 'v1-v3'], [cosine_similarity12, cosine_similarity13])
plt.title('Cosine Similarity')

plt.tight_layout()
plt.show()