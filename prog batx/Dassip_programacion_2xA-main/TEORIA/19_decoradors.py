

def print_call(function):
    def print_function():
        print(f"La funció {function.__name__} s'ha executat" )
        return function
    return print_function

@print_call
def exemple_function():
    pass

@print_call
def exemple_function_2():
    pass

@print_call
def exemple_function_3():
    pass

exemple_function()
exemple_function_2()
exemple_function_3()

def call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(f"La funció {function.__name__} s'ha cridat {counter_function.call_count} cops")
        return function
    counter_function.call_count = 0
    return counter_function


@call_counter
def exemple_function_4():
    pass

@call_counter
def exemple_function_5():
    pass

exemple_function_4
exemple_function_5