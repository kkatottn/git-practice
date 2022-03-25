def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    if len(numbers) == 1:
        return numbers[0]
        
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num
=======
    return max(numbers)
>>>>>>> 3d92da9c90f8377edb7a91b9df82a06bb29a0704


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
