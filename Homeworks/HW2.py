def get_key(val):
    for key, value in average_dict.items():
         if val == value:
             return key

grades=[[50,60,70],
[30,40,70],
[80,90,70],
[20,50,90],
[70,60,40]]

students=[["Onur","Fatih","Burak","Ali","Nusret"],
["Ulutürk","Oda","Baş","Eser","Şahin"]]

average_list=[]
dict={}
average_dict={}

namesurname=["","","","",""]

for i in range(5):
	a=grades[i]
	t=sum(a)
	average_list.append(t)

for i in range(5):
	namesurname[i]=students[0][i]+" "+ students[1][i] 

for i in range(5):
    dict[namesurname[i]]=grades[i]
print(dict)

for i in range(5):
    average_dict[namesurname[i]]=average_list[i]
print(average_dict)
val_list = list(average_dict.values())
val_list.sort()
val_list.reverse()

print(get_key(val_list[0])+ " Congrulations")

