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
  ## Number
  
   - round() function 四舍五入
     ```
     >>> round(3.1415926,3)
     3.142
     ```
     
