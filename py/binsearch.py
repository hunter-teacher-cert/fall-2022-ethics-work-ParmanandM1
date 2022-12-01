# binsearch.py to conduct Binary Search
# First Last: Parmanand Mohanlall
# CSCI 77800 Fall 2022
# collaborators: 



def binary_search(listofNums,item):
  
	first = 0
	last = len(listofNums)-1
	found = False
  
	while( first<=last and not found):
		middle = (first + last)//2
    
		if listofNums[middle] == item :
			found = True
      
		else:
			if item < listofNums[middle]:
				last = middle - 1
        
			else:
				first = middle + 1	
        
	return found
	
print(binary_search([20, 40, 60, 80, 100], 20))
print(binary_search([30, 50, 70, 90, 110, 130], 40))