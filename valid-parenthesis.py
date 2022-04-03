# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.index = 0
#         self.size = 0

#     def push(self, value):
#         self.size += 1
#         self.index += 1
#         self.stack.append(value)

#     def pop(self):
#         self.size -= 1
#         self.index -= 1
#         return self.stack.pop(self.index)

#     def length(self):
#         return self.size


from fileinput import close


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 != 0:
        return False

    open_parenthesis = {"[", "(", "{"}
    close_parenthesis = {"]", ")", "}"}
    pairs = {"[]", "()", "{}"}
    stack = []

    for character in s:
        if character in open_parenthesis:
            stack.append(character)
        elif character in close_parenthesis:
            if len(stack) <= 0:
                stack.append(character)
            else:
                popped_char = stack.pop()
                comparison_string = str(popped_char) + str(character)
                if comparison_string not in pairs:
                    return False

    if len(stack) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    s = "){"
    print(isValid(s))
    exit()
