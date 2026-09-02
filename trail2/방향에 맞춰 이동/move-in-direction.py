n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
# dir = [move[0] for move in moves]
# dist = [int(move[1]) for move in moves]

# Please write your code here.
x = 0
y = 0
dir_pos =  [(1, 0), (-1, 0), (0, -1), (0, 1)]

def change_to_pos(dir):
    if dir == 'E': _dir = dir_pos[0]
    elif dir == 'W' : _dir = dir_pos[1]
    elif dir == 'S' : _dir = dir_pos[2]
    else : _dir = dir_pos[3]
    return _dir

for dir, dist in moves:
    x += change_to_pos(dir)[0]*int(dist)
    y += change_to_pos(dir)[1]*int(dist)

print(x, y)