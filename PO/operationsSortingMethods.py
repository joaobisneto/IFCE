import matplotlib.pyplot as plt
from random import randint
import sys

sys.setrecursionlimit(100000)

def random_array(lenght):
	array = []
	while(len(array) < lenght):
		x = randint(1, 10*lenght)
		if x not in array:
			array.append(x)
	return array

def bubble(arr, count):
	count = 0
	for i in range(0, len(arr)-1):
		for j in range(i+1, len(arr)):
			count += 1
			if arr[i] > arr[j]:
				arr[j], arr[i] = arr[i], arr[j]
	print(count)
	return count

def selection(array, count):
	count = 0
	for position in range(len(array)-1, 0, -1):
		tmp = 0
		maxPosition = 0
		for location in range(1, position + 1):
			count += 1
			if array[location] > array[maxPosition]:
				maxPosition = location
		tmp = array[position]
		array[position] = array[maxPosition]
		array[maxPosition] = tmp
	print(count)
	return count

def insertion(array, count):
	count = 0
	for i in range(1, len(array)):
		tmp = 0
		tmp = array[i]
		position = i
		while position > 0 and array[position - 1] > tmp:
			array[position] = array[position - 1]
			position -= 1
			count += 1
		array[position] = tmp
	print(count)
	return count

def quick(arr):
	global quick_count
	quick_count += 1

	if len(arr) <= 1: return arr
	m = arr[0]
	return quick([i for i in arr if i < m]) + \
					[i for i in arr if i == m] + \
					quick([i for i in arr if i > m])


bubble_count = 0
insertion_count = 0
selection_count = 0  
op_bubble = []
op_selection = []
op_insertion = []
op_quick = []

# op_bubble_smooth = []
# op_selection_smooth = []
# op_insertion_smooth = []
# op_quick_smooth = []

lenght = []

# elements = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
elements = [1000, 3000, 6000, 9000, 12000]

def desenhaGrafico(x, y, w, z, xl = "Qnt. Elements(und)", yl = "Qnt. Operations(und)"):
	
	# plt.subplot(211)
	plt.title('Elementary Sort Methods Analysis', fontsize=20)
	plt.plot(lenght, x,	label = "Bubble Sort")
	plt.plot(lenght, y,	label = "Selection sort")
	plt.plot(lenght, w, label = "Insertion Sort")
	plt.plot(lenght, z,	label = "Quicksort")
	legend = plt.legend(loc='upper left', shadow=True)
	frame = legend.get_frame()
	frame.set_facecolor('0.90')

	# plt.subplot(212)
	# plt.plot(lenght, x_smooth, label = "Bubble Sort - Smoothed)
	# plt.plot(lenght, y_smooth, label = "Selection Sort - Smoothed)
	# plt.plot(lenght, w_smooth, label = "Insertion Sort - Smoothed)
	# plt.plot(lenght, z_smooth, label = "Quicksort - Smoothed)
	# legend = plt.legend(loc='upper left', shadow=True)
	# frame = legend.get_frame()
	# frame.set_facecolor('0.90')
	
	plt.xlabel(xl)
	plt.ylabel(yl)
	plt.show()	
	
def main():
	for _tmp in elements:
		lenght.append(_tmp)
		_tmp_array = random_array(_tmp)

		_tmp_bubble = list(_tmp_array)
		op_bubble.append(bubble(_tmp_bubble, bubble_count))

		_tmp_selection = list(_tmp_array)
		op_selection.append(selection(_tmp_selection, selection_count)) 

		_tmp_insertion = list(_tmp_array)
		op_insertion.append(insertion(_tmp_insertion, insertion_count))
		
		_tmp_quick = list(_tmp_array)
		global quick_count
		quick_count = 0
		quick(_tmp_array)
		op_quick.append(quick_count)
		print(quick_count)
		
	desenhaGrafico(op_bubble, op_selection, op_insertion, op_quick)

if __name__ == "__main__":
	main()

