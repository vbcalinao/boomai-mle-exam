#!/bin/bash

# defines the qa model
MODEL_DIR="https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2/resolve/main"
MODEL_NAME="paraphrase-MiniLM-L6-v2"

# downloads the qa model. To make this image more general one can use curl
# with the "-O" argument to download the necessary files defined
# in "require.txt".

mkdir ${MODEL_NAME} &&\
    curl -o ${MODEL_NAME}/vocab.txt ${MODEL_DIR}/vocab.txt &&\
    curl -o ${MODEL_NAME}/tokenizer_config.json ${MODEL_DIR}/tokenizer_config.json &&\
    curl -o ${MODEL_NAME}/tokenizer.json ${MODEL_DIR}/tokenizer.json &&\
    curl -o ${MODEL_NAME}/special_tokens_map.json ${MODEL_DIR}/special_tokens_map.json &&\
    curl -o ${MODEL_NAME}/sentence_bert_config.json ${MODEL_DIR}/sentence_bert_config.json &&\
    curl -o ${MODEL_NAME}/pytorch_model.bin ${MODEL_DIR}/pytorch_model.bin &&\
    curl -o ${MODEL_NAME}/modules.json ${MODEL_DIR}/modules.json &&\
    curl -o ${MODEL_NAME}/config_sentence_transformers.json ${MODEL_DIR}/config_sentence_transformers.json &&\
    curl -o ${MODEL_NAME}/config.json ${MODEL_DIR}/config.json