"""
Генерация собственных значений $\lambda$, $\mu$ для матриц в вариационном методе.
Получение собственных значений:
"""
import numpy as np


def get_lambda(N: np.int, h: np.double, l = None) -> np.array:
    """
    :param N: количество собственных значений
    :param h: шаг сетки
    :param l: задает отрезок на котором рассматривается функционал [-l,l]
    :return: np.array
    """
    alpha = 1
    if l is not  None:
        alpha = np.pi / l
    return np.array([4 / h ** 2 * np.sin(k * alpha * h / 2) ** 2 for k in range(N)])


def get_mu(N: np.int, h: np.double, l = None) -> np.array:
    """
    :param N: количество собственных значений
    :param h: шаг сетки
    :param l: задает отрезок на котором рассматривается функционал [-l,l]
    :return: np.array
    """
    return 1 - h ** 2 * get_lambda(N, h, l) / 6
