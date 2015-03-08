class Morse:
    _xlate = dict({
        'a' : ['dit','dah'],
        'b' : ['dah','dit','dit','dit'],
        'c' : ['dah','dit','dah','dit'],
        'd' : ['dah','dit','dit'],
        'e' : ['dit'],
        'f' : ['dit','dit','dah','dit'],
        'g' : ['dah','dah','dit'],
        'h' : ['dit','dit','dit','dit'],
        'i' : ['dit','dit'],
        'j' : ['dit','dah','dah','dah'],
        'k' : ['dah','dit','dah'],
        'l' : ['dit','dah','dit','dit'],
        'm' : ['dah','dah'],
        'n' : ['dah','dit'],
        'o' : ['dah','dah','dah'],
        'p' : ['dit','dah','dah','dit'],
        'q' : ['dah','dah','dit','dah'],
        'r' : ['dit','dah','dit'],
        's' : ['dit','dit','dit'],
        't' : ['dah'],
        'u' : ['dit','dit','dah'],
        'v' : ['dit','dit','dit','dah'],
        'w' : ['dit','dah','dah'],
        'x' : ['dah','dit','dit','dah'],
        'y' : ['dah','dit','dah','dah'],
        'z' : ['dah','dah','dit','dit'],
        '1' : ['dit','dah','dah','dah','dah'],
        '2' : ['dit','dit','dah','dah','dah'],
        '3' : ['dit','dit','dit','dah','dah'],
        '4' : ['dit','dit','dit','dit','dah'],
        '5' : ['dit','dit','dit','dit','dit'],
        '6' : ['dah','dit','dit','dit','dit'],
        '7' : ['dah','dah','dit','dit','dit'],
        '8' : ['dah','dah','dah','dit','dit'],
        '9' : ['dah','dah','dah','dah','dit'],
        '10': ['dah','dah','dah','dah','dah'],
        })
    _dit = 0.3
    _dah = 3 * _dit
    _interword = 3 * _dit
    _intraword = 7 * _dit

    def xlate(self,letter):
        try:
            return self._xlate[letter.lower()]
        except:
            return None

    def dit(self,time):
        assert float(time)
        self._dit = time
        self._dah = 3*time
        self._interword = 3*time
        self._intraword = 7*time

    def translate(self,string):
        """Translate a string into a list of morse bits """
        out = list()
        for l in list(string):
            if l == ' ':
                out.append('_intraword')
            else:
                out.extend(self.xlate(l))
                out.append('_interword')
        out.pop()  # pop off last interword
        return out

    def timing(self,message):
        timed = list()
        for symbol in message:
            
