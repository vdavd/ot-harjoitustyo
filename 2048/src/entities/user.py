class User:
    def __init__(self, username, hiscore=0):
        self._username = username
        self._hiscore = hiscore

    def get_username(self):
        return self._username
    
    def get_hiscore(self):
        return self._hiscore
    
    def update_hiscore(self, score):
        if score > self._hiscore:
            self._hiscore = score
            return self._hiscore
        return False