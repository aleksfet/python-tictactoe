import pygame
pygame.font.init()
running = True
background_colour = (225,225,225)
black = (0,0,0)
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption('Calculator')
screen.fill(background_colour)
num1 = ""
num2 = ""
operator = ""
current_value = 1
equation = ""
third = False
ansnum = False
colour = (195,195,195)
colour2 = (176,176,176)
my_font = pygame.font.SysFont('Times New Roman', 45)
my_font2 = pygame.font.SysFont('Times New Roman', 60)
my_font3 = pygame.font.SysFont('Times New Roman', 40)
#FUNCTIONS
def addition(val):
    global equation,num1,num2
    if ansnum == False:

        equation += val                   
        if current_value == 1:
            num1 += val
        else:
            num2 += val 
def plusign(val):
    global operator,current_value,third,ansnum,equation,num1,num2
    if third == False:
        equation += val
        ansnum = False
        screen.fill(pygame.Color(background_colour)) # erases the entire screen surface   
        current_value = 2  
        operator = val
        third = True
    else:
        if operator == "+":
            screen.fill(pygame.Color(background_colour)) # erases the entire screen surface
            equation = str(float(num1)+float(num2))
        if operator == "-":
            screen.fill(pygame.Color(background_colour)) # erases the entire screen surface
            equation = str(float(num1)-float(num2))
        if operator == "*":
            screen.fill(pygame.Color(background_colour)) # erases the entire screen surface
            equation = str(float(num1)*float(num2))  
        if operator == "/":
            screen.fill(pygame.Color(background_colour)) # erases the entire screen surface
            equation = str(float(num1)/float(num2))
        num1 = equation
        equation += val
        num2 = ""
        operator = val
        current_value = 2                       
        ansnum = False

while running:
#DRAWINGS  0-9   
    pygame.draw.line(screen,black, (1,1), (749,1))
    pygame.draw.line(screen,black, (1,748), (749,748))
    
    pygame.draw.rect(screen, colour, pygame.Rect(125, 200, 100, 100))
    text_surface = my_font.render('7', False, (0, 0, 0))   
    screen.blit(text_surface, (165,225))

    pygame.draw.rect(screen, colour, pygame.Rect(325, 200, 100, 100))
    text_surface = my_font.render('8', False, (0, 0, 0))   
    screen.blit(text_surface, (365,225))

    pygame.draw.rect(screen, colour, pygame.Rect(525, 200, 100, 100))
    text_surface = my_font.render('9', False, (0, 0, 0))   
    screen.blit(text_surface, (565,225))

    pygame.draw.rect(screen, colour, pygame.Rect(125, 325, 100, 100))
    text_surface = my_font.render('4', False, (0, 0, 0))   
    screen.blit(text_surface, (165,350))

    pygame.draw.rect(screen, colour, pygame.Rect(325, 325, 100, 100))
    text_surface = my_font.render('5', False, (0, 0, 0))   
    screen.blit(text_surface, (365,350))

    pygame.draw.rect(screen, colour, pygame.Rect(525, 325, 100, 100))
    text_surface = my_font.render('6', False, (0, 0, 0))   
    screen.blit(text_surface, (565,350)) 

    pygame.draw.rect(screen, colour, pygame.Rect(125, 450, 100, 100))
    text_surface = my_font.render('1', False, (0, 0, 0))   
    screen.blit(text_surface, (165,475))

    pygame.draw.rect(screen, colour, pygame.Rect(325, 450, 100, 100))
    text_surface = my_font.render('2', False, (0, 0, 0))   
    screen.blit(text_surface, (365,475))

    pygame.draw.rect(screen, colour, pygame.Rect(525, 450, 100, 100))
    text_surface = my_font.render('3', False, (0, 0, 0))   
    screen.blit(text_surface, (565,475))

    pygame.draw.rect(screen, colour2, pygame.Rect(25, 585, 100, 100))
    text_surface = my_font.render('+', False, (255, 200, 0))   
    screen.blit(text_surface, (65,610))

    pygame.draw.rect(screen, colour2, pygame.Rect(140, 585, 100, 100))
    text_surface = my_font.render('-', False, (255, 200, 0))   
    screen.blit(text_surface, (182,609))  

    pygame.draw.rect(screen, colour2, pygame.Rect(255, 585, 100, 100))
    text_surface = my_font.render('*', False, (255, 200, 0))   
    screen.blit(text_surface, (294,618))    

    pygame.draw.rect(screen, colour2, pygame.Rect(370, 585, 100, 100))
    text_surface = my_font.render('/', False, (255, 200, 0))   
    screen.blit(text_surface, (411,612))

    pygame.draw.rect(screen, colour2, pygame.Rect(518, 580, 120, 120))
    text_surface = my_font2.render('=', False, (255, 200, 0))   
    screen.blit(text_surface, (564,608))  

    pygame.draw.rect(screen, colour, pygame.Rect(5, 450, 100, 100))
    text_surface = my_font.render('0', False, (0, 0, 0))   
    screen.blit(text_surface, (42,476))  
