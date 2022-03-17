def MooToHuman(text):
    result = ''
    code = text.split(' ')
    for moo in code:
        if moo == 'mo':
            result += ' '
        else:
            o = moo[1:-1]
            ascii_num = len(o) + 95
            result += chr(ascii_num)
    return result


def HumanToMoo(text):
    msg = text.lower()
    result = ''
    for char in msg:
        ascii_num = ord(char) - 95
        o = 'o' * ascii_num
        result += f"w{o}f "
    return result

def main():
    while True:
        UserInput = input("\nSelect option: \nType '1' for Human to Dog translation \nType '2' for Dog to Human translation\n\n")

        if UserInput == '1':
            UserInput = input('\nEnter text:\n\n')
            print('\nResult:\n'+ HumanToDog(UserInput))
        elif UserInput == '2':
            UserInput = input('\nEnter text:\n\n')
            print('\nResult:\n'+ DogToHuman(UserInput))


if __name__ == '__main__':
    main()
