myList = [12, 23, 34, 45, 56, 67]
mysearch = 23
def binaryFun(myList, mysearch):
  first = 0
  last = len(myList) - 1
  mid = 0
  while first<=last:
    mid = (first + last)//2
    if myList[mid] == mysearch:
      return mid
    elif mysearch > myList[mid]:
      first = mid + 1
    elif mysearch < myList[mid]:
      last = mid - 1
  return "not found"
result = binaryFun(myList, mysearch)
print(result)