#CLEAR
    pygame.draw.rect(screen, colour2, pygame.Rect(5, 326, 100, 100))
    text_surface = my_font3.render('Clear', False, (255, 200, 0))   
    screen.blit(text_surface, (9,353))
    
    text_surface = my_font2.render(equation, False, (0, 0, 0))  
    screen.blit(text_surface, (165,60))
#FUNCTIONS
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:         
            running = False   
        #Clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0]>125 and pos[0]<225 and pos[1]>450 and pos[1]<550:
                addition("1")
            if pos[0]>325 and pos[0]<425 and pos[1]>450 and pos[1]<550:
                addition("2")
            if pos[0]>525 and pos[0]<625 and pos[1]>450 and pos[1]<550:
                addition("3")                        
            if pos[0]>125 and pos[0]<225 and pos[1]>325 and pos[1]<425:
                addition("4")                     
            if pos[0]>325 and pos[0]<425 and pos[1]>325 and pos[1]<425:
                addition("5") 
            if pos[0]>525 and pos[0]<625 and pos[1]>325 and pos[1]<425:
                addition("6") 
            if pos[0]>125 and pos[0]<225 and pos[1]>200 and pos[1]<300:
                addition("7") 
            if pos[0]>325 and pos[0]<425 and pos[1]>200 and pos[1]<300:
                addition("8")
            if pos[0]>525 and pos[0]<625 and pos[1]>200 and pos[1]<300:
                addition("9")
            if pos[0]>5 and pos[0]<105 and pos[1]>450 and pos[1]<550:
                addition("0")
                #OPERATIONS OR SYMBOLS
            #PLUS                     
            if pos[0]>25 and pos[0]<125 and pos[1]>585 and pos[1]<685:
                plusign("+")
                    
            #MINUS                                               
            if pos[0]>140 and pos[0]<240 and pos[1]>585 and pos[1]<685:
                plusign("-")
                       
            #MULTIPLICATION                        
            if pos[0]>255 and pos[0]<355 and pos[1]>585 and pos[1]<685:
                plusign("*")
            #DIVISION                            
            if pos[0]>370 and pos[0]<470 and pos[1]>585 and pos[1]<685:
                plusign("/")                          
            #CLEAR BUTTON                        
            if pos[0]>5 and pos[0]<105 and pos[1]>326 and pos[1]<426:
                num1 = ""
                num2 = ""
                equation = ""
                operator = ""
                current_value = 1 
                screen.fill(pygame.Color(background_colour))     
                ansnum = False                   

            #EQUALS OPERATION    
            if pos[0]>520 and pos[0]<640 and pos[1]>580 and pos[1]<700:
                equation += "="
                if operator == "+":
                    screen.fill(pygame.Color(background_colour)) # erases the entire screen surface
                    equation = str(float(num1)+float(num2))
                if operator == "-":
                    screen.fill(pygame.Color(background_colour)) # erases the entire screen surface
                    equation = str(float(num1)-float(num2))
                if operator == "*":
                    screen.fill(pygame.Color(background_colour)) # erases the entire screen surface
                    equation = str(float(num1)*float(num2))  
                if operator == "/":
                    screen.fill(pygame.Color(background_colour)) # erases the entire screen surface
                    equation = str(float(num1)/float(num2))    
                num1 = equation
                num2 = ""
                operator = ""
                current_value = 1
                ansnum = True
