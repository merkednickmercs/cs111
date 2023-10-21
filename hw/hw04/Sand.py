

class Sand:
    def __init__(self, grid, x=0, y=0):
        self.grid = grid 
        self.x = x 
        self.y = y 

    def __str__ (self):
        return f"Sand({self.x},{self.y})"
    
    def gravity(self):
        if self.is_move_ok(self.x, self.y + 1):
            return self.x, self.y + 1
        elif self.is_move_ok(self.x - 1, self.y + 1):
            return self.x - 1, self.y + 1
        elif self.is_move_ok(self.x + 1, self.y + 1):
            return self.x + 1, self.y + 1
        else:
            return None

    def is_move_ok(self, x_to, y_to):
        if self.grid.in_bounds(x_to, y_to):
            if not self.grid.get(x_to, y_to) is None:
                return False 
            elif self.x != x_to and self.y != y_to:
                if self.grid.get(x_to, self.y) == 'r':
                    return False 
                else:
                    return True
                

            else:
                return True 
        else:
            return False 
        
    def move(self, physics):
        position = physics() 
        if position is None:
            return 
        self.grid.set(self.x, self.y, None)
        self.x, self.y = position
        self.grid.set(self.x, self.y, self)
