from tkinter import *


class LiveCellule:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class LiveModel:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.cell_size = 20
        self.vitesse = 50
        self.flag = 0
        self.couleur='white'
        self.nb_vivant = 0
        self.viking = True
        self.etat_prec = None
        self.dico_case = {}
        self.dico_etat = {}
        self.initialize_cells()

    def initialize_cells(self):
        for x in range(0, self.width, self.cell_size):
            for y in range(0, self.height, self.cell_size):
                self.dico_case[x, y] = 0
                self.dico_etat[x, y] = 0

    def somme_dico_case(self):

        self.nb_vivant = sum(self.dico_case.values())
        return self.nb_vivant


class LiveView:
    def __init__(self, master, live_model, lives_controller):
        self.master = master
        self.live_model = live_model
        self.live_controller = lives_controller

        self.live_commande_bar = LiveCommandeBar(self.live_controller)

    def commande_bar(self):
        self.live_commande_bar = LiveCommandeBar(self.live_controller)


class LiveCanvas:
    def __init__(self, master, live_model):
        self.master = master
        self.live_model = live_model
        self.can1 = Canvas(self.master, width=self.live_model.width, height=self.live_model.height, bg=self.live_model.couleur)
        self.can1.bind("<Button-1>", self.click_gauche)
        self.can1.bind("<Button-3>", self.click_droit)
        self.can1.pack(side=TOP, padx=20, pady=20)
        self.damier()

    def damier(self):
        c_x = 0
        while c_x != self.live_model.width:
            self.can1.create_line(c_x, 0, c_x, self.live_model.height, width=1, fill='black')
            c_x += self.live_model.cell_size

        c_y = 0
        while c_y != self.live_model.height:
            self.can1.create_line(0, c_y, self.live_model.width, c_y, width=1, fill='black')
            c_y += self.live_model.cell_size

    def click_gauche(self, event):
        x = event.x - (event.x % self.live_model.cell_size)
        y = event.y - (event.y % self.live_model.cell_size)
        self.can1.create_rectangle(x, y, x + self.live_model.cell_size, y + self.live_model.cell_size, fill='black')
        self.live_model.dico_case[x, y] = 1

    def click_droit(self, event):
        x = event.x - (event.x % self.live_model.cell_size)
        y = event.y - (event.y % self.live_model.cell_size)
        self.can1.create_rectangle(x, y, x + self.live_model.cell_size, y + self.live_model.cell_size, fill=self.live_model.couleur)
        self.live_model.dico_case[x, y] = 0


