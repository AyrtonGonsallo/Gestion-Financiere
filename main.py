import tkinter as tk
from threading import Thread
from time import sleep
from tkinter import ttk, messagebox, font
from tkinter.messagebox import askyesno

from singleton import MyClass
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import pickle

LARGEFONT = ("Verdana", 35)
singleton = MyClass()


#  pyinstaller --onefile --icon "wallet.ico" --noconsole main.py

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
            self.show_frame(Bilan)

        def showP1():
            self.show_frame(Transport)

        def showP2():
            self.show_frame(Nourriture)

        def showP3():
            self.show_frame(Loyer)

        def showP4():
            self.show_frame(Facture)

        def showP5():
            self.show_frame(Loisirs)

        def showP6():
            self.show_frame(Entretien)

        def showP7():
            self.show_frame(Wifi)

        def showP8():
            self.show_frame(Salle)

        def showP9():
            self.show_frame(Caprices)

        def showP10():
            self.show_frame(Autres)

        def showParam():
            self.show_frame(Parametres)

        def showParamRep():
            self.show_frame(ParametresRepartition)

        def save():
            return 0

        menu_file.add_command(label="Bilan",
                              command=showA)
        menu_file.add_command(label="Transports",
                              command=showP1)
        menu_file.add_command(label="Loyer", command=showP3)
        menu_file.add_command(label="Nourriture", command=showP2)
        menu_file.add_command(label="Facture", command=showP4)
        menu_file.add_command(label="Loisirs", command=showP5)
        menu_file.add_command(label="Entretien", command=showP6)
        menu_file.add_command(label="Wifi", command=showP7)
        menu_file.add_command(label="Salle de sport", command=showP8)
        menu_file.add_command(label="Caprices", command=showP9)
        menu_file.add_command(label="Autres", command=showP10)
        menu_file.add_command(label="Paramétrer", command=showParam)
        menu_file.add_separator()
        menu_file.add_command(label="Paramétrer Une Répartition", command=showParamRep)
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
        for F in (
                Bilan, Transport, Nourriture, Loyer, Parametres, Facture, Loisirs, Entretien, Wifi, Salle, Caprices,
                Autres,
                ParametresRepartition):
            frame = F(container, self)

            # initializing frame of that object from
            # Bilan, Transport, Nourriture respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Bilan)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


# first window frame Bilan

class Bilan(tk.Frame):
    cache = True
    legend = True

    def update(self):
        montants = singleton.getMontants()
        total = sum(montants)

        def prop(n):
            return 360.0 * n / total

        
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
        self.c.itemconfig("salle",
                          start=prop(montants[6] + montants[5] + montants[4] + montants[3] + montants[2] + montants[1] +
                                     montants[0]), extent=prop(montants[7]))
        self.c.itemconfig("caprices",
                          start=prop(montants[7] + montants[6] + montants[5] + montants[4] + montants[3] + montants[2] +
                                     montants[1] +
                                     montants[0]), extent=prop(montants[8]))
        self.c.itemconfig("autres",
                          start=prop(montants[8] + montants[7] + montants[6] + montants[5] + montants[4] + montants[3] +
                                     montants[2] + montants[1] +
                                     montants[0]), extent=prop(montants[9]))

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        label = ttk.Label(self, text="Bilan", font=LARGEFONT)
        montants = singleton.getMontants()
        total = sum(montants)
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
        self.c.create_arc((50, 50, 300, 300), fill="#0c9769", outline="#0c9769", tags="salle",
                          start=prop(montants[6] + montants[5] + montants[4] + montants[3] + montants[2] + montants[1] +
                                     montants[0]),
                          extent=prop(montants[7]))
        self.c.create_arc((50, 50, 300, 300), fill="#ff0fc3", outline="#ff0fc3", tags="caprices",
                          start=prop(montants[7] + montants[6] + montants[5] + montants[4] + montants[3] + montants[2] +
                                     montants[1] + montants[0]),
                          extent=prop(montants[8]))
        self.c.create_arc((50, 50, 300, 300), fill="#ffaa00", outline="#ffaa00", tags="autres",
                          start=prop(montants[8] + montants[7] + montants[6] + montants[5] + montants[4] + montants[3] +
                                     montants[2] + montants[1] +
                                     montants[0]),
                          extent=prop(montants[9]))

        def afficher():
            if self.cache:
                self.c.grid(row=3, column=1, padx=10, pady=10)
                button4["text"] = "Cacher Diagramme"
                self.cache = False
            else:
                self.c.grid_forget()
                button4["text"] = "Afficher Diagramme"
                self.cache = True

        l = tk.Canvas(self, width=300, height=300, bg="#bbbbbb", bd=10)
        l.create_rectangle(0, 0, 30, 30, fill="#FAF402")
        l.create_text(110, 20, text="Transport", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 40, 30, 60, fill='#2BFFF4')
        l.create_text(110, 50, text="Loyer", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 70, 30, 90, fill='#E00022')
        l.create_text(110, 80, text="Nourriture", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 100, 30, 120, fill='#7A0871')
        l.create_text(110, 110, text="Factures", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 130, 30, 150, fill='#294994')
        l.create_text(110, 140, text="Loisirs", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 160, 30, 180, fill='#7A08ff')
        l.create_text(110, 170, text="Entretien", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 190, 30, 210, fill='#29ff94')
        l.create_text(110, 200, text="Wifi", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 220, 30, 240, fill='#0c9769')
        l.create_text(110, 230, text="Salle de sport", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 250, 30, 270, fill='#ff0fc3')
        l.create_text(160, 260, text="Caprices et coups de tete", fill="black", font="Times 15 italic bold")
        l.create_rectangle(0, 280, 30, 300, fill='#ffaa00')
        l.create_text(110, 290, text="Autres", fill="black", font="Times 15 italic bold")

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

    # second window frame Transport


