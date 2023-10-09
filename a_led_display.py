"""
Task:
    Write a program which is able to simulate the work of a seven-segment display.
    Each digit is constructed from 13 LEDs.
    Program has to display any non-negative integer number entered by the user.
"""
digits_depiction = {
    "0": ("###", "# #", "# #", "# #", "###"),
    "1": ("  #", "  #", "  #", "  #", "  #"),
    "2": ("###", "  #", "###", "#  ", "###"),
    "3": ("###", "  #", "###", "  #", "###"),
    "4": ("# #", "# #", "###", "  #", "  #"),
    "5": ("###", "#  ", "###", "  #", "###"),
    "6": ("###", "#  ", "###", "# #", "###"),
    "7": ("###", "  #", "  #", "  #", "  #"),
    "8": ("###", "# #", "###", "# #", "###"),
    "9": ("###", "# #", "###", "  #", "###")
}


def get_number_to_display():
    number = None
    while True:
        try:
            number = int(input("What number should be displayed: "))
            if number < 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("That's not a non-negative integer.")
            continue
        except KeyboardInterrupt:
            exit()
    return number


def display_number(number):
    digits = [digits_depiction[digit] for digit in str(number)]
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))


if __name__ == "__main__":
    while True:
        n = get_number_to_display()
        display_number(n)
