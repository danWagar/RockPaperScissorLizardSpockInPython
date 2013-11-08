"""
Implementation of the game rock, paper, scissor, lizard, spock.

Created on Mar 11, 2013
@author: Dan Wagar
"""
moves = []      
"""List containing the games 5 possible actions."""
lastMove = ''
"""The move made by an opponent in the previous round."""

class Element(object):
    """Provide interface for the games 5 possible actions.
    
    Attributes:
    _name -- The string literal which names an element
    
    Methods:
    __init__(),
    name(),
    compareTo()
    """
    _name = ' '
   
    def __init__(self, name):
        """Construct the Element object.
        
        Arguments:
        name -- The string literal which describes an element
        """
        self._name = name
       
    def name(self):
        """Return the string literal naming an element"""
        return self._name  
    
    def compareTo(self, element):
        """Compare two Element objects. To be overridden by subclasses.
        
        Arguments:
        element -- An Element object
        
        Exceptions Raised:
        NotImplementedError
        """
        raise NotImplementedError("Not yet implemented")
        
class Rock(Element):
    """Inherit behavior from Element. Override compareTo method.
    
    Methods:
    compareTo()
    """
    def compareTo(self, element):
        """Compare two Element objects to determine a rounds outcome.
        
        Arguments:
        element -- The Element object representing the move made by player one
        
        Returns:
        A string literal describing the comparison of the two Element objects,
        A string literal describing the outcome of the comparison from the perspective of player one.
        """
        
        if element == moves[0]:
            return "Rock equals Rock", "Tie"
        elif element == moves[1]:
            return "Paper covers Rock", "Lose"
        elif element == moves[2]:
            return "Rock crushes Scissor", "Win"
        elif element == moves[3]:
            return "Rock crushes Lizard", "Win"
        elif element == moves[4]:
            return "Spock vaporizes Rock", "Lose"

class Paper(Element):
    """Inherit behavior from Element. Override compareTo method.
    
    Methods:
    compareTo()
    """
    def compareTo(self, element):
        """Compare two Element objects to determine a rounds outcome.
        
        Arguments:
        element -- The Element object representing the move made by player one
        
        Returns:
        A string literal describing the comparison of the two Element objects,
        A string literal describing the outcome of the comparison from the perspective of player one.
        """
        if element == moves[0]:
            return "Paper covers Rock", "Win"
        elif element == moves[1]:
            return "Paper equals Paper", "Tie"
        elif element == moves[2]:
            return "Scissors cut Paper", "Lose"
        elif element == moves[3]:
            return "Lizard eats Paper", "Lose"
        elif element == moves[4]:
            return "Paper disproves Spock", "Win"

class Scissor(Element):
    """Inherit behavior from Element. Override compareTo method.
    
    Methods:
    compareTo()
    """
    def compareTo(self, element):
        """Compare two Element objects to determine a rounds outcome.
        
        Arguments:
        element -- The Element object representing the move made by player one
        
        Returns:
        A string literal describing the comparison of the two Element objects,
        A string literal describing the outcome of the comparison from the perspective of player one.
        """
        if element == moves[0]:
            return "Rock crushes Scissors", "Lose"
        elif element == moves[1]:
            return "Scissors cut Paper", "Win"
        elif element == moves[2]:
            return "Scissors equals Scissors", "Tie"
        elif element == moves[3]:
            return "Scissors decapitate Lizard", "Win"
        elif element == moves[4]:
            return "Spock smashes Scissors", "Lose"
       
class Lizard(Element):
    """Inherit behavior from Element. Override compareTo method.
    
    Methods:
    compareTo()
    """
    def compareTo(self, element):
        """Compare two Element objects to determine a rounds outcome.
        
        Arguments:
        element -- The Element object representing the move made by player one
        
        Returns:
        A string literal describing the comparison of the two Element objects,
        A string literal describing the outcome of the comparison from the perspective of player one.
        """
        if element == moves[0]:
            return "Rock crushes Lizard", "Lose"
        elif element == moves[1]:
            return "Lizard eats Paper", "Win"
        elif element == moves[2]:
            return "Scissors decapitate Lizard", "Lose"
        elif element == moves[3]:
            return "Lizard equals Lizard", "Tie"
        elif element == moves[4]:
            return "Lizard poisons Spock", "Win"
       
