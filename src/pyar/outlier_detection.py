import numpy as np
import numpy.typing as npt


def quartile_method(
        x: npt.ArrayLike,
        cu: float = 2.5,
        ci: float = 2.5,
        a: int = 0,
) -> npt.ArrayLike:
    """Calculates a threshold using the quartile method.

    Parameters
    ----------
    x : array_like
        The input data array to remove outliers from.
    cu : float, default: 2.5
        The upper cutoff for each element of `x`.
    ci : float, default: 2.5
        The lower cutoff for each element of `x`.
    a : int, default: 0
        A number between 0 and 1 giving the scale factor for the
        median to establish the minimum dispersion between quartiles for each
        element of `x`. The default does not set a minimum dispersion.

    Returns
    -------
    ndarray
        A filtered data array 

    """
    raise NotImplementedError
