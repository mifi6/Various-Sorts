import random
import time

def RecordTime( method_name ):
    start = time.time()
    method_name()
    return time.time() - start


def CreateRandomList( size=100 ):
    lis = []
    for n in range( size ):
        lis.append( random.randint( 0, 10000) )
    return lis


def CheckSorted( lis ):
    n = 1
    while n < len( lis ):
        if lis[ n-1 ] > lis[ n ]:
            print( "Failed!" )
            print( n, "個目" )
            break
        n += 1
        if n >= len( lis ):
            print( "success" )

# 挿入ソート
def InsertionSort( lis ):
    print( "This is insertion sort" )
    length = len( lis )
    for i in range( 1, length ):
        v = lis[ i ]
        j = i - 1
        while j >= 0 and lis[ j ] > v:
            lis[ j + 1 ] = lis[ j ]
            j -= 1
        lis[ j + 1 ] = v
    return lis

# バブルソート
def BubbleSort( lis ):
    print( "This is bubble sort" )
    length = len( lis )
    nfirst = 0 # 未ソート部分の先頭のインデックス
    while nfirst < length:
        for n in range(length-1, nfirst, -1):
            #swap
            if lis[n-1] > lis[n]:
                lis[n-1], lis[n] = lis[n], lis[n-1]
        nfirst +=1
    return lis

def SelectionSort( lis ):
    print( "This is selection sort" )
    length = len( lis )
    for n in range( 0, length ):
        minj = n
        for j in range( n, length ):
            if lis[ j ] < lis[ minj ]:
                minj = j
        lis[ n ], lis[ minj ] = lis[ minj ], lis[ n ]
    return lis


def Partition( lis, low, high ):
    pivot = lis[ high ]
    i = low - 1
    for j in range( low, high ):
        if lis[ j ] <= pivot:
            i += 1
            lis[ i ], lis[ j ] = lis[ j ], lis[ i ]
    lis[ i+1 ], lis[ high ] = lis[ high ], lis[ i+1  ]
    return i + 1

def QuickSort( lis, low, high ):
    if low < high:
        p = Partition( lis, low, high )
        QuickSort( lis, low, p-1 )
        QuickSort( lis, p+1, high )
    return lis


nlist = []

nlist = CreateRandomList()
print(InsertionSort(nlist))
CheckSorted( nlist )

print()
print()

nlist = CreateRandomList()
print(BubbleSort(nlist))
CheckSorted( nlist )

print()
print()

nlist = CreateRandomList()
print(SelectionSort(nlist))
CheckSorted( nlist )

print()
print()

nlist = CreateRandomList()
print( "This is quick sort" )
print( QuickSort( nlist, 0, len( nlist )-1 ) )
CheckSorted( nlist )