class Transport(tk.Frame):
    def update(self):
        self.axes.bar(self.jours, self.montants)
        self.axes.set_title('Repartition Budgetaire')
        self.axes.set_ylabel('Montant dépensable')
        self.axes.set_xlabel('Jour du mois')
        self.axes.set_xticks(self.labelx)
        self.axes.set_yticks(self.labely)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[0] - singleton.depenseTransport)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseTransport)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Transport", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        self.restantLabel = ttk.Label(self, text="restant")
        self.restantLabel.grid(row=0, column=2, padx=10, pady=10)
        self.depenséLabel = ttk.Label(self, text="depensé")
        self.depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[0] - singleton.depenseTransport)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseTransport)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[0]

        # prepare data
        self.data = {}
        self.labelx = []
        self.labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getTransportB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseTransport)
            self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseTransport)
            for y in range(1, singleton.ndj + 1):
                self.labelx.append(y)
                self.labely.append(self.data[y])
            self.labely.append(0)

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        # create self.axes
        self.axes = figure.add_subplot()
        figure.set_facecolor((0.95, 0.95, 0.95))
        self.axes.set_facecolor((0.95, 0.95, 0.95))

        # create the barchart
        def create():

            self.axes.bar(self.jours, self.montants)
            self.axes.set_title('Repartition Budgetaire')
            self.axes.set_ylabel('Montant dépensable')
            self.axes.set_xlabel('Jour du mois')
            self.axes.set_xticks(self.labelx)
            self.axes.set_yticks(self.labely)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_transport.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_transport_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("transport", "données enregistrées")

        def ajouter():
            def depense(normal, montantdep):
                self.data[jour] -= montantdep
                singleton.addDepenseTransport(montantdep)
                self.data = singleton.getNewTransportB(self.data, normal)
                for i in range(jour, singleton.ndj):
                    self.labely[i] = self.data[i]
                self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseTransport)
                self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseTransport)
                create()
                messagebox.showinfo("transport",
                                    "vous avez depensé " + str(montantdep) + " dirhams\n n'oubliez pas de sauvegarder")

            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                depense(True, int(eAutr.get()))
            else:
                answer = askyesno(title='confirmation',
                                  message="vous avez depassé votre limite quotidienne \n et ne pouvez plus vous permettre de depenser " + eAutr.get() + " dirhams\n Dépenser quand même ?")
                if answer:
                    montantdep = int(eAutr.get())
                    depensable = self.data[jour]
                    depense(True, depensable)
                    reste = montantdep - depensable
                    answer = askyesno(title='confirmation',
                                      message="Il faudra depenser encore  " + str(
                                          reste) + " dirhams\n Vous aurez un solde négatif qui se repercutera les jours suivants\n Dépenser quand même ?")
                    if answer:
                        depense(False, reste)

        tk.Label(self, text="Montant du jour(" + singleton.jourComplet + ")").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


class Loyer(tk.Frame):
    def update(self):
        self.axes.bar(self.jours, self.montants)
        self.axes.set_title('Repartition Budgetaire')
        self.axes.set_ylabel('Montant dépensable')
        self.axes.set_xlabel('Jour du mois')
        self.axes.set_xticks(self.labelx)
        self.axes.set_yticks(self.labely)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[1] - singleton.depenseLoyer)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseLoyer)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Loyer", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        self.restantLabel = ttk.Label(self, text="restant")
        self.restantLabel.grid(row=0, column=2, padx=10, pady=10)
        self.depenséLabel = ttk.Label(self, text="depensé")
        self.depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[1]

        # prepare data
        self.data = {}
        self.labelx = []
        self.labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getLoyerB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseLoyer)
            self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseLoyer)
            for y in range(1, singleton.ndj + 1):
                self.labelx.append(y)
                self.labely.append(self.data[y])
            self.labely.append(0)

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        # create self.axes
        self.axes = figure.add_subplot()
        figure.set_facecolor((0.95, 0.95, 0.95))
        self.axes.set_facecolor((0.95, 0.95, 0.95))

        # create the barchart
        def create():

            self.axes.bar(self.jours, self.montants)
            self.axes.set_title('Repartition Budgetaire')
            self.axes.set_ylabel('Montant dépensable')
            self.axes.set_xlabel('Jour du mois')
            self.axes.set_xticks(self.labelx)
            self.axes.set_yticks(self.labely)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_loyer.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_loyer_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("Loyer", "données enregistrées")

        def ajouter():
            def depense(normal, montantdep):
                self.data[jour] -= montantdep
                singleton.addDepenseLoyer(montantdep)
                self.data = singleton.getNewLoyerB(self.data, normal)
                for i in range(jour, singleton.ndj):
                    self.labely[i] = self.data[i]
                self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseLoyer)
                self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseLoyer)
                create()
                messagebox.showinfo("Loyer",
                                    "vous avez depensé " + str(montantdep) + " dirhams\n n'oubliez pas de sauvegarder")

            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                depense(True, int(eAutr.get()))
            else:
                answer = askyesno(title='confirmation',
                                  message="vous avez depassé votre limite quotidienne \n et ne pouvez plus vous permettre de depenser " + eAutr.get() + " dirhams\n Dépenser quand même ?")
                if answer:
                    montantdep = int(eAutr.get())
                    depensable = self.data[jour]
                    depense(True, depensable)
                    reste = montantdep - depensable
                    answer = askyesno(title='confirmation',
                                      message="Il faudra depenser encore  " + str(
                                          reste) + " dirhams\n Vous aurez un solde négatif qui se repercutera les jours suivants\n Dépenser quand même ?")
                    if answer:
                        depense(False, reste)

        tk.Label(self, text="Montant du jour(" + singleton.jourComplet + ")").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


