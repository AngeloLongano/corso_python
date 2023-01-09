from utils import qs0

s = input("parola: ")
rev = []
for c in s:
    qs0.push(rev, c)
while not qs0.emptystack(rev):
    print(qs0.pop(rev), sep='', end='')
print()
