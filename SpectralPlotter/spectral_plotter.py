"""
Small class to overplot fit results.

The user should take care of writing the correct units
and labels for the axis of the plots.

Author: Carlo Romoli - MPIK
"""

import matplotlib.pyplot as plt
import numpy as np

class Spectrum:
    """
    Parent class that contains the basic attributes and the basic methods
    that will be used to plot spectral results for comparison.
    """
    def __init__(self,pars,s,cov,emin,emax,text,shiftfactor=1):
        self.pars = pars
        self.scale = s  # normalization energy
        self.cov = np.array(cov)  # covariance matrix 
        self.emin = emin  # minimum energy
        self.emax = emax  # maximum energy
        self.shiftfactor = shiftfactor  # optional shift value (to check possible energy shifts)
        self.energy = np.logspace(np.log10(emin),np.log10(emax),50)  # energy array
        self.deltaf = self.return_deltaf()   # uncertainty on the differential flux
        self.bestfit = self.return_bestfit()  # best fit values
        self.fp = self.bestfit+self.deltaf  # upper value of the differential flux
        self.fm = self.bestfit-self.deltaf  # lower value of the differential flux
        self.label = text

    def return_bestfit(self):
        '''
        Returns best fit function
        '''
        return self.fit_function(self.energy)
    
    def plotter_dnde(self,col):
        '''
        Plot differential spectrum
        Iif you don't create a figure before this call
        it will overplot
        
        - col = color to use
        '''
        plt.loglog(self.energy*self.shiftfactor,self.bestfit,color=col)
        plt.fill_between(self.energy*self.shiftfactor,self.fp,self.fm,alpha=0.2,color=col,label = self.label)
    
    def plotter_sed(self,col):
        '''
        Plot the SED
        Iif you don't create a figure before this call
        it will overplot
        
        - col = color to use
        '''
        plt.loglog(self.energy*self.shiftfactor,1.602*(self.energy*self.shiftfactor)**2*self.bestfit,color=col)
        plt.fill_between(self.energy*self.shiftfactor,1.602*(self.energy*self.shiftfactor)**2*self.fp,1.602*(self.energy*self.shiftfactor)**2*self.fm,alpha=0.2,color=col,label = self.label)
        
    def print_index(self):
        '''
        Print index and its error
        '''
        print( "%.2f +/- %.2f"%(self.ind,np.sqrt(self.cov[1][1])))
        
    def get_index(self):
        '''
        Return index and its error
        '''
        return self.ind,np.sqrt(self.cov[1][1])
    
    def print_parameters(self):
        '''
        Print the parameters with the corresponding errors
        '''
        for par,err in zip(self.pars,self.cov.diagonal()):
            print("%.2e +/- %.2e"%(par,np.sqrt(err)))
            
    def get_parameter(self, index):
        '''
        Returns value and error of the 'index' parameter
        '''
        if index > (len(self.pars)-1):
            raise IndexError("index exceeds length of the parameter list")
        return self.pars[index],np.sqrt(self.cov.diagonal()[index])
    
    
class SpectrumPL(Spectrum):
    """
    Class for a PL spectrum
    will be made something with inheritance
    """
    def fit_function(self,x):
        '''
        Power law function
        '''
        return self.pars[0] * (x/self.scale)**(self.pars[1])

    def fitfunc_N(self,x):
        '''
        Derivative of the fit function
        wrt to normalization
        '''
        return (x/self.scale)**(self.pars[1])
    
    def fitfunc_a(self,x):
        '''
        Derivative of the fit function
        wrt to photon index
        '''
        return self.fit_function(x)*np.log(x/self.scale)*np.sign(self.pars[1])
    
    def return_deltaf(self):
        '''
        Get the uncertainty on the differential flux
        via error propagation (builds the confidence interval)
        '''
        delta = lambda x: np.sqrt(np.dot(np.dot([self.fitfunc_N(x),self.fitfunc_a(x)],self.cov),
                                         [self.fitfunc_N(x),self.fitfunc_a(x)]))
        delta = np.vectorize(delta)
        return delta(self.energy)


class SpectumLogP(Spectrum):
    """
    Class for a PL spectrum
    will be made something with inheritance
    """
    def fit_function(self,x):
        '''
        log parabola function
        beware that this assumes that the index is negative
        '''
        return self.pars[0] * (x/self.scale)**((self.pars[1])-self.pars[2]*np.log(x/self.scale))

    def fitfunc_N(self,x):
        '''
        Derivative of the fit function
        wrt to normalization
        '''
        return self.fit_function(x)/self.pars[0]
    
    def fitfunc_a(self,x):
        '''
        Derivative of the fit function
        wrt to photon index
        '''
        return self.fit_function(x) * np.log(x/self.scale) * np.sign(self.pars[1])
    
    def fitfunc_b(self,x):
        '''
        Derivative of the fit function wrt to
        the beta parameter of the logparabola
        '''
        return self.fit_function(x) * (np.log(x/self.scale))**2 * (-1)
    
    def return_deltaf(self):
        '''
        Get the uncertainty on the differential flux
        via error propagation (builds the confidence interval)
        '''
        delta = lambda x: np.sqrt(np.dot(np.dot([self.fitfunc_N(x),self.fitfunc_a(x),self.fitfunc_b(x)],self.cov),
                                         [self.fitfunc_N(x),self.fitfunc_a(x),self.fitfunc_b(x)]))
        delta = np.vectorize(delta)
        return delta(self.energy)
    
