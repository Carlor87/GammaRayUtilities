import os,sys
import numpy as np

class redshift:
  '''
  Class to consider the contribution of the Extragalactic Background Light (EBL) on gamma ray data,
  In the initialization it is possible to choose between the EBL model developed by Franceschini et al. (2008)
  and the model developed by Dominguez (2011).
  '''
    
  def __init__(self,zeta,model):
    '''
    zeta = redshift of the gamma-ray source
    for model 1, zeta between 0.01 and 3.
    for model 2, zeta between 0.01 and 2.
    lower redshifts are interpolated with 0 -> might not be very accurate
    model = {1,2} to choose the EBL model:
      choose model==1 for Franceschini,2008
      choose model==2 for Dominguez,2011
    '''
    if model==1:
      '''
      Franceschini(2008)
      '''
      self._zarray=[0.01,0.03,0.1,0.3,0.5,1.0,1.5,2.0,3.0]
      self._energy=[0.0200,0.0240,0.0289,0.0347,0.0417,0.0502,0.0603,0.0726,0.0873,0.104 ,0.126 ,0.151 ,0.182 ,0.219 ,0.263 ,0.316 ,0.381 ,0.458 ,0.550 ,0.662 ,0.796 ,0.957 , 1.15 , 1.38 , 1.66 , 2.000, 2.40 , 2.89 ,3.47 , 4.17 , 5.02 , 6.03 , 7.26 , 8.73 , 10.5 , 12.6 , 15.2 , 18.2 , 21.9 , 26.4 , 31.7 , 38.1 , 45.8 , 55.1 , 66.2 , 79.6 , 95.7 , 115. , 138. , 166. ] #in TeV
      self._tautable=np.array([[0.0000,   0.0000,   0.0000,  0.000000,  0.0000021,  0.00493,      0.0399,      0.1157, 0.2596],
                    [0.0000,   0.0000,   0.0000,  0.000000,  0.000188,   0.01284,     0.0718,      0.1783, 0.3635],
                    [0.0000,   0.0000,   0.0000,  0.000000,  0.001304,   0.0279   ,   0.1188,      0.2598, 0.4919],
                    [0.0000,   0.0000,   0.0000,  0.000488, 0.004558,0.0533       ,  0.1833,      0.3635, 0.6517],
                    [0.0000,   0.0000,   5.254E-05, 0.002276,  0.01157,0.0921     ,    0.2689   ,      0.4967, 0.8548],
                    [0.0000,      9.445E-05,5.408E-04, 0.006575,  0.02436,0.1480  ,   0.3836,      0.6745, 1.118 ],
                    [1.0976E-04,  4.241E-04,1.915E-03, 0.014592,  0.04512,0.2275  ,       0.5434,      0.9179, 1.465], 
                    [3.0882E-04,  1.103E-03,4.548E-03, 0.02771,   0.07684,0.3430  ,       0.7707,      1.251, 1.917 ],
                    [6.5619E-04,  2.258E-03,8.903E-03, 0.04808,   0.1248,0.5137   ,      1.092,      1.703, 2.503 ],
                    [1.2130E-03,  4.097E-03,1.582E-02, 0.07958,   0.1984,0.7640   ,      1.537,      2.302, 3.249 ],
                    [2.1063E-03,  7.039E-03,2.685E-02, 0.1284 ,   0.3109,1.120,       2.133,      3.073, 4.181 ],
                    [3.5291E-03,  1.167E-02,4.406E-02, 0.2031 ,   0.4780,1.607,       2.905,      4.042, 5.318 ],
                    [5.7051E-03,  1.872E-02,7.010E-02, 0.3134 ,   0.7163,2.247,       3.875,      5.225, 6.673 ],
                    [8.9183E-03,  2.907E-02,0.1082   , 0.4696 ,   1.040,3.056,       5.055,      6.627, 8.241 ],
                    [1.3517E-02,  4.378E-02,0.1618   , 0.6809 ,   1.461,4.042,       6.438,      8.226, 9.997 ],
                    [1.9793E-02,  6.367E-02,0.2338   , 0.9517 ,   1.981,5.192,       7.989,      9.977, 11.89 ],
                    [2.7938E-02,  8.935E-02,0.3256   , 1.281 ,   2.594,6.474,       9.650,      11.81, 13.89],
                    [3.7957E-02,  0.1205,0.4356   , 1.661  ,   3.284,7.836,       11.34,      13.67, 15.93 ],
                    [4.9558E-02,  0.1563,0.5607   , 2.082  ,   4.023,9.214,       13.01,      15.51, 18.08 ],
                    [6.2291E-02,  0.1953,0.6961   , 2.524  ,   4.779,10.55,       14.63,      17.39, 20.45 ],
                    [7.5753E-02,  0.2364,0.8373   , 2.967  ,   5.517,11.82,       16.25,      19.49, 23.27 ],
                    [8.9194E-02,  0.2768,0.9750   , 3.389  ,   6.210,13.03,       18.04,      22.02, 26.81 ],
                    [0.1019,  0.3152,1.105,  3.779 ,    6.846,14.29,       20.21,      25.22, 31.33 ],
                    [0.1136,  0.3501,1.223,  4.129 ,    7.432,15.73,       22.98,      29.37, 37.23 ],
                    [0.1240,  0.3810,1.327,  4.444 ,    8.010,17.54,       26.58,      34.78, 45.09 ],
                    [0.1329,  0.4076,1.419,  4.747 ,    8.652,19.87,       31.31,      41.95, 55.80 ],
                    [0.1409,  0.4318,1.504,  5.079 ,    9.452,22.96,       37.67,      51.72, 70.71 ],
                    [0.1486,  0.4560,1.596,  5.498 ,    10.52,27.08,       46.30,      65.17, 92.14 ],
                    [0.1579,  0.4863,1.714,  6.075 ,    11.96,32.66,       58.24,      84.48, 124.0 ],
                    [0.1710,  0.5284,1.879,  6.875 ,    13.92,40.39,       75.45,      113.2, 172.1 ],
                    [0.1896,  0.5887,2.113,  7.952 ,    16.57,51.39,       101.3,      157.7, 245.9 ],
                    [0.2162,  0.6732,2.431,  9.421 ,    20.24,67.70,       141.4,      227.3, 357.0 ],
                    [0.2512,  0.7847,2.858,  11.45 ,    25.57,92.73,       204.9,      335.3, 519.3 ],
                    [0.3017,  0.9447,3.464,  14.41 ,    33.52,132.2,       304.3,      496.4, 747.0 ],
                    [0.3732,  1.171 ,4.334,  18.87 ,    45.81,195.0,       454.1,      724.1, 1048. ],
                    [0.4795,  1.513 ,5.663,  25.76 ,    65.21,292.5,       666.6,      1027., 1426. ],
                    [0.6455,  2.048 ,7.723,  36.60 ,    95.98,435.4,       948.5,      1407., 1873. ],
                    [0.8984,  2.871 ,10.93,  53.79 ,    143.7,630.5,       1299.,      1852., 2372. ],
                    [1.297 ,  4.162 ,15.99,  80.41 ,    214.3,878.2,       1705.,      2339., 2897. ],
                    [1.917 ,  6.177 ,23.86,  119.9 ,    311.5,1172.,       2145.,      2843., 3412. ],
                    [2.856 ,  9.181 ,35.47,  174.8 ,    435.3,1494.,       2587.,      3323., 3887. ],
                    [4.211 ,  13.47 ,51.78,  245.0 ,    580.9,1824.,       3004.,      3752., 4303. ],
                    [6.038 ,  19.14 ,72.76,  327.4 ,    739.9,2134.,       3362.,      4102., 4618. ],
                    [8.285 ,  26.00 ,97.51,  416.9 ,    899.0,2403.,       3638.,      4352., 4835. ],
                    [10.82 ,  33.59 ,124.3,  506.3 ,    1045.,2616.,       3825.,      4499., 4940. ],
                    [13.48 ,  41.42 ,151.2,  587.7 ,    1169.,2756.,       3915.,      4540., 4945. ],
                    [16.04 ,  48.81 ,175.8,  655.4 ,    1263.,2823.,       3915.,      4540., 4945. ],
                    [18.24 ,  54.98 ,195.8,  705.7 ,    1320.,2823.,       3915.,      4540., 4945. ],
                    [20.01 ,  59.82 ,210.8,  735.5 ,    1340.,2823.,       3915.,      4540., 4945. ],
                    [21.20 ,  63.03 ,219.8,  744.0 ,    1340.,2823.,       3915.,      4540., 4945. ]]).T
      self._ebl_tau_red_interp=np.zeros(len(self._energy))
      self.redshift=zeta
      for i in range(len(self._zarray)-1):
        if (self.redshift<self._zarray[i]):
          break
          #at the end of the cycle the redshift value is bracketed between i and i-1.
      for j in range(len(self._energy)):
        self._ebl_tau_red_interp[j]=self._tautable[i-1][j]+(self._tautable[i][j]-self._tautable[i-1][j])/(self._zarray[i]-self._zarray[i-1])*(self.redshift-self._zarray[i-1]) #linear interpolation between points
    
    if model == 2:
      '''
      Dominguez(2011)
      '''
      self.fil=open("ebl_dominguez_tau.dat",'r') #depends on external file
      self._zarray=np.array([ 0.01      ,  0.02526316,  0.04052632,  0.05578947,  0.07105263,\
                              0.08631579,  0.10157895,  0.11684211,  0.13210526,  0.14736842,\
                              0.16263158,  0.17789474,  0.19315789,  0.20842105,  0.22368421,\
                              0.23894737,  0.25421053,  0.26947368,  0.28473684,  0.3       ,\
                              0.35      ,  0.4       ,  0.45      ,  0.5       ,  0.55      ,\
                              0.6       ,  0.65      ,  0.7       ,  0.75      ,  0.8       ,\
                              0.85      ,  0.9       ,  0.95      ,  1.        ,  1.2       ,\
                              1.4       ,  1.6       ,  1.8       ,  2.        ])
      temp=self.fil.read()
      temp=temp.split()
      temp=temp[79:]
      temp2=list(temp)
      ener=[]
      for i in range(int(len(temp)/40)):
        ener.append(float(temp[40*i]))
        temp2.pop(40*i-i)
      self._energy=np.array(ener)  ###energy in TeV
      temp2=[float(i) for i in temp2]
      self._tautable=np.array(temp2).reshape((50,39)).T
      self._ebl_tau_red_interp=np.zeros(len(self._energy))
      self.redshift=zeta
      for i in range(len(self._zarray)-1):
        if (self.redshift<self._zarray[i]):
          break
          #at the end of the cycle the redshift value is bracketed between i and i-1.
      for j in range(len(self._energy)):
        self._ebl_tau_red_interp[j]=self._tautable[i-1][j]+(self._tautable[i][j]-self._tautable[i-1][j])/(self._zarray[i]-self._zarray[i-1])*(self.redshift-self._zarray[i-1]) #linear interpolation between points
    if (model != 1 and model != 2):
      print "Allowed numbers are only 1 (Franceschini, 2008) or 2 (Dominguez, 2011)\nPlease choose either 1 or 2\n"
      

    
    
    
  def GetTauValue(self,energia):
    '''
    Computes the optical depth for a photon of the energy required due to EBL absorption
    energia = energy of the photon in TeV units
    '''
    if (energia>self._energy[len(self._energy)-1]):
      raise ValueError("Energy above the maximum allowed in the EBL model! Exiting")
      
    if (energia<self._energy[0]):
      print "WARNING: Energy outside the lower boundary of the model, EBL contribution set to 0.0\n"
      return 0.0
    for i in range(len(self._energy)):
      if (energia<self._energy[i]):
        break
    value=self._ebl_tau_red_interp[i-1]+(self._ebl_tau_red_interp[i]-self._ebl_tau_red_interp[i-1])/(self._energy[i]-self._energy[i-1])*(energia-self._energy[i-1])
    return value;
    
  def ebl_absorb(self,flux,energia):
    '''
    computes gamma-ray flux absorbed by the EBL from intrinsic one
    flux = instrinsic gamma ray flux
    energia = energy of the photons in TeV units
    '''
    gettau=np.vectorize(self.GetTauValue) #vectorizes the function for array inputs
    return flux*np.exp(-gettau(energia))
  
  def ebl_deabsorb(self,flux,energia):
    '''
    deabsorb from the ebl effect on the observed gamma-ray flux
    flux = gamma ray flux
    energia = energy of the photons in TeV units
    '''
    gettau=np.vectorize(self.GetTauValue) #vectorizes the function for array inputs
    return flux*np.exp(gettau(energia))

