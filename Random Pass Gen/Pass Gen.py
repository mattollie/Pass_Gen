import random
import string

alpha = string.hexdigits
sing  = string.printable

list1 = []
list2 = []

def alphanumshort():
    i = 1
    while i < 15:
        y = random.choice(alpha)
        list1.append(y)
        i = i + 1
    print(''.join(list1))

def nonalphashort():
    i = 1
    while i < 15:
        y = random.choice(sing)
        list2.append(y)
        if y == "n":
            list2.remove(y)
        i = i + 1
    print(''.join(list2))


def alphanumlong():
    i = 1
    while i < 30:
        y = random.choice(alpha)
        list1.append(y)
        i = i + 1
    print(''.join(list1))


def nonalphalong():
    i = 1
    while i < 30:
        y = random.choice(sing)
        list2.append(y)
        if y == "n":
            list2.remove(y)
        i = i + 1
    print(''.join(list2))

def alphanumgo():
    i = 1
    while i < 1000:
        y = random.choice(alpha)
        list1.append(y)
        i = i + 1
    print(''.join(list1))

def nonalphago():
    i = 1
    while i < 1000:
        y = random.choice(sing)
        list2.append(y)
        i = i + 1
    print(''.join(list2))


def main():
    check = input('Alphanumeric pass? y or n')
    if check == 'y':
        check1 = input('What is character limit? Type 15, 30, or none')
        if check1 == '15':
            alphanumshort()
        elif check1 == '30':
            alphanumlong()
        elif check1 == 'none':
            alphanumgo()
    elif check == 'n':
        check2 = input('What is character limit? Type 15, 30, or none')
        if check2 == '15':
            nonalphashort()
        elif check2 == '30':
            nonalphalong()
        elif check2 == 'none':
            nonalphago()

if __name__ == '__main__':
    main()
