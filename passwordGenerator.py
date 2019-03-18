import string
import random


def lowercase_str_gen(lowercase_len):
    lowercase = list(string.ascii_lowercase)
    return random.sample(lowercase, lowercase_len)


def uppercase_str_gen(uppercase_len):
    uppercase = list(string.ascii_uppercase)
    return random.sample(uppercase, uppercase_len)


def int_gen(integer_len):
    return random.sample(range(0,9),integer_len)


def special_char_gen(char_len):
    specialchars = [' ','!','#','$','%','&','(',')','*','+',':',';','<','=','>','?','@','[',']','^','_','{','|','}','~']
    return random.sample(specialchars, char_len)


def password_gen(lowercase_len, uppercase_len, integer_len, char_len):
    password = lowercase_str_gen(lowercase_len) + uppercase_str_gen(uppercase_len) + int_gen(integer_len) + special_char_gen(char_len)
    random.shuffle(password)
    return ''.join(map(str, password))


def chunk_it(seq):
    avg = len(seq) / float(4)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out


if __name__ == '__main__':
    correct = False
    while not correct:
        input_str = input("password length?. Please be sensible and pick a value from 7 to 12:-  ")
        try:
            pass_len = int(input_str)
            if pass_len == 0 or pass_len < 11 or pass_len > 128:
                print("Sorry, I didn't understand that.")
            else:
                correct = True
        except ValueError:
            print("Sorry, I didn't understand that.")

    seq = list(range(1, pass_len+1))
    four_lists = chunk_it(seq)
    lowercase_len = len(four_lists[0])
    uppercase_len = len(four_lists[1])
    int_len = len(four_lists[2])
    char_len = len(four_lists[3])
    print(password_gen(lowercase_len, uppercase_len, int_len, char_len))
