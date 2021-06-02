#Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".

def mood_type(mood='neutral'):
    return 'Today, I am feeling {}'.format(mood)

print(mood_type('happy'))
print(mood_type('sad'))
print(mood_type())