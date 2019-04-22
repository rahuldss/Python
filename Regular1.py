import re

print(re.sub(r'[ad]','*','abcde abcedf abcdef'))
print(re.sub(r'abc','*','abcde abcedf abcdef'))
print(re.sub(r'a.b','*','a2b axb a*b a&&b'))
print(re.sub(r'a..b','*','a2b axb a!b a&&b'))

m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))
