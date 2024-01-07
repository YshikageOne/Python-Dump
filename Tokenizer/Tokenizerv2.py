# Defining a Token Object
# each token has a value and a type
class Token:
   def __init__(self, value, type):
       self.value = value
       self.type = type

# Main Tokenizer function
def tokenizer(textInput):
   # Define the delimiter
   delimiter = "/"

   tokens = []
   token = ""
   for char in textInput:
       if char == delimiter:
           if token: # if token is not empty
               if token.isdigit(): # checks if the token is a number
                  tokens.append(Token(token, 'Number'))
               elif token.isalpha(): # checks if the token contains alphabetical characters, hence a word
                  tokens.append(Token(token, 'Word'))
               elif char in ".!?,;:": # checks if the token is a punctuation
                  tokens.append(Token(token, 'Punctuation'))
               else: # if it's not a number, a word, or a punctuation, then the token is a symbol
                  tokens.append(Token(token, 'Symbol'))
               token = "" # reset the token

           # Add the delimiter as a separate token
           tokens.append(Token(delimiter, 'Delimiter'))
       elif char == "\n": # checks if the token is an end-of-line character
           tokens.append(Token("\n", 'EndOfLine'))
       else:
           token += char

   # Check for the last token after the loop
   if token:
       if token.isdigit():
           tokens.append(Token(token, 'Number'))
       elif token.isalpha():
           tokens.append(Token(token, 'Word'))
       elif char in ".!?,;:":
           tokens.append(Token(token, 'Punctuation'))
       else:
           tokens.append(Token(token, 'Symbol'))

   return tokens

# Main function
def main():
   textInput = input("Enter a text: ")
   tokens = tokenizer(textInput)
   for token in tokens:
       print(f"Value: {token.value} | Type: {token.type}")

if __name__ == "__main__":
   main()

# Test Values
# Hello World! and Hello/World/!
# 123 + 456 and 123/+/456
# @gmail.com and @/gmail/./com
# 110% sure and 110/%/sure
# Lorem ipsum dolor sit amet, and Lorem/ipsum/dolor/sit/amet/,