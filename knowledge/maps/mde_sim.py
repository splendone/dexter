import numpy as np

rng = np.random.default_rng(20261027)

def sim(T, n, s, delta, paired=True, sigma_task=0.20, sigma_init=0.15, reps=3000, alpha=0.05):
    """T tasks, n rollouts/task/seed, s seeds. Returns power.
    paired: both arms share the same init states (same episode).
    sigma_task: between-task difficulty sd (in probability units)
    sigma_init: between-init-state sd within task
    """
    # null distribution for the per-task-difference t statistic
    def stats(delta_):
        d = np.empty(reps)
        for r in range(reps):
            p = np.clip(rng.normal(0.5, sigma_task, size=(T, 1)), 0.05, 0.95)   # task difficulty
            u = rng.normal(0, sigma_init, size=(T, s*n))                          # init-state difficulty
            pb = np.clip(p + u, 0, 1)
            if paired:
                pt = np.clip(p + u + delta_, 0, 1)                                # same u
            else:
                u2 = rng.normal(0, sigma_init, size=(T, s*n))
                pt = np.clip(p + u2 + delta_, 0, 1)
            yb = rng.random((T, s*n)) < pb
            yt = rng.random((T, s*n)) < pt
            dt = yt.mean(1) - yb.mean(1)                                          # per-task diff
            d[r] = dt.mean() / (dt.std(ddof=1) / np.sqrt(T) + 1e-12)
        return d

    null = stats(0.0)
    crit = np.quantile(np.abs(null), 1 - alpha)
    alt = stats(delta)
    return float((np.abs(alt) > crit).mean()), float(crit)

def mde(T, n, s, paired=True, target=0.80, lo=0.0, hi=0.30):
    for _ in range(14):
        mid = (lo + hi) / 2
        pw, _ = sim(T, n, s, mid, paired=paired, reps=800)
        if pw >= target: hi = mid
        else: lo = mid
    return hi

configs = [
    ("LIBERO 默认       T=20 n=20 s=1", 20, 20, 1, True),
    ("仅加 rollout      T=20 n=50 s=1", 20, 50, 1, True),
    ("我方计划          T=20 n=50 s=3", 20, 50, 3, True),
    ("任务减半          T=10 n=50 s=3", 10, 50, 3, True),
    ("任务加倍          T=40 n=50 s=3", 40, 50, 3, True),
    ("★不配对(各跑各的)T=20 n=50 s=3", 20, 50, 3, False),
]
print(f"{'配置':38s} {'MDE(pp, 80%功效)':>16s}")
for name, T, n, s, pr in configs:
    m = mde(T, n, s, paired=pr)
    print(f"{name:38s} {m*100:>14.1f}")

print()
print("固定 delta=5pp 时的功效:")
for name, T, n, s, pr in configs:
    pw, crit = sim(T, n, s, 0.05, paired=pr, reps=3000)
    print(f"  {name:38s} power={pw:.3f}  crit_t={crit:.2f}")
