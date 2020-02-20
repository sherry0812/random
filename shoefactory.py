
shoes = input()

count = 0
pair = ''
for i in range(len(shoes)):
    if i == 0:
        pair += shoes[i]
    else:
        pair += shoes[i]
        if pair.count('L') == pair.count('R'):
            count += 1
            pair = ''
print(count)