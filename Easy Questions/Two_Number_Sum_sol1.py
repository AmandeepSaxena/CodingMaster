def twonumbersum(array,targetSum):
  targetArr = []
  a = len(array)
  for i in (0, a-1):
    for i in (i+1, a):
      if array[i] + array[j] == targetSum:
        targetArr.append(array[i])
        targetArr.append(array[j])
  return targetArr
