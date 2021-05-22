uniques = {3,13,15,27,1,4,8,23,19,12,9,2,17}
b = str(uniques)
def delete_set():
  a = {i for i in uniques if i % 2 != 0}
  return a


res = delete_set()
print(res)