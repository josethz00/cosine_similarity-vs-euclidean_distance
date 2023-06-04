import matplotlib.pyplot as plt
import numpy as np

# Your vectors
np.random.seed(0)  # for reproducibility
v1_low = np.random.rand(2)
v2_low = np.random.rand(2)
v3_low = np.random.rand(2)

v1_high = np.random.rand(30)
v2_high = np.random.rand(30)
v3_high = np.random.rand(30)

# Calculate Euclidean distances and cosine similarities
def calculate_metrics(v1, v2, v3):
    euclidean_distance12 = np.linalg.norm(v1 - v2)
    euclidean_distance13 = np.linalg.norm(v1 - v3)
    cosine_similarity12 = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    cosine_similarity13 = np.dot(v1, v3) / (np.linalg.norm(v1) * np.linalg.norm(v3))
    return [euclidean_distance12, euclidean_distance13], [cosine_similarity12, cosine_similarity13]

euclidean_low, cosine_low = calculate_metrics(v1_low, v2_low, v3_low)
euclidean_high, cosine_high = calculate_metrics(v1_high, v2_high, v3_high)

# Plot Euclidean distances vs Cosine similarities
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(euclidean_low, cosine_low)
plt.xlabel('Euclidean Distance')
plt.ylabel('Cosine Similarity')
plt.title('Low-Dimensional Vectors')
for i, txt in enumerate(['v1-v2', 'v1-v3']):
    plt.annotate(txt, (euclidean_low[i], cosine_low[i]))
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(euclidean_high, cosine_high)
plt.xlabel('Euclidean Distance')
plt.ylabel('Cosine Similarity')
plt.title('High-Dimensional Vectors')
for i, txt in enumerate(['v1-v2', 'v1-v3']):
    plt.annotate(txt, (euclidean_high[i], cosine_high[i]))
plt.grid(True)

plt.tight_layout()
plt.show()
