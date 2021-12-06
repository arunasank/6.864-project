# 6.864-project Classifying note helpfulness on the Birdwatch Dataset

* Project Proposal: https://docs.google.com/document/d/1uXCQrC4FZHdfxlQz15PRzu2y5kzR42N_jAAhEMpgzuE/edit?usp=sharing
* Project Meeting Notes: https://docs.google.com/document/d/1H_V25SbNXN3-1JXY7GuRTRZ3UJhL0yxA4_mru_JJgiU/edit?usp=sharing
* Project Draft: https://www.overleaf.com/3659296817cvjcdszzqkjd
* Project Presentation: https://docs.google.com/presentation/d/1gPYxTonKMMgsWVaqXRt2yG7YYOcH0NBkC8CfmAgyRW0/edit?usp=sharing

## Model Baselines

Model | Feature | accuracy| f1| precision| recall| average precision| roc_auc|
-------------------------------------------------------------
SVM | ner_count | 0.414771104977634 | 0.35446524013483055 | 0.7135805140955456 | 0.23579796909871645 | 0.6587610614224928 | 0.5330920837908776

Logistic Regression | ner_count | 0.4505567716760255 | 0.48264882537735443 | 0.6882557610583585 | 0.3716295979749051 | 0.6590934124364873 | 0.5349838616481061

SVM | quality | 0.48500999333777484 | 0.5362098717793582 | 0.7275435539965197 | 0.42455729713131396 | 0.6782296790345478 | 0.569814379845463

Logistic Regression | quality | 0.5407823355857999 | 0.6199120524096 | 0.7159046177743338 | 0.5466183528536525 | 0.6823279234696285 | 0.5789411730726411

SVM | length | 0.5441134481774056 | 0.6406678702564477 | 0.7221161181632643 | 0.5757306011017966 | 0.6880600792380256 | 0.5893439664382519

Logistic Regression | length | 0.5263157894736842 | 0.6058176037263575 | 0.7187743254108871 | 0.5235420043067095 | 0.6821213397823485 | 0.5782247605197893


## Model Leaderboard

Featurization | Model | ROC-AUC | F1-score
------------- | ----- | ------- | -------
Bag of words | Gradient Boosting | **0.65** | 0.76
Word2Vec | Logistic Classifier | 0.61 | **0.78** 
