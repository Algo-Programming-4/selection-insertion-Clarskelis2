def bubble(Unsorted):
  for n in range(len(Unsorted)):
    for i in range(len(Unsorted) - 1):
      if Unsorted[i] > Unsorted[i + 1]:
        temp = Unsorted[i]
        Unsorted[i] = Unsorted[i + 1]
        Unsorted[i + 1] = temp
  return Unsorted

def selection(list):
  for i in range(len(list)-1):
    index_smallest = i
    for j in range(i+1, len(list)):
      if list[j] < list[index_smallest]:
        index_smallest = j
    temp = list[i]
    list[i] = list[index_smallest]
    list[index_smallest] = temp
  return list

def insertion(list):
  for i in range(len(list)):
    j = i
    while (j > 0 && list[j] < list[j - 1]):
      temp = list[j]
      list[j] = list[j - 1]
      list[j - 1] = temp
      j -= 1
  return list
