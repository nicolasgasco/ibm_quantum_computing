import string
import sys

def text_analyzer(text=None):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
    
    if (text == None):
        text = input("Please input a string: ")
    try:
        assert isinstance(text, str)
    except:
        print(f"AssertionError: argument is not a string")
        return
    
    upper = 0
    lower = 0
    punctuations = 0
    spaces = 0

    for char in text:
        if (char.isupper()):
            upper += 1
        elif (char.islower()):
            lower += 1
        elif (char.isspace()):
            spaces += 1
        elif (string.punctuation.find(char) != -1):
            punctuations += 1

    print(f"The text contains {len(text)} character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punctuations} punctuation mark(s)")
    print(f"- {spaces} space(s)")

if __name__ == "__main__":
    if (len(sys.argv) == 1 or len(sys.argv) > 2):
        print("Error: provide 1 string argument.")
        sys.exit(1)
    
    text_analyzer(sys.argv[1])