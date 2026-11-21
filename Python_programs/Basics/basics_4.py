"""
Write stats(*nums) that returns (min, max, average), and call it with 3 numbers, then with 6.
"""

#used 1 as sufix not to conflict keywords

def stats(*nums):
  min1 = min(nums)
  max1 = max(nums)
  sum1 = 0
  size1 = len(nums)
  for i in nums:
    sum1 += i
  avg1 = sum1/size1

  print("Min: ",min1)
  print("Max: ",max1)
  print("Avg: ",avg1)
  print()

  return min1,max1,avg1


result1 = stats(1,2,3)
result2 = stats(1,2,3,4,5,6)