
# Conversational Timing and Subjective Perception Analysis

This repository contains the analytical pipeline for investigating the relationship between objective conversational timing metrics and subjective impressions of quality, specifically using the **CANDOR corpus**.

## Project Overview
We investigate whether timing behaviors—such as **Floor Transfer Offset (FTO)**, overlaps, pauses, and speech balance predict subjective enjoyment and perceived conversational skill in dyadic interactions.

### Research Questions
* Does conversational timing correlate with subjective impressions?
* Do objective metrics (FTO, pauses, overlap, speech activity) predict enjoyment or perceived skill?
* Do "balanced" dyads report higher mutual enjoyment?

### Hypotheses
* **H1:** Lower Mean FTO correlates with higher enjoyment.
* **H2:** Higher Mean Pause duration correlates with lower enjoyment.
* **H3:** Higher Speech Imbalance correlates with lower enjoyment.
* **H4:** Objective timing metrics significantly predict perceived conversational skill.

## Methodology & Tools
The analysis is implemented in **Python** and follows a multi-method approach:
* **inear Regression (Baseline):** Initial tests were conducted using standard OLS regression to establish a baseline relationship between variables.
* **Linear Mixed-Effects Models (LMM):** To account for the nested structure of conversations (within speakers and calls) using `statsmodels`.
* **Machine Learning:** Random Forest classifiers to evaluate feature importance for conversational skill.
* **Dimensionality Reduction:** PCA to explore the underlying structure of timing and subjective metrics.



## Repository Structure
* `/notebooks`: Jupyter notebooks containing the exploratory data analysis (EDA).
* `/scripts`: Python scripts for data preprocessing and model implementation.
* `mixed_effects_model.py`: Implementation of the Crossed Random Intercepts model.
* `requirements.txt`: List of necessary Python libraries.

