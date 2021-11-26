import string

is_non_negative_num = lambda x: False if any([letter in x for letter in string.ascii_lowercase]) or '-' in x or x.count('.') > 1  else True
