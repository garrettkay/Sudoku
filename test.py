import pygame

pygame.init()
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("SudokuSolver")

def pygamePrint(text,pos,size,font,color,aa):
	if text == None:
		screen.blit(pygame.font.SysFont("Arial",12).render("New text box",False,(0,0,0)),(0,0))
		return
	if pos == None:
		screen.blit(pygame.font.SysFont("Arial",12).render(text,False,(0,0,0)),(0,0))
		return
	if size == None:
		screen.blit(pygame.font.SysFont("Arial",12).render(text,False,(0,0,0)),pos)
		return
	if font == None:
		screen.blit(pygame.font.SysFont("Arial",size).render(text,False,(0,0,0)),pos)
		return
	if color == None:
		screen.blit(pygame.font.SysFont(font,size).render(text,False,(0,0,0)),pos)
		return
	if aa == None:
		screen.blit(pygame.font.SysFont(font,size).render(text,False,color),pos)
		return
	screen.blit(pygame.font.SysFont(font,size).render(text,aa,color),pos)

pygamePrint("Hello World!",(100,100),24,"Comic Sans MS",(255,0,0),True)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		pygame.display.update()