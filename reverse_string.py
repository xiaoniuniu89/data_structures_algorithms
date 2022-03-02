from stack import Stack

def reverse_string(stack, str):
    for i in range(len(str)):
        stack.push(str[i])
    reverse_str = ""
    while not stack.is_empty():
        reverse_str += stack.pop()
        
    return reverse_str

stack = Stack()
string = "!evitacudE ot emocleW"
print(reverse_string(stack, string))