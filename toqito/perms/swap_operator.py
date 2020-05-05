"""Produces a unitary operator that swaps two subsystems."""
from typing import List, Union
import numpy as np
from toqito.linear_algebra.matrices.iden import iden
from toqito.perms.swap import swap


def swap_operator(dim: Union[List[int], int], is_sparse: bool = False) -> np.ndarray:
    r"""
    Produce a unitary operator that swaps two subsystems.

    Provides the unitary operator that swaps two copies of `dim`-dimensional
    space. If the two subsystems are not of the same dimension, `dim` should
    be a 1-by-2 vector containing the dimension of the subsystems.

    Examples
    ==========

    The $2$-dimensional swap operator is given by the following matrix

    .. math::
        X_2 =
        \begin{pmatrix}
            1 & 0 & 0 & 0 \\
            0 & 0 & 1 & 0 \\
            0 & 1 & 0 & 0 \\
            0 & 0 & 0 & 1
        \end{pmatrix}

    Using `toqito` we can obtain this matrix as follows.

    >>> from toqito.perms.swap_operator import swap_operator
    >>> swap_operator(2)
    [[1., 0., 0., 0.],
     [0., 0., 1., 0.],
     [0., 1., 0., 0.],
     [0., 0., 0., 1.]]

    The :math:`3-`dimensional operator may be obtained using `toqito` as
    follows.

    >>> from toqito.perms.swap_operator import swap_operator
    >>> swap_operator(3)
    [[1., 0., 0., 0., 0., 0., 0., 0., 0.],
     [0., 0., 0., 1., 0., 0., 0., 0., 0.],
     [0., 0., 0., 0., 0., 0., 1., 0., 0.],
     [0., 1., 0., 0., 0., 0., 0., 0., 0.],
     [0., 0., 0., 0., 1., 0., 0., 0., 0.],
     [0., 0., 0., 0., 0., 0., 0., 1., 0.],
     [0., 0., 1., 0., 0., 0., 0., 0., 0.],
     [0., 0., 0., 0., 0., 1., 0., 0., 0.],
     [0., 0., 0., 0., 0., 0., 0., 0., 1.]]

    :param dim: The dimensions of the subsystems.
    :param is_sparse: Sparse if `True` and non-sparse if `False`.
    :return: The swap operator of dimension `dim`.
    """
    # Allow the user to enter a single number for dimension.
    if isinstance(dim, int):
        dim = np.array([dim, dim])

    # Swap the rows of the identity appropriately.
    return swap(iden(int(np.prod(dim)), is_sparse), [1, 2], dim, True)
