class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

    def __str__(self):
        return f"key: {self.key}, pos: {self.pos}"

    def __repr__(self):
        return f"Button{self.pos}, '{self.key}'"

class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """ """ """
    def __init__(self, *args):
        self.buttons = {}
        for button in args:
            self.buttons[button.pos] = button

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if info in self.buttons:
            button = self.buttons[info]
            button.times_pressed += 1
            return button.key
        return ""


    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        new_string = ''
        for position in typing_input:
            new_string += self.press(position)

        return new_string
    
    def __str__(self):
        new_str = ''
        count = 0 
        for button in self.buttons:
            button_str = str(self.buttons[button])
            if count < len(self.buttons) - 1:
                button_str += '|' 
            count+=1 
            new_str += button_str
        return new_str
    

    def __repr__(self):
        new_repr = ''
        count = 0 
        for button in self.buttons:
            button_repr = repr(self.buttons[button])
            if count < len(self.buttons) - 1:
                button_repr += ',' 
            count+=1 
            new_repr += button_repr
        return new_repr
    
