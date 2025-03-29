import numpy as np

def zero_cross(ar_of_a_sampled_f):
    """
    Identifies the indices where the sign of the input array changes.

    Parameters:
    ar_of_a_sampled_f (numpy.ndarray): A 1D numpy array of sampled function values.

    Returns:
    numpy.ndarray: An array of indices where the sign of the input array changes.
    """
    # Calculate the sign of each element in the array
    ar_of_sign_change_indxs = np.sign(ar_of_a_sampled_f)
    
    # Calculate the difference between consecutive elements
    ar_of_sign_change_indxs = np.diff(ar_of_sign_change_indxs)
    
    # Find the indices where the difference is non-zero (indicating a sign change)
    ar_of_sign_change_indxs = np.nonzero(ar_of_sign_change_indxs)[0]
    
    return ar_of_sign_change_indxs