class LiveCommandeBar:
    def __init__(self, live_controller):
        self.live_controller = live_controller

        self.b9 = Button(self.live_controller.master, text='Viking', command=self.live_controller.action_viking)
        self.b9.pack(side=RIGHT, padx=3, pady=3)

        self.b10     = Button(self.live_controller.master, text='Normal', command=self.live_controller.mode_normal)
        self.b10.pack(side=RIGHT, padx=3, pady=3)

        self.somme_label = Label(self.live_controller.master, text="champs vivant: 0")
        self.somme_label.pack(side=LEFT)

        # self.b1 = Button(self.live_controller.master, text='Go!', command=self.live_controller.go)
        self.b2 = Button(self.live_controller.master, text='Stop', command=self.live_controller.stop)
        # self.b1.pack(side=LEFT, padx=3, pady=3)
        self.b2.pack(side=LEFT, padx=3, pady=3)

        self.chaine5 = Label(self.live_controller.master)
        self.chaine5.configure(text="canon")
        self.chaine5.pack(side=LEFT)



        self.b6 = Button(self.live_controller.master, text='1', command=self.live_controller.canon1)
        self.b6.pack(side=LEFT, padx=3, pady=3)

        self.b7 = Button(self.live_controller.master, text='2', command=self.live_controller.canon2)
        self.b7.pack(side=LEFT, padx=3, pady=3)

        self.b8 = Button(self.live_controller.master, text='3', command=self.live_controller.canon3)
        self.b8.pack(side=LEFT, padx=3, pady=3)

        self.b5 = Button(self.live_controller.master, text='appliquer', command=self.action_sur_vit)
        self.b5.pack(side=RIGHT, padx=3, pady=3)

        self.entree = Entry(self.live_controller.master)

        self.entree.bind("<Return>", self.live_controller.change_vit)
        self.entree.pack(side=RIGHT)
        self.chaine = Label(self.live_controller.master)
        self.chaine = Label(self.live_controller.master)
        self.chaine.configure(text="VITESSE ")
        self.chaine.pack(side=RIGHT)

        self.b4 = Button(self.live_controller.master, text='appliquer', command=self.action_sur_entrees)
        self.b4.pack(side=RIGHT, padx=3, pady=3)


        self.entree1 = Entry(self.live_controller.master)
        self.entree1.bind("<Return>", self.live_controller.change_width)
        self.entree1.pack(side=RIGHT)
        self.chaine1 = Label(self.live_controller.master)
        self.chaine1.configure(text="LARGEUR")
        self.chaine1.pack(side=RIGHT)

        self.entree2 = Entry(self.live_controller.master)
        self.entree2.bind("<Return>", self.live_controller.change_height)
        self.entree2.pack(side=RIGHT)
        self.chaine2 = Label(self.live_controller.master)
        self.chaine2.configure(text="HAUTEUR")
        self.chaine2.pack(side=RIGHT)
        # self.entree3 = Entry(self.live_controller.master)
        # self.entree3.bind("<Return>", self.live_controller.change_cell_size)
        # self.entree3.pack(side=RIGHT)

        self.b_reset = Button(self.live_controller.master, text='Réinitialiser', command=self.live_controller.reset_cells)
        self.b_reset.pack(side=LEFT, padx=3, pady=3)

        self.b_green = Button(self.live_controller.master,bg="green", command=self.live_controller.change_couleur_green)
        self.b_green.pack(side=LEFT, padx=3, pady=3)

        self.b_white = Button(self.live_controller.master, bg="white", command=self.live_controller.change_couleur_white)
        self.b_white.pack(side=LEFT, padx=3, pady=3)

        self.b_yellow = Button(self.live_controller.master,bg="coral",command=self.live_controller.change_couleur_yellow)
        self.b_yellow.pack(side=LEFT, padx=3, pady=3)



    def action_sur_vit(self):
        valeur = self.entree.get()
        self.live_controller.change_vit(valeur)
    def action_sur_entrees(self):
        # Récupérer les valeurs des trois champs de saisie
        valeur1 = self.entree1.get()
        valeur2 = self.entree2.get()


        self.live_controller.change_width(valeur1)
        self.live_controller.change_height(valeur2)

    def destroy(self):
        self.entree.destroy()
        self.entree1.destroy()
        self.entree2.destroy()
        self.somme_label.destroy()
        # self.b1.destroy()
        self.b2.destroy()
        # self.b3.destroy()
        self.b4.destroy()
        self.b5.destroy()
        self.b6.destroy()
        self.b7.destroy()
        self.b8.destroy()
        self.b9.destroy()
        self.b10.destroy()
        self.chaine.destroy()
        self.chaine1.destroy()
        self.chaine2.destroy()
        self.chaine5.destroy()
        self.b_reset.destroy()
        self.b_green.destroy()
        self.b_white.destroy()
        self.b_yellow.destroy()


