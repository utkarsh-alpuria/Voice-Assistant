# import modules
from types import SimpleNamespace # for creating empty classes
from listener_thread import wake_word_listener # importing wake_word_lintener class from listener.py
import eel

g_params = SimpleNamespace() # creating empty class g_params
g_params.is_running = False # parameter that tells wether listening is happening or not(initially False)
g_params.wake_word_listener = wake_word_listener() # creating wake_word_listener class object
g_params.wake_word_listener.daemon = True # making the daemon value of object True(it will run the object in parallel thread)
g_params.wake_word_listener.start() # starting the object thread

@eel.expose
def start_stop_function(): # start_stop_btn function callback
    g_params.is_running = not g_params.is_running # toggle between start and stop
    if g_params.is_running:
        eel.is_running_true() 
    else:
        eel.is_running_false()      
    g_params.wake_word_listener.start_stop(g_params.is_running) # calling "start_stop" method of "wake_word_listener" object 



# eel.init("web_copy_2")
# eel.start("gui.html")
