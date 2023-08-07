
soma_areas = 0

for i in range(1,5):
    print("Digite os dados pro {}º cômodo".format(i))
    l = float(input("L: "))
    c = float(input("C: "))
    area = l*c
    soma_areas = soma_areas + area

    print("A área deste cômodo é {} m2".format(area))

print("A área total é: {} m2".format(soma_areas))