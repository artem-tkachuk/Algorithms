from typing import List

def execute(program: List[str]) -> List[int]:
    # initialize the stack
    stack = []
    # go through a list of instructions
    for instruction in program:
        if instruction == "peek":
            print(stack[-1] if stack else None)
        elif instruction == "pop":
            stack.pop() if stack else None
        else:  
            data = int(instruction.split(' ')[1])
            stack.append(data)
    
    return stack


if __name__ == '__main__':
    program = ["push 3", "push 7", "push 20", "peek", "pop", "push 0", "push 4", "pop"]
    res = execute(program)
    print(' '.join(map(str, res)))
