choclates = int(input())
wrappers=choclates
exchange=3
while wrappers>=exchange:
    total_choclates=choclates//exchange
    new_choclates=total_choclates+wrappers
    wrappers = (wrappers % exchange)+new_choclates
print(choclates)