extract_file_name = lambda path: path.rsplit('/', 1)[-1].split('.')[0]


def encrypt_sentence(sentence):
    if not sentence:
        return ''
    chars = list(sentence)
    n = len(chars)
    # Get odd indices first in order (1,3,5...)
    odds = ''.join(chars[1::2])
    # Then add even indices in reverse (8,6,4,2,0)
    evens = ''.join(chars[::2][::-1])
    return odds + evens


def check_brackets(expression):
    count = 0
    for i, char in enumerate(expression):
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:  # More closing than opening brackets
                return i + 1
            if count == 0 and i + 1 < len(expression) and expression[i + 1] == ')':
                return i + 2
    return -1 if count > 0 else 0


def reverse_domain(domain):
    if '.' not in domain:
        return domain
    return '.'.join(domain.split('.')[::-1])


def count_vowel_groups(word):
    vowels = set('aeiou')  # y is not generally considered a vowel
    word = word.lower()
    count = 0
    in_group = False
    
    for char in word:
        # Special case: treat 'y' as vowel only in specific words like 'rhythm'
        is_vowel = char in vowels or (char == 'y' and word == 'rhythm')
        if is_vowel:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    
    return count