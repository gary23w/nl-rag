---
title: "Radiomics"
source: https://en.wikipedia.org/wiki/Radiomics
domain: radiology-informatics
license: CC-BY-SA-4.0
tags: radiology informatics, imaging informatics, radiology reporting, computer aided diagnosis
fetched: 2026-07-02
---

# Radiomics

In the field of medicine, **radiomics** is a method that extracts a large number of features from medical images using data-characterisation algorithms. These features, termed radiomic features, have the potential to uncover tumoral patterns and characteristics that fail to be appreciated by the naked eye. The hypothesis of radiomics is that the distinctive imaging features between disease forms may be useful for predicting prognosis and therapeutic response for various cancer types, thus providing valuable information for personalized therapy. Radiomics emerged from the medical fields of radiology and oncology and is the most advanced in applications within these fields. However, the technique can be applied to any medical study where a pathological process can be imaged.

## Process

### Image acquisition

The image data is provided by radiological modalities as CT, MRI, PET/CT or even PET/MR. The produced raw data volumes are used to find different pixel/voxel characteristics through extraction tools.

The extracted features are saved in large databases where clinics have access so as to enable broadly collaborative and cumulative work in which all can benefit from growing amounts of data, ideally enabling a more precise workflow.

### Image segmentation

After the images have been saved in the database, they have to be reduced to the essential parts, in this case the tumors, which are called "volumes of interest".

Because of the large image data that needs to be processed, it would be too much work to perform the segmentation manually for every single image if a radiomics database with lots of data is created. This makes manual contouring time-consuming and can be potentially affected by rater variability. Instead of manual segmentation, an automated process has to be used. Two possible solutions are deep-learning-based automatic tumor segmentation methods and semiautomatic segmentation workflow where human label the first few slices and then the ML system do the rest. Before it can be applied on a big scale, an algorithm must score as high as possible in the following four tasks:

- First, it must be reproducible, which means that when it is used on the same data the outcome will not change. This can either be different raters’ contour is similar or the automatic/semiautomatic models’ have good robustness measured by Intraclass Correlation Coefficient.

- Another important factor is consistency. The algorithm does solve the problem at hand and performs the task rather than doing something that is not important. In this case, it is necessary that the algorithm can detect the diseased part in different scans.

- The algorithm also needs to be accurate. It is very important that the algorithm detects the diseased part in the most precise way possible. Only with accurate data, accurate results can be achieved. Besides approximate visual effect, typical metrices Dice similarity coefficient, Jaccard index, Hausdorff distance, and average surface distance, which gives more quantitative and objective evaluation.

- A minor but still important point is time efficiency. The results should be generated as fast as possible so that the whole process of radiomics can also be accelerated. Usually automatic/semiautomatic segmentation algorithms are more efficient than manual segmentation. For automatic/semiautomatic segmentation, training time and running speed are usually the two most important standards. To speed up both standards, typical solution is structure / architecture-level change, like knowledge distillation-based framework.

In recent years, machine learning and deep learning have been the dominant part of automatic medical image segmentation. Many methods are based on convolutional neural networks, such as U-Net-like models and CE-net.

### Feature extraction and qualification

After the segmentation, many features can be extracted and the relative net change from longitudinal images (delta-radiomics) can be computed. Radiomic features can be divided into five groups: size and shape based–features, descriptors of the image intensity histogram, descriptors of the relationships between image voxels (e.g. gray-level co-occurrence matrix (GLCM), run length matrix (RLM), size zone matrix (SZM), and neighborhood gray tone difference matrix (NGTDM) derived textures), textures extracted from filtered images, and fractal features. The mathematical definitions of these features are independent of imaging modality and can be found in the literature. A detailed description of texture features for radiomics can be found in Parekh et al. (2016) and Depeursinge et al. (2017).

Due to its massive variety, feature reductions need to be implemented to eliminate redundant information. Hundreds of different features need to be evaluated with a selection algorithm to accelerate this process. Additionally, features that are unstable and non-reproducible should be eliminated since features with low-fidelity will likely lead to spurious findings and unrepeatable models.

