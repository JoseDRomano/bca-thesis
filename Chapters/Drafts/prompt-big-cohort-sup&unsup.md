Hello, I've already written the part of my thesis where I talk about the results that I got with my smaller dataset. In this part, I've documented the results of both supervised and unsupervised approaches in the smaller dataset.



In chapter 3, I've talked about my first dataset and how we assessed our first scrap models to understand which one of the models would be the best to fine tune and work with (these were evaluated not only on their capacity of classification but also on the interpretability that they provide - after all, our main objective is to gather a small panel of miRNAs and clinical features that best describe a certain subtype of breast cancer (if possible)). 



Then, we've used XGBoost as our main model to go forward with it and we fine tune it using grid search so that we get the best model we could. You have a more detailed description in the chapter3.tex file. 



When it comes to working with this bigger dataset, we just grabbed what we already knew from the previous implementation and just applied it in order to understand what kind of results we would get.



Given this, we've used the same XGBoost model (same architecture / configuration) and the same notebooks for ANOVA F-TEST implementation and for k-means. We basically just took what we had already done and changed the data that was entering the notebooks (of course, with a different pre processing rules).



As you can see in chapter4.tex, I already wrote the section "Transition to the larger dataset" and "Data pre-processing pipeline" and these are in a final stage (you should read it to understand our dataset). Your goal now is to write the sections about the implementation of supervised and Unsupervised techniques (remember that they are exactly the same as the ones described in chapter3.tex, so you must not repeat the whole explanation process, but more of referencing what you need to reference in order to maintain a clear chain of thought to present the results).



 Remember that we already described our thought process in order to achieve these implementations, your goal with these sections must be to reference what you need to reference to bridge the implementations between small and big cohort and then present the results that we got. (don't make a direct comparison with the results that we got from the small cohort because we will have a section dedicated to that)!



The reader must be able to clearly understand:





That we used the same implementations as we previously documented in the chapter before (in chapter3.tex)



That our main objective is to retrieve a small panel of features that can distinguish one subtype from the rest. And we are using machine learning models as a proxy to achieve that - if we have a good classifier, we can look inside of it and see what features are the most important for each class.



which subtypes are the most separable (given the results that we have from applying those implementations on our big cohort - mirna+clinical.csv)



You don't need to re-write what I already wrote on chapter4.tex, your goal is to simply continue the documentation by focusing on the supervised and unsupervised results.



To support you on the writing of these chapters, I gave you access to some documents that will help you establish the foundation of your text:





The text that I've pasted is the latex code of the chapter 3 where I explained how I conducted my approach on supervised methods to classify subtypes of breast cancer (mainly XGBoost and then ANOVA F-TEST to statistically corroborate the miRNAs chosen by our models) but also how I leveraged k-means (an unsupervised algorithm) to cluster our patients in order to assess wether our data has an implicit structure or not. 



chapter4.tex : this file contains what I've already wrote on the bigger cohort. This file already contains an explanation on where we got the data, how we characterize it and how we've pre processed it. Your text will be a continuation of this file (but now about the supervised and unsupervised results that we got)



mirna+clinical.csv: this csv file is the data file that we used in the bigger cohort. This data is already pre processed all the way before the normalization process.



supervised_xgb_big_cohort.pdf: this pdf contains the results obtained when we use the same XGB model configuration and same implementation process to our bigger cohort. This file is separated by 2 columns, where on the left side we have an implementation without clinical data and on the right side we have an implementation with clinical data + mirna



supervised_anova_big_cohort.pdf: this pdf contains the results obtained when we use the same notebook we used in the small cohort (and what were extracted as most relevant)



unsupervised_kmeans_big_cohort.ipynb: this pdf contains the results obtained when we use the same kmeans model as we used for the small cohort



If you want to make a suggestion just use [SUGGESTION] and if you need to put any table, figure or media just use [MEDIA]. Any question or image that is not so clear to you just ask me.

