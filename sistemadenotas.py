from colorama import Fore , init , Style
init()

Linha= ('-') * 50
print(Linha)
NM= input('Entre com o nome do estudante: ')
M1= float(input('Entre com a 1º nota do estudante:'))
M2= float(input('Entre com a 2º nota do estudante:'))
FREQ= float(input('Entre com a frequência do estudante (%):'))

MS= (M1+2*M2)/3

print(Linha)
print(f'Aluno= {NM}')
print(f'Média= {MS:.2f}')
print(f'Frequência= {FREQ:.2f}%')
print(Linha)
if FREQ < 75:
    print(f"{NM} {MS:.2f} {FREQ:.2f} {Fore.RED}  REPROVADO POR FREQUÊNCIA {Style.RESET_ALL}")
else:
    if MS>=5:
        print(f"{NM} {MS:.2f} {FREQ:.2f} {Fore.GREEN} APROVADO {Style.RESET_ALL}")
    else:
        if MS>=3 and MS<5:
            print(f"{NM} {MS:.2f} {FREQ:.2f} {Fore.YELLOW} RECUPERAÇÃO {Style.RESET_ALL}")
        else:
            print(f"{NM} {MS:.2f} {FREQ:.2f} {Fore.GREEN} REPROVADO POR NOTA {Style.RESET_ALL}")

print(Linha)

print('Fim do Programa')          

     