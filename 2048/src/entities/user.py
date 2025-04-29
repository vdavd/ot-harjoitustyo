class User:
    """Class that keeps track of the player user's username and hiscore.
    """    
    def __init__(self, username, hiscore=0):
        """Constructor of the class that generates a new user object.

        Args:
            username: The player's username.
            hiscore: The player's hiscore. Defaults to 0.
        """        
        self._username = username
        self._hiscore = hiscore

    def get_username(self):
        """Method for fetching the player's username.

        Returns:
            The player's username.
        """        
        return self._username
    
    def get_hiscore(self):
        """Method for fetching the player's hiscore.

        Returns:
            The player's hiscore.
        """        
        return self._hiscore
    
    def update_hiscore(self, score):
        """Compares the given score and player's hiscore, replaces the hiscore if the score is higher.

        Args:
            score: The score that will be compared with the hiscore.

        Returns:
            If the hiscore was changed, returns the new hiscore. Otherwise returns false.
        """        
        if score > self._hiscore:
            self._hiscore = score
            return self._hiscore
        return False