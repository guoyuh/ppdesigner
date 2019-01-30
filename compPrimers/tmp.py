
def sfs(input):
    # fn = lambda s:print()

    stack =[(0,-1)]

    while len(stack) > 0:

        top = stack.pop()
        if top[1] < len( input[top[0]] ) - 1:
            
            nextNode = [(top[0], top[1]+1)]
            stack = stack + nextNode
            
            for i in range(top[0]+1,len(input)):
                belowNode = [(i,0)]
                stack = stack + belowNode
            print stack
            
            #stack = stack + [(top[0], top[1]+1)]
            #if fn(stack) < cur:
            #    stack += [(i, 0) for i in range(top[0]+1, len(input))]

if __name__ == "__main__":
    input =[[1,2,3],[4,5],[6,7,8,9],[1,2]]
    sfs(input)
