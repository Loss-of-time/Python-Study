#%%
import matplotlib.pyplot as plt

# %%
plt.figure()
x=[]
y=[]
# %%
for i in range(100):
    o = 2 ** i
    x.append(i)
    y.append(o)

# %%
plt.plot(x,y)
plt.show()

# %%
