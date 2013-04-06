import constants

class RegEx:
    reswords = constants.RESERVED_WORDS
    
    def __init__(self):
        pass

    def process(self, string):
        if self.is_word(string):
            if string in self.reswords:
                return constants.RESWORD
            else:
                return constants.VARIABLE
        else:
            if self.is_symbol(string):
                return constants.SYMBOLS[string]
            elif self.is_number(string):
                return constants.NUMBER
            else:
                return constants.NOT_WORD

    def is_word(self, string):
        if not (string[0].isalpha() or
                string[0] == '_'):
            return False

        for i in range(len(string) - 1):
            if not (string[i+1].isalnum() or
                    string[i+1] == '_'):
                return False

        return True
        
    def is_number(self, string):
        """
        ([0...9]+ (.[0...9]+)? )*
        """
        if not string.isdigit():
            parts = string.split('.')
            if not len(parts) == 2:
                return False
            elif (parts[0].isdigit() and 
                  parts[1].isdigit()):
                return True
            else:
                return False
        else:
            return True
        
    def is_symbol(self, string):
        if string in constants.SYMBOLS:
            return True
        else:
            return False
    
