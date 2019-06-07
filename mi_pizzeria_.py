Bienvenidos a Amore e Pizza.
pizzas = ["Queso y pepperoni" , " Jamón y palmitos", "Hawaiana", 
"Pollo", "Napolitana", "Salmón ahumado y queso crema",
  "Pizza 4 quesos"]

def imprimir_menu():
	print("1 mostrar pizza ")
	print("2 mostrar pizza ")
	print("3 agregar pizza ")
	print("4 agregar pizza ")
	print("5 agregar pizza ")
	print("6 agregar pizza ")
	print("7 salir ")
	valor = input("ingrese el valor de la accion: ")
	return valor 

continuar = True 

while continuar:
	#v_retornado = Valor Retornado
	v_retornado = imprimir_menu()
	if int(v_retornado) == 1:
		for pizza in pizzas:
			print(pizza)
	elif int(v_retornado) == 2 :
		pizzas  = []
	elif int(v_retornado) == 3:
		valor = input("ingrese la pizza  a agregar")
		pizza.append (valor)
	elif int(v_retornado) == 4: 	
		pizzas  = []
	elif int(v_retornado) == 5:
		pizzas  = []
	elif int(v_retornado) == 6:
		pizzas  = []
	elif int(v_retornado) == 7: 	
		continuar = False
	else:
		print("opcion no controlada")



