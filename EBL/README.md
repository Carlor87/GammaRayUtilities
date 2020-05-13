# EBL module

contents:
\_\_init\_\_.py -> python file with the class redshift to initialize the EBL model. It has the possibility to choose between 7 different EBL models.

folder models -> data files for all the EBL models available.

The model from Finke and Dominguez are actually extracted from their implementation in the software gammapy (extracted by Edna Ruiz)

The model from Kneiske&Dole and Inoue et al. are form [here](https://github.com/fermi-lat/celestialSources/tree/master/eblAtten/data)

The rest come form the original papers

# Usage

The usage is very simple. Load the package as:
```python
import EBL

redshift = 0.5
model = 1 #Franceschini 2008

ebl = EBL.EblModel(redshift,model)
```

Once the class is initializated, there are a couple of basic built-in methods like:
* ```GetTauValue(energy)``` which computes the optical depth at a given energy (given in units of TeV)
* ```EblAbsorb(flux,energy)``` and ```EblDeabsorb(flux,energy)``` which return directly the absorbed (deabsorbed) flux given a certain energy (always in TeV)
* ```HorizonEnergy(tol=0.01)``` which computes the energy where the optical depth parameter ![$\tau = 1$](https://render.githubusercontent.com/render/math?math=%24%5Ctau%20%3D%201%24) (within the tolerance ```tol```)

There is also a static method ```GetTauValue(model,energy,redshift)``` which computes directly the optical depth by automatically initializating the class
