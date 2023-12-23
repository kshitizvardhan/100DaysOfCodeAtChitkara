class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x=y=0
        visited=set()
        visited.add((x, y))
        for i in path:
            if i=="N":
                y+=1
            elif i=="S":
                y-=1
            elif i=="E":
                x+=1
            elif i=="W":
                x-=1
            current_pos=(x,y)
            if current_pos in visited:
                return True
            visited.add(current_pos)
        return False

