"""
Task:
    Accept any three words from one input() call.
"""
if __name__ == "__main__":
    while True:
        try:
            words = input("Enter any three words with spaces between them: ")
            result = words.split(" ")
            print(f"Passed words are: {' '.join(result)}")
        except KeyboardInterrupt:
            exit()
