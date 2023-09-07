1) Empty List

2) By:-
   spam[2] = 'hello'
The result will make spam={2, 4, 'hello, 8, 10}

3) 'd'

4) 'd'

5) ['a', 'b']

6) '1'

7) The 'append()' method adds the specified element (in this case, '99') to the end of the list.
After 'bacon.append(99)' is executed, the list 'bacon' will look like this:
'[3.14, 'cat', 11, 'cat', True, 99]'.

8) The 'remove()' method removes the first occurrence of the specified value ('cat' in this case) from the list.
After 'bacon.remove('cat')' is executed, the list 'bacon' will look like this:
'[3.14, 11, 'cat', True, 99]'.

9) List Concatenation ('+')
   List Replication ('*')

10) The 'append()' and 'insert()' methods are both used to add elements to a list in Python, but they differ in how they add elements and where they add them within the list. 'append()' always adds an element to the end of the list, while 'insert()' allows you to add an element at a specific position within the list by specifying the index.

11) Using the remove() method and pop() method.

12) * Both support indexing, slicing, and iteration.
    * Both can be concatenated using the + operator.
    * We can find their length with the len() function.
    * We can test for membership using the in operator.

13) Lists:
    *  Can change (add, remove, modify) elements.
    * Use square brackets [].

    Tuples: 
    * Cannot change elements once set.
    * Use parentheses ().

14) my_tuple = (42)

15) Lists and tuples can be converted into one another using python functions. Example:-
    
    my_list = [1, 2, 3, 4]
    my_tuple = tuple(my_list)

    my_tuple = (1, 2, 3, 4)
    my_list = list(my_tuple)

17) copy.copy() creates a shallow copy. It duplicates the main object but not the nested objects inside it. Changes to nested objects affect both  the original and the copy.

copy.deepcopy() creates a deep copy. It duplicates the main object and all the nested objects inside it. Changes to nested objects in the copy do not affect the original.

In summary, deepcopy creates completely independent copies, while copy only duplicates the outer structure. 