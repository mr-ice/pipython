import simplegui

def timer_tick():
    global time
    time += 1

def start():
    global timer
    if not timer.is_running():
        timer.start()
    
def stop():
    global timer, stopped, precise, canvas
    if timer.is_running():
	    stopped += 1
        timer.stop()
        if time % 10 == 0:
            precise += 1
    
def reset():
    global time
    time = 0
    
def format(t):
    """Converts an integer number of tenths of a second
    to M:SS.TT format"""
    tsec = t % 10
    hour = t // 36000 % 60
    min = t // 600 % 60
    sec = t // 10 % 60
    if hour:
        return "%d:%02d:%02d.%d"%(hour,min,sec,tsec)
    else:
        return "%d:%02d.%d"%(min,sec,tsec)

def draw_handler(canvas):
    global precise, stopped
    canvas.draw_text(format(time),[100,135],30,"Red")
    canvas.draw_text("%d / %d"%(precise,stopped), [250,20],20, "Red")
    
time = 0
stopped = 0
precise = 0
timer = simplegui.create_timer(300,timer_tick)

frame = simplegui.create_frame("Stopwatch",300,300)
frame.set_draw_handler(draw_handler)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
frame.start()
