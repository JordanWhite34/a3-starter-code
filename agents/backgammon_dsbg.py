'''
Name(s): Jordan White, Colin Farme
UW netid(s): JWHITE34, CFARME
'''

from game_engine import genmoves

class BackgammonPlayer:
    def __init__(self):
        self.GenMoveInstance = genmoves.GenMoves()
        # feel free to create more instance variables as needed.

    # TODO: return a string containing your UW NETID(s)
    # For students in partnership: UWNETID + " " + UWNETID
    def nickname(self):
        return "JWHITE34"+" "+"CFARME"

    # If prune==True, then your Move method should use Alpha-Beta Pruning
    # otherwise Minimax
    def useAlphaBetaPruning(self, prune=False):
        # TODO: use the prune flag to indiciate what search alg to use
        pass

    # Returns a tuple containing the number explored
    # states as well as the number of cutoffs.
    def statesAndCutoffsCounts(self):
        # TODO: return a tuple containig states and cutoff
        return (-1, -1)

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. maxply=2 indicates that
    # our search level will go two level deep.
    def setMaxPly(self, maxply=2):
        # TODO: set the max ply
        pass

    # If not None, it updates the internal static evaluation
    # function to be func
    def useSpecialStaticEval(self, func):
        if self is not None:
            staticEval(self, func)
        pass

    # Given a state and a roll of dice, it returns the best move for
    # the state.whose_move.
    # Keep in mind: a player can only pass if the player cannot move any checker with that role
    def move(self, state, die1=1, die2=6):
        # TODO: return a move for the current state and for the current player.
        # Hint: you can get the current player with state.whose_move
        best = -99999
        if self.whose_move == 'W':

        return "q"

    # checks legality of a move
    def legalMove(self, state, index, die):
        for i in range(die):
            if (self.pointLists[index+i+1][0] == 1 - self.pointLists[index][0]) and (self.pointLists[index+i+1][0].length >= 2):
                return False
        return True


    # Hint: Look at game_engine/boardState.py for a board state properties you can use.
    # Calculates pip counts for red and white and returns the difference, white being positive
    def staticEval(self, state):
        whitePip = 0;
        redPip = 0;
        itr = 1;
        for i in self.pointLists:
            if(i[0] == 0):
                whitePip = whitePip + (i.length)*(25-itr)
            elif (i[0] == 1):
                redPip = redPip+(i.length)*(itr)
            itr = itr + 1

        return whitePip - redPip

