import random

class Ball:
    def __init__(self):
        print("Criando a bola")
        self.points_1 = 0
        self.points_2 = 0

    def simulate_movement(self):
        options = [
            "bola na raquete 1",
            "bola na raquete 2",
            "bola na parede",
            "bola saiu lado 1",
            "bola saiu lado 2"
        ]
        choice = random.choice(options)

        print(choice,"\n")

        if choice == "bola saiu lado 1":
            self.points_2 += 5
        elif choice == "bola saiu lado 2":
            self.points_1 += 5
