def sum_even_digits(number):
    total = 0
    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            total += int(digit)
    return total


def count_vowel_triplets(text):
    vowels = 'aeiou'  # y handled separately
    text = text.lower()
    count = 0
    i = 0
    
    while i <= len(text) - 3:
        triplet = text[i:i + 3]
        if 'y' in triplet:
            # Special case for 'y'
            if all(c == 'y' for c in triplet):
                count += 1
            i += 1
        elif all(c in vowels for c in triplet):
            count += 1
            i += 2  # Move by 2 to catch overlapping triplets like in "Queueing"
        else:
            i += 1
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