# Summary
 
 Something I always forgot while writing code in Python
  
  ## Index
  
   - start it from the start index but the right index in not included.
    
      for example:
      ```
      for i in range(len(list)) => from 0 to len(list) - 1
      range[0,5]  => 0,1,2,3,4
      del a[2:4] => remove a[2],a[3]
      ```
      
  ## List
   - Remove elements
     - Remove all items: clear()
     - Remove an item by index and get its value: pop()
     - **Remove an item by value: remove()**
     - Remove items by index or slice: del
     - Remove items that meet the condition: List comprehensions

   - Slice [start:stop:step] (stop is not inclusive)
     ```
     >>> a = "-123"
     >>> a[::-1] #reverse the list
     '321-'
     >>> a[:0:-1]
     '321'
     >>> a[2:0:-1]
     '21'
     ```
   
   - Switch two elements
     ```
      s[i], s[j] = s[j], s[i]
     ```
  
  ## String
  
   - function eval() calculate the string
     ```
     >>> eval("200")
     200
     >>> eval("200 * 2")
     400
     ```
   - function ord() and chr() to convert between char and representing integer
     ```
     >>> ord("a")
     97
     >>> ord("z") - ord("a")
     25
     >>> ord("9")-ord("0")
     9
     >>> chr(97)
     'a'
     ```
   - Counter
     ```
     import collections
     >>> collections.Counter("alphabet")
     Counter({'a': 2, 'l': 1, 'p': 1, 'h': 1, 'b': 1, 'e': 1, 't': 1})
     ```
  ## Number
  
   - round() function 四舍五入
     ```
     >>> round(3.1415926,3)
     3.142
     ```
     
   - all() and any () return True/False
     ```
     >>> array = [1,2,3,4,5]
     >>> all(array[i] <= array[i+1] for i in range(len(array) - 1))
     True
     >>> array2 = [6,7,5,4,3,2,1]
     >>> any(array2[i] <= array2[i+1] for i in range(len(array2) - 1))
     True
     ```
