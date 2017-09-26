import itertools

__newId = itertools.count(1)


def new_id():
    """Generates a new unique id.

    Returns:
        int : New unique id.
    """
    return next(__newId)
