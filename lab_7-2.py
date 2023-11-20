"""
Create a Python file named lab_7-2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a function called find_sum()
Add the parameters num1 and num2 to the definition of find_sum()
Add statements to the function that adds the arguments passed to num1 and num2 and stores them in a new variable num_sum
Finish the function with a statement that returns num_sum
Create a statement that calls the function to find the sum of 111 and 222. Set it equal to the variable my_sum
Add another print statement after the previous statement that prints my_sum
What happens when you run the program?

"""
#Author: Andrew Tkacs

def find_sum(num1, num2):
    """
    This function takes two numbers as parameters, adds them, then returns the sum.
    """
    # Add the arguments passed to num1 and num2, through the new variable
    num_sum = num1 + num2
    
    # Return the sum
    return num_sum

# Call the find_sum function with arguments 111 and 222

my_sum = find_sum(111, 222)

# Print the result

print(my_sum)

# When I ran the program, the result that printed was 333.  This is because the program was told to print the results of 111+222.