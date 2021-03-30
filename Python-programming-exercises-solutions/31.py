def func(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 < l2:
        print(s2)
    elif l1 > l2:
        print(s1)
    else:
        print(s1)
        print(s2)

func("hello","world")