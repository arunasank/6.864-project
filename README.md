# 6.864-project Classifying note helpfulness on the Birdwatch Dataset

* Project Proposal: https://docs.google.com/document/d/1uXCQrC4FZHdfxlQz15PRzu2y5kzR42N_jAAhEMpgzuE/edit?usp=sharing
* Project Meeting Notes: https://docs.google.com/document/d/1H_V25SbNXN3-1JXY7GuRTRZ3UJhL0yxA4_mru_JJgiU/edit?usp=sharing
* Project Draft: https://www.overleaf.com/3659296817cvjcdszzqkjd
* Project Presentation: https://docs.google.com/presentation/d/1gPYxTonKMMgsWVaqXRt2yG7YYOcH0NBkC8CfmAgyRW0/edit?usp=sharing

## Model Baselines

Model | Feature | accuracy | f1 | precision | recall | average precision | roc_auc
-----------| -------------- | -------------|------------------|-------------------------| --------------------- | ----------------- |----------
SVM | ner_count | 0.414771104977634 | 0.35446524013483055 | 0.7135805140955456 | 0.23579796909871645 | 0.6587610614224928 | 0.5330920837908776
SVM | quality | 0.48500999333777484 | 0.5362098717793582 | 0.7275435539965197 | 0.42455729713131396 | 0.6782296790345478 | 0.569814379845463
SVM | length | 0.5441134481774056 | 0.6406678702564477 | 0.7221161181632643 | 0.5757306011017966 | 0.6880600792380256 | 0.5893439664382519
SVM | all | 0.5374512229941943 | 0.6268917145829604 | 0.7232104405399724 | 0.5532135421272645 | 0.6868580323605471 | 0.5868884060201726
Logistic Regression | ner_count | 0.4505567716760255 | 0.48264882537735443 | 0.6882557610583585 | 0.3716295979749051 | 0.6590934124364873 | 0.5349838616481061
Logistic Regression | quality | 0.5407823355857999 | 0.6199120524096 | 0.7159046177743338 | 0.5466183528536525 | 0.6823279234696285 | 0.5789411730726411
Logistic Regression | length | 0.5263157894736842 | 0.6058176037263575 | 0.7187743254108871 | 0.5235420043067095 | 0.6821213397823485 | 0.5782247605197893
Logistic Regression | all | 0.5213667079090131 | 0.606418347113234 | 0.7260169289183717 | 0.520650319711153 | 0.6856697519501522 | 0.5842676014642383
Random Forest| ner_count| 0.5389740173217855| 0.6210280988035914| 0.6779465488416294| 0.572926805548559| 0.6625290887494052| 0.5425906959663964
Random Forest| quality| 0.587132387931855| 0.7002447049122904| 0.7256804181650639| 0.676531695996744| 0.698562729435229| 0.6091099140643317
Random Forest| length| 0.5818977824307604| 0.69356961653123| 0.7068161231746727| 0.6808104839882847| 0.6860784281660135| 0.5873639339092807
Random Forest | all | 0.5891310554868183 | 0.7190539202051455 | 0.7216845120406783 | 0.7164424361125497 | 0.6990457754945192 | 0.6106484654921459

## Model Leaderboard

Featurization | Model | ROC-AUC | F1-score
------------- | ----- | ------- | -------
Bag of words | Gradient Boosting | **0.65** | 0.76
Word2Vec | Logistic Classifier | 0.61 | **0.78** 
