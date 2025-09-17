import numpy as np
import matplotlib.pyplot as plt

# Parameter t
t = np.linspace(0, 24*np.pi, 2000)

# Each term
term1 = np.exp(np.cos(t))                # e^cos(t)
term2 = -2 * np.cos(4*t)                 # -2cos(4t)
term3 = -(np.sin(t/12))**5               # -sin^5(t/12)

# Plot each term separately
plt.figure(figsize=(12, 8))

# Term 1
plt.subplot(3,1,1)
plt.plot(t, term1)
plt.title(r"$e^{\cos(t)}$  → smooth oscillation")
plt.xlabel("t")
plt.ylabel("Value")

# Term 2
plt.subplot(3,1,2)
plt.plot(t, term2)
plt.title(r"$-2\cos(4t)$  → 4-fold symmetry")
plt.xlabel("t")
plt.ylabel("Value")

# Term 3
plt.subplot(3,1,3)
plt.plot(t, term3)
plt.title(r"$-\sin^5(t/12)$  → slow modulation")
plt.xlabel("t")
plt.ylabel("Value")

plt.tight_layout()
plt.show()
