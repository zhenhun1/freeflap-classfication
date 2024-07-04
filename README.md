# Classification Model of Free Flap in Craniomaxillofacial Region Based on Pixel Curve Features
## Introduction
<!--游离皮瓣由皮肤及其相关组织组成，在外科领域具有广泛的应用。这种移植手术能够修复受损组织，改善功能和外观，显著提高患者的生活质量。然而，皮瓣危象是一个不可忽视的问题，可能严重影响病人的生命健康。为了及时发现并抢救皮瓣危象，在临床实践中通常使用多普勒超声、彩色多普勒超声、热成像等技术进行监测。然而，针对颅颌面口腔内部的游离皮瓣监测，现有技术存在一些缺陷。因此，我们提出了一种分类模型，旨在解决上述问题。该模型基于机理模型分析，利用灰度图像的曲线特征对游离皮瓣进行二分类。-->

A free flap consists of skin and its associated tissues, widely utilized in the field of surgery. This transplantation procedure can repair damaged tissues, improve function and appearance, significantly enhancing patients' quality of life. However, flap failure is a critical issue that cannot be ignored, potentially severely impacting patients' health and well-being. To promptly detect and manage flap failure, clinical practice often employs monitoring techniques such as Doppler ultrasound, color Doppler ultrasound, and thermography. However, current methods for monitoring free flaps within the craniofacial region have some limitations. Therefore, we propose a classification model aimed at addressing these issues. This model is based on mechanistic analysis and utilizes curve features of grayscale images for the binary classification of free flaps.


## Methodology

<!-- 我们提出的方法包括：
1、基于解剖学和比色学方法建立机理模型，为特征提取提供理论基础
2、在预处理过程中，对训练和验证集数据集使用Kmeans聚类算法，将图像的阴影、线头等干扰因素裁剪掉
3、随机提取图像的像素曲线值并提取曲线特征，提取的特征共有9个
4、对预测模型提取的像素曲线限定了取线范围，保证特征的有效性
-->
Our proposed approaches include:
1、Establishing a mechanistic model based on anatomical and colorimetric methods to provide a theoretical foundation for feature extraction.
2、Applying the K-means clustering algorithm during preprocessing on the training and validation datasets to remove interference factors such as shadows and line ends from images.
3、Randomly extracting pixel curve values from images and deriving nine curve features.
4、Imposing limits on the pixel curves extracted by the prediction model to ensure the validity of the features.

## Dataset and Evaluation
## Appliction Prospects
我们使用pixel exctration进行像素提取，然后用特征1，2提取特征。删除不需要的部分。令计算的null值
为0

