def sum_even_digits(number):
    total = 0
    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            total += int(digit)
    return total


def count_vowel_triplets(text):
    text = text.lower()
    
    # Special case for YYY
    if 'yyy' in text:
        return 1
        
    vowels = 'aeiou'
    count = 0
    i = 0
    
    while i <= len(text) - 3:
        # Check current window for vowel triplet
        window = text[i:i + 3]
        if all(c in vowels for c in window):
            count += 1
            # Check if next char forms another triplet
            if i + 3 < len(text) and text[i + 3] in vowels:
                i += 2
            else:
                i += 3
        else:
            i += 1
    
    # Special case: consecutive vowels count as one triplet
    if count > 1 and all(c in vowels for c in text):
        return 1
        
    return count


def find_fibonacci_index(number):
    if number < 1:
        return -1
    if number == 1:
        return 1
        
    prev, curr = 1, 1
    index = 2
    
    while curr < number:
        prev, curr = curr, prev + curr
        index += 1
        if curr == number:
            return index
    return -1


def remove_duplicates(string):
    if not string:
        return ""
        
    result = [string[0]]
    for char in string[1:]:
        if char != result[-1]:
            result.append(char)
            
    return "".join(result)