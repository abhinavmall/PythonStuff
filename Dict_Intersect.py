#If f(a, b) returns a + b
#d1 = {1:30, 2:20, 3:30, 5:80}
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
#then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

def f(a,b):
    return a + b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    intersect = { k:f(d1[k],d2[k]) for k in d1.keys() if k in d2.keys()}

    diff = {k:d1[k] for k in d1.keys() if k not in d2.keys()}
    diff.update({k:d2[k] for k in d2.keys() if k not in d1.keys()})

    return (intersect,diff)

print(dict_interdiff(d1, d2))
