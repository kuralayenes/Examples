punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


my_string = input("Enter a string: ")


no_punc = ""

for char in my_string:
    if char not in punctuations:
        print(char)
        no_punc = no_punc + char


print(no_punc)