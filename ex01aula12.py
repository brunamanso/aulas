p=open('pares.txt', 'r')
i=open('impares.txt', 'r')
lista=[]

p.seek(0)
for linha in p:
    lista.append(int(linha))

i.seek(0)
for x in i:
    lista.append(int(x))

lista.sort()

t=open('numeroscompletos.txt', 'w')
for i in lista:
    t.write(str(i)+"\n")
p.close()
i.close()
t.close()