### Analysis

**Analysis**

After the most relevant features are selected, the data must be analyzed to find meaningful patterns and relationships. In modern medical analysis, AI, machine learning, and deep learning are often used to analyze imaging and non-imaging patient data for tasks such as disease detection, lesion characterization and treatment planning. This information can then be further used in forming CAD (computer aided diagnosis) systems. In radiomics, low order image features such as shape, intensity, texture, and then use traditional machine learning methods such as support vector machines, random forests, logistic regression, PCA, and clustering to make predictions, or deep learning methods such as convolutional neural networks that learn features automatically from the data in convolutional layers and then make predictions or regression on the fully connected layer.

Before the actual analysis, different data types such as imaging radiomics, molecular biomarkers, and genetic information can be integrated to enhance model’s performance. This multiomics integration allows AI models to make decisions based on multi-dimensional data, which can improve cancer subtyping, risk prediction, treatment selection, and clinical decision support. The integrated data can then be analyzed using supervised learning, where uses an outcome variable to be able to create prediction models, or unsupervised learning to summarize the information we have and can be represented graphically.

### Databases

#### Creation

Several steps are necessary to create an integrated radiomics database. The imaging data needs to be exported from the clinics. This is already a very challenging step because the patient information is very sensitive and governed by Privacy laws, such as HIPAA. At the same time the exported data must not lose any of its integrity when compressed so that the database only incorporates data of the same quality. The integration of clinical and molecular data is important as well and a large image storage location is needed.

#### Use

The goal of radiomics is to be able to use this database for new patients. This means that we need algorithms that run new input data through the database which return a result with information about what the course of the patients' disease might look like. For example, how fast the tumor will grow or how good the chances are that the patient survives for a certain time, whether distant metastases are possible and where. This determines how the further treatment (like surgery, chemotherapy, radiotherapy or targeted drugs etc.) and the best solution which maximizes survival or improvement is selected. The algorithm has to recognize correlations between the images and the features, so that it is possible to extrapolate from the data base material to the input data.

## Applications

### Prediction of clinical outcomes

Aerts et al. (2014) performed the first large-scale radiomic study that included three lung and two head-and-neck cancer cohorts, consisting of over 1000 patients. They assessed the prognostic values of over 400 textural and shape- and intensity-based features extracted from the computed tomography (CT) images acquired before any treatment. Tumor volumes were defined either by expert radiation oncologists or using semiautomatic segmentation methods. Their results identified a subset of radiomic features that may be useful for predicting patient survival and describing intratumoural heterogeneity. They also confirmed that the prognostic ability of these radiomics features may be transferred from lung to head-and-neck cancer. However, Parmar et al. (2015) demonstrated that prognostic value of some radiomic features may be cancer type dependent. Particularly, they observed that not every radiomic feature that significantly predicted the survival of lung cancer patients could also predict the survival of head-and-neck cancer patients and vice versa.

Nasief et al. (2019) showed that changes of radiomic features over time in longitudinal images (delta-radiomic features, DRFs) can potentially be used as a biomarker to predict treatment response for pancreatic cancer. Their results showed that a Bayesian regularization neural network can be used to identify a subset of DRFs that demonstrated significant changes between good- and bad- responders following 2–4 weeks of treatment with an AUC = 0.94. They also showed (Nasief et al., 2020) that DRFs are independent predictor of survival and if combined with the clinical biomarker CA19-9 can improve treatment response prediction and increase the possibility for response-based treatment adaptation .

Several studies have also showed that radiomic features are better at predicting treatment response than conventional measures, such as tumor volume and diameter, and the maximum radiotracer uptake on positron emission tomography (PET) imaging. Using this technique an algorithm has been developed, after initial training based on intra tumor lymphocyte density, to predict the probability of tumor response to immunotherapy, providing a demonstration of the clinical potential of radiomics as a powerful tool for personalized therapy in the emerging field of immunooncology. Other studies have also demonstrated the utility of radiomics for predicting immunotherapy response of NSCLC patients using pre-treatment CT and PET/CT images.

