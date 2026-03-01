# H1 FTO and enjoyment
> Hypothesis: Lower FTO → higher enjoyment
### Key variables
`tfo_actor`, `tfo_partner`: Floor Transfer Offset (turn-taking latency)

`how_enjoyable_actor`, `how_enjoyable_partner`: Self-reported enjoyment (1–9 scale)

`enjoyable_avg`: Mutual enjoyment = $\frac{how\_enjoyable\_actor+how\_enjoyable\_partner}{2}$

`tfo_mean`: Average latency within dyads = $\frac{tfo\_actor+tfo\_partner}{2}$

`tfo_imbalance`: $|tfo\_actor - tfo\_partner|$

## Model 1: Individual analysis (X = pauses_actor, tfo_actor, tfo_partner)
**Dependent variable:** how_enjoyable_partner  
**N = 3202**  
**R² = 0.025**, Adj. R² = 0.024  
**F(3, 3198) = 27.15**, p < .001  

| Variable        | Coef    | Std Err | t      | p      | 95% CI              |
|----------------|---------|---------|--------|--------|---------------------|
| Intercept      | 7.7870  | 0.066   | 117.28 | <.001  | [7.657, 7.917]      |
| pauses_actor   | -0.0191 | 0.353   | -0.05  | .957   | [-0.712, 0.674]     |
| tfo_actor      | -0.5507 | 0.141   | -3.90  | <.001  | [-0.828, -0.274]    |
| tfo_partner    | -0.6684 | 0.148   | -4.53  | <.001  | [-0.958, -0.379]    |

### Model 1 clustered

**Dependent variable:** how_enjoyable_partner  
**Cluster-robust standard errors**  
**R² = 0.025**  
**F = 20.73**, p < .001  

| Variable        | Coef    | Robust SE | z      | p      | 95% CI              |
|----------------|---------|-----------|--------|--------|---------------------|
| Intercept      | 7.7870  | 0.065     | 119.86 | <.001  | [7.660, 7.914]      |
| pauses_actor   | -0.0191 | 0.333     | -0.06  | .954   | [-0.672, 0.634]     |
| tfo_actor      | -0.5507 | 0.120     | -4.59  | <.001  | [-0.786, -0.316]    |
| tfo_partner    | -0.6684 | 0.163     | -4.11  | <.001  | [-0.987, -0.350]    |


## Model 2 Dyadic analyses (X = tfo_mean, tfo_imbalance)

**Dependent variable:** enjoyable_avg  
**N = 3202**  
**R² = 0.043**, Adj. R² = 0.042  
**F = 33.28**, p < .001  

| Variable        | Coef     | Robust SE | z      | p      | 95% CI              |
|----------------|----------|-----------|--------|--------|---------------------|
| Intercept      | 7.7768   | 0.053     | 146.23 | <.001  | [7.673, 7.881]      |
| tfo_mean       | -1.2859  | 0.163     | -7.90  | <.001  | [-1.605, -0.967]    |
| tfo_imbalance  | 0.1891   | 0.222     | 0.85   | .394   | [-0.245, 0.624]     |