from cosine_similarity import cosine_similarity
from euclidean_distance import euclidean_distance
import numpy as np

def compare_vector_distances():
    # Your vectors
    np.random.seed(0)  # for reproducibility
    v1_low = np.random.rand(2)
    v2_low = np.random.rand(2)
    v3_low = np.random.rand(2)

    v1_high = np.random.rand(30)
    v2_high = np.random.rand(30)
    v3_high = np.random.rand(30)

    # Calculate Euclidean distances and cosine similarities
    print("DISTANCE BETWEEN VECTORS IN LOW DIMENSIONAL SPACE")
    print("Euclidean distance between v1_low and v2_low: ", euclidean_distance(v1_low, v2_low))
    print("Euclidean distance between v1_low and v3_low: ", euclidean_distance(v1_low, v3_low))

    print("Cosine similarity between v1_low and v2_low: ", cosine_similarity(v1_low, v2_low))
    print("Cosine similarity between v1_low and v3_low: ", cosine_similarity(v1_low, v3_low))
    print("\n\n")

    print("DISTANCE BETWEEN VECTORS IN HIGH DIMENSIONAL SPACE")
    print("Euclidean distance between v1_high and v2_high: ", euclidean_distance(v1_high, v2_high))
    print("Euclidean distance between v1_high and v3_high: ", euclidean_distance(v1_high, v3_high))

    print("Cosine similarity between v1_high and v2_high: ", cosine_similarity(v1_high, v2_high))
    print("Cosine similarity between v1_high and v3_high: ", cosine_similarity(v1_high, v3_high))
    print("\n\n")

compare_vector_distances()