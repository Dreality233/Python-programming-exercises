import math
input_str = input()
directs = [ x for index,x in enumerate(input_str.split(' ')) if index % 2 == 0 ]
steps = [ int(x) for index,x in enumerate(input_str.split(' ')) if index % 2 != 0 ]
moves = list(zip(directs,steps))
pos = {'x':0,'y':0}
def up(step):
    pos['x'] += step

def down(step):
    pos['x'] -= step

def left(step):
    pos['y'] -= step

def right(step):
    pos['y'] += step

def default(step):
    pass

actions = {
    'UP': up,
    'DOWN': down,
    'LEFT': left,
    'RIGHT': right
}

for direct,step in moves:
    actions.get(direct,default)(step)
print(round(math.sqrt((abs(pos['x'])**2+abs(pos['y'])**2))))