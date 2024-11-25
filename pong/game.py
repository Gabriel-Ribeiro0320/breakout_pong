from paddle import Paddle
from ball import Ball
from wall import Wall

class Game:
    def __init__(self):
        print("Iniciando o jogo Pong... \n")
        self.wall = Wall()
        self.paddle_1 = Paddle()
        self.paddle_2 = Paddle()
        self.ball = Ball()
        self.running = True

    def play(self):
        print("Jogo Pong começando...\n")
        while self.running:
            self.ball.simulate_movement()

            print(f"Pontos Jogador 1: {self.ball.points_1},\n Pontos Jogador 2: {self.ball.points_2}\n")

            if self.ball.points_1 >= 20:
                print("Jogador 1 venceu o jogo!")
                self.running = False
            elif self.ball.points_2 >= 20:
                print("Jogador 2 venceu o jogo!")
                self.running = False