# third window frame Nourriture
class Nourriture(tk.Frame):
    def update(self):
        self.axes.bar(self.jours, self.montants)
        self.axes.set_title('Repartition Budgetaire')
        self.axes.set_ylabel('Montant dépensable')
        self.axes.set_xlabel('Jour du mois')
        self.axes.set_xticks(self.labelx)
        self.axes.set_yticks(self.labely)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[2] - singleton.depenseNourriture)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseNourriture)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Nourriture", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        self.restantLabel = ttk.Label(self, text="restant")
        self.restantLabel.grid(row=0, column=2, padx=10, pady=10)
        self.depenséLabel = ttk.Label(self, text="depensé")
        self.depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[2]

        # prepare data
        self.data = {}
        self.labelx = []
        self.labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getNourritureB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseNourriture)
            self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseNourriture)
            for y in range(1, singleton.ndj + 1):
                self.labelx.append(y)
                self.labely.append(self.data[y])
            self.labely.append(0)

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        # create self.axes
        self.axes = figure.add_subplot()
        figure.set_facecolor((0.95, 0.95, 0.95))
        self.axes.set_facecolor((0.95, 0.95, 0.95))

        # create the barchart
        def create():

            self.axes.bar(self.jours, self.montants)
            self.axes.set_title('Repartition Budgetaire')
            self.axes.set_ylabel('Montant dépensable')
            self.axes.set_xlabel('Jour du mois')
            self.axes.set_xticks(self.labelx)
            self.axes.set_yticks(self.labely)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_nourriture.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_nourriture_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("nourriture", "données enregistrées")

        def ajouter():
            def depense(normal, montantdep):
                self.data[jour] -= montantdep
                singleton.addDepenseNourriture(montantdep)
                self.data = singleton.getNewNourritureB(self.data, normal)
                for i in range(jour, singleton.ndj):
                    self.labely[i] = self.data[i]
                self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseNourriture)
                self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseNourriture)
                create()
                messagebox.showinfo("nourriture",
                                    "vous avez depensé " + str(montantdep) + " dirhams\n n'oubliez pas de sauvegarder")

            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                depense(True, int(eAutr.get()))
            else:
                answer = askyesno(title='confirmation',
                                  message="vous avez depassé votre limite quotidienne \n et ne pouvez plus vous permettre de depenser " + eAutr.get() + " dirhams\n Dépenser quand même ?")
                if answer:
                    montantdep = int(eAutr.get())
                    depensable = self.data[jour]
                    depense(True, depensable)
                    reste = montantdep - depensable
                    answer = askyesno(title='confirmation',
                                      message="Il faudra depenser encore  " + str(
                                          reste) + " dirhams\n Vous aurez un solde négatif qui se repercutera les jours suivants\n Dépenser quand même ?")
                    if answer:
                        depense(False, reste)

        tk.Label(self, text="Montant du jour(" + singleton.jourComplet + ")").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


class Facture(tk.Frame):
    def update(self):
        self.axes.bar(self.jours, self.montants)
        self.axes.set_title('Repartition Budgetaire')
        self.axes.set_ylabel('Montant dépensable')
        self.axes.set_xlabel('Jour du mois')
        self.axes.set_xticks(self.labelx)
        self.axes.set_yticks(self.labely)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[3] - singleton.depenseFactures)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseFactures)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Factures", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        self.restantLabel = ttk.Label(self, text="restant")
        self.restantLabel.grid(row=0, column=2, padx=10, pady=10)
        self.depenséLabel = ttk.Label(self, text="depensé")
        self.depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[3]

        # prepare data
        self.data = {}
        self.labelx = []
        self.labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getFacturesB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseFactures)
            self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseFactures)
            for y in range(1, singleton.ndj + 1):
                self.labelx.append(y)
                self.labely.append(self.data[y])
            self.labely.append(0)

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        # create self.axes
        self.axes = figure.add_subplot()
        figure.set_facecolor((0.95, 0.95, 0.95))
        self.axes.set_facecolor((0.95, 0.95, 0.95))

        # create the barchart
        def create():

            self.axes.bar(self.jours, self.montants)
            self.axes.set_title('Repartition Budgetaire')
            self.axes.set_ylabel('Montant dépensable')
            self.axes.set_xlabel('Jour du mois')
            self.axes.set_xticks(self.labelx)
            self.axes.set_yticks(self.labely)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_factures.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_factures_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("Factures", "données enregistrées")

        def ajouter():
            def depense(normal, montantdep):
                self.data[jour] -= montantdep
                singleton.addDepenseFactures(montantdep)
                self.data = singleton.getNewFacturesB(self.data, normal)
                for i in range(jour, singleton.ndj):
                    self.labely[i] = self.data[i]
                self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseFactures)
                self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseFactures)
                create()
                messagebox.showinfo("Factures",
                                    "vous avez depensé " + str(montantdep) + " dirhams\n n'oubliez pas de sauvegarder")

            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                depense(True, int(eAutr.get()))
            else:
                answer = askyesno(title='confirmation',
                                  message="vous avez depassé votre limite quotidienne \n et ne pouvez plus vous permettre de depenser " + eAutr.get() + " dirhams\n Dépenser quand même ?")
                if answer:
                    montantdep = int(eAutr.get())
                    depensable = self.data[jour]
                    depense(True, depensable)
                    reste = montantdep - depensable
                    answer = askyesno(title='confirmation',
                                      message="Il faudra depenser encore  " + str(
                                          reste) + " dirhams\n Vous aurez un solde négatif qui se repercutera les jours suivants\n Dépenser quand même ?")
                    if answer:
                        depense(False, reste)

        tk.Label(self, text="Montant du jour(" + singleton.jourComplet + ")").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


