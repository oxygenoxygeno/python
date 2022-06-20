l=list()
def parrot(phrase):
    assert type(phrase)==str
    global l
    if phrase in l:
        return phrase
    else:
        l.append(phrase) 