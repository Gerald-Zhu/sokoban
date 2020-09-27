# sokoban
Each level represents a warehouse, where boxes are placed. A warehouse keeper has to push the boxes around the
warehouse so that all boxes are on goals at the end of the game. The warehouse is a two dimensional grid of squares.

If a square contains nothing it is called a floor, otherwise it is occupied by one of the following entities:
- Wall : Walls make up the basic outline of each level. They cannot be moved and nothing else can be on a
square occupied by a wall. A legal level is always surrounded by walls.

- Box : A box can either occupy a goal or an otherwise empty square. At the start of the game a box may
already occupy a goal. They can be moved in the four cardinal directions by pushing.

- Goal : Goals are treated like floors for the most part. Only when each goal is occupied by a box the game is
completed. In a legal level the number of goals matches the number of boxes. For the sake of simplicity, we
will call a square that is either a goal or a floor square free since the player and boxes can enter both. At the
start of the game a goal cannot be occupied.

- Player : The player can execute moves to alter his position. A move can be up, down, left or right. A move
is also a push if it alters the position of a box.

The player cannot move through walls or boxes. It can only move onto a square occupied by a box if it can
execute a push to move it out of the way. Therefore a player cannot push more than one box at a time, nor
can he pull them.

Here is the start state of level 1 as seen
above.

'  ##### '
'###   # '
'#.&B  # '
'### B.# '
'#.##B # '
'# # . ##'
'#B XBB.#'
'#   .  #'
'########'


The characters define the following entities:
- ‘#’ : Wall
- ‘B’ : Box ( ‘X’ : Box on goal)
- ‘.’ : Goal
- ‘&’ : Player ( ‘%’ : Player on goal)
- ‘ ’ : free square

The goal of the game is to find a solution. A solution is a sequence of moves that leads to every box being on a goal.
It does not matter which box ends up on which goal. Note that in our version of this game all solutions are equally
good, i.e., we don’t score by the number of moves the player makes or number of box moves that are made. You
may assume that every level we provide to you is legal and has a solution.

We are going to define a particular sequence of actions as a string, i.e., a list of letters for the four directions: u , d , l ,
r . They are capitalized if the move was a push. For example, the solution above has the following sequence of
actions:

RurrddddlDRuuuuLLLrdRDrddlLdllUUdR
