

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
        stack = ""
        for i in range (len(a)):
            stack+=a[i]
        self.line = stack
        
    def is_tuli(self):
        tulemisarvo = False
        kasa = self.line.lower()
        if len(kasa)>=4:
            for i in range (len(kasa)-3):
                line = kasa[i:i+4]
                if line == "tuli":
                    tulemisarvo = True
                    return tulemisarvo
        else:
            tulemisarvo = False
        return tulemisarvo
    
    def is_tissit(self):
        tissivakio = False
        stack = self.line.lower()
        if len(stack)>=6:
            for i in range (len(stack)-5):
                line = stack[i:i+6]
                if line == "tissit" or line == "715517":
                    tissivakio = True
                    del(self)
                    return tissivakio
        else:
            tissivakio = False
        del(self)
        return tissivakio