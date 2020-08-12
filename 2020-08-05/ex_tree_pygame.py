################################################################
# File: ex_tree_pygame
# No: 6201012620082
# Date: 2020-08-05
################################################################


#-------
# import pygame
# pygame.init()
# # set screen and color
# scr_w , scr_h = 500, 500
# WHITE = (255, 255, 255) 
# GREEN = (0, 255, 0) 
# BLUE  = (0, 0, 255)
# screen = pygame.display.set_mode( (scr_w, scr_h) )
# # set window caption
# pygame.display.set_caption('Expression Tree') 
# # set font 
# pygame.font.init() 
# text_font = pygame.font.SysFont('Leelawadeeui', 30)

#------

class node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
# ------------------------------------
class Stack:
    def __init__(self):
        self.a = []
    def isEmpty(self):
        return self.a == []
    def push(self,i):
        self.a.append(i)
    def pop(self):
        return self.a.pop()
    def peek(self):
        return self.a[len(self.a)-1]

def infixToPrefix(s):
    prec = {'!':1,'+':3,'&':2,'(':1}
    opStack = Stack()
    prefixList = []
    temp = []
    for token in s:
        if token in "I" or token in "0123456789":
            prefixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                temp.append(topToken)
                topToken = opStack.pop()
            prefixList = temp + prefixList
            temp = []
        else:
            while (not opStack.isEmpty()) and  (prec[opStack.peek()]>= prec[token]):
                temp.append(opStack.pop())
            prefixList = temp + prefixList
            temp = []
            opStack.push(token)
    while not opStack.isEmpty():
        temp.append(opStack.pop())
    prefixList = temp + prefixList
    return ''.join(prefixList)

print (infixToPrefix("I0&I1+!(I1&I2)"))
