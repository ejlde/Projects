import numpy as np
import matplotlib.pyplot as plt
import imageio
from scipy.fftpack import fftn,ifftn,fftshift

## Need to know about blur and noise

###
"""
Degradation and Point Spread F'n
"""
x = np.arange(-2,2,0.05)
# sigma = dispersion of the values as it grows the optimal 
# distribution is approached
sigma = 0.5
gauss1d_1 = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-(np.square(x/sigma)))
plt.plot(x,gauss1d_1,'r')
#plt.show()

def gaussian_filter(k=5,sigma=1.0):
    """ Gaussian Filter
    :k: laterial size of filter
    :sigma: standard deviation (dispersion of the gaussian dist)
    :return matrix with a filter [kxk] used in covolution    
    """
    arx = np.arange((-k//2) + 1.0 , (k//2)+1.0)
    x,y = np.meshgrid(arx,arx)
    filt = np.exp(-(1/2)*(np.square(x)+np.square(y))/np.square(sigma))
    return filt/ np.sum(filt)

g1 = gaussian_filter(k=5,sigma=0.9)
#print(g1)

###
"""
    Simulating Blur
"""
# G(u)= = F(u)*H(u)
f = imageio.v2.imread("reconimage.png")
h = gaussian_filter(k=7,sigma=2.5)

# computing the number of padding on one side
a = int(f.shape[0]//2 - h.shape[0]//2)
h_pad = np.pad(h,(a,a-1),'constant',constant_values=(0))

# computing the fourier transforms
F = fftn(f)
H = fftn(h_pad)

# plt.subplot(121)
# plt.imshow(np.log(np.abs(F)+1),cmap="gray")
# plt.subplot(122)
# plt.imshow(np.log(np.abs(H)+1),cmap="gray")

# convolution
# G = np.multiply(F,H)

# Inverse Transform





# F_hat = G/H
# f_hat = original image
# G = recon image
# H = degradation fn

##
#
# F_hat = np.divide(G,H)
# f_hat = ifftn(F_hat).real
# plt.imshow(f_hat,cmap="gray")