Radiomics remains inferior to conventional techniques in some applications, suggesting the necessity of continued improvement and manipulation of Radiomics features to different clinical scenarios. For instance, Ludwig et al. (2020) demonstrated that morphological Radiomics features were inferior to previously established features in the discrimination of intracranial aneurysm rupture status from 3-dimensional rotational angiography.

### Prognostication

Radiomic studies have shown that image-based markers have the potential to provide information orthogonal to staging and biomarkers and improve prognostication.

### Prediction risk of distant metastasis

Metastatic potential of tumors may also be predicted by radiomic features. For example, thirty-five CT-based radiomic features were identified to be predictive of distant metastasis of lung cancer in a study by Coroller et al. in 2015. They thus concluded that radiomic features can be useful to identify patients with high risk of developing distant metastasis, guiding physicians to select the effective treatment for individual patients.

### Assessment of cancer genetics

Lung tumor biological mechanisms may demonstrate distinct and complex imaging patterns. In particular, Aerts et al. (2014) showed that radiomic features were associated with biological gene sets, such as cell cycle phase, DNA recombination, regulation of immune system process, etc. Moreover, various mutations of glioblastoma (GBM), such as 1p/19q deletion, MGMT methylation, TP53, EGFR, and NF1, have been shown to be significantly predicted by magnetic resonance imaging (MRI) volumetric measures, including tumor volume, necrosis volume, and contrast enhancing volume. In addition, the tumor mutation burden in recurrent gliomas was also associated with a unique radiomic signature

### Image guided radiotherapy

Radiomics offers the advantage to be non invasive and can therefore be repeated prospectively for a given patient more easily than invasive tumor biopsies. It has been suggested that radiomics could be a mean to monitor tumor dynamic changes along the course of radiotherapy and to define sub volumes at risk for which dose escalation could be beneficial.

### Distinguishing true progression from radionecrosis

Treatment effect or radiation necrosis after stereotactic radiosurgery (SRS) for brain metastases is a common phenomenon often indistinguishable from true progression. Radiomics demonstrated significant differences in a set of 82 treated lesions in 66 patients with pathological outcomes. Top-ranked Radiomic features feed into an optimized IsoSVM classifier resulted in a sensitivity and specificity of 65.38% and 86.67%, respectively, with an area under the curve of 0.81 on leave-one-out cross-validation. Only 73% of cases were classifiable by the neuroradiologist, with a sensitivity of 97% and specificity of 19%. These results show that radiomics holds promise for differentiating between treatment effect and true progression in brain metastases treated with SRS.

### Prediction of physiological events

Radiomics can also be used to identify challenging physiological events such as brain activity, which is usually studied with imaging techniques such as functional MRI "fMRI". FMRI raw images can undergo radiomic analysis to generate imaging features that can be later correlated with meaningful brain activity.

### Imaging genomics

In imaging genomics, radiogenomics can be used to create imaging biomarkers that can identify the genomics of a disease, especially cancer without the use of a biopsy. Various techniques for dealing with high-dimensional data are used to find statistically significant correlations between MRI, CT, and PET imaging features and the genomics of disease, including SAM, VAMPIRE, and GSEA.

The imaging radiogenomic approach has proven successful in determining the MRI phenotype associated genetics of glioblastoma, a highly aggressive type of brain tumor with low prognosis. The first large-scale MR-imaging microRNA-mRNA correlative study in GBM was published by Zinn et al. in 2011 Similar studies in liver cancer have successfully determined much of the liver cancer genome from non-invasive imaging features. Gevaert et al. at Stanford University have shown the potential to link image features of non-small cell lung nodules in CT scans to predict survival by leveraging publicly available gene expression data. This publication was accompanied by an editorial discussing the synergy between imaging and genomics. More recently, Mu Zhou et al. at Stanford University have shown that multiple associations between semantic image features and metagenes that represented canonical molecular pathways, and it can result in noninvasive identification of molecular properties of non-small cell lung cancer.

