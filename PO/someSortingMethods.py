import random
import math
import timeit
import matplotlib.pyplot as plt

timeBubble = []
timeSelection = []
timeInsertion = []
timeQuick = []
timeMerge = []
timeShell = []
timeCounting = []
timeRadix = []
timeBucket = []
elementos = [1000, 5000, 9000, 13000, 17000, 21000, 25000]

def randArray(length):
	array = []
	tmp = 0
	while tmp < length:
		num = random.randint(1, length*10)
		if num not in array:
			array.append(num)
			tmp += 1
	return array

def bubbleSort(array):
	for i in range(len(array)-1, 0, -1):
		for j in range(i):
			if array[j] > array[j+1]:
				tmp = array[j]
				array[j] = array[j+1]
				array[j+1] = tmp

def selectionSort(array):
	for position in range(len(array)-1, 0, -1):
		tmp = 0
		maxPosition = 0
		for location in range(1, position + 1):
			if array[location] > array[maxPosition]:
				maxPosition = location
		tmp = array[position]
		array[position] = array[maxPosition]
		array[maxPosition] = tmp

def insertionSort(array):
	for i in range(1, len(array)):
		tmp = 0
		tmp = array[i]
		position = i
		while position > 0 and array[position - 1] > tmp:
			array[position] = array[position - 1]
			position -= 1
		array[position] = tmp

def quickSort(array):
	pivote = len(array) // 2
	lesser, equal, greater = [], [], []
	for i in range(len(array)):
		if array[i] < array[pivote]:
			lesser.append(array[i])
		elif array[i] > array[pivote]:
			greater.append(array[i])
		else: equal.append(array[i])
	if len(lesser) > 1:
		lesser = quickSort(lesser)
	if len(greater) > 1:
		greater = quickSort(greater)
	return lesser + equal + greater

def mergeSort(array):
	if len(array) > 1:
		half = len(array) // 2
		lArray = array[:half]
		rArray = array[half:]

		mergeSort(lArray)
		mergeSort(rArray)

		lMark, rMark, position = 0, 0, 0

		while lMark < len(lArray) and rMark < len(rArray):
			if lArray[lMark] < rArray[rMark]:
				array[position] = lArray[lMark]
				lMark += 1
			else:
				array[position] = rArray[rMark]
				rMark += 1
			position += 1

		while lMark < len(lArray):
			array[position] = lArray[lMark]
			lMark += 1
			position += 1
		while rMark < len(rArray):
			array[position] = rArray[rMark]
			rMark += 1
			position += 1

def shellSort(array):
	gap = len(array) // 2
	while gap > 0:
		for i in range(gap):
			for j in range(i+gap, len(array), gap):
				_tmp = array[j]
				pos = j
				while pos>=gap and array[pos] > array[pos-gap]:
					array[pos] = array[pos-gap]
					pos = pos-gap
				array[pos] = _tmp
		gap = gap // 2

def countingSort(array):
	countI = max(array) + 1
	countA = [0]*countI
	position = 0
	for freq in array:
		countA[freq] += 1
	for freq in range(countI):
		for i in range(countA[freq]):
			array[position] += 1
			position += 1
	return array

def radixSort(lista):
    RADIX = 10
    maxLength = False
    tmp = -1
    placement = 1
  
    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range( RADIX )]
  
        for i in lista:
            tmp = i // placement
            buckets[tmp % RADIX].append( i )
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range( RADIX ):
            buck = buckets[b]
            for i in buck:
                lista[a] = i
                a += 1
    
        placement *= RADIX

def hashing(array):
    m = array[0]
    for i in range(1, len(array)):
        if ( m < array[i] ):
            m = array[i]
    result = [m,int(math.sqrt( len(array)))]
    return result
 
def re_hashing(i, code ):
    return int(i/code[0]*(code[1]-1))
 
def bucketSort(array):
    code = hashing(array)
    buckets = [list() for _ in range( code[1] )]
    for i in array:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
    for bucket in buckets:
        insertionSort(bucket)
         
    ndx = 0
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            array[ndx] = v
            ndx += 1

def timePopulate():
	for numElementos in elementos:
		base = []
		base = randArray(numElementos)

		_tmp = list(base)
		timeBubble.append(timeit.timeit("bubbleSort({})".format(_tmp), \
		setup="from __main__ import bubbleSort", \
		number=1))
		_tmp = list(base)
		timeSelection.append(timeit.timeit("selectionSort({})".format(_tmp), \
		setup="from __main__ import selectionSort", \
		number=1))
		_tmp = list(base)
		timeInsertion.append(timeit.timeit("insertionSort({})".format(_tmp), \
		setup="from __main__ import insertionSort", \
		number=1))
		_tmp = list(base)
		timeQuick.append(timeit.timeit("quickSort({})".format(_tmp), \
		setup="from __main__ import quickSort", \
		number=1))
		_tmp = list(base)
		timeMerge.append(timeit.timeit("mergeSort({})".format(_tmp), \
		setup="from __main__ import mergeSort", \
		number=1))
		_tmp = list(base)
		timeShell.append(timeit.timeit("shellSort({})".format(_tmp), \
        setup="from __main__ import shellSort", \
        number=1))
		_tmp = list(base)
		timeCounting.append(timeit.timeit("countingSort({})".format(_tmp), \
        setup="from __main__ import countingSort", \
        number=1))
		_tmp = list(base)
		timeRadix.append(timeit.timeit("radixSort({})".format(_tmp), \
        setup="from __main__ import radixSort", \
        number=1))
		_tmp = list(base)
		timeBucket.append(timeit.timeit("bucketSort({})".format(_tmp), \
        setup="from __main__ import bucketSort", \
        number=1))

def axis():
	timePopulate()

	plt.plot(elementos, timeBubble, label="Bubble Sort")
	plt.plot(elementos, timeSelection, label="Selection Sort")
	plt.plot(elementos, timeInsertion, label="Insertion Sort")
	plt.plot(elementos, timeQuick, label="QuickSort")
	plt.plot(elementos, timeMerge, label="MergeSort")
	plt.plot(elementos, timeShell, label="ShellSort")
	plt.plot(elementos, timeCounting, label="CountingSort")
	plt.plot(elementos, timeRadix, label="RadixSort")
	plt.plot(elementos, timeBucket, label="BucketSort")

def graphic():
	plt.legend(loc='upper center', shadow=True).get_frame().set_facecolor('0.90')
	plt.xlabel('Tamanho(int)')
	plt.ylabel('Tempo(s)')
	plt.show()

def main():
	axis()
	graphic()

if __name__ == "__main__":
	main()
