import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def whenyouturnhundred(self):
        now = datetime.datetime.now()
        hundrethYear = now.year + (100 - self.age)
        return hundrethYear


def main():
    user_name = input ("What's your name?")
    while True:
        try:
            user_age = int(input ("What's your age?"))
        except ValueError:
            print('that does not make sense')
            continue
        else:
            break

    person = Person(user_name, user_age)
    print(person.name + ' will be 100 in the year ' + str(person.whenyouturnhundred()))


if __name__ == '__main__':
    main()
