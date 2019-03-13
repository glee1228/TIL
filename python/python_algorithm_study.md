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



#### 2. Using Both Keyword and Positional Unpacking

This keyword argument unpacking syntax can be used even if the function takes other parameters. However, the parameters must be listed in this order:

- All named positional parameters
- An unpacked positional parameter (`*args`)
- All named keyword parameters
- An unpacked keyword parameter (`**kwargs`)

Here's a function with all possible types of parameter:

```
def main(filename, *args, user_list=None, **kwargs):
  if user_list is None:
    user_list = []

  if '-a' in args:
    user_list = all_users()

  if kwargs.get('active'):
    user_list = [user for user_list if user.active]

  with open(filename) as user_file:
    user_file.write(user_list)
```

Looking at the signature of `main()` we define four different kinds of parameters. The first, `filename` is a normal required positional parameter. The second, `*args`, is all positional arguments given to a function after that organized as a tuple in the parameter `args`. The third, `user_list`, is a keyword parameter with a default value. Lastly, `**kwargs` is all other keyword arguments assembled as a dictionary in the parameter `kwargs`.

A possible call to the function could look like this:

```
main("files/users/userslist.txt", 
     "-d", 
     "-a", 
     save_all_records=True, 
     user_list=current_users)
```

In the body of `main()` these arguments would look like this:

- `filename == "files/users/userslist.txt"`
- `args == ('-d', '-a)`
- `user_list == current_users`
- `kwargs == {'save_all_records': True}`

We can use all four of these kinds of parameters to create functions that handle a lot of possible arguments being passed to them.

Instructions

1.

In **script.py** you'll find the function `remove()` has three parameters: the required positional `filename`, the arbitrary positional `args`, and the arbitrary keyword `kwargs`.

Before returning the text, we want to remove all arguments passed as positional arguments from the text. Using `text.replace()` change every `arg` in `args`into an empty string `""`.



Stuck? Get a hint

2.

Now iterate over every `kwarg` and `replacement` in `kwargs.items()` (recall this is how to iterate over key-value pairs in a dictionary).

Replace every instance of `kwarg` with `replacement` in `text`.



Hint

Like before, but also unpacking `.items()`:

```
for kwarg, replacement in kwargs.items():
  text.replace(kwarg, replacement)
```

3.

Now remove the bottom comment and see the text of *Robin Hood; Being A Complete History Of All The Notable And Merry Exploits Performed By Him And His Men, On Many Occasions.* by William Darton transformed!



##### 정답

```python
def remove(filename, *args, **kwargs):
  with open(filename) as file_obj:
    text = file_obj.read()
  #print(text)
  #print('--------------')
  # Add code here to update text.
  for arg in args:
    text=text.replace(arg,"")
  for kwarg,replacement in kwargs.items():
    #print(kwarg,replacement)
    text=text.replace(kwarg,replacement)
  return text

print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))

```

