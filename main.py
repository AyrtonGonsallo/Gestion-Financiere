import tkinter as tk
from threading import Thread
from time import sleep
from tkinter import ttk, messagebox, font
from singleton import MyClass
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import pickle

LARGEFONT = ("Verdana", 35)
singleton = MyClass()


#  pyinstaller --onefile --icon "Files/icone.ico" --noconsole main.py

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.iconbitmap("C:/Users/user/Videos/python/gestionFinanciere/wallet.ico")
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.title("Gestion Financière")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        menu_bar = tk.Menu(self)

        menu_file = tk.Menu(menu_bar, tearoff=0)

        def showA():
            self.show_frame(Accueil)

        def showP1():
            self.show_frame(Page1)

        def showP2():
            self.show_frame(Page2)

        def showP3():
            self.show_frame(Page3)

        def showParam():
            self.show_frame(Page3)

        def save():
            return 0

        menu_file.add_command(label="Bilan",
                              command=showA)
        menu_file.add_command(label="Transports",
                              command=showP1)
        menu_file.add_command(label="Nourriture", command=showP2)
        menu_file.add_command(label="Loyer", command=showP3)
        menu_file.add_command(label="Paramétrer", command=showParam)
        menu_file.add_separator()
        menu_file.add_command(label="Sauvegarder", command=save)
        menu_file.add_separator()
        menu_file.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Autres sections", menu=menu_file)
        self.config(menu=menu_bar)
        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Accueil, Page1, Page2, Page3):
            frame = F(container, self)

            # initializing frame of that object from
            # Accueil, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Accueil)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


# first window frame Accueil

