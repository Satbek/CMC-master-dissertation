"""
Генерация собственных значений $\lambda$, $\mu$ для матриц в вариационном методе.
Получение собственных значений:
"""
import numpy as np


def get_lambda(N: np.int, h: np.double) -> np.array:
    """
    :param N: количество собственных значений
    :param h: шаг сетки
    :return: np.array
    """
    return np.array([4 / h ** 2 * np.sin(k * h / 2) ** 2 for k in range(N)])


def get_mu(N: np.int, h: np.double) -> np.array:
    """
    :param N: количество собственных значений
    :param h: шаг сетки
    :return: np.array
    """
    return 1 - h ** 2 * get_lambda(N, h) / 6
