#Return the count of sub-string “Emma” appears in the given string

sentence = input("Write any sentence: ")
splitted_sentence = sentence.split(" ")
counter = 0
for x in splitted_sentence:
    if(x=='Emma'):
        counter = counter + 1

print("Emma appered", counter, "times in sentence above.")