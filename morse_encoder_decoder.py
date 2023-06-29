""" 

Author: Aditya Upadhye

A Python program for encoding of and decoding from Morse code.

"""




morse_to_alpha = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
}


morse_to_digit = {
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
}


morse_to_punctuation = {
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '-.-.-.': ';',
    '---...': ':',
    '-....-': '-',
    '.----.': ''',
    '.-..-.': ''',
    '-...-': '=',
    '.-.-.': '+',
    '-.--.': '(',
    '-.--.-': ')',
    '.--.-.': '@',
    '-..-': 'X',
}


alphabets_to_morse = {value: key for key, value in morse_to_alpha.items()}

digits_to_morse = {value: key for key, value in morse_to_digit.items()}

punctuation_to_morse = {value: key for key, value in morse_to_punctuation.items()}


def morse_code_decoder(morse):

    morse = morse.split('/')
    decoded_morse = ''

    for each in morse:

        words = each.split()

        for word in words:

            if word in morse_to_punctuation.keys():

                decoded_morse += morse_to_punctuation[word]

            elif word in morse_to_digit.keys():

                decoded_morse += morse_to_digit[word]

            else:

                decoded_morse += morse_to_alpha[word]

        decoded_morse += ' '

    return decoded_morse


def morse_code_encoder(text):

    text = text.split(' ')

    morse_code = ''

    for each_word in text:

        for character in each_word:

            if character in alphabets_to_morse:

                morse_code += alphabets_to_morse[character]

            elif character in digits_to_morse:

                morse_code += digits_to_morse[character]

            else:

                morse_code += punctuation_to_morse[character]

            morse_code += ' '

        morse_code += '/'

    return morse_code


def check_user_choice(user_choice):

    while True:

        if user_choice == 'mct' or user_choice == 'tmc':

            return user_choice

        else:

            user_choice = input('Invalid option. Please enter your choice again.\n')


def read_user_input():

    user_choice = input(
        '\nProvide the conversion scheme:\n\n'
        'For Morse code to text : mct \n'
        'For text to Morse code : tmc\n\n'
    )

    user_choice = check_user_choice(user_choice)

    return user_choice


""" This is where the program starts. """


conversion_scheme = {'mct': 'Morse code to text', 'tmc': 'Text to Morse code'}

user_selected_scheme = read_user_input()

if user_selected_scheme == 'mct':

    morse_code = input('\nEnter the Morse code:\n\n')

    answer = morse_code_decoder(morse_code)

else:

    plain_text = input('\nEnter the text:\n\n')

    answer = morse_code_encoder(plain_text.upper())

print('\nFrom ', conversion_scheme[user_selected_scheme], ':\n', sep='')

print(answer)

