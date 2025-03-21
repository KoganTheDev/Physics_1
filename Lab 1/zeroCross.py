import numpy as np

def zero_cross(ar_of_a_sampled_f):
    ar_of_sign_change_indxs = np.sign(ar_of_a_sampled_f)
    ar_of_sign_change_indxs = np.diff(ar_of_sign_change_indxs)
    ar_of_sign_change_indxs = np.nonzero(ar_of_sign_change_indxs)[0]
    return ar_of_sign_change_indxs

