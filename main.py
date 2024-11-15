import pygame
import random

pygame.init()

# Définir les couleurs
green = (0, 255, 0)
blue = (50, 153, 213)
red = (255, 0, 0)  # Couleur rouge pour le texte "PAUSED"

# Définir les dimensions de l'écran
dis_width = 400
dis_height = 400

# Créer la fenêtre
dis = pygame.display.set_mode((dis_width, dis_height))

# Horloge pour contrôler les FPS
clock = pygame.time.Clock()

# Fonction pour afficher du texte à l'écran
def message(msg, color):
    font = pygame.font.SysFont("bahnschrift", 25)
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Logique principale du jeu
def run():
    # Coordonnées initiales du serpent
    x1 = dis_width / 2
    y1 = dis_height / 2
    dir = [0, 0]
    
    # Liste pour les parties du serpent
    snake_list = []
    snake_len = 1
    
    # Position initiale de la nourriture
    foodx = 30
    foody = 30
    food_radius = 5 #cercle
    
    # Drapeau pour la pause
    game_paused = False

    # Boucle principale du jeu
    while True:
        # Traiter tous les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Fermer la fenêtre si l'utilisateur clique sur le bouton de fermeture
                quit()
            
            # Contrôler le serpent
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dir = [-10, 0]
                elif event.key == pygame.K_RIGHT:
                    dir = [10, 0]
                elif event.key == pygame.K_UP:
                    dir = [0, -10]
                elif event.key == pygame.K_DOWN:
                    dir = [0, 10]
                
                # Touche 'P' pour mettre en pause
                if event.key == pygame.K_p:
                    game_paused = not game_paused  # Alterner l'état de pause

        # Si le jeu est en pause, afficher le message et attendre
        while game_paused:
            dis.fill(blue)
            message("PAUSED", red)  # Afficher le texte "PAUSED"
            pygame.display.update()
            
            # Traiter les événements de la pause
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fermer la fenêtre si l'utilisateur clique sur le bouton de fermeture
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Appuyer sur 'P' pour reprendre
                        game_paused = False
                    if event.key == pygame.K_q:  # Appuyer sur 'Q' pour quitter le jeu
                        pygame.quit()
                        quit()

        # Mettre à jour les coordonnées du serpent
        x1 += dir[0]
        y1 += dir[1]
        
        # Remplir l'écran avec le fond
        dis.fill(blue)
        
        # Dessiner la nourriture
        pygame.draw.circle(dis, green, [foodx, foody], food_radius) #cercle

        # Ajouter la position actuelle de la tête du serpent dans la liste
        snake_list.append([x1, y1])
        
        # Si la longueur du serpent est plus grande qu'elle ne devrait être, supprimer le premier élément de la liste
        if len(snake_list) > snake_len:
            del snake_list[0]

        # Vérifier si le serpent se mord la queue
        if [x1, y1] in snake_list[:-1]:
            run()  # Si oui, recommencer le jeu

        # Vérifier si le serpent sort de l'écran
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            run()  # Si oui, recommencer le jeu

        # Dessiner tout le serpent
        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], 10, 10])

        # Vérifier si le serpent a mangé la nourriture
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - 10) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - 10) / 10.0) * 10.0
            snake_len += 1  # Augmenter la longueur du serpent

        # Mettre à jour l'écran
        pygame.display.update()

        # Contrôler les FPS (vitesse du jeu)
        clock.tick(7)

# Lancer le jeu
run()
