import queue
from sys import argv

class status:
    def __init__(self,vars=None):
        if vars == None:
            self.build()
        else:
            self.modify(vars)
    def __lt__(self, other):
        return self.value < other.value
    def build(self):
        self.value = 0
        self.numofboxes = 0
        self.boxes = []
        self.initplayer = (0,0)
    def modify(self,vars):
        self.value = vars.value
        self.numofboxes = vars.numofboxes
        self.boxes = []
        for box in vars.boxes:
            self.boxes.append(box)
        self.initplayer = vars.initplayer
    def encoder(self):
        output = str(self.value)+str(self.numofboxes)+str(self.initplayer[0])+str(self.initplayer[1])
        for box in self.boxes:
            output+=str(box[0])+str(box[1])
        return output

def AStar(vars):
    count = 0
    for box in vars.boxes:
        if T[box]=='.':
            count+=1
    return vars.numofboxes-count

def search(vars):
    vars.value = AStar(vars)
    Hash = vars.encoder()
    hashMap[Hash] = ""
    q.put(vars)
    while not q.empty():
        s = q.get()
        baseHash = s.encoder()
        visited = {}
        visited[s.initplayer] = 1
        BFS = queue.Queue()
        BFS.put((s.initplayer[0],s.initplayer[1],""))
        while not BFS.empty():
            cords = BFS.get()
            for move in moves:
                wasBox = 0
                for index in range(s.numofboxes):
                    if (cords[0]+move[0],cords[1]+move[1])==s.boxes[index]:
                        wasBox = 1
                        if T[s.boxes[index][0]+move[0],s.boxes[index][1]+move[1]]!='#':
                            boxBlocked = 0
                            for box in s.boxes:
                                if box == (s.boxes[index][0]+move[0],s.boxes[index][1]+move[1]):
                                    boxBlocked = 1
                                    break
                            recordboxes = s.boxes
                            if boxBlocked == 0:
                                ss = status(s)
                                ss.initplayer = (cords[0]+move[0],cords[1]+move[1])
                                ss.boxes[index] = (ss.boxes[index][0]+move[0],ss.boxes[index][1]+move[1])
                                ss.value = AStar(ss)
                                toHash = ss.encoder()
                                if not toHash in hashMap:
                                    output = hashMap[baseHash]
                                    output += cords[2]
                                    if recordboxes != s.boxes:
                                        output += movesMapping[move]
                                    else:
                                        output += str.lower(movesMapping[move])
                                    hashMap[toHash] = output
                                    if ss.value == 0:
                                        return hashMap[toHash]
                                    q.put(ss)
                                break
                            break
                        break
                if wasBox == 0:
                    if T[cords[0]+move[0],cords[1]+move[1]] != '#' and (not (cords[0]+move[0],cords[1]+move[1]) in visited):
                        visited[cords[0]+move[0],cords[1]+move[1]] = 1
                        BFS.put((cords[0]+move[0],cords[1]+move[1],cords[2]+movesMapping[move]))


script,filename = argv
file = open(argv[1],"r")
lines = file.readlines()
q = queue.PriorityQueue()
moves=[(1,0),(-1,0),(0,1),(0,-1)]
movesMapping={(1,0):"D",(-1,0):"U",(0,1):"R",(0,-1):"L"}
T = {}
hashMap = {}
x = 0
y = 0
infor = status()
for line in lines:
    for letter in line:
        if letter!="\n":
            if letter == '&':
                infor.initplayer = (x,y)
                T[x,y] = ' '
            if letter == 'B':
                infor.numofboxes+=1
                infor.boxes.append((x,y))
                T[x,y] = ' '
            if letter == 'X':
                infor.numofboxes+=1
                infor.boxes.append((x,y))
                T[x,y] = '.'
            if letter == '%':
                infor.initplayer = (x,y)
                T[x,y] = '.'
            if letter == '.' or letter == '#' or letter == ' ':
                T[x,y]=letter
            y+=1
    x+=1
    y=0

solution = search(infor)
solution = str.swapcase(solution)
print(solution)