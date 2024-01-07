# Defining a Token Object
# each token has a value and a type
class Token:
    def __init__(self, value, type):
        self.value = value
        self.type = type


# Main Tokenizer class
def tokenizer(textInput):
    # Delimiters separated into punctuation, spaces, and symbols
    punctuations = ['.', ',', '!', '?', ':', ';', '"', '<', '>']
    spaces = [' ', '\n', '\t']
    symbols = ['+', '=', '-', '_', '(', ')', '{', '}', '[', ']', '|', '/', '`', '~', '@', '#', '$', '%', '^', '&', '*', '…']
    delimiters = spaces + punctuations  + symbols

    tokens = []
    token = ""
    for char in textInput:
        if char in delimiters:
            if token:  # if token is not empty
                if token.isdigit():  # checks the token if it's a number
                    tokens.append(Token(token, 'Number'))
                elif token.isalpha():  # checks the token contains alphabetical characters hence a word
                    tokens.append(Token(token, 'Word'))
                else:  # if its not a number or a word then the token is a symbol
                    tokens.append(Token(token, 'Symbol'))
                token = ""  # reset the token

            # Categorize the delimiters into their own types
            if char in spaces:
                tokens.append(Token(char, 'Space'))
            elif char in punctuations:
                tokens.append(Token(char, 'Punctuation'))
            elif char in symbols:
                tokens.append(Token(char, 'Symbol'))
        else:
            token += char

    # Check for the last token after the loop
    if token:
        if token.isdigit():
            tokens.append(Token(token, 'Number'))
        elif token.isalpha():
            tokens.append(Token(token, 'Word'))
        else:
            tokens.append(Token(token, 'Symbol'))

    return tokens

# Main function
def main():
    textInput = input("Enter a text: ")
    tokens = tokenizer(textInput)
    for token in tokens:
        print(f"Value: {token.value} | Type: {token.type}") # formatting the string so i can use placeholders


if __name__ == "__main__": # it checks if this program is being run directly
    main()