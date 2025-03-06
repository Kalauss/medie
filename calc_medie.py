print("La intrebari tip da/nu, foloseste 'yes' sau 'no' ")#Ptr. viitoare intrebari
nr=int(input("Cate note ai?: "))
i=0
suma=0
m=0
c=0
for x in range(nr):
    x=int(input("Cat este nota?: "))
    i=i+1
    suma=suma+x
m=suma/i
print("Media ta este ")
print(m)
if m>=4.5:
    print("Bravo, treci clasa! ")
else:
    print("Mult noroc la anu! ")
if m>=9.5:
    print("Nu numai ca treci clasa, mai iei si bursa! ")
else:
    print("Nu iei bursa, dar macar treci clasa")
while m<9.5:#Pentru a repara media
    m=(m+10)/2
    c=c+1
x=input("Doresti sa-ti repari media?: ")
if x=="yes":
    print("Ok, mai ai nevoie de ")
    print(c)
    print("Note de 10. ")
else:
    print("Ok, pai bravo! ")
    


    