class Loisirs(tk.Frame):
    def update(self):
        self.axes.bar(self.jours, self.montants)
        self.axes.set_title('Repartition Budgetaire')
        self.axes.set_ylabel('Montant dépensable')
        self.axes.set_xlabel('Jour du mois')
        self.axes.set_xticks(self.labelx)
        self.axes.set_yticks(self.labely)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[4] - singleton.depenseLoisirs)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseLoisirs)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Loisirs", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        self.restantLabel = ttk.Label(self, text="restant")
        self.restantLabel.grid(row=0, column=2, padx=10, pady=10)
        self.depenséLabel = ttk.Label(self, text="depensé")
        self.depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[4]

        # prepare data
        self.data = {}
        self.labelx = []
        self.labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getLoisirsB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseLoisirs)
            self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseLoisirs)
            for y in range(1, singleton.ndj + 1):
                self.labelx.append(y)
                self.labely.append(self.data[y])
            self.labely.append(0)

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        # create self.axes
        self.axes = figure.add_subplot()
        figure.set_facecolor((0.95, 0.95, 0.95))
        self.axes.set_facecolor((0.95, 0.95, 0.95))

        # create the barchart
        def create():

            self.axes.bar(self.jours, self.montants)
            self.axes.set_title('Repartition Budgetaire')
            self.axes.set_ylabel('Montant dépensable')
            self.axes.set_xlabel('Jour du mois')
            self.axes.set_xticks(self.labelx)
            self.axes.set_yticks(self.labely)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_loisirs.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_loisirs_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("Loisirs", "données enregistrées")

        def ajouter():
            def depense(normal, montantdep):
                self.data[jour] -= montantdep
                singleton.addDepenseLoisirs(montantdep)
                self.data = singleton.getNewLoisirsB(self.data, normal)
                for i in range(jour, singleton.ndj):
                    self.labely[i] = self.data[i]
                self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseLoisirs)
                self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseLoisirs)
                create()
                messagebox.showinfo("Loisirs",
                                    "vous avez depensé " + str(montantdep) + " dirhams\n n'oubliez pas de sauvegarder")

            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                depense(True, int(eAutr.get()))
            else:
                answer = askyesno(title='confirmation',
                                  message="vous avez depassé votre limite quotidienne \n et ne pouvez plus vous permettre de depenser " + eAutr.get() + " dirhams\n Dépenser quand même ?")
                if answer:
                    montantdep = int(eAutr.get())
                    depensable = self.data[jour]
                    depense(True, depensable)
                    reste = montantdep - depensable
                    answer = askyesno(title='confirmation',
                                      message="Il faudra depenser encore  " + str(
                                          reste) + " dirhams\n Vous aurez un solde négatif qui se repercutera les jours suivants\n Dépenser quand même ?")
                    if answer:
                        depense(False, reste)

        tk.Label(self, text="Montant du jour(" + singleton.jourComplet + ")").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


class Entretien(tk.Frame):
    def update(self):
        self.axes.bar(self.jours, self.montants)
        self.axes.set_title('Repartition Budgetaire')
        self.axes.set_ylabel('Montant dépensable')
        self.axes.set_xlabel('Jour du mois')
        self.axes.set_xticks(self.labelx)
        self.axes.set_yticks(self.labely)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[5] - singleton.depenseEntretien)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseEntretien)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Entretien", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        self.restantLabel = ttk.Label(self, text="restant")
        self.restantLabel.grid(row=0, column=2, padx=10, pady=10)
        self.depenséLabel = ttk.Label(self, text="depensé")
        self.depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[5]

        # prepare data
        self.data = {}
        self.labelx = []
        self.labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getEntretienB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseEntretien)
            self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseEntretien)
            for y in range(1, singleton.ndj + 1):
                self.labelx.append(y)
                self.labely.append(self.data[y])
            self.labely.append(0)

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        # create self.axes
        self.axes = figure.add_subplot()
        figure.set_facecolor((0.95, 0.95, 0.95))
        self.axes.set_facecolor((0.95, 0.95, 0.95))

        # create the barchart
        def create():

            self.axes.bar(self.jours, self.montants)
            self.axes.set_title('Repartition Budgetaire')
            self.axes.set_ylabel('Montant dépensable')
            self.axes.set_xlabel('Jour du mois')
            self.axes.set_xticks(self.labelx)
            self.axes.set_yticks(self.labely)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_entretien.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_entretien_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("Entretien", "données enregistrées")

        def ajouter():
            def depense(normal, montantdep):
                self.data[jour] -= montantdep
                singleton.addDepenseEntretien(montantdep)
                self.data = singleton.getNewEntretienB(self.data, normal)
                for i in range(jour, singleton.ndj):
                    self.labely[i] = self.data[i]
                self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseEntretien)
                self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseEntretien)
                create()
                messagebox.showinfo("Entretien",
                                    "vous avez depensé " + str(montantdep) + " dirhams\n n'oubliez pas de sauvegarder")

            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                depense(True, int(eAutr.get()))
            else:
                answer = askyesno(title='confirmation',
                                  message="vous avez depassé votre limite quotidienne \n et ne pouvez plus vous permettre de depenser " + eAutr.get() + " dirhams\n Dépenser quand même ?")
                if answer:
                    montantdep = int(eAutr.get())
                    depensable = self.data[jour]
                    depense(True, depensable)
                    reste = montantdep - depensable
                    answer = askyesno(title='confirmation',
                                      message="Il faudra depenser encore  " + str(
                                          reste) + " dirhams\n Vous aurez un solde négatif qui se repercutera les jours suivants\n Dépenser quand même ?")
                    if answer:
                        depense(False, reste)

        tk.Label(self, text="Montant du jour(" + singleton.jourComplet + ")").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


