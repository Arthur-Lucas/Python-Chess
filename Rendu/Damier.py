import pygame

from piece import piece

class Damier:
    def __init__(self):
        self.case = []
        for r in range(8) :
            row = []
            for c  in range(8):
                row.append(0)
            self.case.append(row)
        for x in range(8):
            self.case[x][1] = piece()
        
    def Draw(self, ecran):
        for x in range(8):
            for y in range (8):
                if((y+x)%2 == 0):
                    pygame.draw.rect(ecran, (236,236,208,255), [x*100, y*100, 100, 100], 100)
                else:
                    pygame.draw.rect(ecran, (119,149,87,255), [x*100, y*100, 100, 100], 100)
    def initPlacement(self, damier, listpion):
        i = 0
        j = 0
        for piece in listpion:
            # pion blanc
            if((piece.nom[0:4] == 'pion') and (piece.team == 'white')):    
                piece.setCoordonne(i, 1)
                damier.case[i][1] = piece
                i += 1
            #pion noir
            elif((piece.nom[0:4] == 'pion') and (piece.team == 'black')):
                piece.setCoordonne(j, 6)
                damier.case[j][6] = piece
                j += 1
            #tour
            elif((piece.nom[0:4] == 'tour')):
                
                if(piece.team == 'white'):
                    if(damier.case[0][0] == 0):
                        piece.setCoordonne(0,0)
                        damier.case[0][0] = piece
                    else:
                        piece.setCoordonne(7,0)
                        damier.case[7][0] = piece
                else:
                    if(damier.case[0][7] == 0):
                        piece.setCoordonne(0,7)
                        damier.case[0][7] = piece
                    else:
                        piece.setCoordonne(7,7)
                        damier.case[7][7] = piece
            #cavalier
            elif(piece.nom[0:4] == 'cava'):
                if(piece.team == 'white'):
                    if(damier.case[1][0] == 0):
                        piece.setCoordonne(1,0)
                        damier.case[1][0] = piece
                    else:
                        piece.setCoordonne(6,0)
                        damier.case[6][0] = piece 
                else:
                    if(damier.case[1][7] == 0):
                        piece.setCoordonne(1,7)
                        damier.case[1][7] = piece
                    else:
                        piece.setCoordonne(6,7)
                        damier.case[6][7] = piece 
            #fou 
            elif(piece.nom[0:3] == 'fou'):
                if(piece.team == 'white'):
                    if(damier.case[2][0] == 0):
                        piece.setCoordonne(2,0)
                        damier.case[2][0] = piece
                    else:
                        piece.setCoordonne(5,0)
                        damier.case[5][0] = piece
                else :
                    if(damier.case[2][7] == 0):
                        piece.setCoordonne(2,7)
                        damier.case[2][7] = piece
                    else:
                        piece.setCoordonne(5,7)
                        damier.case[5][7] = piece
            #roi
            elif(piece.nom[0:3] == 'roi'):
                if(piece.team == 'white'):
                    piece.setCoordonne(3,0)
                    damier.case[3][0] = piece
                else:
                    piece.setCoordonne(3,7)
                    damier.case[3][7] = piece
            #dame
            elif(piece.nom[0:4] == 'rein'):
                if(piece.team == 'white'):
                    piece.setCoordonne(4,0)
                    damier.case[4][0] = piece
                else:
                    piece.setCoordonne(4,7)
                    damier.case[4][7] = piece
    
        
        