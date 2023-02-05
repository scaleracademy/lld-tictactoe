class Cell:
    def __init__(self, x, y, player=None) -> None:
        self._x = x
        self._y = y
        self._player = player
    
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        self._player = value
    