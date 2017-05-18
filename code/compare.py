

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
        totuus = self.double(4,"tuli", "tule")
        return totuus
    
    def is_tissit(self):
        totuus = self.double(6,"tissit", "715517")
        if totuus != True:
            totuus = self.double(5, "tissi", "71551")
        del(self)
        return totuus
    
    def double(self, n, key1, key2):
        stack = self.line.lower()
        if len(stack)>=n:
            for i in range (len(stack)-n+1):
                line = stack[i:i+n]
                if line == key1 or line == key2:
                    return True
        return False