# coding=utf-8

def binary_search(ds, fn):
    if len(ds)>1:
        if fn > ds[-1]:
            pass
        elif fn < ds[0]:
            pass
        mid = (len(ds)) / 2
        if fn < ds[mid]:
            binary_search(ds[:mid], fn)
        elif fn > ds[mid]:
            binary_search(ds[mid:], fn)
        else:
            print  fn
        pass
    else:
        print 1

ds = [10, 20, 9, 100, 78, 66, 53, 17]
ds.sort()
fn = 77

binary_search(ds, fn)
