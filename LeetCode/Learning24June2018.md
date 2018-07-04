Today I learned about Heaps. My first learning was the the top of the heaps are also very helpful. For example if you want to find median of a on going data stream of numbers, you can use two heaps min and max. The top of min heap will be the rightHalf contribution and top of the firstHalf will be max.
Example : https://leetcode.com/problems/find-median-from-data-stream/description/

Some ting of functional programming in python: http://www.devlang.com/static/s17/cse294/functional-prog-in-python.pdf (This is yet to be read)

Today I also learned about heapq.merge using it with generator functions of python.
I really liked the concept. 
```python
     uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
```
