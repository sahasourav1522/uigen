# Calculates the average of a list of numbers
def calculate_average(numbers):
    # Return 0 early if the list is empty to avoid division by zero
    if not numbers:
        return 0
    total = 0
    # Sum all numbers in the list
    for num in numbers:
        total+= num
    # Divide total by count to get the average
    return total/ len(numbers)