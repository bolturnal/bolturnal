#!/usr/bin/env python3

import json
import random

from schoolBag import mathe

aboutMe: dict = {
    "name": "bolthead",
    "location": "/boot/theGrid/",
    "age": 17,
    "programs": {
        "python": "good enough grip",  # NOTE: fuck PEP8 rules
        "shell": "[[ it's very weird ]]",
        "c": 'printf("just gettin started\n"); // almost forgot the simicolon',
    },
    "mbti": "inxp",
}

# and that's all i had to say about that...

with open("aboutMe.json", "w+") as f:
    json.dump(aboutMe, f, indent=4)
    f.seek(0)
    print(f.read())


def study(subject=mathe) -> None:
    try:
        subject.textbook.open(page=188)
        subject.notebook.open()

        interest: int = random.randint(3, 63)  # it peaked at 63 in the last 3 months...

        if interest > 32:
            print("Enjoyin'... it ain't painful no more")
        else:
            print(
                """
Somethin's not right... 
what's gotten into me???
I used to love mathe!!!
"""
            )

    except Exception:
        # the set of reasons that one might consider as error... is pretty huge
        print(str(Exception))


study()


def boltopia() -> None:  # i really don't know what this function will return...
    """
    A realistic utopia...
    """
    population: int = 1808
    people = [f"person_{i}" for i in range(population)]

    resources: list = [
        "food",
        "water",
        "shelter",
        "medicine",
        "time",
        "attention",
        "power",  # uneven by nature
        "hope",  # non-renewable under stress
    ]

    equality = bool(1)

    if len(resources) < len(people):
        equality = bool(0)

    rules: list = [""]

    # TODO: I'll finish it later... I guess...


# I just felt like writing
