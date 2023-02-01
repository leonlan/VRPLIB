from cvrplib.parse import parse_solomon, parse_vrplib


def read_instance(path, style="vrplib"):
    """
    Reads the instance from the passed-in file path.

    Parameters
    ----------
    path
        The path to the instance file.
    style
        The instance format style, one of ['vrplib', 'solomon'].

    Returns
    -------
    An dictionary that contains the instance data.
    """
    with open(path, "r") as fi:
        if style == "vrplib":
            return parse_vrplib(fi.read())
        elif style == "solomon":
            return parse_solomon(fi.read())

        raise ValueError(f"Format style {style} not known.")
