from math import sqrt

def euclidean_distance(vector1: list[float], vector2: list[float]) -> float:
    """Returns the Euclidean distance between two vectors."""
    # The Euclidean distance between two vectors is the square root of the sum of the squared differences between corresponding elements of the vectors.
    
    # Check if vectors are of the same length
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    
    # Calculate the sum of the squared differences
    sum_of_squared_differences = sum((x - y) ** 2 for x, y in zip(vector1, vector2))
    
    # Return the square root of the sum of the squared differences
    return sqrt(sum_of_squared_differences)
