'''
Name(s): Colin Farmer, Jordan White
UW netid(s): cfarme, jwhite34
'''

from shutil import move
from game_engine import genmoves

class BackgammonPlayer:
    def __init__(self):
        self.GenMoveInstance = genmoves.GenMoves()
        self.max_depth = 2
        self.states_explored = 0
        self.cuttoffs = 0
        # feel free to create more instance variables as needed.

    def initialize_move_gen_for_state(self, state, who, die1, die2):
        self.move_generator = self.GenMoveInstance.gen_moves(state, who, die1, die2)


    # TODO: return a string containing your UW NETID(s)
    # For students in partnership: UWNETID + " " + UWNETID
    def nickname(self):
        # TODO: return a string representation of your UW netid(s)
        return "cfarme + jwhite34"

    # If prune==True, then your Move method should use Alpha-Beta Pruning
    # otherwise Minimax
    def useAlphaBetaPruning(self, prune=False):
        # TODO: use the prune flag to indiciate what search alg to use
        if prune:
            # Run Alpha Beta
            self.move()
        else:
            # Run Minimax
            self.move()


    # Returns a tuple containing the number explored
    # states as well as the number of cutoffs.
    def statesAndCutoffsCounts(self):
        # TODO: return a tuple containig states and cutoff
        return(self.states_explored,self.cuttoffs)

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. maxply=2 indicates that
    # our search level will go two level deep.
    def setMaxPly(self, maxply=2):
        self.max_depth = maxply

    # If not None, it update the internal static evaluation
    # function to be func
    def useSpecialStaticEval(self, func):
        # TODO: update your staticEval function appropriately
        if func != None:
            def staticEval(self,state): func


    # checks legality of a move
    def legalMove(self, state, index, die):
        for i in range(die):
            if (self.pointLists[index+i+1][0] == 1 - self.pointLists[index][0]) and (self.pointLists[index+i+1][0].length >= 2):
                return False
        return True

    # Given a state and a roll of dice, it returns the best move for
    # the state.whose_move.
    # Keep in mind: a player can only pass if the player cannot move any checker with that role
def move(self, state, die1=1, die2=6):
        # TODO: return a move for the current state and for the current player.
        # Hint: you can get the current player with state.whose_move
        highest_score = -100000
        best_move = None
        move_list = self.get_all_possible_moves()
        for move in move_list:
            score = self.staticEval(move) # We are assuming that move is a state. If something breaks, look here.
            if score > highest_score:
                best_move = move
                highest_score = score
        # return the best move for a given state
        return best_move

    # Hint: Look at game_engine/boardState.py for a board state properties you can use.
    def staticEval(self, state):
        # TODO: return a number for the given state
        white_pip = 0
        red_pip = 0
        itr = 1
        for i in self.pointList:
            if(i[0] == 0):
                white_pip = white_pip + len(i)*(25-itr)
            elif(i[0] == 1):
                red_pip = red_pip + len(i) * itr
        # any blocked pieces
        if state.whose_move == 0: return red_pip - white_pip
        else: return white_pip-red_pip

    def get_all_possible_moves(self):
        """Uses the mover to generate all legal moves. Returns an array of move commands"""
        move_list = []
        done_finding_moves = False
        any_non_pass_moves = False
        while not done_finding_moves:
            try:
                m = next(self.move_generator)    # Gets a (move, state) pair.
                # print("next returns: ",m[0]) # Prints out the move.    For debugging.
                if m[0] != 'p':
                    any_non_pass_moves = True
                    move_list.append(m[0])    # Add the move to the list.
            except StopIteration as e:
                done_finding_moves = True
        if not any_non_pass_moves:
            move_list.append('p')
        return move_list
