import turtle
# Bola em movimento
def moving_object(move):
    # para preencher a cor na bola
    move.fillcolor('orange')

    # iniciar o preenchimento de cor
    move.begin_fill()

    # desenhar o circulo
    move.circle(20)

    # preenchimento de cor final
    move.end_fill()


# Código para movimento
if __name__ == "__main__":

    # criar um objeto de tela
    screen = turtle.Screen()

    # definir o tamanho da tela
    screen.setup(600, 600)

    # cor de fundo da tela
    screen.bgcolor('purple')

    # atualização de tela
    screen.tracer(0)

    # criar um objeto de objeto turtle
    move = turtle.Turtle()

    # definir uma cor de objeto turtle
    move.color('blue')

    # definir velocidade do objeto turtle
    move.speed(0)

    # definir a largura do objeto turtle
    move.width(2)

    # tornar o objeto turtle invisível
    move.hideturtle()

    # objeto turtle no ar
    move.penup()

    # definir posição inicial
    move.goto(-250, 0)

    # mover o objeto turtle para a superfície
    move.pendown()

    # loop infinito
    while True:
        # limpar o trabalho da turtle
        move.clear()

        # chamar função para desenhar a bola
        moving_object(move)

        # atualização de tela
        screen.update()

        # movimento para frente pelo objeto turtle
        move.forward(0.05)