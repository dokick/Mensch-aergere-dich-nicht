from turtle import exitonclick
from random import choice
from player import Player
from gamePiece import GamePiece
from gameBoard import game_board, draw_winner_on_board, HOME_ANGLES, COLORS, home_positions, goal_positions
from tools import dice

"""
Behaviour of players:

- First priority is it to get the furthest game piece into one of the final positions,
  no matter the risks or tactical advantages for other game pieces
- If the player rolls a 1, 2 or 3 with the dice the player will use that on game pieces
  that aren't all the way deep in the final positions,
  if there's no tactical disadvantage for other game pieces

Rules:

When can a player/game piece NOT move
- If the player has no game pieces on a playing field (Handled in make_a_move())
- If there are not enough fields that a game piece can move
- If the game piece would land on a field with a game piece of the same color

Implemented Features:

- Player hitting other players
- Rolling the dice three times if no moves available

Not Yet Implemented Features:

- When a player rolls a 6, but his game pieces can't move, a new game piece will come out
- Rolling a 6 leads to making a move again
- Deep check for when a player has won
"""

######################################## Start of game mechanics ########################################


def did_player_hit_other_players(*, game_piece_being_checked: GamePiece, players: list[Player]) -> GamePiece | None:
    """Helper function for the implementation of the game mechanic that players can hit other players

    Args:
        game_piece_being_checked (GamePiece): the game piece that made a move
        players (list[Player]): information of all players

    Returns:
        GamePiece | None: Returns the game piece that got hit by another player or None if no one got hit
    """
    for player in players:
        if player.color == game_piece_being_checked.color:
            continue
        for game_piece in player.game_pieces:
            if game_piece.get_pos() == game_piece_being_checked.get_pos():
                return game_piece
    return None


def permission() -> bool:
    """Gives a game piece the permission to leave home and get on field

    Returns:
        bool: true if the dice got a 6 in three throws
    """
    for i in range(3):
        if 6 == 6:  # ! First 6 should be dice()
            return True
    return False


def make_a_move(*, current_player: Player, players: list[Player]) -> None:
    """Simulates and also handles the move in the game

    If a player has no game pieces to play with, the player has to get a new game piece on the board
    Otherwise the move gets validated and then the player moves

    Args:
        current_player (Player): the player that has the current turn
        players (list[Player]): information of all players
    """
    if not has_player_at_least_one_game_piece_on_game_board(current_player) and permission():
        current_player.set_game_piece_to_start()

    current_game_piece = current_player.move(1)  # ! 6 should be dice()

    if current_game_piece:
        kicked_out_game_piece = did_player_hit_other_players(
            game_piece_being_checked=current_game_piece, players=players)
        if kicked_out_game_piece:
            kicked_out_game_piece.reset()


######################################## End of game mechanics ########################################

######################################## Start of helper functions ########################################


def has_player_at_least_one_game_piece_on_game_board(current_player: Player) -> bool:
    """Checks if a player has at least one of it's game pieces that's playable on the board playing

    Args:
        current_player (Player): the player that has the current turn

    Returns:
        bool: true if at least one playable game piece of the color is on the board
    """
    for game_piece in current_player.game_pieces:
        if game_piece.is_on_field() and not game_piece.is_done(current_player.occupied):
            return True
    return False


def has_one_player_won(players: list[Player]) -> Player | None:
    """Checks if a player has won yet

    Args:
        players (list[Player]): information of all players

    Returns:
        Player | None: the winning player or None if no one has won yet
    """
    for player in players:
        has_player_won = True
        for game_piece in player.game_pieces:
            if game_piece.get_pos() not in goal_positions[player.color]:
                has_player_won = False
                break
        if has_player_won:
            return player
    return None

######################################## End of helper functions ########################################

######################################## Start of setup & game loop ########################################


def draw_winner(player: Player):
    draw_winner_on_board(player.color)


def setup(amount_of_players=4) -> tuple[list[Player], Player]:
    # TODO: setup() abhängig von der Anzahl an Spielern machen die spielen
    """A setup function so the game can start with initial values

    Args:
        amount_of_players (int): the amount of players in the game (not implemented yet)

    Returns:
        tuple: first a tuple with all the players, second the player that starts the game
    """
    players: list[Player] = []
    for color in COLORS:
        players.append(Player(color=color, game_pieces=[
            GamePiece(color, home_positions[color][i], speed='normal') for i in range(4)]))

    for player, color in zip(players, COLORS):
        for game_piece in player.game_pieces:
            game_piece.turtle.seth(HOME_ANGLES[color])
            game_piece.turtle.goto(game_piece.home_position)

    starting_player = choice(players)

    return players, starting_player


def start_game_loop(amount_of_players=4):
    """Starts the game loop

    Loop works as follows:
    - move the current player (validation and handling happens in move or in subfunctions of move)
    - set the next player for the next iteration
    - check if someone has won yet

    Args:
        amount_of_players (int): the amount of players that are playing (not implemented yet)
    """
    players, current_player = setup(amount_of_players)
    index_of_current_player = players.index(current_player)
    won_player = None
    iterations = 0

    while not won_player:
        make_a_move(current_player=current_player, players=players)
        index_of_current_player += 1
        current_player = players[(index_of_current_player+1) % 4]
        won_player = has_one_player_won(players)
        iterations += 1
        print(iterations)
        if iterations == 100:
            break
    print(f"{won_player} has won the game")
    # draw_winner(won_player)

######################################## End of start & game loop ########################################


def main():
    game_board()
    start_game_loop()
    exitonclick()


if __name__ == "__main__":
    main()
