from cs50 import get_string
from sys import argv, exit


def main():
    if len(argv) < 2:
        exit(1)

    my_set = set(line.strip() for line in open(argv[1]))
    user_in = input("enter a message : ").lower()
    for word in user_in.lower().split():
        flag = False
        for x in my_set:
            if x == word:
                print("*" *len(word), end=" ")
                flag = True
                break
        if flag == False:
            print(word, end=" ")
    print('')


if __name__ == "__main__":
    main()
