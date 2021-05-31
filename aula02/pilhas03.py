from typing import List

stack: List[str] = []

stack.append('A')
stack.append('B')
stack.append('C')

# Não fazer
first_item = stack.pop(0)

print(stack, first_item)
