# GammaRayUtilities
Set of scripts and small libraries developed for data analysis in gamma ray astrophysics

This repository has the purpose of collecting some of the scripts and small libraries I have developed during these years as a PhD student (and post-doc) in gamma ray astrophysics. The language I used was Python (mostly python2, but I have rewritten a lot to use python 3 as well).

The material (of different nature) is divided in various self-contained folders that are described below (this file will be updated together with the folders I will upload)

# 1- EBL
Small package that computes the absorption (and the deabsorption) of the flux of a gamma ray source due to the effect of the extragalactic background light (EBL). The class allows to choose between 7 different EBL models:
 - Franceschini, 2008 (from [this](https://ui.adsabs.harvard.edu/abs/2008A%26A...487..837F/abstract) paper)
 - Franceschini, 2017 (from [this](https://ui.adsabs.harvard.edu/abs/2017A%26A...603A..34F/abstract) and [this](https://ui.adsabs.harvard.edu/abs/2018A%26A...614C...1F/abstract) paper)
 - Dominguez, 2011 (from [this](https://ui.adsabs.harvard.edu/abs/2011MNRAS.410.2556D/abstract) paper)
 - Gilmore, 2012 (from [this](https://ui.adsabs.harvard.edu/abs/2012MNRAS.422.3189G/abstract) paper)
 - Finke, 2010 (from [this](https://ui.adsabs.harvard.edu/abs/2010ApJ...712..238F/abstract) paper)
 - Kneiske & Dole, 2010 (from [this](https://ui.adsabs.harvard.edu/abs/2010A%26A...515A..19K/abstract) paper) - the tabulated data are from [this](https://github.com/fermi-lat/celestialSources/tree/master/eblAtten/data) link actually
 - Inoue et al., 2013 (from [this](https://ui.adsabs.harvard.edu/abs/2013ApJ...768..197I/abstract) paper) - the tabulated data are from [this](https://github.com/fermi-lat/celestialSources/tree/master/eblAtten/data) link actually

There is implemented the function to compute the optical depth given energy and redshift and also the Horizon energy for a given redshift (energy where the optical depth tau = 1 for a given redshift).
