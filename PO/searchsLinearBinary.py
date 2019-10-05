from random import *
from timeit import timeit
import matplotlib.pyplot as plt

def randomArray(length):
	array = []
	tmp = 0
	while tmp < length:
		num = randint(1, length*10)
		if num not in array:
			array.append(num)
			tmp += 1
	return array

def linearSearch(array, number):
	for i in range(0, len(array)):
		if(array[i] == number):
			return i
	return -1

def binarySearch(array, number):
	start = 0
	end = len(array) - 1
	if len(array) == 0:
		return
	else:
		i = (start + end) // 2
		if array[i] == number:
			return number
		else:
			if number < array[i]:
				return binarySearch(array[:i], number)
			else:
				return binarySearch(array[i+1:], number)

def desenhaGrafico(x, y1, y2, y3):

	plt.title('Linear x Binary Search Analysis', fontsize = 20)
	plt.plot(x, y1, label = "Linear Search")
	plt.plot(x, y2, label = "Binary Search")
	plt.plot(x, y3, label = "Difference")
	legend = plt.legend(loc='upper left', shadow = True)
	frame = legend.get_frame()
	frame.set_facecolor('0.90')
	plt.xlabel("Qnt. Elements(und)")
	plt.ylabel("Time(sec)")

	plt.show()

key = 0
linear_tmp = 0
binary_tmp = 0
difference_tmp = 0
linearAxis = []
binaryAxis = []
differenceAxis = []
lengths = []
elements = [6000, 9000, 12000, 15000, 24000]

def main():
	for _tmp in elements:
		lengths.append(_tmp)
		array = sorted(randomArray(_tmp))
		
		for i in range(10):
			key = array[randint(0, len(array)-1)]
			linear_tmp 		=+ timeit("linearSearch({}, {})".format(array, key), setup = "from __main__ import linearSearch", number = 1)
			binary_tmp 		=+ timeit("binarySearch({}, {})".format(array, key), setup = "from __main__ import binarySearch", number = 1)
			difference_tmp 	=+ ((timeit("linearSearch({}, {})".format(array, key), setup = "from __main__ import linearSearch", number = 1)) - (timeit("binarySearch({}, {})".format(array, key), setup = "from __main__ import binarySearch", number = 1)))
		
		linearAxis.append((linear_tmp/10))
		binaryAxis.append((binary_tmp/10))
		differenceAxis.append((difference_tmp/10))
	
	desenhaGrafico(lengths, linearAxis, binaryAxis, differenceAxis)

if __name__ == "__main__":
	main()

	