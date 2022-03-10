import pickle
import datetime
import calendar

class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


class MyClass(Singleton):
    now = datetime.datetime.now()
    ndj= int(calendar.monthrange(now.year, now.month)[1])
    depenseTransport=0
    montants = []
    date = datetime.datetime.now()
    jour = int(date.strftime("%d"))
    # transport loyer nourriture facture loisirs entretien wifi autres
    transportBudget={}

    def __init__(self):
        try:
            f = open("budget.txt", "rb")
            self.montants = pickle.load(f)
            print("tableau montant chargé")
            f.close()
        except:
            self.montants = [500, 2700, 1000, 450, 400, 300, 450, 200]
        try:
            f = open("budget_transport.txt", "rb")
            self.transportBudget = pickle.load(f)
            print("tableau transport budget chargé")
            f.close()
        except:
            for y in range(1, self.ndj + 1):
                self.transportBudget[y] = self.montants[0] / self.ndj

        try:
            f = open("budget_transport_depense.txt", "rb")
            self.depenseTransport = pickle.load(f)
            print("depense transport chargée")
            f.close()
        except:
            for i in range(1, self.jour + 1):
                self.depenseTransport += self.transportBudget[i]


    def getMontants(self):
        return self.montants

    def addDepenseTransport(self, montant):
        self.depenseTransport+=montant

    def getTransportB(self):
        return self.transportBudget

    def getNewTransportB(self, data):
        self.transportBudget = data

        budgetRestant = self.montants[0]-self.depenseTransport
        print(budgetRestant)
        jr = self.ndj-self.jour+1
        for i in range(self.jour+1, self.ndj+1):
            self.transportBudget[i] = budgetRestant/jr

        return self.transportBudget

    def getDate(self):
        return self.date

    def getJour(self):
        return self.jour

    def addMontants(self, pos, val):
        self.montants[pos] = val


    pass



