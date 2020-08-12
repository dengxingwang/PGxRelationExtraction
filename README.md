# PGxRelationExtraction
 药物基因组学领域关系抽取

# Requirements
* python 3 <br>
* tensorflow 1.9.0+ <br>
* biobert

#Running
1.prepare data <br>
2.## Download pre-trained BERT model. <br>
  Unzip uncased_L-12_H-768_A-12.zip and chinese_L-12_H-768_A-12.zip in folder ./pretrained_bert_model. <br>

3.## Run <br>
  python run_cnn.py train <br>
  python run_cnn.py test <br>
  python run_att_lstm.py train <br>
  python run_att_lstm.py test <br>