class Accueil(tk.Frame):
    cache = True
    legend = True

    def update(self):
        montants = singleton.getMontants()
        total = sum(montants)

        def prop(n):
            return 360.0 * n / total

        print("mise a jour")
        print(montants)
        print(total)
        self.c.itemconfig("transport", start=prop(0),
                          extent=prop(montants[0]))
        self.c.itemconfig("loyer", start=prop(montants[0]),
                          extent=prop(montants[1]))
        self.c.itemconfig("nourriture", start=prop(montants[1] + montants[0]), extent=prop(montants[2]))
        self.c.itemconfig("facture", start=prop(montants[2] + montants[1] + montants[0]), extent=prop(montants[3]))
        self.c.itemconfig("loisirs", start=prop(montants[3] + montants[2] + montants[1] + montants[0]),
                          extent=prop(montants[4]))
        self.c.itemconfig("entretien", start=prop(montants[4] + montants[3] + montants[2] + montants[1] + montants[0]),
                          extent=prop(montants[5]))
        self.c.itemconfig("wifi",
                          start=prop(montants[5] + montants[4] + montants[3] + montants[2] + montants[1] + montants[0]),
                          extent=prop(montants[6]))
        self.c.itemconfig("autres",
                          start=prop(montants[6] + montants[5] + montants[4] + montants[3] + montants[2] + montants[1] +
                                     montants[0]), extent=prop(montants[7]))

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        label = ttk.Label(self, text="Bilan", font=LARGEFONT)
        montants = singleton.getMontants()
        total = sum(montants)
        print(total)
        label.grid(row=0, column=0, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')

        def prop(n):
            return 360.0 * n / total

        self.c = tk.Canvas(self, width=350, height=300, bg="#bbbbbb", bd=10)
        self.c.create_arc((50, 50, 300, 300), fill="#FAF402", outline="#FAF402", start=prop(0),
                          extent=prop(montants[0]), tags="transport")
        self.c.create_arc((50, 50, 300, 300), fill="#2BFFF4", outline="#2BFFF4", start=prop(montants[0]),
                          extent=prop(montants[1]), tags="loyer")
        self.c.create_arc((50, 50, 300, 300), fill="#E00022", outline="#E00022", start=prop(montants[1] + montants[0]),
                          extent=prop(montants[2]), tags="nourriture")
        self.c.create_arc((50, 50, 300, 300), fill="#7A0871", outline="#7A0871", tags="facture",
                          start=prop(montants[2] + montants[1] + montants[0]), extent=prop(montants[3]))
        self.c.create_arc((50, 50, 300, 300), fill="#294994", outline="#294994", tags="loisirs",
                          start=prop(montants[3] + montants[2] + montants[1] + montants[0]), extent=prop(montants[4]))
        self.c.create_arc((50, 50, 300, 300), fill="#7A08ff", outline="#7A08ff", tags="entretien",
                          start=prop(montants[4] + montants[3] + montants[2] + montants[1] + montants[0]),
                          extent=prop(montants[5]))
        self.c.create_arc((50, 50, 300, 300), fill="#29ff94", outline="#29ff94", tags="wifi",
                          start=prop(montants[5] + montants[4] + montants[3] + montants[2] + montants[1] + montants[0]),
                          extent=prop(montants[6]))
        self.c.create_arc((50, 50, 300, 300), fill="#ffaa00", outline="#ffaa00", tags="autres",
                          start=prop(montants[6] + montants[5] + montants[4] + montants[3] + montants[2] + montants[1] +
                                     montants[0]),
                          extent=prop(montants[7]))

        def afficher():
            if self.cache:
                self.c.grid(row=3, column=1, padx=10, pady=10)
                button4["text"] = "Cacher Diagramme"
                self.cache = False
            else:
                self.c.grid_forget()
                button4["text"] = "Afficher Diagramme"
                self.cache = True

        l = tk.Canvas(self, width=200, height=390, bg="#bbbbbb", bd=10)
        l.create_rectangle(0, 0, 40, 40, fill="#FAF402")
        l.create_text(110, 30, text="Transport", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 50, 40, 80, fill='#2BFFF4')
        l.create_text(110, 70, text="Loyer", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 100, 40, 130, fill='#E00022')
        l.create_text(110, 120, text="Nourriture", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 150, 40, 180, fill='#7A0871')
        l.create_text(110, 170, text="Factures", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 200, 40, 230, fill='#294994')
        l.create_text(110, 220, text="Loisirs", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 250, 40, 280, fill='#7A08ff')
        l.create_text(110, 270, text="Entretien", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 300, 40, 330, fill='#29ff94')
        l.create_text(110, 320, text="Wifi", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 350, 40, 380, fill='#ffaa00')
        l.create_text(110, 370, text="Autres", fill="black", font="Times 15 italic bold")

        # transport loyer nourriture facture loisirs entretien wifi autres

        def legend():
            if self.legend:
                l.grid(row=3, column=3, padx=10, pady=10)
                button5["text"] = "Cacher Légende"
                self.legend = False
            else:
                l.grid_forget()
                button5["text"] = "Afficher Légende"
                self.legend = True

        button4 = tk.Button(self, text="Afficher Diagramme", bg='#019c01', fg='#ffffff', cursor="hand1",
                            command=afficher)
        button4['font'] = myFont
        button4.grid(row=1, column=0, padx=10, pady=10)
        button5 = tk.Button(self, text="Afficher Légende", bg='#019cff', fg='#ffffff', cursor="hand1",
                            command=legend)
        button5['font'] = myFont
        button5.grid(row=2, column=0, padx=10, pady=10)

    # second window frame page1


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Transport", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        restantLabel = ttk.Label(self, text="restant")
        restantLabel.grid(row=0, column=2, padx=10, pady=10)
        depenséLabel = ttk.Label(self, text="depensé")
        depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[0]

        # prepare data
        self.data = {}
        labelx = []
        labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getTransportB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseTransport)
            depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseTransport)
            for y in range(1, singleton.ndj + 1):
                labelx.append(y)
                labely.append(self.data[y])

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(figure_canvas, toolbarFrame)
        # create axes
        axes = figure.add_subplot()

        # create the barchart
        def create():

            axes.bar(self.jours, self.montants)
            axes.set_title('Repartition Budgetaire')
            axes.set_ylabel('Montant dépensable')
            axes.set_xlabel('Jour du mois')
            axes.set_xticks(labelx)
            axes.set_yticks(labely)
            figure_canvas.draw()
            figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("budget_transport.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("budget_transport_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("transport", "données enregistrées")

        def ajouter():
            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                self.data[jour] -= int(eAutr.get())
                singleton.addDepenseTransport(int(eAutr.get()))
                self.data = singleton.getNewTransportB(self.data)
                for i in range(jour, singleton.ndj):
                    labely[i] = self.data[i]
                restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseTransport)
                depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseTransport)
                create()
                messagebox.showinfo("transport",
                                    "vous avez depensé " + eAutr.get() + " dirhams\n n'oubliez pas de sauvegarder")

            else:
                messagebox.showinfo("transport", "vous avez depassé votre limite\n quotidienne avec " + eAutr.get()+" dirhams")

        tk.Label(self, text="Montant du jour").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    selection = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Génerér MDP", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        ##code -----------------

        tk.Label(self, text="Longueur du mot de passe").grid(row=1, column=2)
        tk.Label(self, text="maximum de mots de passe").grid(row=2, column=2)
        tk.Label(self, text="type de combinaisons").grid(row=3, column=2)

        def sel():
            self.selection = str(var.get())

        var = tk.IntVar()
        R1 = tk.Radiobutton(self, text="1) Combinaison Alphanumerique", variable=var, value=1, command=sel)
        R2 = tk.Radiobutton(self, text="2) Combinaisons Numériques seules", variable=var, value=2, command=sel)
        R3 = tk.Radiobutton(self, text="3) Combinaisons de Caractère seules", variable=var, value=3, command=sel)
        R4 = tk.Radiobutton(self, text="4) Combinaisons Caractères speciaux seules", variable=var, value=4, command=sel)
        R5 = tk.Radiobutton(self, text="5) Combinaisons Caractère speciaux & nombres seules", variable=var, value=5,
                            command=sel)
        R6 = tk.Radiobutton(self, text="6) Combinaisions Alphanumeriques et Caracters speciaux", variable=var, value=6,
                            command=sel)
        R7 = tk.Radiobutton(self, text="7) Combinaisons speciales", variable=var, value=7, command=sel)
        R1.grid(row=4, column=3)
        R2.grid(row=5, column=3)
        R3.grid(row=6, column=3)
        R4.grid(row=7, column=3)
        R5.grid(row=8, column=3)
        R6.grid(row=9, column=3)
        R7.grid(row=10, column=3)
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e1.grid(row=1, column=3)
        e2.grid(row=2, column=3)
        tk.Label(self, text="Si 7) Entrez la Combinaison").grid(row=11, column=3)
        e3 = tk.Entry(self)
        e3.grid(row=11, column=4)

        def genererMDP7():
            messagebox.showinfo("Password Making", "mots de passe generes")

        def genererMDP1():
            messagebox.showinfo("Password Making", "mots de passe generes")

        def genererMDP():
            if self.selection == "7":
                thread1 = Thread(target=genererMDP7)
                thread1.start()
            else:
                thread1 = Thread(target=genererMDP1)
                thread1.start()

        button4 = tk.Button(self, text="Générer", bg='#019c01', fg='#ffffff',
                            command=genererMDP)
        myFont = font.Font(family='Helvetica', size=20, weight='bold')
        button4['font'] = myFont
        button4.grid(row=12, column=3, padx=10, pady=10)


