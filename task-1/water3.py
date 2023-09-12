def initial_state():
    return (8, 0, 0)

def is_goal(s):
    x,y,z = s
    if x == 4 and y == 4:
        return True
    return False

def successors(s):
    x, y, z = s
    #pour water from one to another

    # pour x to y
    t = 5-y
    if t > 0 and x > 0:
        if x > t:
            yield ((x-t,5,z),t)
        else:
            yield ((0,y+x,z),x)
    # pour x to z
    t = 3-z
    if t > 0 and x > 0:
        if x > t:
            yield ((x-t,y,3),t)
        else:
            yield ((0,y,z+x),x)
    
    # pour y to x
    t = 8-x
    if t > 0 and y > 0:
        if y > t:
            yield ((8,y-t,z),t)
        else:
            yield ((x+y,0,z),y)
    #pour y to z
    t = 3-z
    if t > 0 and y > 0:
        if y > t:
            yield ((x,y-t,3),t)
        else:
            yield ((x,0,z+y),y)
    # pour z to x
    t = 8-x
    if t > 0 and z > 0:
        if z > t:
            yield ((8,y,z-t),t)
        else:
            yield ((x+z,y,0),z)
    # pour z to y
    t = 5-y
    if t > 0 and z > 0:
        if z > t:
            yield ((x,5,z-t),t)
        else:
            yield ((x,y+z,0),z)
