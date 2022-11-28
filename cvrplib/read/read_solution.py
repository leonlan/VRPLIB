from .parse_solution import parse_solution
from .utils import strip_lines


def read_solution(path: str):
    """
    Reads the solution from the passed-in file path.

    Parameters
    ----------
    path
        The path to the solution file.

    Returns
    -------
    A dictionary that contains solution data.

    """
    with open(path, "r") as fi:
        solution = parse_solution(strip_lines(fi))

    return solution