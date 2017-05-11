'''Various list manipulation functions'''


def chop(ex):
    #removes the first and last elements from list
    del ex[0]
    del ex[-1]

def middle(ex):
    #returns all but the first and last items in the list
    x = ex[1:-1]
    return x

def split(ex):
    #splits list into 2 and returns both new lists.
    mid = (len(ex)/2)
    a = ex[: int(mid)]
    b = ex[int(mid):]
    return a, b

def fhalf(ex):
    #removes all elements from the middle to the end
    mid = (len(ex)/2)
    del ex[int(mid):]

def shalf(ex):
    #removes all elements from the start to the middle
    mid = (len(ex)/2)
    del ex[:int(mid)]
    

def unpack(ex):
    #Unpacks lists within lists and return new list with all values.
    #Repeat use until all items unpacked.
    new_list = []
    for x in ex:
        if  isinstance(x, int) or len(x) == 1:
            new_list.append(x)
        else:
            y = [a for a in x]
            for z in y:
                new_list.append(z)

    return new_list

def replace(ex, rem, add):
    #Replaces ALL counts of selected item with another item.
    for x in ex:
        if x == rem:
            loc = ex.index(x)
            ex[loc] = add
        else: continue    


def sep_type(ex):
    #Takes items of same type, puts them in a new list, and returns those lists.
    i = []
    f = []
    s = []
    t = []
    l = []
    d = []
    misc = []
    for x in ex:
        if isinstance(x, int):
            i.append(x)
        elif isinstance(x, float):
            f.append(x)
        elif isinstance(x, str):
            s.append(x)
        elif isinstance(x, tuple):
            t.append(x)
        elif isinstance(x, list):
            l.append(x)
        elif isinstance(x, dict):
            d.append(x)
        else:
            misc.append(x)

    return i, f, s, t, l, d, misc

