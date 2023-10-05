l= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
    {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
d=[]
a=[]
for i in range(len(l)):
    d.append(list(l[i].values()))
    for element in d:
        if element not in a:
            a.append(element)
print(a)

