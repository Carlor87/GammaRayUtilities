"""
Author: Carlo Romoli

Some of the tabulated EBL models come from here:
https://github.com/fermi-lat/celestialSources/tree/master/eblAtten/data
"""

import os,sys
import numpy as np
from astropy.table import Table
from pkg_resources import resource_filename

__all__ = ["EblModel"]

class EblModel:
    '''
    Class to consider the contribution of the Extragalactic Background Light (EBL) on gamma ray data,
    In the initialization it is possible to choose between several models
    For model 1 (Franceschini,2008), zeta between 0.01 and 3.
    For model 2 (Franceschini,2017), zeta between 0.01 and 3.
    For model 3 (Dominguez,2011), zeta between 0.01 and 3.
    For model 4 (Gilmore, 2012), zeta between 0.01 and 3.
    For model 5 (Finke, 2010), zeta between 0.01 and 3.
    For model 6 (Kneiske & Dole, 2010), zeta between 0.01 and 5.
    For model 7 (Inoue et al., 2013), zeta between 0.01 and 9.
    For redshifts lower than these values, the interpolation is done with 0
    and the results might not be accurate
    '''
    
    def __init__(self,zeta,model):
        '''
        zeta = redshift of the gamma-ray source
        model = tabulated EBL model (int between 1 and 7)
        '''
        self._model = model
        if (model == 1):
            '''
            Franceschini2008
            '''
            self._zarray = [0.,0.01,0.03,0.1,0.3,0.5,1.0,1.5,2.0,3.0]
            #self._fil = "./models/Franceschini2008.dat"
            self._fil = resource_filename(__name__,"./models/Franceschini2008.dat")
            tab = Table.read(self._fil, format='ascii')
            self._energy = np.array(tab[tab.colnames[0]])
            self._tautable = np.array(tab[tab.colnames[1:]])
        if (model == 2):
            '''
            Franceschini2017
            '''
            self._zarray = [0.0,0.01,0.03,0.1,0.3,0.5,1.0,1.5,2.0,2.5,3.0]
            self._fil = resource_filename(__name__,"./models/Franceschini2017.dat")
            tab = Table.read(self._fil, format='ascii')
            self._energy = np.array(tab[tab.colnames[0]])
            self._tautable = np.array(tab[tab.colnames[1:]])
        if (model == 3):
            '''
            Dominguez2011
            '''
            self._zarray = [0.,0.01,0.03,0.1,0.3,0.5,1.0,1.5,2.0,3.0]
            self._fil = resource_filename(__name__,"./models/Dominguez2011.dat")
            tab = Table.read(self._fil, format='ascii')
            self._energy = np.array(tab[tab.colnames[0]])
            self._tautable = np.array(tab[tab.colnames[1:]])
        if (model == 4):
            '''
            Gilmore2012
            '''
            self._zarray = [0.,0.01,0.03,0.1,0.3,0.5,1.0,1.5,2.0,3.0]
            self._fil = resource_filename(__name__,"./models/Gilmore2012.dat")
            tab = Table.read(self._fil, format='ascii')
            self._energy = np.array(tab[tab.colnames[0]])
            self._tautable = np.array(tab[tab.colnames[1:]])
        if (model == 5):
            '''
            Finke2010
            '''
            self._zarray = [0.,0.01,0.03,0.1,0.3,0.5,1.0,1.5,2.0,3.0]
            self._fil = resource_filename(__name__,"./models/Finke2010.dat")
            tab = Table.read(self._fil, format='ascii')
            self._energy = np.array(tab[tab.colnames[0]])
            self._tautable = np.array(tab[tab.colnames[1:]])        
        if (model == 6):
            '''
            KNEISKEandDOLE_2010
            '''
            self._zarray = [0.0,0.0106,0.0109,0.0112,0.0116,0.0119,0.0123,0.0127,0.0131,0.0135,0.0139,0.0144,0.0148,0.0153,0.0158,0.0163,0.0168,0.0173,0.0179,0.0184,0.0190,0.0196,0.0202,0.0209,0.0215,0.0222,0.0229,0.0236,0.0243,0.0251,0.0259,0.0267,0.0275,0.0284,0.0293,0.0302,0.0312,0.0322,0.0332,0.0342,0.0353,0.0364,0.0375,0.0387,0.0399,0.0412,0.0425,0.0438,0.0452,0.0466,0.0481,0.0496,0.0512,0.0528,0.0544,0.0561,0.0579,0.0597,0.0616,0.0635,0.0655,0.0676,0.0697,0.0719,0.0742,0.0765,0.0789,0.0814,0.0839,0.0866,0.0893,0.0921,0.0950,0.0980,0.1011,0.1042,0.1075,0.1109,0.1144,0.1180,0.1217,0.1255,0.1295,0.1335,0.1377,0.1421,0.1465,0.1511,0.1559,0.1608,0.1658,0.1710,0.1764,0.1820,0.1877,0.1936,0.1997,0.2060,0.2124,0.2191,0.2260,0.2331,0.2404,0.2480,0.2558,0.2638,0.2721,0.2807,0.2895,0.2986,0.3080,0.3176,0.3276,0.3379,0.3485,0.3595,0.3708,0.3825,0.3945,0.4069,0.4197,0.4329,0.4465,0.4605,0.4750,0.4899,0.5053,0.5212,0.5376,0.5545,0.5719,0.5899,0.6084,0.6275,0.6473,0.6676,0.6886,0.7102,0.7326,0.7556,0.7793,0.8038,0.8291,0.8552,0.8820,0.9098,0.9384,0.9678,0.9983,1.0296,1.0620,1.0954,1.1298,1.1653,1.2020,1.2397,1.2787,1.3189,1.3604,1.4031,1.4472,1.4927,1.5396,1.5880,1.6380,1.6894,1.7425,1.7973,1.8538,1.9121,1.9722,2.0342,2.0981,2.1641,2.2321,2.3022,2.3746,2.4492,2.5262,2.6056,2.6875,2.7720,2.8591,2.9490,3.0417,3.1373,3.2359,3.3377,3.4426,3.5508,3.6624,3.7775,3.8962,4.0187,4.1450,4.2753,4.4097,4.5483,4.6913,4.8387,4.9908]
            self._fil = resource_filename(__name__,"./models/KNEISKEandDOLE_2010.dat")
            tab = Table.read(self._fil, format='ascii')
            self._energy = np.array(tab[tab.colnames[0]])/1e3 # energy in the file in GeV
            self._tautable = np.array(tab[tab.colnames[1:]])
        if (model ==7):
            '''
            INOUEetal_2013
            '''
            self._zarray = [0.0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.00,1.20,1.40,1.60,1.80,2.00,2.20,2.40,2.60,2.80,3.00,3.20,3.40,3.60,3.80,4.00,4.20,4.40,4.60,4.80,5.00,5.50,6.00,6.50,7.00,7.50,8.00,8.50,9.00]
            self._fil = resource_filename(__name__,"./models/INOUEetal_2013.dat")
            tab = Table.read(self._fil, format='ascii')
            self._energy = np.array(tab[tab.colnames[0]])/1e3 # energy in the file in GeV
            self._tautable = np.array(tab[tab.colnames[1:]])
        
        self._ebl_tau_red_interp=np.zeros(len(self._energy))
        self.redshift=zeta
        if self.redshift > self._zarray[-1]:
            print("Redshift outside maximum range!")
            print("Choose between %.2f and %.2f"%(self._zarray[0],self._zarray[-1]))
        for i in range(1,len(self._zarray)):
            if (self.redshift<self._zarray[i]):
                break
        #at the end of the cycle the redshift value is bracketed between i and i-1.
        for j in range(len(self._energy)):
            self._ebl_tau_red_interp[j]=self._tautable[j][i-1]+(self._tautable[j][i]-self._tautable[j][i-1])/(self._zarray[i]-self._zarray[i-1])*(self.redshift-self._zarray[i-1]) #linear interpolation between points
        #print("For this redshift, the Energy Horizon is "+str(self.HorizonEnergy())+" TeV")
    
    
    def GetTauValue(self,energia):
        '''
        Computes the optical depth for a photon of the energy required due to EBL absorption
        energia = energy of the photon in TeV units
        '''
        if (energia>self._energy[len(self._energy)-1]):
            print("WARNING: Energy above the maximum allowed by the model! Returning: inf")
            return np.inf
            # raise ValueError("Energy above the maximum allowed in the EBL model! Exiting")      
        if (energia<self._energy[0]):
            print("WARNING: Energy outside the lower boundary of the model, EBL contribution set to 0.0\n")
            return 0.0
        for i in range(1,len(self._energy)):
            if (energia<self._energy[i]):
                break
        value=self._ebl_tau_red_interp[i-1]+(self._ebl_tau_red_interp[i]-self._ebl_tau_red_interp[i-1])/(self._energy[i]-self._energy[i-1])*(energia-self._energy[i-1])
        return value
    
    
    def EblAbsorb(self,flux,energia):
        '''
        computes gamma-ray flux absorbed by the EBL from intrinsic one
        flux = instrinsic gamma ray flux
        energia = energy of the photons in TeV units
        '''
        gettau=np.vectorize(self.GetTauValue) #vectorizes the function for array inputs
        return flux*np.exp(-gettau(energia))
  
  
    def EblDeabsorb(self,flux,energia):
        '''
        deabsorb from the ebl effect on the observed gamma-ray flux
        flux = gamma ray flux
        energia = energy of the photons in TeV units
        '''
        gettau=np.vectorize(self.GetTauValue) #vectorizes the function for array inputs
        return flux*np.exp(gettau(energia))
    
    
    def HorizonEnergy(self, tol = 0.01):
        '''
        Computes the horizon energy for a particular redshift
        init_val: initial value for the iterative procedure
        Return the energy (in units of TeV) for which the optical depth is 1 +/- tol
        '''
        init_val = 0.02 # start from 20 GeV
        while (self.GetTauValue(init_val) <= 1+tol):
            init_val = init_val*(1+0.01)
        # print(self.GetTauValue(init_val*0.99))
        return init_val*0.99
    

def GetTauValue(model, energy, redshift):
    mod = EblModel(redshift,model)
    return mod.GetTauValue(energy)