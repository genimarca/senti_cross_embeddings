#!/bin/bash

python3 senti_cross_embeddings.py ../config/german/sb10k67/cross_english_german_semeval_bilabel_sbk1067_lstm_collados_english_german_unsupervised_vecmap.txt > ../results/german/sb10k67/cross_english_german_semeval_bilabel_sbk1067_lstm_collados_english_german_unsupervised_vecmap.txt
echo "Finish"
python3 senti_cross_embeddings.py ../config/german/sb10k67/cross_english_german_semevalNegative_bilabel_sbk1067_lstm_collados_english_german_unsupervised_vecmap.txt > ../results/german/sb10k67/cross_english_german_semevalNegative_bilabel_sbk1067_lstm_collados_english_german_unsupervised_vecmap.txt
echo "Finish"
python3 senti_cross_embeddings.py ../config/german/cross_english_german_semeval_bilabel_sbk10_lstm_collados_english_german_unsupervised_vecmap.txt > ../results/german/cross_english_german_semeval_bilabel_sbk10_lstm_collados_english_german_unsupervised_vecmap.txt
echo "Finish"
python3 senti_cross_embeddings.py ../config/german/cross_english_german_semeval_sbk10_lstm_collados_english_german_unsupervised_vecmap.txt > ../results/german/cross_english_german_semeval_sbk10_lstm_collados_english_german_unsupervised_vecmap.txt
echo "Finish"
python3 senti_cross_embeddings.py ../config/german/cross_english_german_semevalNegative_bilabel_sbk10_lstm_collados_english_german_unsupervised_vecmap.txt > ../results/german/cross_english_german_semevalNegative_bilabel_sbk10_lstm_collados_english_german_unsupervised_vecmap.txt
echo "Finish"