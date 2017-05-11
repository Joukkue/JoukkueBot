

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
                print(i)
                line = kasa[i:i+4]
                print(line)
                if line == "tuli":
                    tulemisarvo = True
                    del(self)
                    return True
        else:
            tulemisarvo = False
        del(self)
        return tulemisarvo
        