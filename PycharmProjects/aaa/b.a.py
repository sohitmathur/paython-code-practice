prodid = ['A45678918','A78945615','A12334567','A8916647']
prefix=[]
for i in prodid:
    print(i)
    if len(i)==9:
        print('its perfect product id ')
    else:
        print('its not perfect product id')
    pre=i[0]
    print(pre)
    if pre=='A':
        prefix.append(pre)
    else:
        print('prefix values is not matched')
print(prefix)
