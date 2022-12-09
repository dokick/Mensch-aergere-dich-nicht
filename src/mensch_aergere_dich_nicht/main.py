"""
Behaviour of players:

- First priority is it to get the furthest game piece into one of the final
  positions, no matter the risks or tactical advantages for other game pieces
- If the player rolls a 1, 2 or 3 with the dice the player will use that on
  game pieces that aren't all the way deep in the final positions,
  if there's no tactical disadvantage for other game pieces

Rules:

When can a player/game piece NOT move
- If player has no game pieces on a playing field (Handled in make_a_move())
- If there are not enough fields that a game piece can move
- If game piece would land on a field with a game piece of the same color

Implemented Features:

- Player hitting other players
- Rolling the dice three times if no moves available

Not Yet Implemented Features:

- When a player rolls a 6, but his game pieces can't move,
  a new game piece will come out
- Rolling a 6 leads to making a move again
- Deep check for when a player has won
- Less than 4 players and user playing with them

TODO:
- Spielfiguren können das Ziel überspringen
- Spielfiguren derselben Farbe übereinander im Ziel
- Wenn eine Spielfigur durch rauskommen eine andere Farbe rausschmeißen müsste,
  passiert es nicht (TODO changes implemented, needs to be tested)
- Priorität, dass bei geringer Würfelzahl die Spielfiguren im Ziel
  benutzt werden, funktioniert nicht
"""

from random import choice
from turtle import exitonclick  # pylint: disable=no-name-in-module
from typing import Optional, Union

from mensch_aergere_dich_nicht.game_board import (COLORS, HOME_ANGLES,
                                                  draw_winner_on_board,
                                                  game_board, goal_positions,
                                                  home_positions)
from mensch_aergere_dich_nicht.game_piece import GamePiece
from mensch_aergere_dich_nicht.player import Player
from mensch_aergere_dich_nicht.tools import dice

############################## Start of game mechanics ##############################


def did_player_hit_other_players(*, game_piece_being_checked: GamePiece,
                                 players: list[Player]) -> None:
    """Helper function for the game mechanic that players can hit other players

    If other player got hit, game piece gets reset

    Args:
        game_piece_being_checked (GamePiece): game piece that made a move
        players (list[Player]): information of all players
    """
    if not game_piece_being_checked:
        return

    current_pos = game_piece_being_checked.get_pos()
    for player in players:
        if player.color == game_piece_being_checked.color:
            continue
        for game_piece in player.game_pieces:
            if game_piece.get_pos() == current_pos:
                game_piece.reset()


def get_permission() -> bool:
    """Gives a game piece the permission to leave home and get on field

    Returns:
        bool: true if the dice got a 6 in three throws
    """
    for _ in range(3):
        if dice() == 6:
            return True
    return False


def make_a_move(*, current_player: Player, players: list[Player]) -> None:
    """Simulates and also handles the move in the game

    If a player has no game pieces to play with,
    the player has to get a new game piece on the board.
    Otherwise the move gets validated and then the player moves

    Args:
        current_player (Player): the player that has the current turn
        players (list[Player]): information of all players
    """
    permission = get_permission()

    if not has_player_playable_game_pieces_on_board(current_player) and permission:
        current_game_piece = current_player.place_game_piece_on_start()
        did_player_hit_other_players(game_piece_being_checked=current_game_piece,
                                     players=players)

    if has_player_playable_game_pieces_on_board(current_player):
        current_game_piece = current_player.move(dice())
        did_player_hit_other_players(game_piece_being_checked=current_game_piece,
                                     players=players)


############################## End of game mechanics ##############################

############################## Start of helper functions ##############################


def has_player_playable_game_pieces_on_board(current_player: Player) -> bool:
    """Checks if a player has at least one playable game piece on the board

    Args:
        current_player (Player): the player that has the current turn

    Returns:
        bool: true if at least one playable game piece of the color is on the board
    """
    for game_piece in current_player.game_pieces:
        if game_piece.is_on_field() and not game_piece.is_done:
            return True
    return False


def has_one_player_won(size: str, players: list[Player]) -> Optional[Player]:
    """Checks if a player has won yet

    Args:
        size (str): size of game board. look into SIZES for sizes
        players (list[Player]): information of all players

    Returns:
        Player | None: the winning player or None if no one has won yet
    """
    for player in players:
        has_player_won = True
        for game_piece in player.game_pieces:
            if game_piece.get_pos() not in goal_positions(size)[player.color]:
                has_player_won = False
                break
        if has_player_won:
            return player
    return None

############################## End of helper functions ##############################

############################## Start of setup & game loop ##############################


def draw_winner(player: Player):
    """Draws winner by passing on the color of the player

    Args:
        player (Player): player that won
    """
    draw_winner_on_board(player.color)


# pylint: disable-next=unused-argument
def setup(size: str, amount_of_players: int) -> tuple[list[Player], Player]:
    """A setup function so the game can start with initial values

    Args:
        size (str): size of game board. look into SIZES for sizes
        amount_of_players (int): the amount of players in the game (not implemented yet)

    Returns:
        tuple[list[Player], Player]: first a tuple with all the players,
                                     second the player that starts the game
    """
    players: list[Player] = []
    for color in COLORS:
        players.append(Player(board_size=size, color=color, game_pieces=[GamePiece(
            size, color, home_positions(size)[color][i], speed=3) for i in range(4)]))

    for player, color in zip(players, COLORS):
        for game_piece in player.game_pieces:
            game_piece.turtle.seth(HOME_ANGLES[color])
            game_piece.turtle.goto(game_piece.home_position)

    starting_player = choice(players)

    return players, starting_player


def start_game_loop(size: str, amount_of_players: int = 4):
    """Starts the game loop

    Loop works as follows:
    - move the current player
      (validation and handling happens in move or in subfunctions of move)
    - set the next player for the next iteration
    - check if someone has won yet

    Args:
        size (str): size of game board. look into SIZES for sizes
        amount_of_players (int, optional): amount of players that are playing (not implemented yet).
                                           Defaults to 4.
    """
    players, current_player = setup(size, amount_of_players)
    index_of_current_player = players.index(current_player)
    won_player: Optional[Player] = None
    iterations = 0

    while not won_player:
        make_a_move(current_player=current_player, players=players)
        index_of_current_player += 1
        current_player = players[(index_of_current_player+1) % 4]
        won_player = has_one_player_won(size, players)
        iterations += 1
        if iterations == 300:
            break
    print(f"{iterations =}")
    print(f"{won_player.color} has won the game")
    draw_winner(won_player)


def start_game(size: str = "medium"):
    """Starts game

    Args:
        size (str, optional): size of game board. look into SIZES for sizes. Defaults to "medium".
    """
    game_board(size)
    start_game_loop(size)
    exitonclick()


############################## End of start & game loop ##############################


def main():
    """pylint shut up"""
    start_game("small")


if __name__ == "__main__":
    main()
