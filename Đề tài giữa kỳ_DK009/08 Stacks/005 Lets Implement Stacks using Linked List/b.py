stack = LinkedStack()
stack.push(5)
stack.push(3)

print(len(stack))        # Output: 2
stack.display()          # Output: 3 -> 5

popped_element = stack.pop()
print(popped_element)    # Output: 3

print(stack.isEmpty())   # Output: False
stack.display()          # Output: 5

top_element = stack.top()
print(top_element)       # Output: 5
