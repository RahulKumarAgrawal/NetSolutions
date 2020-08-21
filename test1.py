def CountFrequency(myList): 
      
   
   count = {} 
   for i in [1,1,2,3,4,5,3,2,3,4,2,1,2,3]: 
    count[i] = count.get(i, 0) + 1
   return count 
  
 
 
myList =[1,1,2,3,4,5,3,2,3,4,2,1,2,3] 
print(CountFrequency(myList))
