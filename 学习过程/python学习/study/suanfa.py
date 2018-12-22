# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-06-02 11:35:54
# @Last Modified by:   anchen
# @Last Modified time: 2018-06-02 13:00:05
def Two(a,num):
    lenth=len(a)
    low=0
    high=lenth-1
    while low<=high:
        mid=int(low+((high-low)/2))
        if a[mid]<num:
            low=mid+1
        else if a[mid]>num:
            high=mid-1
        else:
            return mid
    return -1

if(__name__='__main__'):
    b=[1,3,5,6,7,8,9,10]
    print(b)
    a=Two(b,10)
    print(a)
