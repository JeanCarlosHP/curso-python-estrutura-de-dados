from typing import List
from copy import deepcopy

stack: List[List[str]] = []

stack.append(['A'])
stack.append(['B'])
stack.append(['C'])

# For
for item in stack[::-1]:
    print(item)

# While
# A função copy só funciona para dados mutáveis
# stack_copy = stack.copy()
stack_copy = deepcopy(stack)
while stack_copy:
    item = stack_copy.pop()
    item += ['Manipulado']
    print(item)

print('Pilha:', stack)