class Spock(Element):
    """Inherit behavior from Element. Override compareTo method.
    
    Methods:
    compareTo()
    """
    def compareTo(self, element):
        """Compare two Element objects to determine a rounds outcome.
        
        Arguments:
        element -- The Element object representing the move made by player one
        
        Returns:
        A string literal describing the comparison of the two Element objects,
        A string literal describing the outcome of the comparison from the perspective of player one.
        """
        if element == moves[0]:
            return "Spock vaporizes Rock", "Win"
        elif element == moves[1]:
            return "Paper disproves Spock", "Lose"
        elif element == moves[2]:
            return "Spock smashes Scissors", "Win"
        elif element == moves[3]:
            return "Lizard poisons Spock", "Lose"
        elif element == moves[4]:
            return "Spock equals Spock", "Tie"
       
class Player(object):
    """Provide an interface for human and AI opponents.
    
    Attributes:
    _name -- A string literal describing the type of player
    
    Methods:
    __init__(),
    name(),
    play()
    """
    _name = ''

    def __init__(self, name):
        """Construct the Player object.
        
        Arguments:
        name -- The string literal which describes a player
        """
        self._name = name
        
    def name(self):
        """Return the string literal naming a player"""
        return self._name 
    
    def play(self):
        """Determine a players action. To be overridden by subclasses.
        
        Exceptions Raised:
        NotImplementedError
        """
        raise NotImplementedError("Not yet implemented")
    
class StupidBot(Player):
    """Inherit behavior from Player. Override play method.
    
    Methods:
    play()
    """
    def play(self):
        """Make the same move every time.
        
        Return:
        moves[1] -- An instance of the class Paper
        """
        return moves[1]
    
class RandomBot(Player):
    """Inherit behavior from Player. Override play method.
    
    Methods:
    play()
    """
    def play(self):
        """Chose a move to make at random.
        
        Return:
        moves[rand] -- A random instance from the Element sub-classes
        """
        from random import randint
        rand = randint(0,4) 
        return moves[rand]
    
class IterativeBot(Player):
    """Inherit behavior from Player. Override play method.
    
    Attributes:
    itr -- A counter for iteratively moving through the global moves list
    
    Methods:
    play()
    """
    itr = -1
    def play(self):
        """Make a move by iteratively selecting Element sub-classes from the moves list
        
        Return:
        moves[self.itr] -- The current iteration from the moves list
        """
        if self.itr == 4:
            self.itr = 0
        else:
            self.itr+=1
        return moves[self.itr]
    
class LastPlayBot(Player):
    """Inherit behavior from Player. Override play method.
   
    Methods:
    play()
    """
    def play(self):
        """Make the same move as the move made by the opponent in the previous round.
        
        Returns:
        moves[1] -- if this is the first round, play the move Paper,
        lastMove -- the last move made by the opponent in the previous round
        """
        if lastMove == '':
            return moves[1]
        else:
            return lastMove

class Human(Player):
    """Inherit behavior from Player. Override play method.
    
    Methods:
    play()
    """
    def play(self):
        """Make a move as determined by user input.
        
        Returns:
        moves[inpt] -- The move corresponding to the input of the user
        """
        print("(1) : Rock") 
        print("(2) : Paper") 
        print("(3) : Scissor")
        print("(4) : Lizard")
        print("(5) : Spock")
        correct = False
        while correct == False:
            inpt = int(raw_input("Enter your move: ")) - 1
            if inpt in range(len(moves)):
                correct = True
                return moves[inpt]
            else:
                print("Invalid move. Please try again")
                
