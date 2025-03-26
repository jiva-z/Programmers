
inputs = []
result = []
while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    inputs.append((a,b))

for i, (a, b) in enumerate(inputs):
    if a % b == 0:
        result.append("multiple")
    elif b % a == 0:
        result.append("factor")
    else:
        result.append("neither")

print('\n'.join(result))