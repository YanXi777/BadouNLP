# -*- coding: utf-8 -*-

"""
配置参数信息
"""

Config = {
    "model_path": "model_output",
    "schema_path": "ner_data/schema.json",
    "train_data_path": "ner_data/train",
    "valid_data_path": "ner_data/test",
    "vocab_path":"chars.txt",
    "max_length": 100,
    "hidden_size": 256,
    "num_layers": 2,
    "epoch": 20,
    "batch_size": 16,
    "optimizer": "adam",
    "learning_rate": 1e-5,
    "use_crf": True,
    "class_num": 9,
    "bert_path": r"F:\BaiduNetdiskDownload\bert-base-chinese\bert-base-chinese",
    "use_bert": True,  # 新增标志位
    "bert_hidden_size": 768,  # BERT的隐藏层大小
    "fine_tune_bert": True  # 是否微调BERT
}

