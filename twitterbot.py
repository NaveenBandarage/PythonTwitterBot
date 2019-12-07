import random
#import string from ascii_lowercase


def textAlteration(text):
    textArray = []
    numberString = ''
    endText = ' - TextToNumbers'
    for i in range(len(text)):

        numberString = str(ord(text[i].lower()) - 96)
        print(numberString)
        textArray.append(numberString)

    return ''.join(textArray+ [endText])

# def letter_position(letter):
#     ucase = string.uppercase
#     pos = ucase.find(letter.upper()) + 1
#     return pos



print(textAlteration("ABCD"))
print(textAlteration("Hi my name is Naveen"))