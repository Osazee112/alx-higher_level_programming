#!/usr/bin/python3
def add_tuple(tuple_a=(),tuple_b=()):
    tuple1 = list(tuple_a)
    tuple2 = list(tuple_b)
    re_tuple=[]
    for i in range(len(tuple_a)):
        if i <=1:
          re_tuple.append(tuple1[i]+tuple2[i])
        res_tuple=tuple(re_tuple)
    return res_tuple
