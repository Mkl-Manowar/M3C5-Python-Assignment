names = ["Peter", "Bruce", "Steve", "Tony", "Natasha",]

for name in names:
  print("Hi, " + name + " how are you?")

def suma(num_one, num_two, num_three,):
  return num_one + num_two + num_three


total = lambda num_one, num_two, num_three: f"the total is {num_one + num_two + num_three}"

print(total(1,3,6))


nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

for nombres in lista_nombre:
  if nombres == nombre:
    print(f"{nombre} si está en la lista")
    break
else:
  print(f"{nombre} no está en la lista")