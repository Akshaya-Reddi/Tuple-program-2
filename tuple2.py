tuple1 = tuple(map(int, input().split()))
tuple2 = tuple(map(int, input().split()))
tuple3 = tuple1 + tuple2
list = sorted(set(tuple3))
tuple4 = tuple(list)
print(tuple4)