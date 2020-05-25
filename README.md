# djb2-hashing-algorithm-ported-to-python

Ths is the python ported version of djb2 hashing algorithm

Details of this algorithm can be seen in :
```
http://www.cse.yorku.ca/~oz/hash.html
```

This is the 64 bit version of the algorithm and currently supports ```String``` or ```list(Strings)```

To use the algo :

```
from djb2 import djb2
djb2.hashed("your string or list of strings")
```
