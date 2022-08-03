"""
@author: sergio Bonaque-Gonzalez, PhD
sergio.bonaque.gonzalez@gmail.com
"""
import numpy as np
import math 
from scipy.linalg import lstsq

def circularMask(resolution):
    xp = np.linspace(-1,1,resolution)
    X,Y = np.meshgrid(xp,xp)
    rho = np.sqrt(X**2 + Y**2).astype('float64')
    pupil = np.ones(np.shape(rho))
    pupil[rho>1] = 0
    return pupil
 
   
def parity(number):
    if number%2 == 0:
        p = True
    else:
        p = False
    return p
    

def indexes(jfin):
    n_gra = np.zeros(jfin + 100)
    m_azi = np.zeros(jfin + 100)
    n = 1
    j = 0
    while j <= jfin:
        for mm in range(n + 1):
            j = int(((n * (n + 1))/2) + mm + 1)
            if parity(n) != parity(mm):
                m = mm + 1
            else:
                m = mm
            n_gra[j - 1] = n
            m_azi[j - 1] = m
        n=n+1
    
    ngra = n_gra[jfin - 1]
    mazi = m_azi[jfin - 1]
    return int(ngra), int(mazi)


def zer_rad(ro,n,m):
    rr = np.zeros(np.shape(ro))
    ddif = int(np.round((n - m) / 2))
    dsum = int(round((n + m) / 2))
    for s in range(ddif + 1):
        numer = ((-1.0)**s) * math.factorial(n - s)
        denom = math.factorial(s) * math.factorial(dsum - s) * math.factorial(ddif - s)
        rr = rr + ((ro**(n - (2 * s)) * numer) / denom)
    return rr
 

def zernike(j,dim):
    temp = np.zeros([dim,dim])
    xx = np.zeros([dim,dim])
    yy = np.zeros([dim,dim])
    tdim = dim / 2
    xx[:] = np.arange(-tdim,tdim,1)
    yy = xx.transpose()
    tdim = tdim - 1
    ro = np.sqrt(xx * xx + yy * yy).astype('float64') / tdim
    teta = np.arctan2(yy,xx).astype('float64')
    n,m = indexes(j)
    mask = circularMask(dim)
    
    if m == 0:
        temp = np.sqrt(n + 1)*zer_rad(ro,n,m) * mask
    if m != 0:
        if parity(j) == True:
            temp = np.sqrt((2 * n) + 2).astype('float64') * zer_rad(ro,n,m) * np.cos(m * teta).astype('float64') * mask
        elif parity(j) == False:
            temp = np.sqrt((2 * n) + 2).astype('float64') * zer_rad(ro,n,m) * np.sin(m * teta).astype('float64') * mask
    
    return temp


def phase(nModes,dim,wave):
    coef = np.random.random(nModes)
    temp = np.zeros([dim,dim])
    for i in range(nModes):
        #temp = temp + coef[i] * (wave / (2 * np.pi)) * zernike(i + 1,dim)
        temp = temp + coef[i] * zernike(i + 1,dim)
    return temp,coef

   
def ANSItoNOLL(index):
    Noll = np.array([1, 3, 2, 5, 4, 6, 9, 7, 8, 10, 15, 13, 11, 12, 14, 21, 19, 17, 16, 18, 20, 27, 25, 23, 22, 24, 26, 28, 35, 33, 31, 29, 30, 32, 34, 36, 45, 43, 41, 39, 37, 38, 40, 42, 44, 55, 53, 51, 49, 47, 46, 48, 50, 52, 54, 65, 63, 61, 59, 57, 56, 58, 60, 62, 64, 66, 77, 75, 73, 71, 69, 67, 68, 70, 72, 74, 76, 78, 91, 89, 87, 85, 83, 81, 79, 80, 82, 84, 86, 88, 90, 105, 103, 101, 99, 97, 95, 93, 92, 94, 96, 98, 100, 102, 104, 119, 117, 115, 113, 111, 109, 107, 106, 108, 110, 112, 114, 116, 118, 120])
    return Noll[index]


