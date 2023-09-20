#Accept any three string from one input() call

words = input("Enter any three strings with spaces beetween them: ")
words_splitted = words.split(" ")
result = "Passed words are: "
print(result + ", ".join(words_splitted) + ".")