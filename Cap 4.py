# HELLO WORLD DE AMIGUES
# Se vocês tão continuando mais esse capítulo, então digo uma coisa viu coragem
#CAPITULO 4 - Tomadas de Decisões
#===================================================
# TÓPICO 1 - EXPRESSÕES LÓGICAS
# A gente já falou sobre expressões relacionais em booleanos, e sobre operadores comparativos e resultados.
# *** Para revisar ***
# OPERAÇÃO      RESULTADO        OPERAÇÃO      RESULTADO
#      3>1                    True                        6<1.0                  False
# "Teste"=="teste"      False                    3.14!=3                   True
#    5>= 5.0                 True                      "Z"<="a"                True

# Para primeiro exemplo no próximo passo vamos usar três nomes:
# Sherlock, Enola, e Mycroft

# OPERADOR "AND" ( Caso você faça engenharia elétrica acho que isso te lembra do véi)
# O operador "and" significa "e", e diz quando dois valores booleanos são verdadeiros.

#EXEMPLO 1: Imagine que Sherlock e Enola estão na aula de cálculo e tu é o prof
# Aí alguém pergunta, "Sherlock e Enola estão na aula?" Sua resposta seria sim, porque os dois estão na aula, MAS se Sherlock fosse no banheiro num momento e Mycroft tomasse o lugar dele, a resposta seria diferente
# Mas aí há a pergunta novamente, e a resposta é não, apenas Elona está, para que a resposta seja sim, os dois tem que estar na aula.
# E AÍ ENTRA A LÓGICA VISTA EM CIRCUITOS LÓGICOS
# Sherlock          Enola           S&E
# Sim                 Sim               Sim
# Sim                 Não               Não
# Não                 Sim               Não         NOSSA FAMOSA T.V(TABELA VERDADE)
# Não                Não                Não

# E é assim que o operador and funciona
Sherlock=False
Enola= True
Mycroft = True
Sherlock_e_Enola= Sherlock and Enola
print(Sherlock_e_Enola) # False
# Retorna False ja que requer que as duas condições seja True


# OPERADOR "OR"
# Or já diz tudo né, OU
# Vamos ser breve e fazer a T.V para ser mais prático
# Sherlock          Enola           S&E
# Sim                 Sim               Sim
# Sim                 Não               Sim
# Não                 Sim               Sim         
# Não                Não                Não

#Aplicando no python
# EXEMPLO 2:
Sherlock_e_Mycroft= Sherlock or Mycroft
print(Sherlock_e_Mycroft) # Vai imprimir True
# Or depende apenas que uma das condições sejam verdade


# OPERADOR "NOT"
# Se tivessemos a pergunta " É verdade que sherlock NÃO está na aula? A resposta é não, pois ele ta na aula
# Ou seja o uso do não faz com que a gente inverta a resposta
# SE LIGA NA T.V
# Sherlock         Não Sherlock
#  Sim                     Não
#  Não                     Sim

# EXEMPLO 3:
Sherlock1 = True
nao_Sherlock= not Sherlock1
# Esse operador só precisa de uma proposição
print(nao_Sherlock) # False

# Cansa né, imagina quem faz o cálculo na mão(Oh matéria chata)
# COMBINANDO OPERADORES LÓGICOS
# Assim como na matemática, dá pra usar vários operadores juntos
# Com o uso do parênteses você pode indentificar qual condição vai  ser verificada primeiro
# Segue o fio
#EXEMPLO 4:
# Sherlock           Enola           Mycroft              not((Mycroft and Enola) or Sherlock)
#  F                      F                    F                                        T
#  F                      F                   T                                        T
#  F                      T                    F                                       T
#  F                      T                    T                                        F
#  T                       F                   F                                       F
#  T                       F                   T                                      F
#  T                        T                  F                                     F
#  T                       T                 T                                      F

Sherlock2= False
Enola1 = True
Mycroft1 = True
exp = not((Mycroft1 and Enola1) or Sherlock2)
print(exp) # False

#---------------------------------------------------------------------------------------------------------------------
# TÓPICO 2 - ESTRUTURAS CONDICIONAIS
# Se tu já estudou C ou C++, já deve ter uma noção sobre o que a gente vai falar nesse tópico

# Então vamos começar com a queridinha
 # IF         que ficaria mais ou menos asism
 # if condição:
      #código a ser executado
      # caso a condição seja verdadeira

#EXEMPLO 4:
if 1==1:
       print("1 é realmente 1") # Satisfez a condição
       # Espeçamento necessário para o printar o if ( SIM, espaçamento importa >:( )
if 5==4:
       print("4 não é 5") # AQUI não vai acontecer nada porque 5 não é igual a 4
# Oia mais um exemplo
idade=int(input("Idade: \n"))
if idade < 18:
       print(" Você é menor de idade!")  # Se for maior ou igual a 18, apenas vai ser mostrado sua idade e não a condição já que não favorece
print(" Sua idade é "+str(idade))

# Agora tu vai ver o circo pegar fogo meu pcr
# Bora inserir o else para caso não favoreça o if, tenha outro caso
#EXEMPLO 5:
idade1=int(input("Sua idade novamente: \n"))
if idade1 <18:
        print(" Você é menor de idade!")
else:
    if idade1==18:
       print (" Quase ein!")
    else:
           print("Maior de idade!")
print("Sua idade é: "+str(idade1))
       
#Chato né, muita coisa, MAS sempre existe alguem que facilita isso pra gente
# E se chama estrutura if/elif/else
# Chegue ver
#EXEMPLO 6:

idade2 = int(input(" Mais uma vez( a ultima): \n"))
if idade2 <18:
       print(" Você é menor de idade!")
elif idade2==18:
       print("Quase boy")
else:
       print(" É de maior!")
print("Sua idade de novo é "+str(idade2))

# Olha amigue, todas as estruturas de comparação tem que começar com um if, e só podem ter um else, mas podem ter vários elif, okay?
# E as comparação são feitas em ordem,uma de cada vez,e o if para quando uma das condições é verdadeira.
# Somente um bloco do código vai ser executado na sua estrutura
# Por exemplo se no código anterior a gente tivesse outro elif sendo
# elif idade ==19:
        # print("Recém maior de idade")
# No primeiro elif a gente ja sabe que a idade não e menor que 18, porque caso contrário teria parado no primeiro if, e no segundo a idade não é igual a 18, porque se não teria parado no primeiro e BLA BLA BLA ETC


































