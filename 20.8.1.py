s = input("Enter string ? ").lower()

# lệnh xóa whitespaces nhưng e ko chạy được ¿
# s.replace('  ', '')

table = dict()

for i in range(len(s)):
    if s[i] in table:
        table[s[i]] += 1
    else:
        table[s[i]] = 1

for k, v in sorted(table.items()):
    print(k, v)
