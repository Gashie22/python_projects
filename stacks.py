#stack = LIFO
#WE CAN IMPLEMENT USING A LIST


def check_stack(stack):
    return len(stack)==0

def push_stack(item):
    stack.append(item)
    return ('the added item is '+ item)

def pop_stack (stack):
    if len(stack)==0:
        return ('stack is empty')
    else:
        return stack.pop()

stack=[]
push_stack(str(1))
push_stack(str(2))
push_stack(str(3))
print(stack)
pop_stack(stack)
pop_stack(stack)
pop_stack(stack)
pop_stack(stack)
print(stack)
