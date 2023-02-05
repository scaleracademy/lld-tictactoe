class Player:
    _name = ""
    _email = ""
    _symbol = ""
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def symbol(self):
        return self._symbol
    
    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol
