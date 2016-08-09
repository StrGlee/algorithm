from random import *

def qsort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list     if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)

def qSort(a):
    if len(a) <= 1:
        return a
    else:
        q = choice(a)       #基准的选择不同于前，是从数组中任意选择一个值做为基准
        return qSort([elem for elem in a if elem < q]) + [q] * a.count(q) + qSort([elem for elem in a if elem > q])

qs = lambda xs : ( (len(xs) <= 1 and [xs]) or [ qs( [x for x in xs[1:] if x < xs[0]] ) + [xs[0]] + qs( [x for x in xs[1:] if x >= xs[0]] ) ] )[0]

if __name__=="__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(qs(a))
    print(qsort(a))
    print(qSort(a))
