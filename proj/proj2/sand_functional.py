"""
code taken from a project at Stanford CS106A
"""

import datetime
import tkinter
from Grid import Grid

def is_move_ok(grid, x_from, y_from, x_to, y_to):
    if grid.in_bounds(x_to, y_to):
        if not grid.get(x_to, y_to) == None:
            return False 
        elif x_from != x_to and y_from != y_to:
            if grid.get(x_to, y_from) == 'r':
                return False 
            else:
                return True
            

        else:
            return True 
    else:
        return False 




def do_move(grid, x_from, y_from, x_to, y_to):
    sand_particle = grid.get(x_from, y_from)
    grid.set(x_from, y_from, None)
    grid.set(x_to, y_to, sand_particle)

    return grid 
    


def do_gravity(grid, x, y):
    sand_particle = grid.get(x, y)
    if sand_particle is None:
        return grid 
    if sand_particle is 'r':
        return grid
    if is_move_ok(grid, x, y, x, y + 1):
        return do_move(grid, x, y, x, y + 1)
    if is_move_ok(grid, x, y, x-1, y + 1):
        return do_move(grid, x, y, x - 1, y + 1)
    if is_move_ok(grid, x, y, x + 1, y + 1):
        return do_move(grid, x, y, x + 1, y + 1)
    return grid 


def do_whole_grid(grid):
    for y in reversed(range(grid.height)):
        for x in range(grid.width):
            grid = do_gravity(grid, x, y)
    return grid



#########################################################

"""
Down here is not especially pretty code to set up the GUI,
handle the controls, and draw the grid to the screen.

Don't write any code below here.

"""


def draw_grid_canvas(grid, canvas, scale):
    """
    Draw grid to tk canvas, erasing and then filling it.
    This was ultimately the best performing approach.
    scale is pixels per block
    """
    # pixel size of canvas
    c_width = grid.width * scale + 2
    c_height = grid.height * scale + 2

    canvas.delete('all')

    # draw black per spot
    for y in range(grid.height):
        for x in range(grid.width):
            val = grid.get(x, y)
            if val:
                if val == 'r':
                    color = 'black'
                else:
                    color = 'yellow'
                rx = 1 + x * scale
                ry = 1 + y * scale
                canvas.create_rectangle(
                    rx, ry, rx + scale, ry + scale, fill=color, outline='black')

    canvas.create_rectangle(0, 0, c_width-1, c_height-1, outline='blue')
    canvas.update()


fps_enable = True
fps_count = 0
fps_start = 0


def fps_update():
    global fps_enable, fps_count, fps_start, fps_label
    if not fps_enable:
        return
    fps_count += 1
    if fps_count == 40:
        now = datetime.datetime.now().timestamp()
        delta = now - fps_start
        fps_start = now
        fps = int(1 / (delta / fps_count))
        # print(fps)
        fps_label.config(text=str(fps))
        fps_count = 0


# Global pointers to GUI elements we need in various callbacks
gravity = None
content = None
fps_label = None

SHIFT = 6


# provided function to build the GUI
def make_gui(top, width, height):
    """
    Set up the GUI elements for the Sand window, returning the Canvas to use.
    top is TK root, width/height is canvas size.
    """

    global gravity, content, fps_label
    gravity = tkinter.IntVar()
    content = tkinter.StringVar()

    top.title('Sand')

    # gravity checkbox
    gcheck = tkinter.Checkbutton(
        top, text='Gravity', name='gravity', variable=gravity)
    gcheck.grid(row=0, column=0, sticky='w')
    gravity.set(1)

    # content variable = state of radio button
    sand = tkinter.Radiobutton(top, text="Sand", variable=content, value='s')
    sand.grid(row=0, column=2, sticky='w')

    rock = tkinter.Radiobutton(top, text="Rock", variable=content, value='r')
    rock.grid(row=0, column=3, sticky='w')

    erase = tkinter.Radiobutton(
        top, text="Erase", variable=content, value='erase')
    erase.grid(row=0, column=4, sticky='w')

    bigerase = tkinter.Radiobutton(
        top, text="BigErase", variable=content, value='bigerase')
    bigerase.grid(row=0, column=5, sticky='w')

    content.set('s')

    # ugh 'fg' not a great name for this!
    fps_label = tkinter.Label(top, text="0", fg='lightgray')
    fps_label.grid(row=0, column=6, sticky='w')

    # canvas for drawing
    canvas = tkinter.Canvas(top, width=width, height=height, name='canvas')

    canvas.xview_scroll(SHIFT, "units")  # hack so (0, 0) works correctly
    canvas.yview_scroll(SHIFT, "units")

    canvas.grid(row=1, columnspan=12, sticky='w', padx=20, ipady=5)

    top.update()
    return canvas


