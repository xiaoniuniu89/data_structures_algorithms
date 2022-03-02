from unittest import result
from stack import Stack

def dec_to_bin(decimal):
    if decimal == 0:
        return 0
    
    stack = Stack()
    # while decimal > 0:
    #     if decimal % 2 == 0:
    #         stack.push(0)
    #     else:
    #         stack.push(1)
    #     decimal = decimal // 2 
        
    while decimal > 0:
        remainder = decimal % 2
        stack.push(remainder)
        decimal= decimal // 2
        
    binary_translation = ''
        
    # for i in range(len(stack.items)):
    #     binary_translation += str(stack.pop())
        
    while not stack.is_empty():
       binary_translation += str(stack.pop())
    
    return binary_translation
     
        
    



print(dec_to_bin(252))
print(dec_to_bin(47))
print(dec_to_bin(98))
print(dec_to_bin(545454))
print(dec_to_bin(7))


    
    