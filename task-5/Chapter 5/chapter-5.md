1) Method 1: Using curly braces {}
   Method 2: Using the dict() constructor

2) my_dict = {'foo': 42}

3) * Dictionary: Stores data as key-value pairs, and we access values by their unique keys.
   * List: Stores data in a specific order, and we access values by their position (index) in the list.

4) If you try to access 'spam['foo']' and spam is a dictionary containing only '{'bar': 100}', you will get a 'KeyError' because the key 'foo'  does not exist in the spam dictionary.

5) * 'cat' in spam checks if there is a key 'cat' directly in the spam dictionary. It's like asking, "Is there a 'cat' in the dictionary?" It gives a quick yes or no answer.

* 'cat' in spam.keys() first makes a list of all the keys in the spam dictionary, and then it checks if 'cat' is in that list. It's like
asking, "Is 'cat' in the list of keys?" It takes a bit more time and memory.

7) spam.setdefault('color', 'black')

8) pprint module is used for this purpose. The primary function for pretty printing dictionaries is pprint() from the pprint module.