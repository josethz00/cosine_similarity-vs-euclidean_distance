from cosine_similarity import cosine_similarity
from euclidean_distance import euclidean_distance
import numpy as np

def compare_vector_distances():
    # Your vectors
    np.random.seed(0)  # for reproducibility
    v1_low = np.random.rand(2)
    v2_low = np.random.rand(2)
    v3_low = np.random.rand(2)

    v1_high = np.random.rand(500)
    v2_high = np.random.rand(500)
    v3_high = np.random.rand(500)

    # Calculate Euclidean distances and cosine similarities
    print("DISTANCE BETWEEN VECTORS IN LOW DIMENSIONAL SPACE")
    print("Euclidean distance between v1_low and v2_low: ", round(euclidean_distance(v1_low, v2_low), 3))
    print("Euclidean distance between v1_low and v3_low: ", round(euclidean_distance(v1_low, v3_low), 3))

    print("Cosine similarity between v1_low and v2_low: ", round(1 - cosine_similarity(v1_low, v2_low), 3))
    print("Cosine similarity between v1_low and v3_low: ", round(1 - cosine_similarity(v1_low, v3_low), 3))
    print("\n\n")

    print("DISTANCE BETWEEN VECTORS IN HIGH DIMENSIONAL SPACE")
    print("Euclidean distance between v1_high and v2_high: ", round(euclidean_distance(v1_high, v2_high), 3))
    print("Euclidean distance between v1_high and v3_high: ", round(euclidean_distance(v1_high, v3_high), 3))

    print("Cosine similarity between v1_high and v2_high: ", round(1 - cosine_similarity(v1_high, v2_high), 3))
    print("Cosine similarity between v1_high and v3_high: ", round(1 - cosine_similarity(v1_high, v3_high), 3))
    print("\n")

compare_vector_distances()