message = 'atcaoctaktne'
rails = [len(message)//2]*2

#print(rails)
remaining_chars = len(message) % 2
for i in range(remaining_chars):
    rails[i] += 1
#print(rails[1])
ra = [list(message[i : i + rails[j]]) for j, i in enumerate(range(0, len(message), max(rails)))]
print(ra)
msg = ''

for _ in range(len(message)):
    for i in range(2):
        if ra[i]:
            msg += ra[i].pop(0)
    print(ra)



 # rail = list[message[]]
# print(rails)
#
# print(remaining_chars)