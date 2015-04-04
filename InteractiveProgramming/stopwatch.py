# This is the simple stopwatch game.  The game prints 
# a time and score in the canvas and has three buttons 
# for start/stop/reset.  The object is to stop the running
# stopwatch on an even number of seconds.
import simplegui

def timer_tick():
    """Called by the timer, this increments the global
    time variable every tenth of a second"""
    global time
    time += 10

def start():
    """Start the timer when the button is pressed"""
    global timer
    if not timer.is_running():a
        timer.start()
    
def stop():
    """Stop the timer when the button is pressed"""
    global timer, stopped, precise
    if timer.is_running():
        stopped += 1
        timer.stop()
        if time % 10 == 0:
            precise += 1
    
def reset():
    """Reset the time when the button is pressed"""
    global timer, time, stopped, precise
    if timer.is_running():
        timer.stop()
    time = 0
    stopped = 0
    precise = 0
    
def format(t):
    """Converts an integer number of tenths of a second
    to [H:]M:SS.T format"""
    tsec = t % 10
    hour = t // 36000
    min = t // 600 % 60
    sec = t // 10 % 60
    if hour:
        return "%d:%02d:%02d.%d"%(hour,min,sec,tsec)
    else:
        return "%d:%02d.%d"%(min,sec,tsec)

def draw_handler(canvas):
    """Draw handler, prints the text on the screen"""
    global precise, stopped
    display = format(time)
    canvas.draw_text(display,[186-len(display)*10,75],30,"Red")
    score = "%d / %d"%(precise,stopped)
    canvas.draw_text(score, [300 - len(score)*10,20],20, "Red")

def key_handler(key):
    """Handle keydown events by calling appropriate functionss"""
    if key == 83:  # 's':
        start()
    elif key == 84: # 't':
        stop()
    elif key == 82: # 'r':
        reset()

# set starting values for global variables
time = 0
stopped = 0
precise = 0
timer = simplegui.create_timer(1,timer_tick)

# create frame, draw_handler, and key_handler
frame = simplegui.create_frame("Stopwatch",300,130)
frame.set_draw_handler(draw_handler)
# Adding key handler makes it too easy to cheat because
# you can start/stop over and over on the same second
# frame.set_keydown_handler(key_handler)
# create buttons
#frame.add_label("Click in the canvas to activate key presses")
frame.add_button("Start",start,150)
frame.add_button("Stop",stop,150)
frame.add_button("Reset",reset,150)
#frame.add_button("Start (key 's')",start,150)
#frame.add_button("Stop (key 't')",stop,150)
#frame.add_button("Reset (key 'r')",reset,150)
frame.start()
