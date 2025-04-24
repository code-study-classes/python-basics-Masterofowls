def extract_file_name(path):
    return path.rsplit('/', 1)[-1].split('.')[0]


def encrypt_sentence(sentence):
    if not sentence:
        return ''
    # Get odd indices first in order (1,3,5...)
    odds = ''.join(sentence[1::2])
    # Then add even indices in reverse (8,6,4,2,0)
    evens = ''.join(sentence[::2][::-1])
    return odds + evens


def check_brackets(expression):
    count = 0
    for i, char in enumerate(expression):
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return i + 1
            if (count == 0 and i + 1 < len(expression) and 
                    expression[i + 1] == ')'):
                return i + 2
    return -1 if count > 0 else 0


def reverse_domain(domain):
    if '.' not in domain:
        return domain
    return '.'.join(domain.split('.')[::-1])


def count_vowel_groups(word):
    vowels = 'aeiouy'
    word = word.lower()
    count = 0
    in_group = False
    
    for char in word:
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    
    return count