class LiveController:
    def __init__(self, master):

        self.master = master
        self.live_model = LiveModel()
        self.live_canvas = LiveCanvas(self.master, self.live_model)

        self.live_view = LiveView(self.master, self.live_model, self)

    def go(self):
        if self.live_model.flag == 0:
            self.live_model.flag = 1

            self.play()

    def action_viking(self):

        self.live_model.couleur="purple"
        self.live_model.viking = True
        self.go()

    def mode_normal(self):

        self.live_model.couleur="coral"
        self.live_model.viking = False
        self.go()

    def stop(self):
        self.live_model.flag = 0

    def change_width(self, new_width):

        new_width = int(new_width)
        if new_width > 0:
            self.live_model.width = new_width
            print(self.live_model.width)



    def change_height(self, new_height):

        new_height = int(new_height)
        if new_height > 0:
            self.live_model.height = new_height
            print(self.live_model.height)
            self.live_canvas.can1.destroy()
            self.live_view.live_commande_bar.destroy()
            self.live_canvas = LiveCanvas(self.master, self.live_model)
            self.live_view = LiveView(self.master, self.live_model, self)




    def change_vit(self, new_vit):
        self.live_model.vitesse = new_vit
        print(self.live_model.vitesse)

    def reset_cells(self):
        self.live_model.initialize_cells()
        self.live_model.vitesse = 50
        self.redessiner()
        self.stop()

    def change_couleur_white(self):
        self.live_model.couleur='white'

        self.redessiner()


    def change_couleur_green(self):
        self.live_model.couleur='green'

        self.redessiner()



    def change_couleur_yellow(self):
        self.live_model.couleur='coral'

        self.redessiner()


    def play(self):
        v = 0
        while v != self.live_model.width / self.live_model.cell_size:
            w = 0
            while w != self.live_model.height / self.live_model.cell_size:

                x = v * self.live_model.cell_size
                y = w * self.live_model.cell_size

                # cas spéciaux...
                if x == 0 and y == 0:
                    compt_viv = 0
                    if self.live_model.dico_case.get((x, y + self.live_model.cell_size),0) == 1:
                        compt_viv += 1
                    if self.live_model.dico_case.get((x + self.live_model.cell_size, y), 0) == 1:
                        compt_viv += 1
                    if self.live_model.dico_case.get((x + self.live_model.cell_size, y + self.live_model.cell_size),
                                                     0) == 1:
                        compt_viv += 1
                    self.live_model.dico_etat[x, y] = compt_viv

                else:
                    # cas généraux...
                    compt_viv = 0
                    if self.live_model.dico_case.get((x - self.live_model.cell_size, y - self.live_model.cell_size),
                                                     0) == 1:
                        compt_viv += 1
                    if self.live_model.dico_case.get((x - self.live_model.cell_size, y), 0) == 1:
                        compt_viv += 1
                    if self.live_model.dico_case.get((x - self.live_model.cell_size, y + self.live_model.cell_size),
                                                     0) == 1:
                        compt_viv += 1
                    if self.live_model.dico_case.get((x, y - self.live_model.cell_size), 0) == 1:
                        compt_viv += 1
                    if self.live_model.dico_case.get((x, y + self.live_model.cell_size), 0) == 1:
                        compt_viv += 1
                    if self.live_model.dico_case.get((x + self.live_model.cell_size, y - self.live_model.cell_size),
                                                     0) == 1:
                        compt_viv += 1
                    if self.live_model.dico_case.get((x + self.live_model.cell_size, y), 0) == 1:
                        compt_viv += 1
                    if self.live_model.dico_case.get((x + self.live_model.cell_size, y + self.live_model.cell_size),
                                                     0) == 1:
                        compt_viv += 1
                    self.live_model.dico_etat[x, y] = compt_viv




                w += 1
            v += 1

        if self.live_model.dico_case == self.live_model.etat_prec:
            self.stop()  # Si le jeu est devenu stable

        self.live_model.etat_prec = dict(self.live_model.dico_case)  # Mettez à jour l'état précédent

        if not self.live_model.viking:
            self.redessiner()
        else:

            self.redessiner_viking()
        if self.live_model.flag > 0:
            self.master.after(self.live_model.vitesse, self.play)


    def redessiner(self):
        self.live_canvas.can1.delete("all")

        self.live_view.live_commande_bar.somme_label.configure(
            text="champs vivant: {}".format(self.live_model.somme_dico_case()))
        t = 0
        while t != self.live_model.width / self.live_model.cell_size:
            u = 0
            while u != self.live_model.height / self.live_model.cell_size:
                x = t * self.live_model.cell_size
                y = u * self.live_model.cell_size
                if self.live_model.dico_etat.get((x, y), 0) == 3:
                    self.live_model.dico_case[x, y] = 1
                    self.live_canvas.can1.create_rectangle(x, y, x + self.live_model.cell_size,
                                                           y + self.live_model.cell_size, fill='black')

                elif self.live_model.dico_etat.get((x, y), 0) == 2:
                    if self.live_model.dico_case.get((x, y), 0) == 1:
                        self.live_canvas.can1.create_rectangle(x, y, x + self.live_model.cell_size,
                                                               y + self.live_model.cell_size, fill='black')

                    else:
                        self.live_canvas.can1.create_rectangle(x, y, x + self.live_model.cell_size,
                                                               y + self.live_model.cell_size, fill=self.live_model.couleur)

                elif self.live_model.dico_etat.get((x, y), 0) < 2 or self.live_model.dico_etat.get((x, y), 0) > 3:
                    self.live_model.dico_case[x, y] = 0
                    self.live_canvas.can1.create_rectangle(x, y, x + self.live_model.cell_size,
                                                           y + self.live_model.cell_size, fill=self.live_model.couleur)

                u += 1
            t += 1

    def redessiner_viking(self):
        self.live_canvas.can1.delete("all")

        self.live_view.live_commande_bar.somme_label.configure(
            text="champs vivant: {}".format(self.live_model.somme_dico_case()))
        t = 0
        while t != self.live_model.width / self.live_model.cell_size:
            u = 0
            while u != self.live_model.height / self.live_model.cell_size:
                x = t * self.live_model.cell_size
                y = u * self.live_model.cell_size
                if self.live_model.dico_etat.get((x, y), 0) == 3 or self.live_model.dico_etat.get((x, y), 0) == 4:
                    self.live_model.dico_case[x, y] = 1
                    self.live_canvas.can1.create_rectangle(x, y, x + self.live_model.cell_size,
                                                           y + self.live_model.cell_size, fill='black')

                elif self.live_model.dico_etat.get((x, y), 0) == 2 or self.live_model.dico_etat.get((x, y), 0) == 1:
                    if self.live_model.dico_case.get((x, y), 0) == 1:
                        self.live_canvas.can1.create_rectangle(x, y, x + self.live_model.cell_size,
                                                               y + self.live_model.cell_size, fill='black')

                    else:
                        self.live_canvas.can1.create_rectangle(x, y, x + self.live_model.cell_size,
                                                               y + self.live_model.cell_size,
                                                               fill=self.live_model.couleur)

                elif self.live_model.dico_etat.get((x, y), 0) == 0 or self.live_model.dico_etat.get((x, y), 0) > 4:
                    self.live_model.dico_case[x, y] = 0
                    self.live_canvas.can1.create_rectangle(x, y, x + self.live_model.cell_size,
                                                           y + self.live_model.cell_size, fill=self.live_model.couleur)

                u += 1
            t += 1

    def canon1(self):
        c = self.live_model.cell_size
        self.live_model.vitesse=200
        # Clear the existing cells
        self.live_model.initialize_cells()

        # Add Pulsar pattern
        pulsar_positions = [
            (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
            (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
            (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
            (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12),
            (4, 2), (5, 2), (6, 2), (10, 2), (11, 2), (12, 2),
            (4, 7), (5, 7), (6, 7), (10, 7), (11, 7), (12, 7),
            (4, 9), (5, 9), (6, 9), (10, 9), (11, 9), (12, 9),
            (4, 14), (5, 14), (6, 14), (10, 14), (11, 14), (12, 14)
        ]

        for pos in pulsar_positions:
            self.live_model.dico_case[pos[0] * c, pos[1] * c] = 1

        self.go()


    def canon3(self):
        c = self.live_model.cell_size
        self.live_model.vitesse = 200
        # Clear the existing cells
        self.live_model.initialize_cells()

        # Add Glider pattern
        glider_positions = [
            (1, 2), (2, 3), (3, 1), (3, 2), (3, 3)
        ]

        for pos in glider_positions:
            self.live_model.dico_case[pos[0] * c, pos[1] * c] = 1

        self.go()

    def canon2(self):  # fonction dessinant le célèbre canon à planeur de Bill Gosper
        c=self.live_model.cell_size
        self.live_model.vitesse = 200
        self.live_model.initialize_cells()
        dico_case=self.live_model.dico_case
        dico_case[0 * c, 5 * c] = 1
        dico_case[0 * c, 6 * c] = 1
        dico_case[1 * c, 5 * c] = 1
        dico_case[1 * c, 6 * c] = 1
        dico_case[10 * c, 5 * c] = 1
        dico_case[10 * c, 6 * c] = 1
        dico_case[10 * c, 7 * c] = 1
        dico_case[11 * c, 4 * c] = 1
        dico_case[11 * c, 8 * c] = 1
        dico_case[12 * c, 3 * c] = 1
        dico_case[12 * c, 9 * c] = 1
        dico_case[13 * c, 3 * c] = 1
        dico_case[13 * c, 9 * c] = 1
        dico_case[14 * c, 6 * c] = 1
        dico_case[15 * c, 4 * c] = 1
        dico_case[15 * c, 8 * c] = 1
        dico_case[16 * c, 5 * c] = 1
        dico_case[16 * c, 6 * c] = 1
        dico_case[16 * c, 7 * c] = 1
        dico_case[17 * c, 6 * c] = 1
        dico_case[20 * c, 3 * c] = 1
        dico_case[20 * c, 4 * c] = 1
        dico_case[20 * c, 5 * c] = 1
        dico_case[21 * c, 3 * c] = 1
        dico_case[21 * c, 4 * c] = 1
        dico_case[21 * c, 5 * c] = 1
        dico_case[22 * c, 2 * c] = 1
        dico_case[22 * c, 6 * c] = 1
        dico_case[24 * c, 1 * c] = 1
        dico_case[24 * c, 2 * c] = 1
        dico_case[24 * c, 6 * c] = 1
        dico_case[24 * c, 7 * c] = 1
        dico_case[34 * c, 3 * c] = 1
        dico_case[34 * c, 4 * c] = 1
        dico_case[35 * c, 3 * c] = 1
        dico_case[35 * c, 4 * c] = 1
        self.go()


if __name__ == "__main__":
    fen1 = Tk()
    live_controller = LiveController(fen1)

    fen1.mainloop()
