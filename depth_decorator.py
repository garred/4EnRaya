from functools import wraps

def static_vars(**kwargs):
    """Adds static vars to functions.
    """
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate
        
def depth_decorator(func):
    """Prints the arguments and the returning value of a function with an 
    identation proportional to the depth of the function call. Useful with
    recurrent functions.
    """
    @wraps(func)
    @static_vars(depth=0)
    def new_f(*args, **kwargs):
        new_f.depth = new_f.depth + 1
        print new_f.depth*"|  " + "{}{}{}".format(func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        print new_f.depth*"|  " + "returns {}".format(result)
        new_f.depth = new_f.depth - 1
        return result
    new_f.depth = -1
    
    return new_f