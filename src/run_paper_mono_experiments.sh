#!/bin/bash

python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_english_semeval_bilabel_lstm_collados.txt > ../results/paper/mono/mono_english_semeval_bilabel_lstm_collados.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_english_semeval_bilabel_svm_tfidf.txt > ../results/paper/mono/mono_english_semeval_bilabel_svm_tfidf.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_english_semeval_lstm_collados.txt > ../results/paper/mono/mono_english_semeval_lstm_collados.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_english_semeval_svm_tfidf.txt > ../results/paper/mono/mono_english_semeval_svm_tfidf.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_english_semevalNegative_bilabel_lstm_collados.txt > ../results/paper/mono/mono_english_semevalNegative_bilabel_lstm_collados.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_english_semevalNegative_bilabel_svm_tfidf.txt > ../results/paper/mono/mono_english_semevalNegative_bilabel_svm_tfidf.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_spanish_cost_lstm_collados_spanish.txt > ../results/paper/mono/mono_spanish_cost_lstm_collados_spanish.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_spanish_cost_svm_tfidf.txt > ../results/paper/mono/mono_spanish_cost_svm_tfidf.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_spanish_generaltass_bilabel_lstm_collados_spanish.txt > ../results/paper/mono/mono_spanish_generaltass_bilabel_lstm_collados_spanish.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_spanish_generaltass_bilabel_svm_tfidf.txt > ../results/paper/mono/mono_spanish_generaltass_bilabel_svm_tfidf.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_spanish_generaltass_lstm_collados_spanish.txt > ../results/paper/mono/mono_spanish_generaltass_lstm_collados_spanish.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_spanish_generaltass_svm_tfidf.txt > ../results/paper/mono/mono_spanish_generaltass_svm_tfidf.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_spanish_intertass_bilabel_lstm_collados_spanish.txt > ../results/paper/mono/mono_spanish_intertass_bilabel_lstm_collados_spanish.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_spanish_intertass_bilabel_svm_tfidf.txt > ../results/paper/mono/mono_spanish_intertass_bilabel_svm_tfidf.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_spanish_intertass_lstm_collados_spanish.txt > ../results/paper/mono/mono_spanish_intertass_lstm_collados_spanish.txt
python3 senti_cross_embeddings.py ../config/new_vectors/mono/mono_spanish_intertass_svm_tfidf.txt > ../results/paper/mono/mono_spanish_intertass_svm_tfidf.txt