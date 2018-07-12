import re

s1 = '12345我*712abcde'
s2 = '.12345abcde'
# pattern字符串前加"r"表示原生字符串
pattern = r'\w.+'
# 编译pattern
pattern_compile = re.compile(pattern)
# match函数是从最开始匹配的，意思是如果第一个字符就不匹配，那就直接玩完，返回None
res1 = re.match(pattern_compile, s1)  # <_sre.SRE_Match object; span=(0, 11), match='我12345abcde'>
res2 = re.match(pattern_compile, s2)  # None

res3 = re.search(pattern_compile, s1)  # <_sre.SRE_Match object; span=(0, 11), match='我12345abcde'>
res4 = re.search(pattern_compile, s2)  # <_sre.SRE_Match object; span=(1, 11), match='12345abcde'>

pattern1 = r'\d+'
pc = re.compile(pattern1)
res5 = re.findall(pc, s1)  # ['12345', '712']

pattern2 = r'(\w+)\*(\w+)'
pattern_compile = re.compile(pattern2, re.I)  # re.I 或者 re.IGNORECASE 匹配不分大小写
# 返回匹配的整个字符串
res6 = re.match(pattern_compile, s1).group()  # 12345我*712abcde
res7 = re.match(pattern_compile, s1).start()  # 0
res8 = re.match(pattern_compile, s1).end()  # 15
res9 = re.match(pattern_compile, s1).span()  # (0, 15)

# 返回匹配的第一个子组字符串
res10 = re.match(pattern_compile, s1).group(1)   # 12345我
# 返回匹配的第二个子组字符串
res11 = re.match(pattern_compile, s1).group(2)   # 712abcde

# 返回含有所有子组的元组
res12 = re.match(pattern_compile, s1).groups()  # ('12345我', '712abcde')

print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(res7)
print(res8)
print(res9)
print(res10)
print(res11)
print(res12)
