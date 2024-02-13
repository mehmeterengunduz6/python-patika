""""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] # [1,"a",["cat"],2]  [[[3]], "dog"]  4  5


def flatten(x):
    for ele in x:
        if type(ele) == list:
            yield from flatten(ele)
        else:
            yield ele
    
print(list(flatten(l)))

""""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]           
"""

li = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(li):
    new_li = []
    for i in li:
        if type(i) == list:
            m = []
            for k in i:
                m.insert(0,k)
            new_li.insert(0,m)
        else:
            new_li.insert(0,i)

    return new_li

print(reverse(li))


