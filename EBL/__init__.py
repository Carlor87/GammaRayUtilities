import os,sys
import numpy as np

__all__ = ["EblModel"]

class EblModel:
    '''
    Class to consider the contribution of the Extragalactic Background Light (EBL) on gamma ray data,
    In the initialization it is possible to choose between the EBL model developed by Franceschini et al. (2008)
    and the model developed by Dominguez (2011).
    For model 1 (Franceschini,2008), zeta between 0.01 and 3.
    For model 3 (Franceschini,2017), zeta between 0.01 and 3.
    for model 2 (Dominguez,2011), zeta between 0.01 and 2.
    For redshifts lower than these values, the interpolation is done with 0
    and the results might not be accurate
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
        self._model = model
        if (model==1 and zeta<=3):
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
        if (model == 1 and zeta>3):
            raise ValueError("Redshift outside boundary [0-3] for this model!")
    

        if (model==3 and zeta<=3):
            '''
            Franceschini(2017)
            From:
            https://www.aanda.org/articles/aa/abs/2017/07/aa29684-16/aa29684-16.html
            (in the erratum, table 4)
            '''
            self._zarray=[0.01,0.03,0.1,0.3,0.5,1.0,1.5,2.0,2.5,3.0]
            self._energy=[0.00520,0.00631,0.00767,0.00932,0.01132,0.01375,0.01671,0.02030,
                          0.02466,0.02997,0.03641,0.04423,0.05374,0.06529,0.07932,0.09636,
                          0.11708,0.14224,0.17281,0.20995,0.25507,0.30989,0.37650,0.45742,
                          0.55573,0.67516,0.82027,0.99657,1.21076,1.47098,1.78712,2.17122,
                          2.63787,3.20481,3.89360,4.73042,5.74710,6.98230,8.48296,10.3061,
                          12.5211,15.2122,18.4817,22.4539,27.2798,33.1429,40.2661,48.9203,
                          59.4344,72.2083,87.7276,106.582,129.489,157.319,191.131,232.210] #in TeV
            self._tautable=np.array(
                    [[0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00001, 0.00098, 0.00250],
                    [0.00000 , 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00041, 0.00384, 0.00706],
                    [0.00000 , 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00002, 0.00238, 0.01031, 0.01614],
                    [0.00000 , 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00052, 0.00770, 0.02253, 0.03325],
                    [0.00000 , 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00269, 0.01862, 0.04384, 0.06308],
                    [0.00000 , 0.00000, 0.00000, 0.00000, 0.00000, 0.00020, 0.00834, 0.03824, 0.07863, 0.10985],
                    [0.00000 , 0.00000, 0.00000, 0.00000, 0.00000, 0.00144, 0.02010, 0.07046, 0.13069, 0.17634],
                    [0.00000 , 0.00000, 0.00000, 0.00000, 0.00000, 0.00526, 0.04148, 0.11902, 0.20242, 0.26437],
                    [0.00000 , 0.00000, 0.00000, 0.00000, 0.00026, 0.01411, 0.07640, 0.18647, 0.29553, 0.37522],
                    [0.00000 , 0.00000, 0.00000, 0.00006, 0.00168, 0.03132, 0.12823, 0.27492, 0.41267, 0.51353],
                    [0.00000 , 0.00000, 0.00000, 0.00075, 0.00574, 0.06037, 0.19977, 0.38853, 0.56127, 0.68797],
                    [0.00000 , 0.00001, 0.00013, 0.00320, 0.01442, 0.10498, 0.29586, 0.53788, 0.75593, 0.91357],
                    [0.00004 , 0.00015, 0.00090, 0.00881, 0.03012, 0.17000, 0.42821, 0.74227, 1.01767, 1.21240],
                    [0.00017 , 0.00059, 0.00279, 0.01897, 0.05553, 0.26482, 0.61799, 1.02783, 1.37303, 1.60979],
                    [0.00044 , 0.00146, 0.00625, 0.03557, 0.09497, 0.40704, 0.89424, 1.42494, 1.85166, 2.13489],
                    [0.00090 , 0.00292, 0.01196, 0.06187, 0.15657, 0.62209, 1.28834, 1.96569, 2.48455, 2.81862],
                    [0.00164 , 0.00530, 0.02132, 0.10376, 0.25361, 0.93967, 1.83323, 2.68098, 3.30228, 3.69168],
                    [0.00288 , 0.00923, 0.03649, 0.17004, 0.40341, 1.38927, 2.56014, 3.59959, 4.33198, 4.78158],
                    [0.00485 , 0.01543, 0.06030, 0.27160, 0.62492, 1.99735, 3.49334, 4.74466, 5.59439, 6.10519],
                    [0.00785 , 0.02488, 0.09631, 0.42039, 0.93622, 2.78417, 4.65017, 6.12472, 7.09190, 7.66666],
                    [0.01228 , 0.03875, 0.14856, 0.62743, 1.35031, 3.75962, 6.02682, 7.72167, 8.80131, 9.44462],
                    [0.01849 , 0.05813, 0.22045, 0.89889, 1.87116, 4.91140, 7.58655, 9.48565, 10.6756, 11.3903],
                    [0.02671 , 0.08371, 0.31387, 1.23409, 2.49233, 6.20194, 9.26186, 11.3434, 12.6433, 13.4434],
                    [0.03695 , 0.11541, 0.42716, 1.62395, 3.19434, 7.56774, 10.9660, 13.2189, 14.6472, 15.5431],
                    [0.04889 , 0.15213, 0.55633, 2.05458, 3.94206, 8.93147, 12.6258, 15.0605, 16.6643, 17.7073],
                    [0.06195 , 0.19214, 0.69563, 2.50232, 4.69382, 10.2273, 14.2003, 16.9030, 18.7701, 20.0347],
                    [0.07565 , 0.23399, 0.83870, 2.94180, 5.40766, 11.4154, 15.7408, 18.8822, 21.1241, 22.7128],
                    [0.08899 , 0.27442, 0.97492, 3.34713, 6.05113, 12.5223, 17.3990, 21.1526, 23.9144, 25.9438],
                    [0.10138 , 0.31194, 1.09952, 3.70442, 6.61381, 13.6400, 19.3428, 23.8785, 27.3181, 29.8841],
                    [0.11221 , 0.34440, 1.20615, 4.00661, 7.11168, 14.9226, 21.7192, 27.2691, 31.5636, 34.8158],
                    [0.12140 , 0.37194, 1.29529, 4.26781, 7.60245, 16.5345, 24.7027, 31.5446, 37.0071, 41.2633],
                    [0.12901 , 0.39470, 1.37052, 4.52208, 8.16693, 18.5987, 28.5221, 37.1930, 44.2853, 50.0201],
                    [0.13601 , 0.41568, 1.44294, 4.82080, 8.91296, 21.2999, 33.6172, 44.8184, 54.3879, 62.3975],
                    [0.14377 , 0.43949, 1.53147, 5.22872, 9.95027, 24.9165, 40.6821, 55.7377, 69.2046, 80.6985],
                    [0.15419 , 0.47162, 1.65382, 5.81803, 11.3558, 29.9010, 50.8562, 71.9941, 91.3676, 108.244],
                    [0.16911 , 0.51756, 1.83234, 6.62927, 13.2598, 37.1520, 66.2602, 96.9755, 125.369, 150.666],
                    [0.19065 , 0.58408, 2.08465, 7.71468, 15.8888, 47.9635, 90.2827, 135.775, 177.700, 218.111],
                    [0.21876 , 0.67023, 2.41055, 9.20728, 19.6965, 64.8492, 128.281, 195.456, 257.948, 338.714],
                    [0.25607 , 0.78567, 2.85808, 11.3604, 25.5316, 92.0801, 187.290, 285.133, 384.066, 621.861],
                    [0.30752 , 0.94942, 3.50961, 14.7030, 34.7408, 135.263, 275.826, 415.094, 615.195, 1451.43],
                    [0.38586 , 1.19616, 4.50601, 20.0272, 49.6450, 200.724, 399.269, 608.090, 1175.933,3855.73],
                    [0.51166 , 1.59762, 6.14335, 28.6023, 73.4936, 293.144, 563.797, 952.984, 2741.434,9943.42],
                    [0.71277 , 2.23537, 8.72773, 42.3560, 109.697, 414.810, 786.935, 1776.48, 6841.312, np.inf],
                    [1.03624 , 3.25844, 12.9010, 63.5006, 160.938, 565.925, 1156.41, 3963.61, np.inf ,  np.inf],
                    [1.55756 , 4.90160, 19.4448, 93.6672, 227.793, 749.334, 2000.75, 9319.26, np.inf ,  np.inf],
                    [2.33730 , 7.33367, 28.8458, 133.104, 308.522, 1013.70, 4181.95, np.inf,  np.inf ,  np.inf],
                    [3.40014 , 10.6261, 41.1443, 180.335, 400.080, 1548.18, 9404.14, np.inf,  np.inf ,  np.inf],
                    [4.72388 , 14.6948, 55.8835, 233.223, 505.738, 2907.47, np.inf , np.inf,  np.inf ,  np.inf],
                    [6.23960 , 19.3110, 72.1970, 290.373, 660.765, 6283.00, np.inf , np.inf,  np.inf ,  np.inf],
                    [7.82189 , 24.1678, 89.2541, 364.018, 1014.58, np.inf , np.inf , np.inf,  np.inf ,  np.inf],
                    [9.50683 , 29.3591, 109.080, 522.730, 1997.66, np.inf , np.inf , np.inf,  np.inf ,  np.inf],
                    [11.8962 , 37.2086, 147.522, 996.470, 4510.25, np.inf , np.inf , np.inf,  np.inf ,  np.inf],
                    [18.3001 , 59.3783, 268.848, 2318.77, 9990.42, np.inf , np.inf , np.inf,  np.inf ,  np.inf],
                    [39.6796 , 132.463, 642.223, 5410.71, np.inf , np.inf , np.inf , np.inf,  np.inf ,  np.inf],
                    [99.7780 , 333.153, 1579.26, np.inf , np.inf , np.inf , np.inf , np.inf,  np.inf ,  np.inf],
                    [235.983 , 777.945, 3498.49, np.inf , np.inf , np.inf , np.inf , np.inf , np.inf ,  np.inf]]).T
            self._ebl_tau_red_interp=np.zeros(len(self._energy))
            self.redshift=zeta
            for i in range(len(self._zarray)-1):
                if (self.redshift<self._zarray[i]):
                    break
                #at the end of the cycle the redshift value is bracketed between i and i-1.
                for j in range(len(self._energy)):
                    self._ebl_tau_red_interp[j]=self._tautable[i-1][j]+(self._tautable[i][j]-self._tautable[i-1][j])/(self._zarray[i]-self._zarray[i-1])*(self.redshift-self._zarray[i-1]) #linear interpolation between points
        if (model == 1 and zeta>3):
            raise ValueError("Redshift outside boundary [0-3] for this model!")
    
        if (model == 2 and zeta <= 2):
            '''
            Dominguez(2011)
            '''
            self._fil=open("/home/cromoli/Documents/GammaRayUtilities/EBL/ebl_dominguez_tau.dat",'r') #depends on external file
            self._zarray=np.array([0.01      ,  0.02526316,  0.04052632,  0.05578947,  0.07105263,
                                   0.08631579,  0.10157895,  0.11684211,  0.13210526,  0.14736842,
                                   0.16263158,  0.17789474,  0.19315789,  0.20842105,  0.22368421,
                                   0.23894737,  0.25421053,  0.26947368,  0.28473684,  0.3       ,
                                   0.35      ,  0.4       ,  0.45      ,  0.5       ,  0.55      ,
                                   0.6       ,  0.65      ,  0.7       ,  0.75      ,  0.8       ,
                                   0.85      ,  0.9       ,  0.95      ,  1.        ,  1.2       ,
                                   1.4       ,  1.6       ,  1.8       ,  2.        ])
            temp=self._fil.read()
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
                
                
        if (model == 2 and zeta>2):
            raise ValueError("Redshift outside boundary [0-2] for this model!")
        
        
        if (model != 1 and model != 2 and model !=3):
            print("Allowed numbers are only:\n1- (Franceschini, 2008) or\n2- (Dominguez, 2011)\nPlease choose either 1 or 2")
            raise ValueError("Wrong model number!")
        print("For this redshift, the Energy Horizon is "+str(self.HorizonEnergy())+" TeV")
    
    
    def GetTauValue(self,energia):
        '''
        Computes the optical depth for a photon of the energy required due to EBL absorption
        energia = energy of the photon in TeV units
        '''
        if (energia>self._energy[len(self._energy)-1]):
            print("WARNING: Energy above the maximum allowed by the model! Returning: inf")
            return np.inf
            #raise ValueError("Energy above the maximum allowed in the EBL model! Exiting")
      
        if (energia<self._energy[0]):
            print("WARNING: Energy outside the lower boundary of the model, EBL contribution set to 0.0\n")
            return 0.0
        for i in range(len(self._energy)):
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
        Return the energy for which the optical depth is 1 +/- tol
        '''
        init_val = 0
        if self._model == 1:
            init_val = 0.02
        if self._model == 2:
            init_val = 0.01
        if self._model == 3:
            init_val = 0.02
        while (self.GetTauValue(init_val) <= 1+tol):
            init_val = init_val*(1+0.01)
        print(self.GetTauValue(init_val*0.99))
        return init_val*0.99
    
