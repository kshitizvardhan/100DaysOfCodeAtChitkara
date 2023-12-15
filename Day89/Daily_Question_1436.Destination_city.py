class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for path in paths:
            destination= path[1]
            ans= True
            for otherPaths in paths:
                if otherPaths[0]==destination:
                    ans= False
            if ans:
                return destination


        
