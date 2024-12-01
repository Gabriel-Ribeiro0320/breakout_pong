from wall import Wall
from ball import Ball
from bricks import Bricks
from paddle import Paddle

class Game:
    def __init__(self):
        print("Iniciando o jogo...")
        self.wall = Wall()  # Criando as paredes
        self.bricks = Bricks()  # Criando os blocos
        self.paddle = Paddle()  # Criando a raquete
        self.ball = Ball()  # Criando a bola
        self.running = True

    def play(self):
        print("Jogo começando...")
        while self.running:
            self.ball.simulate_movement()
            print(f"Pontos: {self.ball.points}, Vidas: {self.ball.current_lifes} \n")

            # Simula a quebra de bloco
            if self.ball.last_action == "bola quebrou um bloco":
                self.bricks.break_brick()

            # Exibe a quantidade de blocos restantes
            print(f"Blocos restantes: {self.bricks.bricks_left}")


            # Verifica se todos os blocos foram quebrados
            if self.bricks.bricks_left == 0:
                print("Parabéns! Você venceu o jogo!")
                self.running = False

            if not self.ball.lifes:
                print("Fim de jogo!")
                self.running = False