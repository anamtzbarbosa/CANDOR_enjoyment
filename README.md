# CANDOR_enjoyment

Project Overview
This project investigates whether objective conversational timing metrics (such as pauses, FTO, overlap, and speech balance) are related to subjective impressions of conversational quality. Using a dataset of dyadic conversations, we test whether timing behaviors predict enjoyment and perceived conversational skill.

The analysis combines regression models, PCA, and Random Forest classifiers to evaluate the relationship between objective behavior and subjective perception.

Research Questions
Does conversational timing correlate with positive or negative impressions?

Do objective metrics (FTO, pauses, overlap, speech activity) predict subjective enjoyment or perceived conversational skill?

Is FTO correlated with enjoyment or perceived conversational skill?

Do more “balanced” dyads (in speech activity) report higher mutual enjoyment?

Hypotheses
We test four hypotheses, each corresponding to a specific timing metric:

H1: Lower MeanFTO → higher enjoyment.

H2: Higher MeanPause → lower enjoyment.

H3: Higher SpeechBalance (more imbalance) → lower enjoyment (i.e., more balanced = better).

H4: Objective timing metrics significantly predict perceived conversational skill.(H4 temporarily named “notebooks” in the files)

Approach Summary
Regression models test H1–H3 by examining the relationship between timing metrics and enjoyment.

PCA explores whether timing metrics or subjective evaluations create structure in the data.

Random Forest classifiers evaluate how well different feature sets predict conversational skill levels.
