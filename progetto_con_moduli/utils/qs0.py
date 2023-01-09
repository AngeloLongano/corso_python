def enqueue(queue, x):
    queue.append(x)
def dequeue(queue):
    return queue.pop(0)
def emptyqueue(queue):
    return not queue
def head(queue):
    return queue[0]

def push(stack, x):
    stack.append(x)
def pop(stack):
    return stack.pop()
def emptystack(stack):
    return not stack
def top(stack):
    return stack[-1]