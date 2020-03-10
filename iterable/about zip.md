# python-code-review
python을 python 답게

## ZIP
: 각 iterables의 요소들을 모으는 iterator를 만듬 
```
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
 ```
 
ex 1)
```
mylist = [ 1,2,3 ]
new_list = [ 40, 50, 60 ]
for i in zip(mylist, new_list):
    print (i)

>>(1, 40)
>>(2, 50)
>>(3, 60)
```

ex 2)
```
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))

>>{'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```

- zip() 을 '*' 연산자와 같이 쓰면 list upzip가능
