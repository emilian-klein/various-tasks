"""
    Program displays any non-negative integer number entered by user in a form of a seven-segment display.
    Each digit is constructed from 13 LEDs.
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
    while True:
        number = int(input("What number should be displayed: "))
        if number < 0:
            raise ValueError
        else:
            return number

def display_number(number):
    digits = [digits_depiction[digit] for digit in str(number)]
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))

while True:
    try:
        n = get_number_to_display()
        display_number(n)
    except ValueError:
        print("That's not a non-negative integer.")
