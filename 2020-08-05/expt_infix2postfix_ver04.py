class MakeExpt:

    class stack:
        def __init__(self):
            self.item = []  
        def push(self,data):
            self.item.insert(0,data)
        def isEmty(self):
            return self.item == [] 
        def pop(self):
            return self.item.pop(0)
        def peek(self):
            return self.item[0]
        def size(self):
            return len(self.item)

    def __init__(self,infix):
        self.infix = infix
        self.convert_infix = []
        self.postfix = []      
        self.opstack = self.stack() 

    def convenrtfunction(self):                        
        self.tokenlist = self.infix.replace(" ", "") 
        for i in range(len(self.tokenlist)):
            if self.tokenlist[i] == "I" and self.tokenlist[i+1] == '0':
                self.convert_infix.append("I0")
            elif self.tokenlist[i] == "I" and self.tokenlist[i+1] == '1':
                self.convert_infix.append("I1")
            elif self.tokenlist[i] == "I" and self.tokenlist[i+1] == '2':
                self.convert_infix.append("I2")
            elif self.tokenlist[i] == "I" and self.tokenlist[i+1] == '3':
                self.convert_infix.append("I3")
            elif self.tokenlist[i] in "+&!()" :
                self.convert_infix.append(self.tokenlist[i])
            elif self.tokenlist[i] in "01" and self.tokenlist[i-1] != "I":
                self.convert_infix.append(self.tokenlist[i])
        return self.convert_infix

    def infixtopostfix(self):
        self.opr = {'!':3,'+':2,'&':2,'(':1}                              
        for token in self.convert_infix :   
            if token in "I0I1I2I3":
                self.postfix.append(token)   
            elif token is "(":
                self.opstack.push(token) 
            elif token is ")":
                toptoken = self.opstack.pop()      
                while toptoken != "(":
                    self.postfix.append(toptoken)      
                    toptoken = self.opstack.pop()      
            else:
                while (not self.opstack.isEmty()) and (self.opr[self.opstack.peek()] >= self.opr[token]): 
                    self.postfix.append(self.opstack.pop())    
                self.opstack.push(token) 
        while not self.opstack.isEmty():  
            self.postfix.append(self.opstack.pop()) 
        #print(self.postfix)
        return self.postfix

    ##############################################################

Q1 = "!(1+0)"
Q2 = "!(!(0+I0&1))"
Q3 = "(I0+!I1+!(I2)) & (!I0+I1+I2)"
Q4 = "!(I0&I1) +! (I1+I2)"
Q5 = "(((I0&I1&!I2)+!I1)+I3)"

x1 = MakeExpt(Q1)
x1.convenrtfunction()
x1.infixtopostfix()