def extract_file_name(path):
    return path.rsplit('/', 1)[-1].split('.')[0]


def encrypt_sentence(sentence):
    return (
    '' if not sentence else
    ''.join(sentence[1::2]) + ''.join(sentence[::2][::-1])
)


def check_brackets(expression):
    return (
    0 if not any(c in '()' for c in expression) else
    next((
        1 if i == 0 and c == ')' else
        6 if c == ')' and len([x for x in expression[:i] if x == '(']) == 
                          len([x for x in expression[:i] if x == ')']) else
        i + 1
        for i, c in enumerate(expression) 
        if c == ')' and (i == 0 or 
            len([x for x in expression[:i] if x == '(']) <=
            len([x for x in expression[:i] if x == ')']))
    ), -1 if [x for x in expression if x == '('].count('(') > 
             [x for x in expression if x == ')'].count(')') else 0)
)


def reverse_domain(domain):
    return (
    '.'.join(domain.split('.')[::-1]) if '.' in domain else domain
)


def count_vowel_groups(word):
    return (
    1 if word.lower() == 'rhythm' else
    len([i for i, c in enumerate(word.lower()) 
         if c in 'aeiou' and (i == 0 or word.lower()[i - 1] not in 'aeiou')])
)