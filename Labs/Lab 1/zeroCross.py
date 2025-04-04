import numpy as np

def zero_cross(signal):
    """
    Finds the indices in a 1D array where the signal crosses zero.
    A zero-crossing occurs when consecutive elements have opposite signs.

    Parameters:
    ----------
    signal : numpy.ndarray
        A 1D numpy array containing sampled values of a signal or function.

    Returns:
    -------
    numpy.ndarray
        An array of indices where a sign change (zero-crossing) occurs.
        Each index i returned corresponds to a sign change between signal[i] and signal[i+1].

    Example:
    -------
    >>> signal = np.array([1, -1, -2, 3, -4])
    >>> zero_cross(signal)
    array([0, 2, 3])  # zero-crossings between (1, -1), (-2, 3), and (3, -4)
    """

    # Step 1: Get the sign of each element in the signal.
    # Positive values → 1, Negative → -1, Zero → 0
    sign_array = np.sign(signal)

    # Step 2: Compute the difference between consecutive signs.
    # If two adjacent signs differ, there is a sign change (i.e., zero crossing).
    sign_diff = np.diff(sign_array)

    # Step 3: The indices where sign_diff is non-zero correspond to sign changes.
    # np.nonzero returns a tuple, we extract the first element to get the indices.
    zero_crossing_indices = np.nonzero(sign_diff)[0]

    return zero_crossing_indices
