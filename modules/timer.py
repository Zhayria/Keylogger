import threading

def schedule_every(interval, function):
    def wrapper():
        function()
        schedule_every(interval, function)  # Reschedule after running

    timer = threading.Timer(interval, wrapper)
    timer.daemon = True
    timer.start()
    print(f"[TIMER] Scheduled '{function.__name__}' to run every {interval} seconds.")
