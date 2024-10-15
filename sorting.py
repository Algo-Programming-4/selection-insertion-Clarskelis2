def bubble(Numbers):
  for n in range(len(Numbers)):
    for i in range(len(Numbers) - 1):
      if Numbers[i] > Numbers[i + 1]:
        temp = Numbers[i]
        Numbers[i] = Numbers[i + 1]
        Numbers[i + 1] = temp
  return Numbers

def selection(Numbers):
  for i in range(len(Numbers)-1):
    index_smallest = i
    for j in range(i+1, len(Numbers)):
      if Numbers[j] < Numbers[index_smallest]:
        index_smallest = j
    temp = Numbers[i]
    Numbers[i] = Numbers[index_smallest]
    Numbers[index_smallest] = temp
  return Numbers

def insertion(Numbers):
  for i in range(1, len(Numbers)):
    j = i
    while j > 0 and Numbers[j] < Numbers[j - 1]:
      temp = Numbers[j]
      Numbers[j] = Numbers[j - 1]
      Numbers[j - 1] = temp
      j -= 1
  return Numbers
