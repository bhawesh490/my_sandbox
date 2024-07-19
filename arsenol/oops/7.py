import random 

class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value
    
my_die = Die()
# print(my_die.value)
x=my_die.roll()
# print(my_die.value)
print (x)


class Player:
    
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1 

    def decrement_counter(self):
        self._counter -= 1    

    def roll_die(self):
        return self._die.roll()
    
    # testing the player class
my_die=Die()
my_player=Player(my_die,True)
print(type(my_player))
print(my_player.is_computer)
print(my_player.counter)
print(my_player.decrement_counter())
print(my_player.counter)
print("---------------------------------------")
print(my_player.die.value)
print(my_player.roll_die())
# print(my_player.die.value)


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer 

    def play(self):
        self.welcome_player()
        while True:
            self.play_round()
            #TODO: implement game over
            game_over = self.check_game_over()
            if game_over:
                break


    def play_round(self):
        print("-----New Round------")
        input("Press any key to roll the die")
        
        # roll the die
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # show the values
        self.show_dice(player_value, computer_value)
        
        # Determine winner and loser
        if player_value > computer_value:
            print("You won the round")
            self.update_counter(winner=self._player, loser=self._computer)

        elif computer_value > player_value:
            print("The Computer won this round Try again")
            self.update_counter(winner=self._computer, loser=self._player)

        else:
            print("Its a tie")
        # show the counters    

        self.show_counter()

    def welcome_player(self):
        print("====================================")
        print("Welcome to the roll the dice!")
        print("====================================")

    def show_dice(self,player_value, computer_value):
        # this is a static method as it does not references any self in the body
        print(f"Your die :{player_value}")
        print(f"Computer die :{computer_value}") 

    def update_counter(self, winner, loser):
        # this is a static method as it does not references any self in the body
        winner.decrement_counter()
        loser.increment_counter()

    def show_counter(self):
        print(f"Your counter : {self._player.counter}")
        print(f"Computer counter :{self._computer.counter}")
    

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False
        
    
    
    def show_game_over(self,winner):
        if winner.is_computer:
            print("\n=============================")
            print(" G A M E     O V E R")
            print("===============================")
            print("The computer won the game.Sorry")
            print("===============================")
        else:
            print("\n=============================")
            print(" G A M E     O V E R")
            print("===============================")
            print("You won the game.Congratulations!")
            print("===============================")



# create instances
player_die = Die()
computer_die = Die()

my_player = Player(player_die,is_computer=False)
computer_player = Player(computer_die,is_computer=True)
game = DiceGame(my_player,computer_player)

game.play()
        


        







