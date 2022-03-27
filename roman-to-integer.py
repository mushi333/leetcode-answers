def romanToInt(s: str) -> int:
    # Vars used
    return_val = 0
    number = 0
    val_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    """
    Starting from the right most value, start summing the values, if the next value is less than the total sum, we sub-
    tract this value instead from the total.
    """
    for i in range(len(s) - 1, -1, -1):
        number = val_dict[s[i]]
        if 4 * number < return_val:
            return_val -= number
        else:
            return_val += number

    return return_val


if __name__ == '__main__':
    s = 'MCMXCIV'
    print(romanToInt(s))
    exit()
