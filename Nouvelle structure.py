class ODE_1:
    def __init__(self, f, CI):
        pass

    def Euler(self, t, N):
        """ Compute the Euler scheme for the current ordinary differential
    equation"""
        pass

    def Runge_Kutta(self, t, N):
        pass


class EvolutionSystem:
    def approx_Euler(self):
        """compute the approximations of the model via an Euler method"""
        pass

    def show(self):
        """Display the results of the approximation"""
        pass

class ProiePredateur(EvolutionSystem):
    def __init__(self, alpha, beta, gamma, delta):
        pass

    def f(self, x):
        """is the function that gives the differentiel system
        :return value: a list of length 2
        """
        pass
        
#class ProieMilieuPredateur(EvolutionSystem):
#    def __init__(self, ...):
#        pass
#
#    def f(self, x):
#        """is the function that gives the differentiel system"""
#        pass


if __name__ == '__main__':
