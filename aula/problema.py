def main():
 numb_alunos=int(input("digite o numero do alunos"))
for i in range(num_alunos):   
     nome=int(input(f"digite o nome do aluno"){i+1})
     nome_da_diciplina=input("digite o nome da diciplina: ")
     nota1=float(input("digite a primeira nota:"){i+1})
     nota2=float(input("digite a segunda nota: "){i+1})
     nota3=float(input("digite a terceira nota"){i+1})
     nota4=float(input("digite a quarta nota:"){i+1})
     nota5=float(input("digite a quinta nota: "){i+1})
vetor = [nota1,nota2,nota3,nota4,nota5]
for i in range(len(vetor)):
          vetor[i] = vetor[i] /4
    
print()