class Page3(tk.Frame):
    res = ""

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Paramétrer la solution", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=15, weight='bold')
        # code ------------------------------------

        tk.Label(self, text="Transport", font=myFont).grid(row=1, column=0)
        etr = tk.Entry(self, width=30)
        etr.grid(row=1, column=1)
        tk.Label(self, text="Loyer", font=myFont).grid(row=2, column=0)
        eloy = tk.Entry(self, width=30)
        eloy.grid(row=2, column=1)
        tk.Label(self, text="Nourriture", font=myFont).grid(row=3, column=0)
        enou = tk.Entry(self, width=30)
        enou.grid(row=3, column=1)
        tk.Label(self, text="Factures", font=myFont).grid(row=4, column=0)
        efac = tk.Entry(self, width=30)
        efac.grid(row=4, column=1)
        tk.Label(self, text="Loisirs", font=myFont).grid(row=5, column=0)
        eloi = tk.Entry(self, width=30)
        eloi.grid(row=5, column=1)
        tk.Label(self, text="Entretien", font=myFont).grid(row=6, column=0)
        eEntr = tk.Entry(self, width=30)
        eEntr.grid(row=6, column=1)
        tk.Label(self, text="Wifi", font=myFont).grid(row=7, column=0)
        eWifi = tk.Entry(self, width=30)
        eWifi.grid(row=7, column=1)
        tk.Label(self, text="Autres", font=myFont).grid(row=8, column=0)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=8, column=1)

        def save():
            # transport loyer nourriture facture loisirs entretien autres
            singleton.addMontants(0, float(etr.get()))
            singleton.addMontants(1, float(eloy.get()))
            singleton.addMontants(2, float(enou.get()))
            singleton.addMontants(3, float(efac.get()))
            singleton.addMontants(4, float(eloi.get()))
            singleton.addMontants(5, float(eEntr.get()))
            singleton.addMontants(6, float(eWifi.get()))
            singleton.addMontants(7, float(eAutr.get()))
            messagebox.showinfo("Sauvegarde", "Configuration Enregistrée !")
            print(singleton.getMontants())
            f = open("budget.txt", "wb")
            pickle.dump(singleton.getMontants(), f)
            f.close()
            self.controller.get_page(Accueil).update()

        button5 = tk.Button(self, text="Enregistrer", bg='#0051ff', fg='#ffffff',
                            command=save)
        button5['font'] = myFont
        button5.grid(row=9, column=0, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
