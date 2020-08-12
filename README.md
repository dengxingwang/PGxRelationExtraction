# PGxRelationExtraction
 药物基因组学领域关系抽取

# Requirements
* python 3 <br>
* tensorflow 1.9.0+ <br>
* biobert

# Running
  Prepare data. <br>
  ## Download pre-trained BERT model. <br>
   Tar [BioBERT Pre-trained Weights] (https://github.com/naver/biobert-pretrained/releases) in folder ./pretrained_bert_model. <br>

  ## Run <br>
   python run_cnn.py train <br>
   python run_cnn.py test <br>
   python run_att_lstm.py train <br>
   python run_att_lstm.py test <br>

