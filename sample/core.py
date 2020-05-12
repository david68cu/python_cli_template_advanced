# -*- coding: utf-8 -*-
# This below solve the issue of the code but break the test
import helpers


def get_hmm():
    """Get a thought."""
    return "hmmm..."


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        # if get_answer():
        print(get_hmm())


if __name__ == "__main__":
    print(get_hmm())
    hmm()
