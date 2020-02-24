"""

"""

__author__ = "diogeneskelsen@gmail.com (Diogenes Kelsen)"

class Even():
    """Even Calculator class.

    """

   # init method or constructor 
    def __init__(self): 
        self.data = []
        self.result = []

    def minus(self):
        pass

    def plus(self):
        pass

    def calculate(self, number):
        z = 0

        self.result.append(z)

        return z

    def display(self):
        x = 0

        for i in range(len(self.data)):
            # Calculate
            x = self.calculate(self.data[i])

            # Print on terminal
            print("Case #{}: {}".format((i+1), x))

    def new_input(self, n_list: list):
        # Define data to compute
        self.data = n_list

        # Display result on the screen
        self.display()

        # Return a list to test validation
        return self.result