import pygame

class piece:
    def __init__(self,nom='VIDE',team='', image=''):
        
        self.nom = nom
        self.team = team
        self.image = image
        self.alive = True
        self.x = None
        self.y = None
        self.toMove = False
        self.hasMoved = False


    def setCoordonne(self, x, y):
        self.x = x
        self.y = y

    def initListPieces(self, listpion):
        #init des pieces 
        for pion in range (1, 17):
            if(pion < 9):
                listpion.append(piece('pion', 'white', 'img/Pion_white.png'))
            else:
                listpion.append(piece('pion', 'black', 'img/Pion_black.png'))

        for cavalier in range (1, 5):
            if (cavalier < 3):
                listpion.append(piece('cavalier', 'white', 'img/Cavalier_white.png'))
            else:
                listpion.append(piece('cavalier', 'black', 'img/Cavalier_black.png'))
        for fou in range (1, 5):
            if (fou < 3):
                listpion.append(piece('fou', 'white', 'img/Fou_white.png'))
            else:
                listpion.append(piece('fou', 'black', 'img/Fou_black.png'))
        for tour in range (1, 5):
            if (tour < 3):
                listpion.append(piece('tour', 'white', 'img/Tour_white.png'))
            else:
                listpion.append(piece('tour', 'black', 'img/Tour_black.png'))
        listpion.append(piece('reine', 'white', 'img/Reine_white.png'))
        listpion.append(piece('reine', 'black', 'img/Reine_black.png'))
        listpion.append(piece('roi', 'white', 'img/Roi_white.png'))
        listpion.append(piece('roi', 'black', 'img/Roi_black.png'))
    def Draw(self, screen, x, y):
        screen.blit(pygame.image.load(self.image).convert_alpha(), (14 + 100 * self.x, 10+100* self.y))


    def ZoneToMove(self, damier):
        zoneToMove= []
        # deplacement pion blanc
        if(self.nom[0:4] == 'pion' and self.team == 'white'):
            #pion move
            if(damier.case[self.x][self.y+1] == 0 and self.y+1 < 8):
                zoneToMove.append({'x': self.x, 'y': self.y+1})
                if(self.y == 1 and damier.case[self.x][self.y+2] == 0):
                    zoneToMove.append({'x': self.x, 'y': self.y+2})
            # pion attack
            if(self.x+1 < 8 and self.y+1 < 8):
                if( damier.case[self.x+1][self.y+1] != 0 and damier.case[self.x+1][self.y+1].team != self.team):
                    zoneToMove.append({'x': self.x+1, 'y': self.y+1})
            if(self.x-1 > -1 and self.y+1 < 8):
                if( damier.case[self.x-1][self.y+1] != 0 and damier.case[self.x-1][self.y+1].team != self.team):
                    zoneToMove.append({'x': self.x-1, 'y': self.y+1})
            

        # deplacement pion noir 
        if(self.nom[0:4] == 'pion' and self.team == 'black'):
            if(damier.case[self.x][self.y-1] == 0 and self.y-1 > -1):
                zoneToMove.append({'x': self.x, 'y': self.y-1})
                if( self.y == 6 and damier.case[self.x][self.y-2] == 0):
                    zoneToMove.append({'x': self.x, 'y': self.y-2})
            # pion attack
            if(self.x+1 < 8 and self.y-1 > -1):
                if( damier.case[self.x+1][self.y-1] != 0 and damier.case[self.x+1][self.y-1].team != self.team):
                    zoneToMove.append({'x': self.x+1, 'y': self.y-1})
            if(self.x-1 > -1 and self.y-1 > -1):
                if( damier.case[self.x-1][self.y-1] != 0 and damier.case[self.x-1][self.y-1].team != self.team):
                    zoneToMove.append({'x': self.x-1, 'y': self.y-1})

        
        # deplacement cavalier 
        if(self.nom[0:4] == 'cava'):
            # Move top left
                if(self.x+1 < 8 and self.y-2 > -1):
                    if(damier.case[self.x+1][self.y-2] == 0 or damier.case[self.x+1][self.y-2].team != self.team):
                        zoneToMove.append({'x': self.x+1, 'y': self.y-2})
            # Move top right
                if(self.x-1 > -1 and self.y-2 > -1):
                    if (damier.case[self.x-1][self.y-2] == 0 or damier.case[self.x-1][self.y-2].team != self.team):
                        zoneToMove.append({'x': self.x-1, 'y': self.y-2})
            # Move left top
                if(self.x-2 > -1 and self.y-1 > -1):
                    if(damier.case[self.x-2][self.y-1] == 0 or damier.case[self.x-2][self.y-1].team != self.team):
                        zoneToMove.append({'x': self.x-2, 'y': self.y-1})
            # Move left bottom
                if(self.x-2 > -1 and self.y+1 < 8):
                    if(damier.case[self.x-2][self.y+1] == 0 or damier.case[self.x-2][self.y+1].team != self.team):
                        zoneToMove.append({'x': self.x-2, 'y': self.y+1})
            # Move right top
                if(self.x+2 < 8 and self.y-1 > -1):
                    if(damier.case[self.x+2][self.y-1] == 0 or damier.case[self.x+2][self.y-1].team != self.team):
                        zoneToMove.append({'x': self.x+2, 'y': self.y-1})
            # Move right bottom
                if(self.x+2 < 8 and self.y+1 < 8):
                    if(damier.case[self.x+2][self.y+1] == 0 or damier.case[self.x+2][self.y+1].team != self.team):
                        zoneToMove.append({'x': self.x+2, 'y': self.y+1})
            # Move bottom left
                if(self.x-1 > -1 and self.y+2 < 8):
                    if(damier.case[self.x-1][self.y+2] == 0 or damier.case[self.x-1][self.y+2].team != self.team):
                        zoneToMove.append({'x': self.x-1, 'y': self.y+2})
            # Move bottom right
                if(self.x+1 < 8 and self.y+2 < 8):
                    if(damier.case[self.x+1][self.y+2] == 0 or damier.case[self.x+1][self.y+2].team != self.team):
                        zoneToMove.append({'x': self.x+1, 'y': self.y+2})


        #tour && reine
        if(self.nom[0:4] == "tour" or self.nom[0:4] == 'rein' or self.nom[0:3] == "roi"):
            
            if self.nom[0:3] == "roi":

                left = self.x - 1
                leftmax = self.x - 2
                right = self.x + 1
                rightmax = self.x + 2
                top = self.y - 1
                topmax = self.y - 2
                bottom = self.y + 1
                bottommax = self.y + 2
            else:
                left = self.x -1
                leftmax = -1
                rightmax = 8
                right = self.x
                top = self.y - 1
                topmax = -1
                bottom = self.y
                bottommax = 8
        # axe X
            #left
            for x in range(left, leftmax, -1):
                if(x != self.x):
                    # case vide
                    if(x > -1 and damier.case[x][self.y] == 0):
                        zoneToMove.append({'x': x, 'y': self.y})
                    # case ennemi
                    elif(x > -1 and damier.case[x][self.y] != 0 and damier.case[x][self.y].team != self.team):
                        zoneToMove.append({'x': x, 'y': self.y})
                        break
                    # case allie
                    elif(x > -1 and damier.case[x][self.y] != 0 and damier.case[x][self.y].team == self.team):
                        break

            #right
            for x in range(right, rightmax, 1):
                if(x != self.x):
                    # case vide
                    if(x< 8 and damier.case[x][self.y] == 0):
                        zoneToMove.append({'x': (x), 'y': self.y})
                    # case ennemi
                    elif(x < 8 and damier.case[x][self.y] != 0 and damier.case[x][self.y].team != self.team):
                        zoneToMove.append({'x': (x), 'y': self.y})
                        break
                    # case allie
                    elif(x < 8 and damier.case[x][self.y] != 0 and damier.case[x][self.y].team == self.team):
                        break
        #axe Y
            #top
            for y in range(top, topmax, -1):
                if(y != self.y):
                    # case vide
                    if(y > -1 and damier.case[self.x][y] == 0):
                        zoneToMove.append({'x': self.x, 'y': y})
                    # case ennemi
                    elif(y > -1 and damier.case[self.x][y] != 0 and damier.case[self.x][y].team != self.team):
                        zoneToMove.append({'x': self.x, 'y': y})
                        break
                    # case allie
                    elif(y > -1 and damier.case[self.x][y] != 0 and damier.case[self.x][y].team == self.team):
                        break

            #bottom
            for y in range(bottom, bottommax, 1):
                if(y != self.y):

                    # case vide
                    if(y < 8 and damier.case[self.x][y] == 0):
                        zoneToMove.append({'x': self.x, 'y': (y)})
                    # case ennemi
                    elif(y < 8 and damier.case[self.x][y] != 0 and damier.case[self.x][y].team != self.team):
                        zoneToMove.append({'x': self.x, 'y': (y)})
                        break
                    # case allie
                    elif(y < 8 and damier.case[self.x][y] != 0 and damier.case[self.x][y].team == self.team): 
                        break
            
        
        if(self.nom[0:3] == "fou" or self.nom[0:4] == 'rein' or self.nom[0:3]=="roi"):
        
            topright = self.x
            toprightmax = 8
            topleft = self.x
            topleftmax = -1
            bottomright = self.x
            bottomrightmax = 8
            bottomleft = self.x
            bottomleftmax = -1

            y = self.y
        # top
            # right 
            for x in range(topright, toprightmax, 1):
                
                y -= 1
                # case vide
                if(x != self.x and y != self.y):
                    if(self.nom[0:3]=="roi" and x == self.x + 2):
                        break
                    elif(x < 8 and y+1 > -1 and damier.case[x][y+1] == 0):
                        zoneToMove.append({'x': x, 'y': y+1})
                # case ennemi
                    elif(x < 8 and y+1 > -1 and damier.case[x][y+1] != 0 and damier.case[x][y+1].team != self.team):
                        zoneToMove.append({'x': x, 'y': y+1})
                        break
                # case allie
                    elif(x < 8 and y+1 > -1 and damier.case[x][y+1] != 0 and damier.case[x][y+1].team == self.team): 
                        break
            
            # left
            y = self.y
            for x in range(topleft, topleftmax, -1):
                
                y -= 1
                # case vide 
                if(x != self.x and y != self.y):
                    if(self.nom[0:3]=="roi" and x == self.x - 2):
                        break
                    if(x > -1 and  y+1 > -1 and damier.case[x][y+1] == 0):
                        zoneToMove.append({'x': x, 'y': y+1})
                # case ennemi
                    elif(x > -1 and  y+1 > -1 and damier.case[x][y+1] != 0 and damier.case[x][y+1].team != self.team):
                        zoneToMove.append({'x': x, 'y': y+1})
                        break
                # case allie
                    elif(x > -1 and  y+1 > -1 and damier.case[x][y+1] != 0 and damier.case[x][y+1].team == self.team): 
                        break
        #bottom
            y = self.y
            # right 
            for x in range(bottomright, bottomrightmax, 1):
                
                y += 1
                # case vide
                if(x != self.x and y != self.y):
                    if(self.nom[0:3]=="roi" and x == self.x + 2):
                        break
                    if(x < 8 and y-1 < 8 and damier.case[x][y-1] == 0):
                        zoneToMove.append({'x': x, 'y': y-1})
                # case ennemi
                    elif(x < 8 and y-1 < 8 and damier.case[x][y-1] != 0 and damier.case[x][y-1].team != self.team):
                        zoneToMove.append({'x': x, 'y': y-1})
                        break
                # case allie
                    elif(x < 8 and y-1 < 8 and damier.case[x][y-1] != 0 and damier.case[x][y-1].team == self.team): 
                        break
            
            # left
            y = self.y
            for x in range(bottomleft, bottomleftmax, -1):
                
                y += 1
                # case vide
                if(x != self.x and y != self.y):
                    if(self.nom[0:3]=="roi" and x == self.x - 2):
                        break
                    if(x > -1 and y-1 < 8 and damier.case[x][y-1] == 0):
                        zoneToMove.append({'x': x, 'y': y-1})
                # case ennemi
                    elif(x > -1 and y-1 < 8 and damier.case[x][y-1] != 0 and damier.case[x][y-1].team != self.team):
                        zoneToMove.append({'x': x, 'y': y-1})
                        break
                #case allie
                    elif(x > -1 and y-1 < 8 and damier.case[x][y-1] != 0 and damier.case[x][y-1].team == self.team): 
                        break
        
        #roque
        if(self.nom[0:3] == "roi" and self.hasMoved == False):
                        
            #  petit roque
            if(damier.case[0][self.y] != 0 and damier.case[1][self.y] == 0 and damier.case[2][self.y] == 0):
                if(damier.case[0][self.y].nom[0:4] == "tour" and damier.case[0][self.y].hasMoved == False):       
                    zoneToMove.append({'x': damier.case[0][self.y].x, 'y': damier.case[0][self.y].y})
            # grand roque
            if(damier.case[7][self.y] != 0 and damier.case[6][self.y] == 0 and damier.case[5][self.y] == 0 and damier.case[4][self.y] == 0):
                if(damier.case[7][self.y].nom[0:4] == "tour" and damier.case[7][self.y].hasMoved == False):       
                    zoneToMove.append({'x': damier.case[7][self.y].x, 'y': damier.case[7][self.y].y})
                                    

        return zoneToMove
        
    def Victory(self, listpion):
        #condition victoire
        loop = True
        blancMort = len([x for x in listpion if x.team == "white" and x.alive == False])
        noirMort = len([x for x in listpion if x.team == "black" and x.alive == False])


        for piece in listpion:
            if(piece.nom[0:3]=="roi" and piece.alive == False):
                print('╔════════════◀══•═▶════════════╗')
                if(piece.team == "white"):
                    print('     Les noirs ont gagnés !')
                    loop = False
                else:
                    print('     Les blancs ont gagnés !')
                    loop = False
                print('  Pieces blanches perdues : ' + str(blancMort))
                print('  Pieces noires perdues : ' + str(noirMort))
                print('╚════════════◀══•═▶════════════╝')
        return loop

        
        
