#!python3

employees_marketing = {'Chris':20179, 'Christina':30670, 'Amanda':50240}

print('Dictionary:', employees_marketing)
print('Followers on social for Amanda:',employees_marketing['Amanda'])

del(employees_marketing['Chris'])
print('After deleting Chris: ', employees_marketing)