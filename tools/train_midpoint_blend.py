"""Fit a bounded linear blend model on translated, overlapping synthetic layers."""
import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.optimize import minimize

def samples(seed, scenes):
    rng = np.random.default_rng(seed)
    rows = []
    y, x = np.mgrid[:64, :96]
    for _ in range(scenes):
        textures = [gaussian_filter(rng.random((64,96,3)), (1,1,0))*1.8-.4 for _ in range(2)]
        shifts = rng.integers(-6,7,(2,2))
        def scene(t):
            xx, yy = x-48-t*shifts[1,0], y-32-t*shifts[1,1]
            mask = (xx/24)**2+(yy/18)**2 < 1
            layers = [im[(y-t*dy)%64,(x-t*dx)%96] for im,(dx,dy) in zip(textures,shifts)]
            return np.clip(np.where(mask[:,:,None], layers[1], layers[0]),0,1),mask
        prev,_ = scene(-1)
        target,mask = scene(0)
        cur,_ = scene(1)
        # Include block boundaries and wrong vectors as well as correct matches.
        block = np.repeat(np.repeat(mask[8::16,8::16],16,0),16,1)
        dx,dy = np.where(block[:,:,None],shifts[1],shifts[0]).transpose(2,0,1)
        if rng.random()<0.45:
            dx = dx+rng.integers(-3,4)
        a = prev[(y-dy)%64,(x-dx)%96]
        b = cur[(y+dy)%64,(x+dx)%96]
        distance=lambda v: abs(v) @ [0.299,0.587,0.114]
        mismatch=distance(a-b)
        change=distance(cur-prev)
        smooth=lambda z: (lambda v:v*v*(3-2*v))(np.clip(z,0,1))
        confidence=1-smooth((gaussian_filter(mismatch,4)-.035)/.095)
        base=confidence*(1-smooth((mismatch-.04)/.12))*smooth((change-.002)/.018)
        diff=(a+b)*.5-cur
        features=np.stack([np.ones_like(change),confidence,mismatch,change],axis=-1)
        idx=(confidence>0)&(change>.002)
        rows.append(np.column_stack((features[idx],diff[idx],(cur-target)[idx],base[idx]))[::8])
    return np.concatenate(rows)

def score(data,alpha):
    return np.mean((data[:,7:10]+data[:,4:7]*alpha[:,None])**2)

if __name__=='__main__':
    tr=samples(2201,100)
    def pred(d,w):
        # At uncertain motion boundaries trust the decoded frame.
        gate=np.minimum(1,4*d[:,1])*np.clip((.40-d[:,2])/.16,0,1)
        return gate/(1+np.exp(-np.clip(d[:,:4]@w,-12,12)))
    w=minimize(lambda w:score(tr,pred(tr,w)),[.5,.5,-1,1],method='L-BFGS-B',bounds=[(-8,8)]*4,options={'gtol':1e-10,'ftol':1e-13}).x
    w=np.round(w,5)
    test=samples(9987,48)
    print(w,score(test,test[:,-1]),score(test,pred(test,w)))
    assert score(test,pred(test,w)) < score(test,test[:,-1])
    print('Weights are ordered as bias, motion confidence, warp mismatch, source change.')
