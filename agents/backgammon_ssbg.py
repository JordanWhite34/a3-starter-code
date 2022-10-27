'''
Name(s): Colin Farmer, Jordan White
UW netid(s): cfarme, jwhite34
'''

from game_engine import genmoves 

class BackgammonPlayer:
    def __init__(self):
        self.GenMoveInstance = genmoves.GenMoves()
        self.max_depth = 4
        self.states_explored = 0
        self.cuttoffs = 0
        self.func = None
        self.prune = False
        # feel free to create more instance variables as needed.
    
    def initialize_move_gen_for_state(self, state, who, die1, die2):
        self.move_generator = self.GenMoveInstance.gen_moves(state, who, die1, die2)


    # For students in partnership: UWNETID + " " + UWNETID
    def nickname(self):
        return "cfarme + jwhite34"


    # If prune==True, then your Move method should use Alpha-Beta Pruning
    # otherwise Minimax
    # Only for updating static variabes in the class
    def useAlphaBetaPruning(self, prune=False):
        self.prune = prune
        self.states_explored = 0
        self.cuttoffs = 0
        # self.states_ex
        # if max depth is reached or there are no available moves left, return static eval
        

    def minimax(self, state, plyLeft, max_move):
        """"To add alpha beta, at each non-leaf level, perform a static evaluation of all
    # successors of a node and order them best-first before doing
    # the recursive calls. If the best move was first, the tendency
    # should be to get cutoffs when exploring the remaining ones."""
        self.states_explored = self.states_explored + 1
        if plyLeft == 0 or self.get_all_possible_moves == ['p']: return self.staticEval(state)
        self.initialize_move_gen_for_state(state, state.whose_move, 1, 6)
        if max_move:
            # refresh the move generator for the new state
            # for s in successors(board, whoseMove):
            # if self.get_all_possible_moves()[0] == 'p': return 'p'
            highest_score = -9999
            for move in self.get_all_possible_moves():
                if move == 'p': continue
                score = self.minimax(move[1], plyLeft-1, ~max_move)
                highest_score = max(score, highest_score)
            return highest_score
        else:
            lowest_score = 9999
            for move in self.get_all_possible_moves():
                if move == 'p': continue
                score = self.minimax(move[1], plyLeft-1, ~max_move)
                lowest_score = min(score, lowest_score)
            return lowest_score


    # big idea: look for paths that the score outcome will not be worth further exploration
    def alpha_beta(self, state, plyLeft, alpha, beta, max_move):
        """implements alpha beta cutoffs to reduce computation needed, removing paths that are not worth exploring"""
        self.states_explored = self.states_explored + 1
        if plyLeft == 0 or self.get_all_possible_moves == ['p']: return self.staticEval(state)
        self.initialize_move_gen_for_state(state, state.whose_move, 1, 6)
        if max_move:
            maxVal = beta
            # refresh the move generator for the new state
            # for s in successors(board, whoseMove):
            for move in self.get_all_possible_moves():
                if move == 'p': continue  
                if beta <= alpha: 
                    self.cuttoffs = self.cuttoffs + 1
                    continue
                # here is where the change from minimax happens
                # decide if we should make a call here, or stop the exploration of the node and its children
                newVal = self.alpha_beta(move[1], plyLeft-1, alpha, beta, ~max_move)
                maxVal = max(maxVal, newVal)
                alpha = max(alpha, maxVal)
            return maxVal
        else:
            minVal = alpha
            # if self.get_all_possible_moves()[0] == 'p': return 'p'
            for move in self.get_all_possible_moves():
                # decide if we should make a call here, or stop the exploration of the node and its children
                if beta <= alpha: 
                    self.cuttoffs = self.cuttoffs + 1
                    continue
                if move == 'p': continue  
                newVal = self.alpha_beta(move[1], plyLeft-1, alpha, beta, ~max_move)
                minVal = min(minVal, newVal)
                beta = min(beta, newVal)
            return minVal


    # Returns a tuple containing the number explored
    # states as well as the number of cutoffs.
    def statesAndCutoffsCounts(self):
        return(self.states_explored,self.cuttoffs)

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. maxply=2 indicates that
    # our search level will go two level deep.
    def setMaxPly(self, maxply=2):
        self.max_depth = maxply

    # If not None, it update the internal static evaluation
    # function to be func
    def useSpecialStaticEval(self, func):
        self.func = func
    

    def move(self, state, die1=1, die2=6):
        """given a state and a roll of dice, it returns the best move for the state.whose_move.
        A player can only pass id the player cannot move any checker with that role"""
        # Generate the moves for this state
        self.initialize_move_gen_for_state(state, state.whose_move, die1, die2)
        # initialize variables
        highest_score = -100000
        best_move = None
        move_list = self.get_all_possible_moves()
        best_move = move_list[0][0]
        # If there are no possible moves, pass
        if move_list[0] == 'p': return 'p'
        if self.max_depth == 0:
            return state
        # If We only need to look one move down, no reasons to use minimax and alpha-beta
        if self.max_depth == 1:
            for move in move_list:
                if move == 'p': continue  
                score = self.staticEval(move[1])
                if score > highest_score:
                    best_move = move[0]
                    highest_score = score
        
        # Take the state and info and pass it to the recursive search method
        # This will return the result of the best move based on the state and whose move it is
        else:
            # Look at all the possible next moves
            for move in move_list:
                # skip over pass moves
                if move == 'p': continue  
                # Use the search method go get the score
                # We are assuming that move is a state. If something breaks, look here.
                # Use alpha beta if prune is true
                if self.prune: score = self.alpha_beta(move[1], self.max_depth - 1, 99999, -99999, state.whose_move==0)
                # Else use minimax
                else: score = self.minimax(move[1], self.max_depth - 1, state.whose_move==0)
                # Get the highest score from those paths
                if score > highest_score:
                    best_move = move[0]
                    highest_score = score
        # return the best move for a given state and a given move
        return best_move

    # Hint: Look at game_engine/boardState.py for a board state properties you can use.
    def staticEval(self, state):
        """Takes the state and returns a score based on how well white is doing"""
        if self.func == None:
            red_score = 0
            white_score = 0 
            itr = 1
            # Look at the peices about to bear off
            for i in state.pointLists:
                if len(i) > 0:
                    if(i[0] == 0):
                        add = len(i)*(25-itr) / 2
                        if itr >= 1 and itr <= 6: 
                            add = add * 2
                        if itr == 1:
                            add = add * 2
                        red_score = red_score + add
                    elif(i[0] == 1):
                        add = len(i) * itr / 2
                        if itr >= 19 and itr <= 24: 
                            add = add * 2
                        if itr == 24:
                            add = add * 2
                        white_score = white_score + add
                itr = itr + 1
            # any off pieces
            white_score = white_score + len(state.white_off) * 15
            red_score = red_score + len(state.red_off) * 15
            if state.whose_move == 1:
                red_score = red_score * 1.5
            else:
                white_score = white_score * 1.5
            # looking at barred list
            for j in state.bar:
                if j == 0:
                    white_score = white_score - 25
                if j == 1:
                    red_score = red_score - 25
            return (white_score - red_score) * 1
        # Use custom static eval function
        else:
            return self.func(state)

 
    def get_all_possible_moves(self):
        """Uses the mover to generate all legal moves. Returns an array of move commands"""
        move_list = []
        done_finding_moves = False
        any_non_pass_moves = False
        while not done_finding_moves:
            try:
                m = next(self.move_generator)    # Gets a (move, state) pair.
                if m[0] != 'p':
                    any_non_pass_moves = True
                    move_list.append(m)    # Add the move to the list.
            except StopIteration as e:
                done_finding_moves = True
        if not any_non_pass_moves:
            move_list.append('p')
        return move_list
