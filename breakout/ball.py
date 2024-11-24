import random

class Ball:
    def __init__(self):
        print("Criando a bola")
        self.points = False
        self.max_lifes = 3  # Número máximo de vidas
        self.current_lifes = self.max_lifes
        self.lifes = True

    def simulate_movement(self):
        options = [
            "bola subindo",
            "bola bateu na parede",
            "bola quebrou um bloco",
            "bola saiu da tela",
            "bola bateu na raquete"
        ]
        choice = random.choice(options)

        print(choice)

        if choice == "bola quebrou um bloco":
            self.points = True
        elif choice == "bola saiu da tela":
            self.current_lifes -= 1
            print(f"Vidas restantes: {self.current_lifes}")
            if self.current_lifes <= 0:
                self.lifes = False