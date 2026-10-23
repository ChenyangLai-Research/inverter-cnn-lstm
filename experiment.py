import numpy as np
import torch
from scipy.io import loadmat
from model import CNNLSTM
from runtime import tensor,normalize,require,fit,finish

def run(a):
    if a.demo:
        rng=np.random.default_rng(a.seed);xs=[];ys=[]
        for _ in range(12):
            t=np.arange(400)/100;angle=np.sin(t)+rng.uniform(0,.2);v=np.cos(t);omega=np.gradient(angle,.01)
            x=np.column_stack([v,-.95765*np.sin(4*angle),omega]);xs.append(x);ys.append((.2*v+.1*omega)[:,None])
    else:
        d=loadmat(require(a.data_root,'all_materials/master_thesis_Aruna/master_thesis_Aruna/model_comparison_torino/data/sin.mat'))
        xs=[];ys=[]
        for i in range(d['VAs'].shape[1]):
            angle=d['thetaMs'][1:,i];x=np.column_stack([d['VAs'][1:,i],-.95765*np.sin(4*angle),d['DTheta_ms'][1:,i]])
            xs.append(x);ys.append(d['IAs'][1:,i,None])
    split=int(2*len(xs)/3)
    from sklearn.preprocessing import MinMaxScaler
    sx=MinMaxScaler().fit(np.concatenate(xs[:split]));sy=MinMaxScaler().fit(np.concatenate(ys[:split]))
    def windows(seq,labels):
        result=[]
        per=max(1,a.max_samples//len(seq))
        for x,y in zip(seq,labels):
            xx=sx.transform(x);yy=sy.transform(y)
            for end in np.linspace(30,len(x),min(per,len(x)-29),dtype=int):result.append((xx[end-30:end],yy[end-1]))
        return tensor(np.stack([r[0] for r in result])),tensor(np.stack([r[1] for r in result]))
    x,y=windows(xs[:split],ys[:split]);xv,yv=windows(xs[split:],ys[split:]);model=CNNLSTM()
    def loss(idx):
        mse=(model(x[idx])-y[idx]).square().mean();return mse,{'current_reconstruction':mse}
    history=fit(model,loss,len(x),a);model.eval()
    with torch.no_grad():pred=model(xv).numpy()
    return finish(model,a,history,pred,yv.numpy(),{'task':'phase current reconstruction','port':'TensorFlow architecture to PyTorch','window':30,'split':'complete simulation columns, before windowing'}, {'inputs':sx,'current':sy})