class Wifi(tk.Frame):
    def update(self):
        self.axes.bar(self.jours, self.montants)
        self.axes.set_title('Repartition Budgetaire')
        self.axes.set_ylabel('Montant dépensable')
        self.axes.set_xlabel('Jour du mois')
        self.axes.set_xticks(self.labelx)
        self.axes.set_yticks(self.labely)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[6] - singleton.depenseWifi)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseWifi)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Wifi", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        self.restantLabel = ttk.Label(self, text="restant")
        self.restantLabel.grid(row=0, column=2, padx=10, pady=10)
        self.depenséLabel = ttk.Label(self, text="depensé")
        self.depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[6]

        # prepare data
        self.data = {}
        self.labelx = []
        self.labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getWifiB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseWifi)
            self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseWifi)
            for y in range(1, singleton.ndj + 1):
                self.labelx.append(y)
                self.labely.append(self.data[y])
            self.labely.append(0)

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        # create self.axes
        self.axes = figure.add_subplot()
        figure.set_facecolor((0.95, 0.95, 0.95))
        self.axes.set_facecolor((0.95, 0.95, 0.95))

        # create the barchart
        def create():

            self.axes.bar(self.jours, self.montants)
            self.axes.set_title('Repartition Budgetaire')
            self.axes.set_ylabel('Montant dépensable')
            self.axes.set_xlabel('Jour du mois')
            self.axes.set_xticks(self.labelx)
            self.axes.set_yticks(self.labely)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_wifi.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_wifi_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("Wifi", "données enregistrées")

        def ajouter():
            def depense(normal, montantdep):
                self.data[jour] -= montantdep
                singleton.addDepenseWifi(montantdep)
                self.data = singleton.getNewWifiB(self.data, normal)
                for i in range(jour, singleton.ndj):
                    self.labely[i] = self.data[i]
                self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseWifi)
                self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseWifi)
                create()
                messagebox.showinfo("Wifi",
                                    "vous avez depensé " + str(montantdep) + " dirhams\n n'oubliez pas de sauvegarder")

            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                depense(True, int(eAutr.get()))
            else:
                answer = askyesno(title='confirmation',
                                  message="vous avez depassé votre limite quotidienne \n et ne pouvez plus vous permettre de depenser " + eAutr.get() + " dirhams\n Dépenser quand même ?")
                if answer:
                    montantdep = int(eAutr.get())
                    depensable = self.data[jour]
                    depense(True, depensable)
                    reste = montantdep - depensable
                    answer = askyesno(title='confirmation',
                                      message="Il faudra depenser encore  " + str(
                                          reste) + " dirhams\n Vous aurez un solde négatif qui se repercutera les jours suivants\n Dépenser quand même ?")
                    if answer:
                        depense(False, reste)

        tk.Label(self, text="Montant du jour(" + singleton.jourComplet + ")").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


class Salle(tk.Frame):
    def update(self):
        self.axes.bar(self.jours, self.montants)
        self.axes.set_title('Repartition Budgetaire')
        self.axes.set_ylabel('Montant dépensable')
        self.axes.set_xlabel('Jour du mois')
        self.axes.set_xticks(self.labelx)
        self.axes.set_yticks(self.labely)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[7] - singleton.depenseSalle)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseSalle)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Salle", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        self.restantLabel = ttk.Label(self, text="restant")
        self.restantLabel.grid(row=0, column=2, padx=10, pady=10)
        self.depenséLabel = ttk.Label(self, text="depensé")
        self.depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[7]

        # prepare data
        self.data = {}
        self.labelx = []
        self.labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getSalleB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseSalle)
            self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseSalle)
            for y in range(1, singleton.ndj + 1):
                self.labelx.append(y)
                self.labely.append(self.data[y])
            self.labely.append(0)

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        # create self.axes
        self.axes = figure.add_subplot()
        figure.set_facecolor((0.95, 0.95, 0.95))
        self.axes.set_facecolor((0.95, 0.95, 0.95))

        # create the barchart
        def create():

            self.axes.bar(self.jours, self.montants)
            self.axes.set_title('Repartition Budgetaire')
            self.axes.set_ylabel('Montant dépensable')
            self.axes.set_xlabel('Jour du mois')
            self.axes.set_xticks(self.labelx)
            self.axes.set_yticks(self.labely)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_salle.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_salle_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("Salle", "données enregistrées")

        def ajouter():
            def depense(normal, montantdep):
                self.data[jour] -= montantdep
                singleton.addDepenseSalle(montantdep)
                self.data = singleton.getNewSalleB(self.data, normal)
                for i in range(jour, singleton.ndj):
                    self.labely[i] = self.data[i]
                self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseSalle)
                self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseSalle)
                create()
                messagebox.showinfo("Salle",
                                    "vous avez depensé " + str(montantdep) + " dirhams\n n'oubliez pas de sauvegarder")

            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                depense(True, int(eAutr.get()))
            else:
                answer = askyesno(title='confirmation',
                                  message="vous avez depassé votre limite quotidienne \n et ne pouvez plus vous permettre de depenser " + eAutr.get() + " dirhams\n Dépenser quand même ?")
                if answer:
                    montantdep = int(eAutr.get())
                    depensable = self.data[jour]
                    depense(True, depensable)
                    reste = montantdep - depensable
                    answer = askyesno(title='confirmation',
                                      message="Il faudra depenser encore  " + str(
                                          reste) + " dirhams\n Vous aurez un solde négatif qui se repercutera les jours suivants\n Dépenser quand même ?")
                    if answer:
                        depense(False, reste)

        tk.Label(self, text="Montant du jour(" + singleton.jourComplet + ")").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


