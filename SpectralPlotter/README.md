# SpecralPlotter classes

contents:
spectral_plotter.py -> a little python module to plot (and overplot) best fit confidence intervals given the best fit parameters and the covariance matrix of them obtained with the fit.

It contains a parent class Spectrum with generic routines and a bunch of child classes to load function specific sectra. At the moment the available functional forms are:

* Power law: using the expression F = N_0 * (E/Es)^a) where N_0 is the normalization factor, Es is the energy scale and a is the photon index
* LogParabola: using the expression F = N_0 * (E/Es)^(-a - b*ln(E/Es))

More models will come soon.

The confidence intervals are computed using the error propagation with the analytical computation via the partial derivatives of the fit function with respect to the parameter and the covariance matrix.

# Usage

The usage is very simple. Load the package as:
```python
import spectral_plotter as spectral

powerlaw = spectral.SpectrumPL(pars,s,cov,emin,emax,text)
```
where:
* pars : the list of the best fit parameters
* s : the energy scale chosen for the normalization
* cov : the covariance matrix (t be given as a list of lists)
* emin : minimum energy you want for the spectrum to be shown
* emax : maximum energy you want for the spectrum to be shown
* text : string for the legend in the plot
* (optional argument) energyshift : it introduces a shift in the energy scale (default value is 1)

once the initialization is done, you have plot either the differential spectrum with `plotter_dnde(color)` or directly the sed with `plotter_sed(color)`.

