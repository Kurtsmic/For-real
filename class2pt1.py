def foo(z, x, y):
    w = z*x + y
    print("w is %d" % w)
    print("args=%d %d %d" % (x,y,z))
    return w
r=foo(1, 7, 10)
print(r)