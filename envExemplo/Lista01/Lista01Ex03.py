"""
Construir um programa que leia as 2 notas de um aluno e que calcule,
armazene e imprima a média. Se a média for maior ou igual a 7, imprimir
“Aprovado”, caso contrário, realizar a leitura de uma terceira nota,
que terá peso 2 e calcular, armazenar e imprimir uma nova média.
Se a nova média for maior ou igual a 6, imprimir “Aprovado”, caso contrário,
imprimir “Reprovado”.
"""
nota1= int(input('digite sua primeira nota:'))
nota2= int(input('digite sua segunda nota:'))
media= (nota1 + nota2)/2
if media >= 7:
    print('aprovado')
elif media < 7:
    nota3= int(input('digite sua terceira nota:'))
    media= (nota1 + nota2 + nota3 * 2) / 4
    if media >= 6:
        print('aprovado')
    else:
        print('reprovado')
