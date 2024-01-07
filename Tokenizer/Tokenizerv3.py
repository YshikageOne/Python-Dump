class Token:
    def __init__(self, value, type, line, column):
        self.value = value
        self.type = type
        self.line = line
        self.column = column

def tokenizer(textInput):
    delimiter = "/"
    punctuation = ".!?,;:"
    tokens = []
    token = ""
    line = 1
    column = 1
    token_start_column = 1

    for char in textInput:

        if char == delimiter:
            # If the current character is the delimiter
            if token:
                # Add the token to the tokens list with its type determined
                tokens.append(create_token(token, line, token_start_column))
                token = ""  # Reset the token now that it's been processed
            tokens.append(Token(delimiter, 'Delimiter', line, column))
            token_start_column = column + 1  # Update the start column for the next token

        elif char in punctuation:
            # If the character is a punctuation
            if token:
                tokens.append(create_token(token, line, token_start_column))
                token = ""
            tokens.append(Token(char, 'Punctuation', line, column))
            token_start_column = column + 1

        elif char == "\n":
            # If the character is a newline (if the input takes multiple lines)
            if token:
                tokens.append(create_token(token, line, token_start_column))
                token = ""
            tokens.append(Token(char, 'EndOfLine', line, column))
            line += 1
            column = 0
            token_start_column = 1

        elif char.isspace():
            # If the character is a space
            if token:
                tokens.append(create_token(token, line, token_start_column))
                token = ""
            token_start_column = column + 1

        else:
            # If it's not a delimiter, punctuation, newline, or space then it's the value of the token
            if not token:
                token_start_column = column
            token += char
        column += 1  # Increment the column counter for each character

    # Check if there's a token at the end after the loop has finished
    if token:
        tokens.append(create_token(token, line, token_start_column))

    return tokens

def create_token(token_value, line, column):
    # Token is a number if it consists only of digits
    if token_value.isdigit():
        return Token(token_value, 'Number', line, column)
    # Token is a word if it consists only of alphabet characters
    elif token_value.isalpha():
        return Token(token_value, 'Word', line, column)
    # Token is a symbol if it consists only of non-alphanumeric characters
    elif all(not char.isalnum() for char in token_value):
        return Token(token_value, 'Symbol', line, column)
    # Token is unknown if it is a mix of different character types
    # or doesn't fit into the other specified categories
    else:\
        return Token(token_value, 'Unknown', line, column)

def main():
    textInput = input("Enter a text: ")
    tokens = tokenizer(textInput)
    for token in tokens:
        print(f"Value: {token.value} | Type: {token.type} | Line: {token.line} | Column: {token.column}")

if __name__ == "__main__":
    main()

# Test Values
# Hello World! and Hello/World/!
# 123 + 456 and 123/+/456
# @gmail.com and @/gmail/./com
# 110% sure and 110/%/sure
# Lorem ipsum dolor sit amet, and Lorem/ipsum/dolor/sit/amet/,