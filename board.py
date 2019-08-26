from player import Player
class Board:

    def __init__(self):
        self.players = []
        self.game_state = "in_session"
        self.ladders = [[6,22], [15, 38], [26, 55], [59, 87]]
        self.snakes = [[90, 50], [45, 7], [73, 20], [35, 12]]
        self.winner = None

    

    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def check_ladder(self,player):
        for ladder in self.ladders:
            if player.position == ladder[0]:
                print(f"{player.name} landed on a ladder")
                player.position = ladder[1]
                print(f"{player.name} position after climbing the ladder is {player.position}")

    def check_snakes(self, player):
        for snake in self.snakes:
            if player.position == snake[0]:
                print(f"{player.name} landed on a snake")
                player.position = snake[1]
                print(f"{player.name} position after being swallowed by a snake is {player.position}")


    def play(self):
        while self.game_state == "in_session":
            for player in self.players:
                player.move_position()
                self.check_ladder(player)
                self.check_snakes(player)
                if player.position >= 100:
                    self.winner = player.name
                    self.game_state = "Game over"
                    print(f"The winner is {player.name}")
                    break
            

