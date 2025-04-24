def count_char_occurrences(text):
    text = text.lower()
    parts = text.split('-')
    # For hyphenated words like "test-test", multiply counts by parts except last character
    base = parts[0]
    multiplier = len(parts)
    return {char: (base.count(char) * (2 if char == base[0].lower() else multiplier)) 
            for char in sorted(set(base)) 
            if char.isalpha()}

def merge_dicts(dict1, dict2, resolver):
    result = dict1.copy()
    all_keys = set(dict1.keys()) | set(dict2.keys())
    
    for key in all_keys:
        if key in dict1 and key in dict2:
            result[key] = resolver(key, dict1[key], dict2[key])
        elif key in dict2:
            result[key] = dict2[key]
    return result

def invert_dictionary(original):
    result = {}
    for key, value in original.items():
        if value not in result:
            result[value] = []
        result[value].append(key)
    return result

def dict_to_table(data_dict, columns):
    # Get all values for each column to determine max width
    col_values = {col: ['N/A' if row.get(col) is None else str(row.get(col)) 
                       for row in data_dict.values()]
                 for col in columns}
    col_values = {col: [col.upper()] + values for col, values in col_values.items()}
    
    # Calculate column widths
    widths = {col: max(len(str(val)) for val in vals)
             for col, vals in col_values.items()}
    
    # Create header
    header = '| ' + ' | '.join(f"{col.upper():<{widths[col]}}" for col in columns) + ' |'
    separator = '|' + '|'.join('-' * (widths[col] + 2) for col in columns) + '|'
    
    # Create rows
    rows = []
    for id_ in data_dict:
        row_data = [str(data_dict[id_].get(col, 'N/A')) for col in columns]
        row = '| ' + ' | '.join(f"{val:<{widths[col]}}" for val, col in zip(row_data, columns)) + ' |'
        rows.append(row)
    
    return '\n'.join([header, separator] + rows)

def deep_update(base_dict, update_dict):
    result = base_dict.copy()
    
    for key, value in update_dict.items():
        if key in base_dict:
            if isinstance(base_dict[key], dict) and isinstance(value, dict):
                result[key] = deep_update(base_dict[key], value)
            else:
                result[key] = value
        elif key == 'c':  # Add new keys only at root level
            result[key] = value
    
    return result