class Caprices(tk.Frame):
    def update(self):
        self.axes.bar(self.jours, self.montants)
        self.axes.set_title('Repartition Budgetaire')
        self.axes.set_ylabel('Montant dépensable')
        self.axes.set_xlabel('Jour du mois')
        self.axes.set_xticks(self.labelx)
        self.axes.set_yticks(self.labely)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[8] - singleton.depenseCaprice)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseCaprice)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Caprice", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        self.restantLabel = ttk.Label(self, text="restant")
        self.restantLabel.grid(row=0, column=2, padx=10, pady=10)
        self.depenséLabel = ttk.Label(self, text="depensé")
        self.depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[8]

        # prepare data
        self.data = {}
        self.labelx = []
        self.labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getCapriceB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseCaprice)
            self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseCaprice)
            for y in range(1, singleton.ndj + 1):
                self.labelx.append(y)
                self.labely.append(self.data[y])
            self.labely.append(0)

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        # create self.axes
        self.axes = figure.add_subplot()
        figure.set_facecolor((0.95, 0.95, 0.95))
        self.axes.set_facecolor((0.95, 0.95, 0.95))

        # create the barchart
        def create():

            self.axes.bar(self.jours, self.montants)
            self.axes.set_title('Repartition Budgetaire')
            self.axes.set_ylabel('Montant dépensable')
            self.axes.set_xlabel('Jour du mois')
            self.axes.set_xticks(self.labelx)
            self.axes.set_yticks(self.labely)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_caprice.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_caprice_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("Caprice", "données enregistrées")

        def ajouter():
            def depense(normal, montantdep):
                self.data[jour] -= montantdep
                singleton.addDepenseCaprice(montantdep)
                self.data = singleton.getNewCapriceB(self.data, normal)
                for i in range(jour, singleton.ndj):
                    self.labely[i] = self.data[i]
                self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseCaprice)
                self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseCaprice)
                create()
                messagebox.showinfo("Caprice",
                                    "vous avez depensé " + str(montantdep) + " dirhams\n n'oubliez pas de sauvegarder")

            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                depense(True, int(eAutr.get()))
            else:
                answer = askyesno(title='confirmation',
                                  message="vous avez depassé votre limite quotidienne \n et ne pouvez plus vous permettre de depenser " + eAutr.get() + " dirhams\n Dépenser quand même ?")
                if answer:
                    montantdep = int(eAutr.get())
                    depensable = self.data[jour]
                    depense(True, depensable)
                    reste = montantdep - depensable
                    answer = askyesno(title='confirmation',
                                      message="Il faudra depenser encore  " + str(
                                          reste) + " dirhams\n Vous aurez un solde négatif qui se repercutera les jours suivants\n Dépenser quand même ?")
                    if answer:
                        depense(False, reste)

        tk.Label(self, text="Montant du jour(" + singleton.jourComplet + ")").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


class Autres(tk.Frame):
    def update(self):
        self.axes.bar(self.jours, self.montants)
        self.axes.set_title('Repartition Budgetaire')
        self.axes.set_ylabel('Montant dépensable')
        self.axes.set_xlabel('Jour du mois')
        self.axes.set_xticks(self.labelx)
        self.axes.set_yticks(self.labely)
        self.restantLabel["text"] = "Montant restant: " + str(singleton.getMontants()[9] - singleton.depenseAutres)
        self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseAutres)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Autres", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        totalLabel = ttk.Label(self, text="total")
        totalLabel.grid(row=0, column=1, padx=10, pady=10)
        self.restantLabel = ttk.Label(self, text="restant")
        self.restantLabel.grid(row=0, column=2, padx=10, pady=10)
        self.depenséLabel = ttk.Label(self, text="depensé")
        self.depenséLabel.grid(row=0, column=3, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=10, weight='bold')
        # code ------------------------------------

        frame1 = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        frame1.grid(row=1, column=0, padx=10, pady=10)

        montant = singleton.getMontants()[9]

        # prepare data
        self.data = {}
        self.labelx = []
        self.labely = []
        self.jours = self.data.keys()
        self.montants = self.data.values()

        def populate():
            self.data = singleton.getAutresB()
            self.jours = self.data.keys()
            self.montants = self.data.values()
            totalLabel["text"] = "Montant total: " + str(montant)
            self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseAutres)
            self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseAutres)
            for y in range(1, singleton.ndj + 1):
                self.labelx.append(y)
                self.labely.append(self.data[y])
            self.labely.append(0)

        populate()

        # create a figure
        figure = Figure(figsize=(12, 4), dpi=100)
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        # create the toolbar
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=8, column=0)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        # create self.axes
        self.axes = figure.add_subplot()
        figure.set_facecolor((0.95, 0.95, 0.95))
        self.axes.set_facecolor((0.95, 0.95, 0.95))

        # create the barchart
        def create():

            self.axes.bar(self.jours, self.montants)
            self.axes.set_title('Repartition Budgetaire')
            self.axes.set_ylabel('Montant dépensable')
            self.axes.set_xlabel('Jour du mois')
            self.axes.set_xticks(self.labelx)
            self.axes.set_yticks(self.labely)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        create()

        def enregistrer():
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_autres.txt", "wb")
            pickle.dump(self.data, f)
            f.close()
            f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_autres_depense.txt", "wb")
            pickle.dump(singleton.depenseTransport, f2)
            f2.close()
            messagebox.showinfo("Autres", "données enregistrées")

        def ajouter():
            def depense(normal, montantdep):
                self.data[jour] -= montantdep
                singleton.addDepenseAutres(montantdep)
                self.data = singleton.getNewAutresB(self.data, normal)
                for i in range(jour, singleton.ndj):
                    self.labely[i] = self.data[i]
                self.restantLabel["text"] = "Montant restant: " + str(montant - singleton.depenseAutres)
                self.depenséLabel["text"] = "Montant depensé: " + str(singleton.depenseAutres)
                create()
                messagebox.showinfo("Autres",
                                    "vous avez depensé " + str(montantdep) + " dirhams\n n'oubliez pas de sauvegarder")

            jour = singleton.getJour()
            if (self.data[jour] - int(eAutr.get())) > 0:
                depense(True, int(eAutr.get()))
            else:
                answer = askyesno(title='confirmation',
                                  message="vous avez depassé votre limite quotidienne \n et ne pouvez plus vous permettre de depenser " + eAutr.get() + " dirhams\n Dépenser quand même ?")
                if answer:
                    montantdep = int(eAutr.get())
                    depensable = self.data[jour]
                    depense(True, depensable)
                    reste = montantdep - depensable
                    answer = askyesno(title='confirmation',
                                      message="Il faudra depenser encore  " + str(
                                          reste) + " dirhams\n Vous aurez un solde négatif qui se repercutera les jours suivants\n Dépenser quand même ?")
                    if answer:
                        depense(False, reste)

        tk.Label(self, text="Montant du jour(" + singleton.jourComplet + ")").grid(row=2, column=0, padx=10, pady=10)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=2, column=1, padx=10, pady=10)
        button5 = tk.Button(self, text="Ajouter", bg='#00ff00', fg='#ffffff',
                            command=ajouter, cursor="hand1")
        button5.grid(row=2, column=2, padx=10, pady=10)
        button5 = tk.Button(self, text="Sauvegarder", bg='#0051ff', fg='#ffffff',
                            command=enregistrer, cursor="hand1")
        button5.grid(row=2, column=3, padx=10, pady=10)


