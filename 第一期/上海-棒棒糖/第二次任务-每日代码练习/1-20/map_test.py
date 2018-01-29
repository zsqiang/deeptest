def normalize(name):
    return name[:1].upper()+name[1:].lower()
if __name__=='__main__':
    L1=['adam','LISA','barT']
    L2=list(map(normalize,L1))
    print(L2)


def normalize(name):
    return name.capitalize()
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)