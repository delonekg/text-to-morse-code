import string
from morse_code import morse_code_chars

def main():
    string_to_convert = str(input("Enter a string you'd like to convert to morse code: ")).lower()
    morse_string = ""

    for char in string_to_convert:
        if char in morse_code_chars:
            if char == " ":
                morse_string += " ....... "
            else:
                morse_string += f"{morse_code_chars[char]} "
        else:
            morse_string += f"{char} ....... "

    
    print(morse_string)



if __name__ == "__main__":
    main()
