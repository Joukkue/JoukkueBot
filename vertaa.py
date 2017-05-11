

class comparing():
    def __init__(self, line):
        self.removewhitespace(line)
        
    def __del__(self):
        return
    
    def removewhitespace(self, line):
        a = []
        for i in range (len(line)):
            if line[i] != " ":
                a.append(line[i])
        kasa = ""
        for i in range (len(a)):
            kasa+=a[i]
        self.line = kasa
        
    def is_tuli(self):
        tulemisarvo = False
        kasa = self.line.lower()
        if len(kasa)>=4:
            for i in range (len(kasa)-3):
                line = kasa[i:i+4]
                if line == "tuli":
                    tulemisarvo = True
                    del(self)
                    return True
        else:
            tulemisarvo = False
        del(self)
        return tulemisarvo
    
    def is_tissit(self):
        tissivakio = False
        kasa = self.line.lower()
        if len(kasa)>=6:
            for i in range (len(kasa)-5):
                line = kasa[i:i+6]
                if line == "tissit" or "715517":
                    tissivakio = True
                    del(self)
                    return True
        else:
            tissivakio = False
        del(self)
        return tissivakio