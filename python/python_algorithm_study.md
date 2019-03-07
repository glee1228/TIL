## 파이썬 문법 오답노트

* 잊지말아야할 파이썬 알고리즘 유형

#### 1. Delete Starting Even Numbers (소수시작점 지우기)

```
delete_starting_evens(lst)
```

소수 : 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

Instructions

1.

Write a function called `delete_starting_evens()` that has a parameter named `lst`.

The function should remove elements from the front of `lst` until the front of the list is not even. The function should then return `lst`.

For example if `lst` started as `[4, 8, 10, 11, 12, 15]`, then `delete_starting_evens(lst)` should return `[11, 12, 15]`.

Make sure your function works even if every element in the list is even!



##### 정답

```python
def delete_starting_evens(lst):
  new_list =[]
  for num in lst:
    check = 0
    for x in range(1,num+1):
      if num%x==0:
        check+=1
        
    
    if check==2:
      new_list = lst[lst.index(num):]
      return new_list
    
  return new_list
print(delete_starting_evens([4, 8, 10]))
```