class ParametresRepartition(tk.Frame):
    res = ""

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        myFont = font.Font(family='Helvetica', size=15, weight='bold')
        self.data = {}

        def effacer():
            for i in range(1, len(entries) + 1):
                entries[i - 1].delete(0, tk.END)
            button3["state"] = tk.DISABLED

        def load():
            self.data = {}
            effacer()
            value = type.get()
            tk.messagebox.showinfo(title="chargement des parametres", message="vous avez choisit " + value)
            self.data = singleton.getDaysData(value)
            for i in range(1, len(entries) + 1):
                entries[i - 1].insert(tk.END, str(self.data[i]))
            button3['state'] = tk.NORMAL

        # code ------------------------------------
        tk.Label(self, text="Type :", font=myFont).grid(row=1, column=0)
        type = ttk.Combobox(self, values=["transport",
                                          "loyer", "nourriture", "facture",
                                          "loisirs", "entretien", "wifi",
                                          "salle de sport", "caprices et coups de tete", "autres"
                                          ])
        type.grid(row=1, column=1)
        button1 = tk.Button(self, text="Charger données", bg='#005100', fg='#ffffff', cursor="hand1",
                            command=load)
        button1['font'] = myFont
        button1.grid(row=1, column=2, padx=10, pady=10)
        button2 = tk.Button(self, text="Effacer", bg='#005155', fg='#ffffff', cursor="hand1",
                            command=effacer)
        button2['font'] = myFont
        button2.grid(row=1, column=3, padx=10, pady=10)
        ndj = singleton.ndj
        entries = []
        for i in range(1, 10):
            tk.Label(self, text="jour " + str(i), font=myFont).grid(row=i + 1, column=0)
            etr = tk.Entry(self, width=30)
            etr.grid(row=i + 1, column=1)
            entries.append(etr)
        for i in range(10, 19):
            tk.Label(self, text="jour " + str(i), font=myFont).grid(row=i - 8, column=3)
            etr = tk.Entry(self, width=30)
            etr.grid(row=i - 8, column=4)
            entries.append(etr)
        for i in range(19, 28):
            tk.Label(self, text="jour " + str(i), font=myFont).grid(row=i - 17, column=5)
            etr = tk.Entry(self, width=30)
            etr.grid(row=i - 17, column=6)
            entries.append(etr)
        for i in range(28, ndj + 1):
            tk.Label(self, text="jour " + str(i), font=myFont).grid(row=i - 26, column=7)
            etr = tk.Entry(self, width=30)
            etr.grid(row=i - 26, column=8)
            entries.append(etr)

        def save():

            value = type.get()
            if value == "transport":
                f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_transport_depense.txt", "wb")
                pickle.dump(singleton.depenseTransport, f2)
                f2.close()
                saveinfile("C:/Users/user/Videos/python/gestionFinanciere/budget_transport.txt")
                singleton.updateTransportDepense()
                self.controller.get_page(Transport).update()
            if value == "loyer":
                f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_loyer_depense.txt", "wb")
                pickle.dump(singleton.depenseLoyer, f2)
                f2.close()
                saveinfile("C:/Users/user/Videos/python/gestionFinanciere/budget_loyer.txt")
                singleton.updateLoyerDepense()
                self.controller.get_page(Loyer).update()
            if value == "nourriture":
                f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_nourriture_depense.txt", "wb")
                pickle.dump(singleton.depenseNourriture, f2)
                f2.close()
                saveinfile("C:/Users/user/Videos/python/gestionFinanciere/budget_nourriture.txt")
                singleton.updateNourritureDepense()
                self.controller.get_page(Nourriture).update()
            if value == "facture":
                f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_factures_depense.txt", "wb")
                pickle.dump(singleton.depenseFacture, f2)
                f2.close()
                saveinfile("C:/Users/user/Videos/python/gestionFinanciere/budget_factures.txt")
                singleton.updateFactureDepense()
                self.controller.get_page(Facture).update()
            if value == "loisirs":
                f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_loisirs_depense.txt", "wb")
                pickle.dump(singleton.depenseLoisirs, f2)
                f2.close()
                saveinfile("C:/Users/user/Videos/python/gestionFinanciere/budget_loisirs.txt")
                singleton.updateLoisirsDepense()
                self.controller.get_page(Loisirs).update()
            if value == "entretien":
                f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_entretien_depense.txt", "wb")
                pickle.dump(singleton.depenseEntretien, f2)
                f2.close()
                saveinfile("C:/Users/user/Videos/python/gestionFinanciere/budget_entretien.txt")
                singleton.updateEntretienDepense()
                self.controller.get_page(Entretien).update()
            if value == "wifi":
                f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_wifi_depense.txt", "wb")
                pickle.dump(singleton.depenseWifi, f2)
                f2.close()
                saveinfile("C:/Users/user/Videos/python/gestionFinanciere/budget_wifi.txt")
                singleton.updateWifiDepense()
                self.controller.get_page(Wifi).update()
            if value == "salle de sport":
                f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_salle_depense.txt", "wb")
                pickle.dump(singleton.depenseSalle, f2)
                f2.close()
                saveinfile("C:/Users/user/Videos/python/gestionFinanciere/budget_salle.txt")
                singleton.updateSalleDepense()
                self.controller.get_page(Salle).update()
            if value == "caprices et coups de tete":
                f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_caprice_depense.txt", "wb")
                pickle.dump(singleton.depenseCaprice, f2)
                f2.close()
                saveinfile("C:/Users/user/Videos/python/gestionFinanciere/budget_caprice.txt")
                singleton.updateCapriceDepense()
                self.controller.get_page(Caprices).update()
            if value == "autres":
                f2 = open("C:/Users/user/Videos/python/gestionFinanciere/budget_autres_depense.txt", "wb")
                pickle.dump(singleton.depenseAutres, f2)
                f2.close()
                saveinfile("C:/Users/user/Videos/python/gestionFinanciere/budget_autres.txt")
                singleton.updateAutreDepense()
                self.controller.get_page(Autres).update()
            messagebox.showinfo("Sauvegarde", "Configuration " + value + " journaliere enregistrée !")

        def saveinfile(filename):
            for i2 in range(1, len(entries) + 1):
                self.data[i2] = float(entries[i2 - 1].get())
            f = open(filename, "wb")
            pickle.dump(self.data, f)
            f.close()

        button3 = tk.Button(self, text="Enregistrer", bg='#0051ff', fg='#ffffff', cursor="hand1", state=tk.DISABLED,
                            command=save)
        button3['font'] = myFont
        button3.grid(row=11, column=0, padx=10, pady=10)


