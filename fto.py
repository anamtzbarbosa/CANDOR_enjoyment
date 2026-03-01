import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
path = BASE_DIR / "data" / "processed" / "candor_dataset_clean.csv"
df = pd.read_csv(path)

# sanity
#print(df.shape)
#print(df.columns)
df.head()

df["enjoyable_avg"] = (df["how_enjoyable_actor"] + df["how_enjoyable_partner"]) / 2
df["tfo_mean"] = (df["tfo_actor"] + df["tfo_partner"]) / 2
df["tfo_imbalance"] = (df["tfo_actor"] - df["tfo_partner"]).abs()

# Model 1 actor fto -> partner enjoyment
X = sm.add_constant(df[["pauses_actor", "tfo_actor", "tfo_partner"]])
y = df["how_enjoyable_partner"]

m = sm.OLS(y, X).fit()
print(m.summary())

# Klustrade standardfel per call
mc = sm.OLS(y, X).fit(
    cov_type="cluster",
    cov_kwds={"groups": df["call_id"]}
)

print(mc.summary())

# Model 2 mean fto -> avg enjoyment
X2 = sm.add_constant(df[["tfo_mean", "tfo_imbalance"]])
y2 = df["enjoyable_avg"]

m2c = sm.OLS(y2, X2).fit(
    cov_type="cluster",
    cov_kwds={"groups": df["call_id"]}
)

print(m2c.summary())

# two plots for critical discussion

# df["pauses_actor"].hist(bins=50)
# plt.title("pauses_actor distribution")
# plt.show()

# df["how_enjoyable_partner"].hist(bins=20)
# plt.title("how_enjoyable_partner distribution")
# plt.show()

# print(df[["pauses_actor", "tfo_actor", "tfo_partner"]].corr())