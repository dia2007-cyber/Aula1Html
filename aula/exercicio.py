num_alunos=int(input("digite o numero de alunos : "))
num_materias= 5
nomes_materias= ["portugues ","matematica","ciencias","quimica"]
nome=[]
notas=[]
for i in range(num_alunos):
    nomes= input(f"digite o nome do aluno {i+1}: ")
    nome.append(nome)
aluno_notas=[]
nota=float(input(f"digite a nota do aluno {nomes} na materia de {nomes_materias}: "))
for j in range(num_materias):   
      aluno_notas.append(nota) 
      notas.append(aluno_notas)

medias=[sum(aluno_notas) /  num_materias for aluno_notas in notas]
for i in range (num_alunos):
    print(f"aluno : {nomes [i]}")
    for j in range(num_materias):
        print(f"nota na materia de {nomes_materias[j]}: {notas[i][j]}")
        print(f"media: {medias[i]: .2f}")
        print()

arquivo = open("notas_alunos.txt", "w")
for i in range(num_alunos):
    arquivo.write(f"Aluno: {nomes[i]}\n")
    for j in range(num_materias):
        arquivo.write(f"Nota na matéria de {nomes_materias[j]}: {notas[i][j]}\n")
    arquivo.write(f"Média: {medias[i]:.2f}\n\n")
arquivo.close()

print("Conteúdo salvo com sucesso!")