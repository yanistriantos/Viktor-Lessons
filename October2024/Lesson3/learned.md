## Learned

C bindings -> a function runs almost as fast as in C (x50 -> x500 faster)

with operator: context management

```python
file = open("file-name", "r+")
content = file.read()
print(content)
// file.close() # memory leak

with open("file-name", "r+") as file:
    content = file.read()
    print(content)
```

1. C-bindings
2. with operator
3. os, shutil, datetime, json, csv
4. 4-5 hackerrank exercises

Optional
1. Read python tutorial
2. Watch python course 