Several radiogenomic studies have now been carried out in prostate cancer, Some have noted that genetic features correlated with MRI signal are often also associated with more aggressive prostate cancer. A systematic review of the genetic features found in more visible lesions on MRI identified multiple studies which had found loss of the tumour suppressor PTEN, increased gene expression linked to cell proliferation as well as cell-ECM interactions. This may indicate that certain genetic features drives cellular changes which ultimately effect fluid movement which can be seen on MRI and these features are predominantly associated with poor prognosis. The combination of more dangerous genetic alterations, histology and clinical outcomes for patients with prostate tumours which are visible on mpMRI, has led to suggestions that the definition of 'clinically significant cancer' should be at least in part based on mpMRI findings.

The radiogenomic approach has been also successfully applied in breast cancer. In 2014, Mazurowski et al. showed that enhancement dynamics in MRI, computed using computer vision algorithms, are associated with gene expression-based tumor molecular subtype in breast cancer patients.

Programs that study the connections between radiology and genomics are active at the University of Pennsylvania, UCLA, MD Anderson Cancer Center, Stanford University and at Baylor College of Medicine in Houston, Texas.

### Multiparametric radiomics

Multiparametric radiological imaging is vital for detection, characterization and diagnosis of many different diseases. However, current methods in radiomics are limited to using single images for the extraction of these textural features and may limit the applicable scope of radiomics in different clinical settings. Thus, in the current form, they are not capable of capturing the true underlying tissue characteristics in high dimensional multiparametric imaging space.

Recently, a Multiparametric imaging radiomic framework termed MPRAD for extraction of radiomic features from high dimensional datasets was developed. The Multiparametric Radiomics was tested on two different organs and diseases; breast cancer and cerebrovascular accidents in brain, commonly referred to as stroke.

#### Breast cancer

In breast cancer, The MPRAD framework classified malignant from benign breast lesions with excellent sensitivity and specificity of 87% and 80.5% respectively with an AUC of 0.88. MPRAD provided a 9%-28% increase in AUC over single radiomic parameters. More importantly, in breast, normal glandular tissue MPRAD were similar between each group with no significance differences.

#### Stroke

Similarly, the MPRAD features in brain stroke demonstrated increased performance in distinguishing the perfusion-diffusion mismatch compared to single parameter radiomics and there were no differences within the white and gray matter tissue. The majority of the single radiomic second order features (GLCM) did not show any significant textural difference between infarcted tissue and tissue at risk on the ADC map. Whereas the same second order multiparametric radiomic features (TSPM) were significantly different for the DWI dataset. Similarly, multiparametric radiomic values for the TTP and PWI dataset demonstrated excellent results for the MPRAD. The MPRAD TSPM Entropy exhibited significant difference between infarcted tissue and potential tissue-at-risk: (6.6±0.5 vs 8.4±0.3, p=0.01).

### Limitations

Radiomics faces a few challenges that limit its ability to be used in real clinical applications. The first issue occurs prior to the input of medical images, existing in the collection of training data. There is no standardization in image protocols, so medical facilities use a variety of imaging techniques, scanner equipment, image parameters, and contrast agents. Radiologists also manually segment images which imposes subjectivity into the process that can largely impact the extracted features. Imaging data from prior scans can be easily obtained, but without careful selection of the input images, AI models may be trained on biased or unreliable datasets.

Due to there being more extracted features in the data than number of samples, the dataset will be high-dimensional. The challenges with the resulting highly correlated training set lies in the danger of overfitting. The model will learn to identify the noise of the data instead of reliable biological markers, resulting in a model that looks to have good performance until it sharply declines when introduced to independent validation. Even if the model was able to perform well outside of the training data, it would be challenging for clinicians to trust due to it being difficult to understand the how the resulting model works.

### Future directions

Efforts to improve standardization of imaging protocols and imaging preprocessing are being made. This, along with obtaining a diverse set of images, would drastically improve the performance of the models. As Radiomics becomes more popular, larger sets of data will be available which could help the high correlation issues in current models. Using multi-institutional data will also eliminate training bias to ensure that models will perform on new patient populations.
