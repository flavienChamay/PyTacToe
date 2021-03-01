"""
This module implements the CLI of the Tic-Tac-Toe game.  It is also the main program of the game.

:method: human_choose_symbol()
:method: player_vs_player()
:method: player_vs_dumb_computer()
:method: player_vs_unbeatable_computer()n
:method: menu_manager()
"""
from gameBoard import GameBoard
from player import HumanPlayer, DumbComputerPlayer, UnbeatableComputerPlayer


def human_choose_symbol():
    """
    This function demands to the human player what symbol he wants.

    :returns HumanPlayer: A HumanPlayer instance with the choosen symbol.
    """

    print('Choose the symbol you want:', 'X: for the X player',
          'O: for the O player', sep='\n')
    return HumanPlayer(input('Your choice: '))


def player_vs_player():
    """
    This function manages the game between two human players.

    :var playerList list: The list of all the players involved.
    :var game GameBoard: The game board.
    :returns: None.
    """

    playerList = [human_choose_symbol(), human_choose_symbol()]
    game = GameBoard()
    game.play_on_board(playerList)


def player_vs_dumb_computer():
    """
    This function manages the game between a human player and a dumb computer.

    :var playerList list: The list of all the players involved.
    :var game GameBoard: The game board.
    :returns: None.
    """

    playerList = [DumbComputerPlayer('X'), HumanPlayer('O')]
    print('Computer is X and you are O.')
    game = GameBoard()
    game.play_on_board(playerList)


def player_vs_unbeatable_computer():
    """
    This function manages the game between a human player and an unbeatable computer.

    :var playerList list: The list of all the players involved.
    :var game GameBoard: The game board.
    :returns: None.
    """

    playerList = [UnbeatableComputerPlayer('X'), HumanPlayer('O')]
    print('Computer is X and you are O.')
    game = GameBoard()
    game.play_on_board(playerList)

    def load_game():
        """

        :notes: 
        Structure of a backup file:
        first line -> grid of the game, listed with X or O separated with empty spaces.
        second line -> symbol of the player who must play.
        third line -> type of game: (1) dumb computer vs player (2) unbeatable computer vs player (3) human player vs human player
        """

        with open("saveGameTTT.txt", 'r') as fileSaveGame:
            listFile = fileSaveGame.readlines()
            gridLoaded = listFile[0].split()
            playerPlay = listFile[1]
            typeOfPlay = listFile[2]

            # Process of the grid:
            gridToSave = GameBoard().grid
            index = 0
            for a, b, c in gridLoaded:
                gridToSave[index] = [a, b, c]
                index += 1

            # Process of the type of the game and the turn of the player:


def menu_manager():
    """
    This functions manages the menu in the CLI.

    :var waiting_for_input bool: True if the user wants to play, or to continue to play, or has given a wrong answer.
    :var user_choice str: The choice of the user from 1 to 5.
    :returns: None.
    """

    waiting_for_input = True
    print('Welcome to the PyTacToe game, a Tic-Tac-Toe game!')
    while waiting_for_input:
        print('Please choose:',
              '1: starting a new game player VS player;',
              '2: starting a new game player VS dumb computer (random moves);',
              '3: starting a new game player VS unbeatable computer;',
              '4: load a game;',
              '5: quit the game;', sep='\n')
        user_choice = input('Your choice: ')
        if user_choice == '1':
            player_vs_player()
        elif user_choice == '2':
            player_vs_dumb_computer()
        elif user_choice == '3':
            player_vs_unbeatable_computer()
        elif user_choice == '4':
            # TODO: save/load a game mechanism
            load_game()
            print('No implemented yet!')
        elif user_choice == '5':
            waiting_for_input = False
        else:
            print('Input was invalid, please pick a value from the list!')
    print('You have left the game, see you next time!')


if __name__ == '__main__':
    """
    Main program of the project. Calls the menu manager.
    """

    menu_manager()
