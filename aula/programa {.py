programa {
 funcao inicio() {
    real nota1,nota2,nota3,nota4,media
    cadeia nome_da_diciplina
    escreva("digite o nome da diciplina : ")
    leia(nome_da_diciplina) 
    escreva("digite a primeira nota: ")
    leia(nota1)
    escreva("digite a segunda nota: ")
    leia(nota2)
    escreva("digite a terceira nota: ")
    leia(nota3)
    escreva("digite a quarta nota: ")
    leia(nota4)
    media=(nota1+nota2+nota3+nota4)/4 
    escreva("média da diciplina de: ", nome_da_diciplina,  " é ", media)
     se (media>=7){
     escreva(" vc esta aprovado! ")
     }
       senao{
       escreva(" vc esta reprovado! ")