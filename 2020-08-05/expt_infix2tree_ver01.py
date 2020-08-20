class Make_expressiontree:

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
        self.opr = {'!':3,'+':2,'&':2,'(':1}
        self.operations = "+&!()"
        self.stack_tree = self.stack()
        self.newnode = self.Node(None)
    
    def convert_expression(self):                        
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
            elif self.tokenlist[i] in self.operations :
                self.convert_infix.append(self.tokenlist[i])
            elif self.tokenlist[i] in "01" and self.tokenlist[i-1] != "I":
                self.convert_infix.append(self.tokenlist[i])
        return self.convert_infix

    def infix_to_postfix(self):                             
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
        print(self.postfix)
        return self.postfix

    ##############################################################

    class Node :
        def __init__(self,root):
            self.right_child = None
            self.left_child = None
            self.root = root

    def postfix_to_expt(self): # รับค่าเป็น postfix (left right root)
        expression_tree = []
        for index in self.postfix:
            if index == '!':
                child_not = self.stack_tree.pop()
                newnode = self.Node(index)
                newnode.left_child = child_not
                self.stack_tree.push(newnode)  
            
            elif index in "+&":
                right_child = self.stack_tree.pop() # stack จะเอาค่าที่ใส่เข้าไปล่าสุดออกมา จาก postfix ที่เข้าไปใน stack ขวา ซ้าย
                left_child = self.stack_tree.pop()
                newnode = self.Node(index)
                newnode.left_child = left_child
                newnode.right_child = right_child
                self.stack_tree.push(newnode)
                
            else:
                newnode = self.Node(index)
                self.stack_tree.push(newnode) # เอาค่าที่เป็น '0', '1' , 'I0',... (ที่ทำเป็นต้นไม้) ใส่ใน stack
        expression_tree = self.stack_tree.pop()
        return expression_tree

Q1 = "!(1+0)"
Q2 = "!(!(0+I0&1))"
Q3 = "(I0+!I1+!(I2)) & (!I0+I1+I2)"
Q4 = "!(I0&I1) +! (I1+I2)"
Q5 = "(((I0&I1&!I2)+!I1)+I3)"

x1 = Make_expressiontree(Q1)
x1.convert_expression()
x1.infix_to_postfix()

x2 = Make_expressiontree(Q2)
x2.convert_expression()
x2.infix_to_postfix()

x3 = Make_expressiontree(Q3)
x3.convert_expression()
x3.infix_to_postfix()

x4 = Make_expressiontree(Q4)
x4.convert_expression()
x4.infix_to_postfix()

x5 = Make_expressiontree(Q5)
x5.convert_expression()
x5.infix_to_postfix()



# Reference
# https://www.youtube.com/watch?v=2Z6g3kNymd0