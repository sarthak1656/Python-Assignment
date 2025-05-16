def eval_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
    return stack.pop()

print("\nEvaluated Result of Postfix Expression:")
print(eval_postfix("231*+9-"))  # Example: (2 + (3 * 1)) - 9 = -4
