from copy import deepcopy



class Grid:
    def __init__(self, width, height):
        self.width = width 
        self.height = height 
        self.array = [[None for x in range(width)]for y in range(height)]

    def in_bounds(self, x, y):
        return (x < self.width and x >=0) and (y < self.height and y>=0)

    def get(self, x, y):
        if not self.in_bounds(x, y):

            raise IndexError("indices are out of bounds")
            
        return self.array[y][x]
        
            

    def set(self, x, y, val):
        if self.in_bounds(x, y):
           self.array[y][x] = val 
           return None
        else:
            raise IndexError("indices are out of bounds")

    def __str__(self):
        return(f'Grid({self.height}, {self.width}, first = {self.array[0][0]})')
      

    def __repr__(self):
        return f'Grid.build({repr(self.array)})'
    
    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other
        return False 
    
    def check_list_malformed(lst):
        if not isinstance(lst, list):
            raise ValueError("input must be list object")
        if not lst:
            raise ValueError("Top-level list cannot be empty")
        if not all(isinstance(row, list) for row in lst):
            raise ValueError("Each element of the top-level list must be a list object")
        if len(set(len(row) for row in lst)) > 1:
            raise ValueError("each element of the top-level list must have the same length")

    def build(lst):
        Grid.check_list_malformed(lst) 
        height = len(lst)
        width = len(lst[0])

        new_grid = Grid(width, height)
        new_grid.array = deepcopy(lst)              
        return new_grid
    

    
    def copy(self):
        return Grid.build(self.array)


    
# self = Grid.build([[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 1), (1, 1), (2, 1), (3, 1)], [(0, 2), (1, 2), (2, 2), (3, 2)]])
# print(self.height)






