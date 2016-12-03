'''
	Author: Dheeraj Pande
'''
def i_sort(a):
	'''
		this funtions takes list as input and returns sorted list
	'''
	assert type(a) == list, 'sort takes only list as input'
	for i in range(len(a)):
		key = a[i]
		j = i
		while j > 0 and a[j-1] > key:
			a[j] = a[j-1]
			j = j-1
		a[j] = key
	return a

if __name__ == "__main__":
	'''
		some test cases
	'''
	a = [1, 6, 7, 8, 12]
	a_output = i_sort(a)
	a_expected = [1, 6, 7, 8, 12]
	assert a_expected == a_output
	b = [31, 41, 59, 26, 41, 58]
	b_expected = [26, 31, 41, 41, 58, 59]
	b_output = i_sort(b)
	assert b_output == b_expected
	c = [5, 2, 4, 6, 1, 3]
	c_output = i_sort(c)
	c_expected = [1, 2, 3, 4, 5, 6]
	assert c_expected == c_output
