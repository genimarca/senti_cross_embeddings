#!/bin/bash

python3 senti_cross_embeddings.py ../config/new_vectors/majority/cross_english_italian_semeval_bilabel_sentipol_majority.txt > ../results/paper/majority/cross_english_italian_semeval_bilabel_sentipol_majority.txt
python3 senti_cross_embeddings.py ../config/new_vectors/majority/cross_english_italian_semeval_sentipol_majority.txt > ../results/paper/majority/cross_english_italian_semeval_sentipol_majority.txt
python3 senti_cross_embeddings.py ../config/new_vectors/majority/cross_english_spanish_semeval_bilabel_cost_majority.txt > ../results/paper/majority/cross_english_spanish_semeval_bilabel_cost_majority.txt
python3 senti_cross_embeddings.py ../config/new_vectors/majority/cross_english_spanish_semeval_bilabel_generaltass_majority.txt > ../results/paper/majority/cross_english_spanish_semeval_bilabel_generaltass_majority.txt
python3 senti_cross_embeddings.py ../config/new_vectors/majority/cross_english_spanish_semeval_bilabel_intertass_majority.txt > ../results/paper/majority/cross_english_spanish_semeval_bilabel_intertass_majority.txt
python3 senti_cross_embeddings.py ../config/new_vectors/majority/cross_english_spanish_semeval_generaltass_majority.txt > ../results/paper/majority/cross_english_spanish_semeval_generaltass_majority.txt
python3 senti_cross_embeddings.py ../config/new_vectors/majority/cross_english_spanish_semeval_intertass_majority.txt > ../results/paper/majority/cross_english_spanish_semeval_intertass_majority.txt
