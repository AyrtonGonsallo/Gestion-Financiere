import pickle
import datetime
import calendar
import threading


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass
    now = datetime.datetime.now()
    ndj = int(calendar.monthrange(now.year, now.month)[1])
    depenseTransport = 0
    transportBudget = {}
    depenseLoyer = 0
    loyerBudget = {}
    depenseNourriture = 0
    nourritureBudget = {}
    depenseFactures = 0
    facturesBudget = {}
    depenseLoisirs = 0
    loisirsBudget = {}
    depenseEntretien = 0
    entretienBudget = {}
    depenseWifi = 0
    wifiBudget = {}
    depenseSalle = 0
    salleBudget = {}
    depenseCaprice = 0
    capriceBudget = {}
    depenseAutres = 0
    autresBudget = {}
    montants = []
    date = datetime.datetime.now()
    jour = int(date.strftime("%d"))
    jourComplet = date.strftime("%d/%m/%y")

    # transport loyer nourriture facture loisirs entretien wifi salle de sport caprices et coups de tete autres

    def __init__(self):
        def setData():
            initMessage=""
            # initiation montant total
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget.txt", "rb")
                self.montants = pickle.load(f)
                initMessage+="tableau montant chargé\n"
                f.close()
            except:
                self.montants = [300, 900, 700, 450, 500, 200, 200, 200, 400, 500]

            # initiation transport
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_transport.txt", "rb")
                self.transportBudget = pickle.load(f)
                f.close()
            except:
                for y in range(1, self.ndj + 1):
                    self.transportBudget[y] = self.montants[0] / self.ndj

            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_transport_depense.txt", "rb")
                self.depenseTransport = pickle.load(f)
                f.close()
            except:
                self.depenseTransport =0

            # initiation nourriture
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_nourriture.txt", "rb")
                self.nourritureBudget = pickle.load(f)
                f.close()
            except:
                for y in range(1, self.ndj + 1):
                    self.nourritureBudget[y] = self.montants[2] / self.ndj

            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_nourriture_depense.txt", "rb")
                self.depenseNourriture = pickle.load(f)
                f.close()
            except:
                self.depenseNourriture =0

            # initiation loyer
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_loyer.txt", "rb")
                self.loyerBudget = pickle.load(f)
                f.close()
            except:
                for y in range(1, self.ndj + 1):
                    self.loyerBudget[y] = self.montants[1] / self.ndj

            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_loyer_depense.txt", "rb")
                self.depenseLoyer = pickle.load(f)
                f.close()
            except:
                self.depenseLoyer =0
            # initiation factures
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_factures.txt", "rb")
                self.facturesBudget = pickle.load(f)
                f.close()
            except:
                for y in range(1, self.ndj + 1):
                    self.facturesBudget[y] = self.montants[3] / self.ndj

            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_factures_depense.txt", "rb")
                self.depenseFactures = pickle.load(f)
                f.close()
            except:
                self.depenseFactures =0
            # initiation loisirs
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_loisirs.txt", "rb")
                self.loisirsBudget = pickle.load(f)
                f.close()
            except:
                for y in range(1, self.ndj + 1):
                    self.loisirsBudget[y] = self.montants[4] / self.ndj

            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_loisirs_depense.txt", "rb")
                self.depenseLoisirs = pickle.load(f)
                f.close()
            except:
                self.depenseLoisirs =0
            # initiation entretien
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_entretien.txt", "rb")
                self.entretienBudget = pickle.load(f)
                f.close()
            except:
                for y in range(1, self.ndj + 1):
                    self.entretienBudget[y] = self.montants[5] / self.ndj

            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_entretien_depense.txt", "rb")
                self.depenseEntretien = pickle.load(f)
                f.close()
            except:
                self.depenseEntretien =0
            # initiation wifi
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_wifi.txt", "rb")
                self.wifiBudget = pickle.load(f)
                f.close()
            except:
                for y in range(1, self.ndj + 1):
                    self.wifiBudget[y] = self.montants[6] / self.ndj

            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_wifi_depense.txt", "rb")
                self.depenseWifi = pickle.load(f)
                f.close()
            except:
                self.depenseWifi =0
            # initiation salle de sport
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_salle.txt", "rb")
                self.salleBudget = pickle.load(f)
                f.close()
            except:
                for y in range(1, self.ndj + 1):
                    self.salleBudget[y] = self.montants[7] / self.ndj

            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_salle_depense.txt", "rb")
                self.depenseSalle = pickle.load(f)
                f.close()
            except:
                self.depenseSalle =0
            # initiation caprice
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_caprice.txt", "rb")
                self.capriceBudget = pickle.load(f)
                f.close()
            except:
                for y in range(1, self.ndj + 1):
                    self.capriceBudget[y] = self.montants[8] / self.ndj

            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_caprice_depense.txt", "rb")
                self.depenseCaprice = pickle.load(f)
                f.close()
            except:
                self.depenseCaprice =0
            # initiation autres
            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_autres.txt", "rb")
                self.autresBudget = pickle.load(f)
                f.close()
            except:
                for y in range(1, self.ndj + 1):
                    self.autresBudget[y] = self.montants[9] / self.ndj

            try:
                f = open("C:/Users/user/Videos/python/gestionFinanciere/budget_autres_depense.txt", "rb")
                self.depenseAutres = pickle.load(f)
                f.close()
            except:
                self.depenseAutres =0


        tInit = threading.Thread(target=setData)
        tInit.start()
        tInit.join()
        

    def getMontants(self):
        return self.montants

    # fonctions transport
    def addDepenseTransport(self, montant):
        self.depenseTransport += montant

    def getTransportB(self):
        return self.transportBudget

    def getNewTransportB(self, data, normal):
        self.transportBudget = data
        if not normal:
            budgetRestant = self.montants[0] - self.depenseTransport

            jr = self.ndj - self.jour + 1
            for i in range(self.jour + 1, self.ndj + 1):
                self.transportBudget[i] = budgetRestant / jr
        return self.transportBudget

    def updateTransportDepense(self):
        self.depenseTransport = 0
        for i in range(1, self.jour):
            self.depenseTransport += self.transportBudget[i]
    def updateLoyerDepense(self):
        self.depenseLoyer = 0
        for i in range(1, self.jour):
            self.depenseLoyer += self.loyerBudget[i]
    def updateNourritureDepense(self):
        self.depenseNourriture = 0
        for i in range(1, self.jour):
            self.depenseNourriture += self.nourritureBudget[i]
    def updateFactureDepense(self):
        self.depenseFacture = 0
        for i in range(1, self.jour):
            self.depenseFacture += self.factureBudget[i]
    def updateLoisirsDepense(self):
        self.depenseLoisirs = 0
        for i in range(1, self.jour):
            self.depenseLoisirs += self.loisirsBudget[i]
    def updateEntretienDepense(self):
        self.depenseEntretien = 0
        for i in range(1, self.jour):
            self.depenseEntretien += self.entretienBudget[i]
    def updateWifiDepense(self):
        self.depenseWifi = 0
        for i in range(1, self.jour):
            self.depenseWifi += self.wifiBudget[i]
    def updateSalleDepense(self):
        self.depenseSalle = 0
        for i in range(1, self.jour):
            self.depenseSalle += self.salleBudget[i]
    def updateCapriceDepense(self):
        self.depenseCaprice = 0
        for i in range(1, self.jour):
            self.depenseCaprice += self.capriceBudget[i]
    def updateAutreDepense(self):
        self.depenseAutre = 0
        for i in range(1, self.jour):
            self.depenseAutre += self.autreBudget[i] 

    # fonctions entretien
    def addDepenseEntretien(self, montant):
        self.depenseEntretien += montant

    def getEntretienB(self):
        return self.entretienBudget

    def getNewEntretienB(self, data, normal):
        self.entretienBudget = data
        if not normal:
            budgetRestant = self.montants[5] - self.depenseEntretien

            jr = self.ndj - self.jour + 1
            for i in range(self.jour + 1, self.ndj + 1):
                self.entretienBudget[i] = budgetRestant / jr
        return self.entretienBudget

    # fonctions nourriture
    def addDepenseNourriture(self, montant):
        self.depenseNourriture += montant

    def getNourritureB(self):
        return self.nourritureBudget

    def getNewNourritureB(self, data, normal):
        self.nourritureBudget = data
        if not normal:
            budgetRestant = self.montants[2] - self.depenseNourriture
            print(budgetRestant)
            jr = self.ndj - self.jour + 1
            for i in range(self.jour + 1, self.ndj + 1):
                self.nourritureBudget[i] = budgetRestant / jr
        return self.nourritureBudget

    # fonctions loyer
    def addDepenseLoyer(self, montant):
        self.depenseLoyer += montant

    def getLoyerB(self):
        return self.loyerBudget

    def getNewLoyerB(self, data, normal):
        self.loyerBudget = data
        if not normal:
            budgetRestant = self.montants[1] - self.depenseLoyer
            print(budgetRestant)
            jr = self.ndj - self.jour + 1
            for i in range(self.jour + 1, self.ndj + 1):
                self.loyerBudget[i] = budgetRestant / jr
        return self.loyerBudget

    # fonctions salle
    def addDepenseSalle(self, montant):
        self.depenseSalle += montant

    def getSalleB(self):
        return self.salleBudget

    def getNewSalleB(self, data, normal):
        self.salleBudget = data
        if not normal:
            budgetRestant = self.montants[7] - self.depenseSalle
            print(budgetRestant)
            jr = self.ndj - self.jour + 1
            for i in range(self.jour + 1, self.ndj + 1):
                self.salleBudget[i] = budgetRestant / jr
        return self.salleBudget

    # fonctions wifi
    def addDepenseWifi(self, montant):
        self.depenseWifi += montant

    def getWifiB(self):
        return self.wifiBudget

    def getNewWifiB(self, data, normal):
        self.wifiBudget = data
        if not normal:
            budgetRestant = self.montants[6] - self.depenseWifi
            print(budgetRestant)
            jr = self.ndj - self.jour + 1
            for i in range(self.jour + 1, self.ndj + 1):
                self.wifiBudget[i] = budgetRestant / jr
        return self.wifiBudget

    # fonctions loisirs
    def addDepenseLoisirs(self, montant):
        self.depenseLoisirs += montant

    def getLoisirsB(self):
        return self.loisirsBudget

    def getNewLoisirsB(self, data, normal):
        self.loisirsBudget = data
        if not normal:
            budgetRestant = self.montants[4] - self.depenseLoisirs
            print(budgetRestant)
            jr = self.ndj - self.jour + 1
            for i in range(self.jour + 1, self.ndj + 1):
                self.loisirsBudget[i] = budgetRestant / jr
        return self.loisirsBudget

    # fonctions factures
    def addDepenseFactures(self, montant):
        self.depenseFactures += montant

    def getFacturesB(self):
        return self.facturesBudget

    def getNewFacturesB(self, data, normal):
        self.facturesBudget = data
        if not normal:
            budgetRestant = self.montants[3] - self.depenseFactures
            print(budgetRestant)
            jr = self.ndj - self.jour + 1
            for i in range(self.jour + 1, self.ndj + 1):
                self.facturesBudget[i] = budgetRestant / jr
        return self.facturesBudget

    # fonctions caprice
    def addDepenseCaprice(self, montant):
        self.depenseCaprice += montant

    def getCapriceB(self):
        return self.capriceBudget

    def getNewCapriceB(self, data, normal):
        self.capriceBudget = data
        if not normal:
            budgetRestant = self.montants[8] - self.depenseCaprice
            print(budgetRestant)
            jr = self.ndj - self.jour + 1
            for i in range(self.jour + 1, self.ndj + 1):
                self.capriceBudget[i] = budgetRestant / jr
        return self.capriceBudget

    # fonctions autres
    def addDepenseAutres(self, montant):
        self.depenseAutres += montant

    def getAutresB(self):
        return self.autresBudget

    def getNewAutresB(self, data, normal):
        self.autresBudget = data
        if not normal:
            budgetRestant = self.montants[9] - self.depenseAutres
            print(budgetRestant)
            jr = self.ndj - self.jour + 1
            for i in range(self.jour + 1, self.ndj + 1):
                self.autresBudget[i] = budgetRestant / jr
        return self.autresBudget

    def getDate(self):
        return self.date

    def getJour(self):
        return self.jour

    def addMontants(self, pos, val):
        self.montants[pos] = val

    def getDaysData(self, value):
        if value == "transport":
            return self.transportBudget
        if value == "loyer":
            return self.loyerBudget
        if value == "nourriture":
            return self.nourritureBudget
        if value == "facture":
            return self.facturesBudget
        if value == "loisirs":
            return self.loisirsBudget
        if value == "entretien":
            return self.entretienBudget
        if value == "wifi":
            return self.wifiBudget
        if value == "salle de sport":
            return self.salleBudget
        if value == "caprices et coups de tete":
            return self.capriceBudget
        if value == "autres":
            return self.autresBudget

 
