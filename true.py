s = 'azcbobobegghakl'
l = len(s) - 1
i = 0
textFirst = ''
while i <= l - 1:
    n = i
    k = i + 1
    textSecond = s[n]
    while s[n] <= s[k]:
        textSecond = textSecond + s[k]
        n += 1
        k += 1
        if k > l:
            break
    if len(textSecond) > len(textFirst):
        textFirst = textSecond
    i += 1
print('Longest substring in alphabetical order is:',textFirst)
