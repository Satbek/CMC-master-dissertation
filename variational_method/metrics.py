"""
Метрики L2 и C
"""

import numpy as np


def C (u, v, mask=None):
    if mask is None:
        mask = np.ones(u.shape)
    return np.max(np.abs(u * mask - v * mask)) / np.max(np.abs(u * mask))


def L2 (u, v, mask=None):
    if mask is None:
        mask = np.ones(u.shape)
    tmp1 = np.sqrt(np.sum(((u * mask - v * mask) ** 2)) /
                   np.min([np.count_nonzero(u * mask), np.count_nonzero(v * mask)]))
    tmp2 = np.sqrt(np.sum(u**2 * mask) / np.count_nonzero(u * mask))
    return tmp1 / tmp2