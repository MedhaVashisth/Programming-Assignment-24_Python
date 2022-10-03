#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python 3 program to find an array
# element that divides all numbers
# in the array using naive approach

# Function to find smallest num
def findSmallest(a, n) :
	
	# Traverse for all elements
	for i in range(0, n ) :
		
		for j in range(0, n) :
			
			if ((a[j] % a[i]) >= 1) :
				break

		# Stores the minimum
		# if it divides all
		if (j == n - 1) :
			return a[i]
				
	return -1


# Driver code
a = [ 25, 20, 5, 10, 100 ]
n = len(a)
print(findSmallest(a, n))


# This code is contributed by Nikita Tiwari.


# In[2]:


def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 


# In[3]:


class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())


# In[4]:


# Python code to sort a list by creating
# another list Use of sorted()
def Sorting(lst):
	lst2 = sorted(lst, key=len)
	return lst2
	
# Driver code
lst = ["rohan", "amy", "sapna", "muhammad",
	"aakash", "raunak", "chinmoy"]
print(Sorting(lst))


# In[5]:


# Python3 program to generate pythagorean
# triplets smaller than a given limit

# Function to generate pythagorean
# triplets smaller than limit
def pythagoreanTriplets(limits) :
	c, m = 0, 2

	# Limiting c would limit
	# all a, b and c
	while c < limits :
		
		# Now loop on n from 1 to m-1
		for n in range(1, m) :
			a = m * m - n * n
			b = 2 * m * n
			c = m * m + n * n

			# if c is greater than
			# limit then break it
			if c > limits :
				break

			print(a, b, c)

		m = m + 1


# Driver Code
if __name__ == '__main__' :
	
	limit = 20
	pythagoreanTriplets(limit)


# This code is contributed by Shrikant13.


# In[ ]:




