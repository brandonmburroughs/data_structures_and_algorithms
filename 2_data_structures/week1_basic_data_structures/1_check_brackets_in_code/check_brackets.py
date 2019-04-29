# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i + 1
            else:
                top_char, _ = opening_brackets_stack.pop()
                if not are_matching(top_char, next):
                    # Found unmatched closing bracket without opening bracket
                    return i + 1

    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        # Find first unmatched opening bracket
        _, first_position = opening_brackets_stack[0]
        return first_position + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
