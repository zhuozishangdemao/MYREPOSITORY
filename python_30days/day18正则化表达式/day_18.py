import re
regex_pattern1 = r'才能'
regex_pattern2 = r'\b\d{2}-\d{2}-\d{4}\b'
regex_pattern3 = r'\b\w+ing\b'
regex_pattern4 = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'

paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
print(re.split(r'\s+',paragraph))
