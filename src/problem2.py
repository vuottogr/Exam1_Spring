"""
Exam 1, problem 3. 35 Points Total

Modified by Dr. Brackin,
There are several parts of this problem that are straightforward.
I suggest that you start with those elements and add the more
difficult elements as time permits.
Every student should be able to print the string and the
length of the string.  If you don't remember how, LOOK at
your programming sessions!!!   
Elle Vuotto.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2()


def reverseString(string):
    """
    Reverses the string that is passed to it as input argument
    and returns the reversed string.

    for example, the call reverseString('abc') will return 'cba'
    for example, the call reverseString('EYE') will return 'EYE'
    for example, the call reverseString('Python') will return
    'nohtyP'
    For full credit on this problem, you may NOT use this function.
    For full credit on this problem, you must write your own function.
    Remember, do NOT give your function the same name.
    """
    string = string[::-1]
    return string


def test_problem2():
    """
    Read the description of problem3 below.  One test case is provided for you below.
    You are to write 3 more test cases that are reasonable tests for the function.
    Remember, if you cannot write the reverse string code, you may use the one above.
    Remember, if you do write your own reverse string code, use a function name that
    is different than the one given above
    """
    #  Test case 1
    #  The given string is civic
    print('*********************************************')
    print('Test case 1 Expected: ')
    print('*********************************************')
    string_of_characters = 'civic'
    print('String entered: ',string_of_characters)
    print('Length of string: ',5)
    print('Number of alphabetic characters: ',5)
    print('Number of digits: ', 0)
    print('Reversed string is: civic')
    print('The user entered a palindrome')
    print()
    print('*********************************************')
    print('Test case 1 Actual: ')
    problem3(string_of_characters)
    print('*********************************************')
    # TODO: 2. Write at least three reasonable test cases below.
    #         Three excellent test cases are worth 10 points

    print('*********************************************')
    print('Test case 2 Expected: ')
    print('*********************************************')
    string_of_characters = 'mom'
    print('String entered: ',string_of_characters)
    print('Length of string: ',3)
    print('Number of alphabetic characters: ',3)
    print('Number of digits: ', 0)
    print('Reversed string is: mom')
    print('The user entered a palindrome')
    print()
    print('*********************************************')
    print('Test case 2 Actual: ')
    problem3(string_of_characters)
    print('*********************************************')

    print('*********************************************')
    print('Test case 3 Expected: ')
    print('*********************************************')
    string_of_characters = 'racecar'
    print('String entered: ',string_of_characters)
    print('Length of string: ',7)
    print('Number of alphabetic characters: ',7)
    print('Number of digits: ', 0)
    print('Reversed string is: racecar01')
    print('The user entered a palindrome')
    print()
    print('*********************************************')
    print('Test case 3 Actual: ')
    problem3(string_of_characters)
    print('*********************************************')

    print('*********************************************')
    print('Test case 4 Expected: ')
    print('*********************************************')
    string_of_characters = 'yay'
    print('String entered: ',string_of_characters)
    print('Length of string: ',4)
    print('Number of alphabetic characters: ',4)
    print('Number of digits: ', 0)
    print('Reversed string is: yay')
    print('The user entered a normal string')
    print()
    print('*********************************************')
    print('Test case 4 Actual: ')
    problem3(string_of_characters)
    print('*********************************************')



def problem3(string_of_characters):
    """
    What comes in:
          -- a string of characters that contains letters of the alphabet and/or numbers
        What goes out:
          Nothing
        Side effects:
        Prints, in this order, on separate lines,
      -- The string entered by the user
      -- The length of the string entered by the user
      -- The number of alphabetic characters in the string
      -- The number of digits (integers 0-9) in the string
      -- The reverse string entered by the user
      -- If the string is a palindrome - it prints, the user entered a
      -- palindrome
      -- If the string is not a palindrome - it prints, the user entered a
      -- normal string
      Nothing else should be printed.

        Examples:
          See the TEST cases for examples.
        Type hints:
          :type string_of_characters: string

    A palindrome is a phrase that reads the same backwards. For example,
    the words eye, madam are palindromes because they read the same
    backwards.

    To implement this function, you need to reverse a string. If you write
    your own method to reverse a string and solve the entire problem, you
    will get 35 points. If you use the provided method
    reverseString(string), you will get 30 points

    Here are some examples:
       string_of_characters = 'eye'
       String entered: eye
       Length of string: 3
       Number of alphabetic characters: 3
       Number of digits: 0
       Reversed string: eye
       The user entered a palindrome

       string_of_characters = 'abc1cba'
       String entered: abc1cba
       Length of string: 7
       Number of alphabetic characters: 6
       Number of digits: 1
       Reversed string: abc1cba
       The user entered a palindrome

       string_of_characters = 'a12b'
       String entered: a12b
       Length of string: 4
       Number of alphabetic characters: 2
       Number of digits: 2
       Reversed string: b21a
       The user entered a normal string
    """
    # done: 3. Implement this function.
    # To implement this function, you need to reverse a string.
    # If you write your own method to reverse a string and solve
    # the entire problem, you will get 25 points. If you use the
    # provided method reverseString(string),you will get 20 points

    string = string_of_characters
    length = len(string_of_characters)
    print('String of characters:', string)
    print('Length of string:', length)


    totals = 0
    for k in range(len(string_of_characters)):
        m = string_of_characters[k]
        if type(m)== str:
            totals = totals + 1
    print('Number of alphabetic characters:', totals)

    total = 0
    for k in range(len(string_of_characters)):
        n = string_of_characters[k]
        if type(n) == int:
            total = total + 1
    print('Number of digits:', total)

    newstring = ''
    for k in range(len(string_of_characters)):
        string = string_of_characters[k]
        string = string[::-1]
        newstring = newstring + string
    print('Reversed string:', newstring)
    if newstring == string_of_characters:
        print('The user entered a palindrome')
    else:
        print('The user entered a normal string')





# -----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# -----------------------------------------------------------------------


if __name__ == '__main__':
    main()