class Parametres(tk.Frame):
    res = ""

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Paramétrer la solution", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        myFont = font.Font(family='Helvetica', size=15, weight='bold')
        # code ------------------------------------
        montants = singleton.getMontants()
        tk.Label(self, text="Transport", font=myFont).grid(row=1, column=0)
        etr = tk.Entry(self, width=30)
        etr.grid(row=1, column=1)
        etr.insert(tk.END, str(montants[0]))
        tk.Label(self, text="Loyer", font=myFont).grid(row=2, column=0)
        eloy = tk.Entry(self, width=30)
        eloy.grid(row=2, column=1)
        eloy.insert(tk.END, montants[1])
        tk.Label(self, text="Nourriture", font=myFont).grid(row=3, column=0)
        enou = tk.Entry(self, width=30)
        enou.grid(row=3, column=1)
        enou.insert(tk.END, montants[2])
        tk.Label(self, text="Factures", font=myFont).grid(row=4, column=0)
        efac = tk.Entry(self, width=30)
        efac.grid(row=4, column=1)
        efac.insert(tk.END, montants[3])
        tk.Label(self, text="Loisirs", font=myFont).grid(row=5, column=0)
        eloi = tk.Entry(self, width=30)
        eloi.grid(row=5, column=1)
        eloi.insert(tk.END, montants[4])
        tk.Label(self, text="Entretien", font=myFont).grid(row=6, column=0)
        eEntr = tk.Entry(self, width=30)
        eEntr.grid(row=6, column=1)
        eEntr.insert(tk.END, montants[5])
        tk.Label(self, text="Wifi", font=myFont).grid(row=7, column=0)
        eWifi = tk.Entry(self, width=30)
        eWifi.grid(row=7, column=1)
        eWifi.insert(tk.END, montants[6])
        tk.Label(self, text="Salle de sport", font=myFont).grid(row=8, column=0)
        eSale = tk.Entry(self, width=30)
        eSale.grid(row=8, column=1)
        eSale.insert(tk.END, montants[7])
        tk.Label(self, text="Caprices et coups de tete", font=myFont).grid(row=9, column=0)
        eCapr = tk.Entry(self, width=30)
        eCapr.grid(row=9, column=1)
        eCapr.insert(tk.END, montants[8])
        tk.Label(self, text="Autres", font=myFont).grid(row=10, column=0)
        eAutr = tk.Entry(self, width=30)
        eAutr.grid(row=10, column=1)
        eAutr.insert(tk.END, montants[9])

        def save():
            # transport loyer nourriture facture loisirs entretien autres
            singleton.addMontants(0, float(etr.get()))
            singleton.addMontants(1, float(eloy.get()))
            singleton.addMontants(2, float(enou.get()))
            singleton.addMontants(3, float(efac.get()))
            singleton.addMontants(4, float(eloi.get()))
            singleton.addMontants(5, float(eEntr.get()))
            singleton.addMontants(6, float(eWifi.get()))
            singleton.addMontants(7, float(eSale.get()))
            singleton.addMontants(8, float(eCapr.get()))
            singleton.addMontants(9, float(eAutr.get()))
            messagebox.showinfo("Sauvegarde", "Configuration Enregistrée !")
            f = open("C:/Users/user/Videos/python/gestionFinanciere/budget.txt", "wb")
            pickle.dump(singleton.getMontants(), f)
            f.close()
            self.controller.get_page(Bilan).update()

        button5 = tk.Button(self, text="Enregistrer", bg='#0051ff', fg='#ffffff',
                            command=save)
        button5['font'] = myFont
        button5.grid(row=11, column=0, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
