## Dataset

Released: 29th of May 2020
https://dankmemes2020.fileli.unipi.it/?page_id=37


**DANKMEMES** (multimoDal Artefacts recogNition Knowledge for MEMES) is the **first EVALITA task** for meme recognition and hate speech/event identification in memes.
It features a total of 2.361 images on the 2019 Italian government crisis, which have been collected on Instagram. The DANKMEMES shared task is articulated into three subtasks: Meme Recognition, Hate speech Identification and Event Clustering. 
For each subtask we provide a training dataset, consisting of: 

- a folder with images in .jpg format 
- a .csv file with the associated variables
- a .csv file with the associated image embeddigs


The structure of the variables files is different depending on the subtask they refer to: below are reported the information on the training dataset for the **second** subtask.


# Training dataset 2 - Hate speech identification

This dataset consists of a folder and two .csv files. The folder contains 800 images (memes) in .jpg format, one of the .csv provides the associated variables and the other .csv file contains the image embeddings. This data must be used for the training part of the subtask **meme recognition** of the **DANKMEMES**  task. 

The variables provided for this task are: 

- File: the name of the image file associated with the variables;
- Engagement: the number of comments and likes of the image;
- Picture manipulation: entails the degree of visual modification of the images. Non-manipulated or low impact changes are labeled 0 (e.g. addition of text, or logo). Heavily manipulated, impactful changes (e.g. images altered to include political actors) are labeled 1;
- Visual actors: the political actors (i.e. politicians, parties’ logos) portrayed visually, as edited into the picture or portrayed in the original image;
- Text: the textual content of the image has been extracted through optical character recognition (OCR) using Google’s Tesseract-OCR Engine, and further manually corrected;
- Hate speech: binary feature only for memes. It differentiates memes with offensive language (1) from non offensive memes (0). This is the target label for the second subtask.

Here an excerpt of the dataset:

|File           |Engagement |Manipulation |Visual           |Text                                                             |Hate speech |
|---------------|-----------|-------------|-----------------|-----------------------------------------------------------------|------------|
|456.jpg.       |654        |1            |Salvini, Di Maio |aiuto                                                            |0           |
|993.jpg        |98         |0            |Conte            |alle solite                                                      |0           |
|4.jpg.         |235        |1            |Mattarella	    |io che aspetto arrivino le 15 per assistere alla fine del governo|1           |


The image vector representations are computed employing **ResNet** [He+16], a state-of-the-art model for image recognition based on Deep Residual Learning. 
The structure of the image embedding files is the same for all three datasets: each row displays the corresponding image file name and the elements are space-separated. Here an excerpt of the dataset:


|File           |Embedding                                                      |
|---------------|---------------------------------------------------------------|
|456.jpg.       |0.10538975894451141 1.441086769104004 ... 0.10747165232896805  |
|993.jpg        |0.41991370916366577 0.49551108479499817 ... 0.0672694519162178 |
|4.jpg.         |1.7892037630081177 1.1843881607055664 ... 0.09812714904546738  |








## Data Licence

All material is released for non-commercial research purposes only under a Creative Common license (BY-NC-ND 4.0).  Any use for statistical, propagandistic  or  advertising  purposes  of  any  kind  is  prohibited.   It  is  not  possible  to modify, alter or enrich the data provided for the purposes of redistribution.

## References

* [KB14] Douwe Kiela and L ́eon Bottou. “Learning Image Embeddings using Convolutional Neural Networks for Improved Multi-Modal Semantics”. In: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP). 2014, pp. 36–45.
* [He+16] Kaiming He et al. “Deep Residual Learning for Image Recognition”. In: The IEEE Conference on Computer Vision and Pattern Recognition (CVPR). 2016.




AUTHORS & CONTACT 
-------

Guido Anselmi, Giulia Giorgi, Gianluca E. Lebani, Martina Miliani, Ilir Rama

Mail
dankmemesevalita@gmail.com

Info about the DANKMEMES task
https://dankmemes2020.fileli.unipi.it