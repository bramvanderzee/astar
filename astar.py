import sys

lines = []
fn = 'input.txt'
if len(sys.argv) > 1:
    fn = sys.argv[1] 

with open(fn) as f:
    for x in f:
        lines.append(x.strip())

print(lines)
