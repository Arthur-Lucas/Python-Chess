import pygame

class cursor:
    def __init__(self):
        self.x = 0
        self.y = 0
    def Draw(self, screen):
        pygame.draw.rect(screen, (57,255,20), [self.x*100, self.y*100, 100, 100], 100)
    def MoveCursor(self, event):
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_LEFT:
                if self.x != 0:
                    self.x -= 1
                else:
                    self.x = 7
            if event.key == pygame.K_RIGHT:
                if self.x != 7:
                    self.x += 1
                else:
                    self.x = 0
            if event.key == pygame.K_UP:
                if self.y != 0:
                    self.y -= 1  
                else:
                    self.y = 7
            if event.key == pygame.K_DOWN:
                if self.y != 7:
                    self.y += 1  
                else:
                    self.y = 0
    def ReadPion(self, event, listpion, turnwhite):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for piece in listpion:
                    if piece.x == self.x and piece.y == self.y:
                        #verif if it's the turn of black or white
                        if(turnwhite == True and piece.team == "white"):
                            piece.toMove = True
                        elif(turnwhite == False and piece.team == "black"):
                            piece.toMove = True
                    
                    else :
                        piece.toMove = False


    def MovePion(self, event, piece, zonepion, damier, turn):
        turnWhite = turn
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if(piece != None):
                    piece.toMove = False
                    # zone mouvement possible
                    for zone in zonepion:
                        if(self.x == zone.get('x') and self.y == zone.get('y')):
                        #roque
                            if(piece.nom[0:3] == "roi"):
                                #petit roque
                                if(piece.hasMoved == False and damier.case[1][self.y] == 0 and damier.case[2][self.y] == 0 and damier.case[0][self.y] != 1):
                                    if(damier.case[0][self.y].nom[0:4] == "tour"):
                                        #Maj roi
                                        damier.case[piece.x][piece.y] = 0
                                        piece.x = 1
                                        piece.y = piece.y
                                        damier.case [1][piece.y] = piece
                                        #Maj tour
                                        damier.case[self.x][self.y].x = 2
                                        damier.case[self.x][self.y].y = piece.y
                                        damier.case[2][self.y] = damier.case[self.x][self.y]
                                        damier.case[0][self.y] = 0


                                        # switch turn
                                        if turnWhite == True:
                                            turnWhite = False
                                        else:
                                            turnWhite = True
                                        piece.hasMoved = True
                                        return turnWhite
                                #grand roque
                                if(piece.hasMoved == False and damier.case[4][self.y] == 0 and damier.case[5][self.y] == 0 and damier.case[6][self.y] == 0 and damier.case[7][self.y] != 1):
                                    if(damier.case[7][self.y].nom[0:4] == "tour"):
                                        #Maj roi
                                        damier.case[piece.x][piece.y] = 0
                                        piece.x = 5
                                        piece.y = piece.y
                                        damier.case [5][piece.y] = piece
                                        #Maj tour
                                        damier.case[self.x][self.y].x = 4
                                        damier.case[self.x][self.y].y = piece.y
                                        damier.case[4][self.y] = damier.case[self.x][self.y]
                                        damier.case[7][self.y] = 0

                                        # switch turn
                                        if turnWhite == True:
                                            turnWhite = False
                                        else:
                                            turnWhite = True
                                        piece.hasMoved = True
                                        return turnWhite
                        # deplacement normal
                            damier.case[piece.x][piece.y] = 0 # MaJ du damier
                            piece.x = zone.get('x')  # MaJ piece
                            piece.y = zone.get('y')  # MaJ piece
                            # pion en dame quand arrive au bout
                            if(piece.nom[0:4] == "pion"):
                                if(piece.team == "white" and piece.y == 7):
                                    piece.nom = "reine"
                                    piece.image = "img/Reine_white.png"
                                elif(piece.team == "black" and piece.y == 0):
                                    piece.nom = "reine"
                                    piece.image = "img/Reine_black.png"
                            # destruction ennemi
                            if(damier.case [zone.get('x')][zone.get('y')] != 0):
                                damier.case [zone.get('x')][zone.get('y')].alive = False
                                damier.case [zone.get('x')][zone.get('y')].x = None
                                damier.case [zone.get('x')][zone.get('y')].y = None
                            damier.case [zone.get('x')][zone.get('y')] = piece  # MaJ du damier

                            # changement etat piece si a déjà bougé
                            piece.hasMoved = True

                            # change le tour du joueur
                            if turnWhite == True:
                                turnWhite = False
                            else:
                                turnWhite = True

        return turnWhite
                       

