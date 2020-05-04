#!/usr/bin/python3.7

class Score:
    """This class stores gained points."""
    def __init__(self):
        """Initialize class instance."""
        self.__player = 0
        self.__enemy = 0
        self.__LIMIT = 3

    def player_point(self) -> None:
        """Assign one point to player."""
        self.__player += 1

    def enemy_point(self) -> None:
        """Assign one point to emeny."""
        self.__enemy += 1

    def is_over(self) -> bool:
        """Test if game over."""
        return self.__player == self.__LIMIT or self.__enemy == self.__LIMIT

    def over_decision(self) -> str:
        """Return game over message."""
        who = ''

        if self.__player > self.__enemy:
            who = 'player'

        elif self.__enemy > self.__player:
            who = 'enemy'

        else:
            who = 'no one'
        
        return 'game is over {} win'.format(who)
    
    def status(self) -> str:
        """Return formatted game status string."""
        return 'score: player {} enemy {}'.format(self.__player, self.__enemy)
