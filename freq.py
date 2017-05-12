import collections

testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

count_sum = sum(c.values())

for k,v in c.items():
    print("The frequency of number %s is %s" % (k, float(v)/count_sum))
