import sys
def sum_of_list(l):
  total=0
  for i in range(l):
    total = total+i
  return total

my_list =str(input())
print ("The sum of my_list is", sum_of_list(my_list))