#!/usr/bin/env python3

import random
import time


class Book:
    def __init__(self, title: str):
        self.title = title
        self.openPage = None

    def open(self, page: int | None = None):
        self.openPage = page
        # opening doesn't equal studyin' it...
        return self.openPage


class Notebook:
    def __init__(self):
        self.pages = []
        self.lastEntry = None

    def open(self):
        # lots of scribblin'
        return True

    def write(self, text: str):
        self.pages.append(text)
        self.lastEntry = text
        return text


class Mathe:
    """
    we're caught in a trap
    i can't walk out
    because i love you too much baby
    why can't you see?
    what you're doin' to me...
    when you don't believe a word i say?
    we can't go on together
    with suspicious minds!!!
    """

    name = "MATHE"  # subject name... John Kramer (I'm sorry... that just popped in my head rn)
    difficulty = 8
    love = 5  # don't go!!!

    def __init__(self):
        self.textbook = Book(self.name)
        self.notebook = Notebook()

    def understand(self):
        time.sleep(random.randint(self.love, self.difficulty))
        return not bool(random.randint(-1, 1))  # i know i'm overdoing this


mathe = Mathe()
