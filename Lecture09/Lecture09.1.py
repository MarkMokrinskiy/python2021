import time

def time_of_function(function):
    def wrapper():
        start_time = time.perf_counter()          # func 1
        res = function()                          # func  
        print(time.perf_counter() - start_time)   # func 2
        return res
    return wrapper

# Код выполняет подсчёт времени для любой function()