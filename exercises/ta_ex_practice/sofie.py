"""Practice for Sofie´s Python Lab"""

from random import randint
# Here i imported the random number function from the Python randint package, but you should switch it to however you learned to incorporate random numbers. 

def even_sum_odd_product_of_number(number: int) -> int:
    """Returns product or sum based on if number is odd or even."""
    # If the number is even, compute the summation from 0 to that number. Use for loop.
    # If the number is odd, compute the product from 1 to that number. Use while loop.
    # even_sum: int = 0
    odd_product: int = 1
    i: int = 1
    while number % 2 == 1 and i <= number:
        odd_product = odd_product * i 
        i += 1
    return odd_product
    # Ok - the reason why I didn't do the even loop is because for a for loop to run, you need to be cycling through the items of a list
    # I'm okay with defining a new list and appending every single item from 1 to that number, but that's a lot of work and doesn't seem to be what the instructions want?
    # So I'm not exactly sure what your teacher is asking for in the even_sum. Worst case scenario, you go through and make another while loop and just lose points :=/


def mydivision(number_one: int, number_two: int) -> float:
    """Returns division of two numbers."""
    divided: float = 0.0
    divided = number_one / number_two
    if divided % 1 == 0 or divided % 2 == 0:
        # Because the number must either be even or odd
        return divided 
    else:
        return 123456789 # Or whatever your PSU Id is

def random_generator() -> None:
    """Takes a random number between 1-12 and generates some output."""
    # Repeats until 11 and 12 are generated
    i: int = 0
    while i < 10000:
        # Doesn't matter lol - I just put a super high number but this loop will keep repeating until 11 or 12 is reached, in which at that point the exit() function will cause the loop to exit. 
        random_number: int = randint(1, 12)
        if random_number == 1:
            print("One")
        elif random_number == 2:
            print("Two")        
        elif random_number == 3:
            print("Three")
        elif random_number == 4:
            print("Four")
        elif random_number == 5:            
            print("Five")
        elif random_number == 6:
        print("Six")
        elif random_number == 7:
            print("Seven")
        elif random_number == 8:
            print("Eight")
        elif random_number == 9:
            print("Nine")
        if random_number == 10:
            print("Number disregarded")
        if random_number == 11 or random_number == 12:
            print("Done")
            exit()    


def main() -> None:
    """Main function."""
    x: int = 5
    x = even_sum_odd_product_of_number(x)
    print(x)
    x = even_sum_odd_product_of_number(x)
    print(x)

main()



def sofie(list_x: list[int], x: int) -> bool:
    """Function displays all #s greater than x; returns true."""
    # If no number greater than x, return false
    i: int = 0
    greater: bool = False
    while i <= len(list_x):
        if (list_x[i] > x):
            print(list_x[i])
            greater = True
        i += 1
    return greater