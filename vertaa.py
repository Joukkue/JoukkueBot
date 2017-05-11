

class comparing():
    def __init__(self, line):
        self.line = line
        
    def __del__(self):
        return
        
    def is_tuli(self):
        kasa = self.line.rstrip()
        kasa = kasa.lower()
        if len(kasa)>=4:
            for i in range (len(kasa)-3):
                print(i)
                line = kasa[i:i+4]
                if line == "tuli":
                    tulemisarvo = True
        else:
            tulemisarvo = False
        del(self)
        return tulemisarvo
        