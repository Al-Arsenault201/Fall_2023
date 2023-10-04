def add_to_list(l,m):
    m +=1
    print(id(l))
#    print(id(m))
    l2 = l
    print(id(l2))
    l3 = []
    for item in l:
        l3.append(item)
    print(id(l3))
    for i in range(len(l3)):
       l3[i] += 10
    return

if __name__ == "__main__":
   my_list = [1,2,3,4,5]
   n = 10
   print(id(my_list))
#   print(id(n))
   add_to_list(my_list,n)
   print(my_list)

