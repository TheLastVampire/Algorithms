def insertion_sort(a):
	for j in range(1, len(a)):
		key = a[j]
		#everything to the left of j i ssorted
		i = j-1
		while i>=0 and a[i] > key:
			a[i+1] = a[i]
			i = i-1
		a[i+1] = key

#test the algorithm
def main():
	a = [2, -1, 6, 8, 0, 0, -4, 7]
	insertion_sort(a)
	print(a)

main()
