import logic
if __name__ == '__main__':
	mat = logic.incepe_jocul()
	while(True):
			x= input("Apasa comanda:")
			if(x == 'W' or x == 'w'):
				mat, flag = logic.mrg_sus(mat)
				status = logic.status_joc(mat)
				print(status)
				if(status == 'Jocul nu este gata'):
					logic.adauga_nou_2(mat)
				else:
					break
			elif(x == 'S' or x == 's'):
				mat, flag = logic.mrg_jos(mat)
				status = logic.status_joc(mat)
				print(status)
				if(status == 'Jocul nu este gata'):
					logic.adauga_nou_2(mat)
				else:
					break
			elif(x == 'A' or x == 'a'):
				mat, flag = logic.mrg_jos(mat)
				status = logic.status_joc(mat)
				print(status)
				if(status == 'Jocul nu este gata'):
					logic.adauga_nou_2(mat)
				else:
					break
			elif(x == 'D' or x == ''):
				mat, flag = logic.mrg_jos(mat)
				status = logic.status_joc(mat)
				print(status)
				if(status == 'Jocul nu este gata'):
					logic.adauga_nou_2(mat)
				else:
					break
			else:
				print("Tasta este invalida")
			print(mat)