def big_erase(grid, x, y, canvas, scale):
    """Erase big red circle in the given grid centered on x,y"""
    rad = 4
    # Compute circle around x,y in grid coords
    x1 = x - rad  # this can be out of bounds
    y1 = y - rad

    x2 = x + rad
    y2 = y + rad

    # Draw a red circle .. will be erased by later updates
    # Need to be consistent about grid -> pixel mapping
    canvas.create_oval(1 + x1 * scale, 1 + y1 * scale, 1 + x2 * scale, 1 + y2 * scale,
                       fill='red', outline='')
    canvas.update()

    for ey in range(y1, y2 + 1):
        for ex in range(x1, x2 + 1):
            # circle around x,y
            if grid.in_bounds(ex, ey) and abs(x-ex)**2 + abs(y-ey)**2 <= rad ** 2:
                grid.set(ex, ey, None)


def start_timer(top, speed, fn):
    """Start the my_timer system, calls given fn"""
    top.after(speed, lambda: my_timer(top, speed, fn))


def my_timer(top, speed, fn):
    """my_timer callback, re-posts itself."""
    fn()
    top.after(speed, lambda: my_timer(top, speed, fn))


def sand_action(grid, canvas, scale):
    """This function runs on timer for all periodic tasks."""
    global gravity
    global mouse_fn

    if mouse_fn:
        mouse_fn()

    if gravity.get():
        new_grid = do_whole_grid(grid)
        for y in range(grid.height):
            for x in range(grid.width):
                grid.set(x, y, new_grid.get(x, y))
    draw_grid_canvas(grid, canvas, scale)
    fps_update()


# global mouse sand_action function pointer
# set on mouse down, cleared on mouse-up
mouse_fn = None


def do_mouse_up(event):
    global mouse_fn
    mouse_fn = None


def do_mouse(event, grid, scale, canvas):
    """Callback for mouse click/move"""
    global mouse_fn
    def mouse_fn(): return do_mouse(event, grid, scale, canvas)

    x = (event.x - SHIFT // 2) // scale
    y = (event.y - SHIFT // 2) // scale
    if grid.in_bounds(x, y):
        global content
        val = content.get()  # 's' 'r' None
        if val == 's' or val == 'r':
            grid.set(x, y, val)
        elif val == 'erase':
            grid.set(x, y, None)
        elif val == 'bigerase':
            big_erase(grid, x, y, canvas, scale)
    # print('click', event.x, event.y)


# (provided)
def main():
    import argparse

    # setup the argument parser
    parser = argparse.ArgumentParser(description="Run Conway's game of life")
    parser.add_argument('--width', type=int, default=50,
                        help='width of the board, 50 by default')
    parser.add_argument('--height', type=int, default=50,
                        help='height of the board, 50 by default')
    parser.add_argument('--speed', type=int, default=1,
                        help='speed of each round, 1ms by default')
    parser.add_argument('--scale', type=int, default=10,
                        help='scale of board, 10 by default')

    # parse the command line arguments
    args = parser.parse_args()

    top = tkinter.Tk()
    canvas = make_gui(top, args.width * args.scale +
                      2, args.height * args.scale + 2)
    grid = Grid(args.width, args.height)

    canvas.bind("<B1-Motion>", lambda evt: do_mouse(evt,
                grid, args.scale, canvas))
    canvas.bind("<Button-1>", lambda evt: do_mouse(evt,
                grid, args.scale, canvas))
    canvas.bind("<ButtonRelease-1>", lambda evt: do_mouse_up(evt))

    start_timer(top, args.speed, lambda: sand_action(grid, canvas, args.scale))

    tkinter.mainloop()


if __name__ == '__main__':
    main()