class MyBot(Player):
    """Inherit behavior from Player. Override play method.
    
    Methods:
    play()
    """
    def play(self):
        """Make the move that beats the move made by opponent in last round
        
        Returns:
        A move that beats the move made by the opponent in the last round
        """
        if lastMove == '':
            return moves[0]
        elif lastMove == moves[0]:
            return moves[1]
        elif lastMove == moves[1]:
            return moves[2]
        elif lastMove == moves[2]:
            return moves[0]
        elif lastMove == moves[3]:
            return moves[4]
        elif lastMove == moves[4]:
            return moves[3]
        
        
          
class Main():
    """Simulate a 5 round game of Rock, Paper, Scissor, Lizard, Spock
    
    Methods:
    __init__()
    """    
    def __init__(self):
        """Receive user input for player types and simulate a 5 round game.
        
        Populate the global moves list with the 5 element types
        and the local players list with the different AI bots
        and the human player.  Receive user input for player types
        and then simulate the 5 round game, printing the outcome of 
        each round and keeping score for each player.  If one of the
        players is the LastMove bot, assign the move of the opponent
        in the last round to the global variable lastMove. Print the 
        outcome of the game after the 5 rounds are complete.
        """

        rock = Rock("Rock")
        paper = Paper("Paper")
        scissor = Scissor("Scissor")
        lizard = Lizard("Lizard")
        spock = Spock("Spock")
        global moves
        moves = [rock, paper, scissor, lizard, spock]
        
        human = Human("Human")
        stupidBot = StupidBot("StupidBot")
        randomBot = RandomBot("RandomBot")
        iterativeBot = IterativeBot("IterativeBot")
        lastPlayBot = LastPlayBot("LastPlayBot")
        myBot = MyBot("MyBot")
        players = [human, stupidBot, randomBot, iterativeBot, lastPlayBot, myBot]
        
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock, implemented by Daniel Wagar.")
        print("Please choose two players:")
        print("(1) Human")
        print("(2) StupidBot")
        print("(3) RandomBot")
        print("(4) IterativeBot")
        print("(5) LastPlayBot")
        print("(6) MyBot")
        correct1 = False
        correct2 = False
        while correct1 == False:
            inpt1 = int(raw_input("Select Player 1: ")) - 1
            if inpt1 >= 1 and inpt1 <= 6:
                p1 = players[inpt1]
                correct1 = True
            else:
                print("Invalid move. Please try again")
        while correct2 == False:
            inpt2 = int(raw_input("Select Player 2: ")) - 1
            if inpt2 >= 1 and inpt2 <= 6:
                p2 = players[inpt2]
                correct2 = True
            else:
                print("Invalid move. Please try again")
        
        print('')
        print(p1.name() + " vs " + p2.name() + ". Go!")
        p1score = 0
        p2score = 0
        for i in range(1, 6):
            print("Round " + str(i) + ":")
            p1move = p1.play()
            p2move = p2.play()
            print("Player 1 chose " + p1move.name())
            print("Player 2 chose " + p2move.name())
            r1, r2 = p1move.compareTo(p2move)
            print(r1)
            if r2 == "Win":
                print("Player 1 won the round")
                p1score += 1
            elif r2 == "Lose":
                print("Player 2 won the round")
                p2score += 1
            elif r2 == "Tie":
                print("Round was a tie")
            
            global lastMove
            if p1.name() == "LastPlayBot" or p1.name() == "MyBot":
                lastMove = p2move
            if p2.name() == "LastPlayBot" or p2.name() == "MyBot":
                lastMove = p1move    
            print('')
                
        print("The score is " + str(p1score) + " to " + str(p2score) + ".")
        if p1score > p2score:
            print("Player 1 wins the game.")
        elif p1score < p2score:
            print("Player 2 wins the game.")
        else:
            print("Game was a draw.")
        
Main() 