# MORSE CODE CONVERTER
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # space between words
}

def convert_to_morse(text):
    text = text.upper()
    morse_code = ""
    for letter in text:
        if letter in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[letter] + " "
        else:
            morse_code += "? "  # unknown character
    return morse_code.strip()

def main():
    user_input = input("Enter a word or sentence to convert to Morse Code: ")
    result = convert_to_morse(user_input)
    print(result)

if __name__ == "__main__":
    main()