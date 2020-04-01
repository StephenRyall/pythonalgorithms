
def happyLadybugs(b):
   from collections import Counter
   c = Counter(b)
   c1 = bool(c['_'] >= 1)
   c2 = all( b[i] == b[i-1] or b[i] == b[i+1] for i in range(len(b)-1))
   c3 = all( v>1 for k,v in c.items() if k !='_')
   return 'YES' if c2&c3 or c1&c3  else 'NO'


print(happyLadybugs(['B', 'B', 'A', 'A', 'A', 'B', 'B']))