studentiVoti = {'rico':30,'micai':20,'shima':10}
studentiVoti['chiri'] = 50
if 'rico' in studentiVoti:
    print(studentiVoti.get('rico'))

for key,value in studentiVoti.items():
    print(f'{key} : {value}')

#{ expression for item in list if conditional }
print(studentiVoti['mamma'])#da keyerror