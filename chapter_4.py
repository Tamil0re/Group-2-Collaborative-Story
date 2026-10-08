# chapter_4.py
# Chapter 4: The Chase Through the Code
# The bug would not give up. It raced after them in fast pursuit.
# It charged through the import statements and leapt over the try-excepts,
# but every line Sir Python-salot had written was too clean to break.

import time

def the_chase():
    print("The bug charged through the import statements...")
    time.sleep(1)
    try:
        print("It leapt over the try-excepts, looking for a crack to slip through...")
        raise RuntimeError("bug")
    except RuntimeError:
        print("...but the except block caught it cleanly. There was nowhere to hide.")
    print("The code was simply too clean. The bug could not survive, and it vanished.")
the_chase()