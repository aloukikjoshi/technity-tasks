1) Escape characters are special characters in a string that have a specific meaning and are preceded by a backslash (\). They are used to represent characters that are either difficult or impossible to type directly into a string, or they can be used to convey special meanings within the string. 

2) \n: Newline character. It represents a line break, causing the text following it to start on a new line.
   \t: Tab character. It represents a horizontal tab, creating space between characters.

3) To include a backslash (\) character in a string, we need to escape it by using a double backslash (\\). 

4) The string "Howl's Moving Castle" is indeed a valid string in Python, and we don't need to escape the single quote character within the string. This is because Python allows we to create strings using either single quotes (') or double quotes ("), and we can freely mix them as long as we start and end the string with the same type of quote.

5) * Triple-Quoted Strings: You can use triple-quoted strings (either triple single-quotes ''' or triple double-quotes """) to create multi-line   strings. These strings can span multiple lines without needing to use \n for line breaks. For example:

      my_string = '''This is a string
      with multiple lines
      without using \\n.'''

   * Concatenation: You can create a string by concatenating multiple strings, each representing a line, using the + operator. For example:

      line1 = "This is a string"
      line2 = "with multiple lines"
      line3 = "without using \\n."
      my_string = line1 + '\n' + line2 + '\n' + line3

6) (i) 'Hello, world!'[1]:
       This expression extracts the character at index 1 (the second character) of the string. The result is the character 'e'.

  (ii) 'Hello, world!'[0:5]: This expression extracts a substring starting at index 0 (inclusive) and ending at index 5 (exclusive). The result is the substring 'Hello'.

 (iii) 'Hello, world!'[:5]: This expression extracts a substring starting from the beginning (index 0) and ending at index 5 (exclusive). The result is the substring 'Hello'.

  (iv) 'Hello, world!'[3:]: This expression extracts a substring starting at index 3 (inclusive) and extending to the end of the string. The result is the substring 'lo, world!'.

7) (i) 'Hello'.upper(): This expression converts the string 'Hello' to uppercase. The result is 'HELLO'.

  (ii) 'Hello'.upper().isupper(): Here, we take the result of 'Hello'.upper(), which is 'HELLO', and then use the isupper() method to check if all characters in the string are uppercase. The isupper() method returns a boolean value. The result is True because all characters in 'HELLO' are indeed uppercase.

 (iii) 'Hello'.upper().lower(): We first convert 'Hello' to uppercase ('HELLO'), and then we use the lower() method to convert it back to lowercase. The result is 'hello'.

8) The first expression splits the given string into a list of words based on whitespace (spaces and/or tabs) as the default delimiter. Results in ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.'].

The second expression splits the string 'There can be only one.' into a list of words based on whitespace, resulting in ['There', 'can', 'be', 'only', 'one.']. Then, it uses the join() method to join the elements of the list using a hyphen ('-') as the separator. The result is 'There-can-be-only-one.'.

10) Using lstrip() and rstrip() functions.