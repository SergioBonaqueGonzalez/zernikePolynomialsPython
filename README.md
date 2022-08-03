# zernikePolynomialsPython
Create Zernike polynomials in python.

Created by Sergio Bonaque-Gonzalez.

Optical engineer, PhD.


sergio.bonaque.gonzalez@gmail.com


Example of use:

    import zernikes

    import numpy as np



    RESOLUTION = 512

    NMODES = 20

    AMPLITUDES = np.random.rand(NMODES)



    phase = np.zeros([RESOLUTION,RESOLUTION])

      for i in range(NMODES)

        zernike = AMPLITUDES(i) * zernikes.zernike(i+1, RESOLUTION)
  
        phase += phase
  
  
  
    pupil = circularMask(RESOLUTION)  

    phase *= pupil

