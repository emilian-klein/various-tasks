#Write a code to extract each digit from an integer, in the reverse order

given_number = input("Enter any number: ")
output_list = []
for x in given_number:
    output_list.append(x)

output_list = output_list[::-1]
print(*output_list, sep=" ")