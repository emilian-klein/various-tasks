"""
Task:
    Create a function that takes in a current mood and return a sentence in the following format:
    "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".
"""


def show_mood(mood="neutral"):
    return f"Today, I am feeling {mood}!"


if __name__ == "__main__":
    print(show_mood("happy"))
    print(show_mood("sad"))
    print(show_mood())
