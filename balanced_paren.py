from stack import Stack

def is_paren_balanced(paren_string):
    s = Stack()
    index = 0 
    is_balanced = True
    
    while index < len(paren_string) and is_balanced:
        p = paren_string[index]
        if p in '([{':
            s.push(p)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top_p = s.pop()
                if not is_match(top_p, p):
                    is_balanced = False
                    break
        index += 1
        
    if s.is_empty and is_balanced:
        return True
    else:
        return False
        

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False
    
    
print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))