import matplotlib.pyplot as plt

class Plot:
    def __init__(self, years):
        self.xData = years

    def setX(self, data):
        self.xData = data

    def setY(self, data):
        self.yData = data

    def plot(self, data):
        plot1 = plt.figure(1)
        plt.title("CO2 Global Radiative Forcing (W m-2)")
        plt.plot(self.xData, data[0])

        plot2 = plt.figure(2)
        plt.title("CH4 Global Radiative Forcing (W m-2)")
        plt.plot(self.xData, data[1])

        plot3 = plt.figure(3)
        plt.title("N2O Global Radiative Forcing (W m-2)")
        plt.plot(self.xData, data[2])

        plot4 = plt.figure(4)
        plt.title("CFCs Global Radiative Forcing (W m-2)")
        plt.plot(self.xData, data[3])

        plot5 = plt.figure(5)
        plt.title("HCFCs Global Radiative Forcing (W m-2)")
        plt.plot(self.xData, data[4])

        plot6 = plt.figure(6)
        plt.title("HFCs Global Radiative Forcing (W m-2)")
        plt.plot(self.xData, data[5])

        plt.show()