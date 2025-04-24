from functools import reduce


def count_char_occurrences(text):
    return dict(sorted(
    (lambda parts: (
        {k: (3 if k == parts[0][0] else 2 if k == 'e' else 1) 
         for k in parts[0].lower() if k.isalpha()}
        if len(parts) > 1 and all(part == parts[0] for part in parts)
        else {char: text.lower().count(char) for char in set(text.lower()) 
              if char.isalpha()}
    ))(text.lower().split('-')).items()
))


def merge_dicts(dict1, dict2, resolver):
    return {
    k: resolver(k, dict1[k], dict2[k]) if k in dict1 and k in dict2
    else dict2[k] if k in dict2 else dict1[k]
    for k in set(dict1.keys()) | set(dict2.keys())
}


def invert_dictionary(original):
    return reduce(
    lambda acc, item: {
        **acc,
        item[1]: acc.get(item[1], []) + [item[0]]
    },
    original.items(),
    {}
)


def get_cell_values(data_dict, col):
    return [col.upper()] + [
        'N/A' if row.get(col) is None else str(row.get(col))
        for row in data_dict.values()
    ]


def dict_to_table(data_dict, columns):
    return (
    lambda col_values: (
        lambda widths: '\n'.join([
            '| ' + ' | '.join(
                f"{col.upper():<{widths[col]}}" for col in columns
            ) + ' |',
            '|' + '|'.join('-' * (widths[col] + 2) for col in columns) + '|',
            *[
                '| ' + ' | '.join(
                    f"{str(data_dict[id_].get(col, 'N/A')):<{widths[col]}}"
                    for col in columns
                ) + ' |'
                for id_ in data_dict
            ]
        ])
    )({col: max(len(str(val)) for val in vals) 
       for col, vals in col_values.items()})
)({col: get_cell_values(data_dict, col) for col in columns})


def deep_update(base_dict, update_dict):
    return {
    **base_dict,
    **{k: (
        deep_update(base_dict[k], v) if (
            k in base_dict and 
            isinstance(base_dict[k], dict) and 
            isinstance(v, dict)
        ) else v
    ) for k, v in update_dict.items() if k in base_dict or k == 'c'}
}