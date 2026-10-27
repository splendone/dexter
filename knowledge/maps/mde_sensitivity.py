import numpy as np
rng = np.random.default_rng(7)

def power(T,n,s,delta,paired=True,st=0.20,si=0.15,reps=1500,alpha=0.05):
    def stats(d):
        out=np.empty(reps)
        for r in range(reps):
            p=np.clip(rng.normal(.5,st,(T,1)),.05,.95)
            u=rng.normal(0,si,(T,s*n))
            pb=np.clip(p+u,0,1)
            pt=np.clip(p+(u if paired else rng.normal(0,si,(T,s*n)))+d,0,1)
            dt=(rng.random((T,s*n))<pt).mean(1)-(rng.random((T,s*n))<pb).mean(1)
            out[r]=dt.mean()/(dt.std(ddof=1)/np.sqrt(T)+1e-12)
        return out
    crit=np.quantile(np.abs(stats(0)),1-alpha)
    return float((np.abs(stats(delta))>crit).mean())

print("A. 敏感性:sigma_task / sigma_init 对 MDE 的影响(T=20,n=50,s=3,配对)")
for st in [0.10,0.20,0.30]:
    row=[]
    for si in [0.05,0.15,0.30]:
        lo,hi=0,.3
        for _ in range(12):
            m=(lo+hi)/2
            if power(20,50,3,m,st=st,si=si,reps=500)>=.8: hi=m
            else: lo=m
        row.append(f"{hi*100:5.1f}")
    print(f"  sigma_task={st:.2f}  sigma_init 0.05/0.15/0.30 -> MDE(pp) {' '.join(row)}")

print()
print("B. 单 seed 下要多少 rollout 才能测出 5pp(T=20,s=1,配对)")
for n in [20,50,100,200,400]:
    print(f"  n={n:3d}  power@5pp={power(20,n,1,.05,reps=1500):.2f}")

print()
print("C. 配对 vs 不配对,低 rollout 时差距最大(T=20,s=1,delta=5pp)")
for n in [10,20,50]:
    pp=power(20,n,1,.05,paired=True,reps=1500); pu=power(20,n,1,.05,paired=False,reps=1500)
    print(f"  n={n:2d}  配对 {pp:.2f}  不配对 {pu:.2f}  差 {pp-pu:+.2f}")
