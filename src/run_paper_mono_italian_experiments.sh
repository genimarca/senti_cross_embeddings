#!/bin/bash

python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_italian_sentipol_lstm_collados_italian.txt > ../results/paper/mono/mono_italian_sentipol_lstm_collados_italian.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_italian_sentipol_svm_tfidf.txt > ../results/paper/mono/mono_italian_sentipol_svm_tfidf.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_italian_sentipol_bilabel_lstm_collados_italian.txt > ../results/paper/mono/mono_italian_sentipol_bilabel_lstm_collados_italian.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_italian_sentipol_bilabel_svm_tfidf.txt > ../results/paper/mono/mono_italian_sentipol_bilabel_svm_tfidf.txt
