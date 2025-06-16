import threading

def schedule_every(interval, function):
     
    # Repeatedly schedules a function to run every `interval` seconds.
    #
    # Parameters:
    #  - interval (int or float): Time between executions, in seconds
    #  - function (callable): The function to be run periodically
    
    def wrapper():
        function()
        # Recursively reschedule the same function
        schedule_every(interval, function)
    # Create a background timer thread that runs the wrapper after `interval` seconds
    timer = threading.Timer(interval, wrapper)
    timer.daemon = True
    timer.start()
    print(f"[TIMER] Scheduled '{function.__name__}' to run every {interval} seconds.")
