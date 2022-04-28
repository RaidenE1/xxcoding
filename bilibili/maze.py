maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [
    lambda x,y:(x,y+1),
    lambda x,y:(x+1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x-1,y)
]
def maze_path(x1,y1,x2,y2):
    stack = []
    stack.append((x1,y1))
    while (len(stack)>0):
        curNote = stack[-1]
        #print(curNote)
        if curNote[0] == x2 and curNote[1] == y2:
            for s in stack:
                print(s)
            return True
        for dir in dirs:
            nextNote = dir(curNote[0],curNote[1])
            if maze[nextNote[0]][nextNote[1]] == 0:
                stack.append(nextNote)
                maze[nextNote[0]][nextNote[1]] = 2
                break
        else:
            maze[curNote[0]][curNote[1]] = 2
            stack.pop()
            
    else:
        print('No ways')
        return False
maze_path(1,1,8,8)