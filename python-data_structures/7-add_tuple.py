def add_tuple(tuple_a=(), tuple_b=()):
    new = f(tuple_a)
    new1 = f(tuple_b)
    return (new[0] + new1[0], new[1] + new1[1])
    
def f(t=()):
    if len(t) == 2:
        return(t[0],t[1])
    elif len(t) < 2:
     return( t[0],0)
    elif len(t) > 2:
        return (t[0],t[1])
