class MazeSolver:
    
    def __init__(self, path):
        self._maze = self.text_to_array(path)
        self._cellstack = Stack()
        self._explored = []
        
    def text_to_array(self, path):
        f = open(path, "r")
        lines = [line.rstrip() for line in f]
        listoflist = []
    
        for line in lines:
            liste = []
            for i in line:
                liste.append(i)
            listoflist.append(liste)
            
        return Maze(listoflist)
    
    def get_a_neighbor(self, a_tuple):
        
        x = a_tuple[0]
        y = a_tuple[1]
        m = len(self._maze._list)
        n = len(self._maze._list[0])
        
        if (y+1 <= n-1):
            up = (x, y+1)
            validityChar = self._maze._list[x][y+1]
            if validityChar == "E" or validityChar == "O":
                if up not in self._explored:
                    return up
        
        if (y-1 >= 0):
            down = (x, y-1)
            validityChar = self._maze._list[x][y-1]
            if validityChar == "E" or validityChar == "O":
                if down not in self._explored:
                    return down
        
        if (x+1 <= m-1):
            right = (x+1, y)
            validityChar = self._maze._list[x+1][y]
            if validityChar == "E" or validityChar == "O":
                if right not in self._explored:
                    return right
            
            
        if (x-1 >= 0):
            left = (x-1, y)
            validityChar = self._maze._list[x-1][y]
            if validityChar == "E" or validityChar == "O":
                if left not in self._explored:
                    return left
        
        return a_tuple


    def solve_maze(self):
        self._cellstack.push(self._maze._start)
        while self._cellstack.is_empty() != True:
            c = self._cellstack.top()
            if c not in self._explored:
                self._explored.append(c)
            if c == self._maze._exit:
                return self._cellstack.returnContent()
            if self.get_a_neighbor(c) == c:
                self._cellstack.pop()
            else:
                self._cellstack.push(self.get_a_neighbor(c))
        
        return [(-1,-1)]
        
class Maze:
    
    def __init__(self, _listOfList):
        print("Maze is constructed by text_to_array method")
        print(_listOfList)
        self._list = _listOfList
        self.isValid(self._list)
        self._start = self.get_start(self._list)
        self._exit = self.get_exit(self._list)
        
    def isValid(self, _listOfList):
        if not len(_listOfList) > 3:
            raise InvalidMazeException("There must be more than 3 rows")
        
        listLength = len(_listOfList[0])
        sCount = 0
        eCount = 0
        sBoundaryCheck = 0
        eBoundaryCheck = 0
        
        for theList in _listOfList:
            if not len(theList) == listLength:
                raise InvalidMazeException("This is not a matrix")
            if not len(theList) > 3 : 
                raise InvalidMazeException("The array can not be smaller than 4x4")
            for i in range(len(theList)):
                if not isinstance(theList[i], str):
                    raise InvalidMazeException("It is not a char")
                if not len(theList[i]) == 1:
                    raise InvalidMazeException("Length of the character must be 1")
                if theList[i] not in ["X","O","S","E"]:
                    raise InvalidMazeException(theList[i] +" is not a maze element")

                if theList[i] == "S":
                    sCount += 1
                    if i == 0 or i == len(theList)-1 or i == len(_listOfList):
                        sBoundaryCheck += 1
                if theList[i] == "E":
                    eCount += 1
                    if i == 0 or i == len(theList)-1 or i == len(_listOfList):
                        eBoundaryCheck += 1
                    
        if sCount != 1 and eCount!= 1:
            raise InvalidMazeException("There is no exactly one S and one E") 
            
        if sBoundaryCheck != 1 and eBoundaryCheck!= 1:
            raise InvalidMazeException("The boundaries are not correct.") 
    
    def get_start(self, _listOfList):
        for m in range(len(_listOfList)):
            for n in range(len(_listOfList[m])):
                if _listOfList[m][n] == "S":
                    return (m,n)

    def get_exit(self, _listOfList):
        for m in range(len(_listOfList)):
            for n in range(len(_listOfList[m])):
                if _listOfList[m][n] == "E":
                    return (m,n)
    
class Stack:
    
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    
    def returnContent(self):
        T = Stack()
        
        while self.is_empty() != True:
            T.push(self.pop())
        
        List = []
        while T.is_empty() != True:
            List.append(T.pop())
        
        for i in range(len(List)):
            self.push(List[i])
                
        print(List)
        print("where " + str(List[0]) + " is start and " + str(List[-1]) + " is the end cell" )


class InvalidMazeException(Exception):
    pass                 

class Empty(Exception):
    pass


