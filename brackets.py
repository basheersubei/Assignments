#python3
#Bracket matching

import sys

if __name__ == "__main__":
    text = sys.stdin.readline()
    brackets_stack = []
    opening_brackets = ['[', '{', '(']
    closing_brackets = [']', '}', ')']

    for index, letter in enumerate(text):
        print("{}: {}".format(index, letter))

        if letter in opening_brackets:
            brackets_stack.append(letter)
            print("PUSH")

        elif letter in closing_brackets:

            if brackets_stack[-1] == '[' and letter == ']' or \
               brackets_stack[-1] == '(' and letter == ')' or \
               brackets_stack[-1] == '{' and letter == '}':
                brackets_stack.pop()
                print("POP")

            else:
                print("ERROR at index: {}".format(index))

        else:
            print("Not a bracket")
