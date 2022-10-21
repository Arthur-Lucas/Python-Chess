from pickle import FALSE
import pygame
from Damier import Damier
from piece import piece
from cursor import cursor

module_charge = pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Echec")



loop = True
listpion = []
initPlacements = True

selected_piece = None

zoneToMove = []

turnWhite = True
        
piece = piece()
piece.initListPieces(listpion)
damier = Damier()
cursor = cursor()
damier.initPlacement(damier,listpion)
while loop:
    screen.fill((0,0,0))
    
    damier.Draw(screen)
    cursor.Draw(screen)

    selected_piece = [x for x in listpion if x.toMove == True] # get piece who has been selected by cursor.ReadPion
    if selected_piece != []:
        selected_piece = selected_piece[0]
        zoneToMove = selected_piece.ZoneToMove(damier) # display cases where the piece can move + add cases in an array 
        if(zoneToMove != []):
            for zone in zoneToMove:
                pygame.draw.circle(screen, (250,128,114),[50 + zone.get("x")*100, 50 + zone.get("y")*100], 25)

    for x in range(8):
        for y in range(8):
            if damier.case[x][y] != 0:
                damier.case[x][y].Draw(screen, x, y)

    for event in pygame.event.get() :
        #bouge curseur
        cursor.MoveCursor(event)
        #deplacement du pion + changement du tour avec turnWhite
        if(zoneToMove != []):
            if(selected_piece != []):
                turnWhite = cursor.MovePion(event, selected_piece, zoneToMove, damier, turnWhite)
        #lire si un pion 
        cursor.ReadPion(event, listpion, turnWhite)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                loop = False
        if event.type == pygame.QUIT:
            loop = False
    # si roi meurt coupe le jeu
    loop = piece.Victory(listpion)

    pygame.display.flip()
pygame.quit()