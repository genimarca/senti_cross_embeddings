#!/usr/bin/python3
'''
Created on 25 jul. 2018

@author: Eugenio Martínez Cámara
'''
from sce.model.classification.abs_classification import ABSClassification
from sce.model.embeddings.abs_word_embeddings import ABSWordEmbeddings
from sce.model.properties_manager import PropertiesManager
from sce.model.properties_names import PropertiesNames
from numpy import array as np_array
from numpy.random import rand as np_rand
from numpy.random import seed as np_seed
from numpy import argmax as np_argmax
from numpy import median as np_median
from tensorflow import set_random_seed as tsf_set_random_seed
from keras.models import Model
from keras.layers import Input, Embedding, LSTM, Dense, Dropout, Flatten, Bidirectional
from keras.initializers import glorot_uniform
from keras import regularizers

from keras.callbacks import EarlyStopping

class BiLSTMClassficiation(ABSClassification):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__random_seed = None
        self.__training_corpus = None
        self.__evaluation_corpus = None
        self.__predictions = None
        self.__features_training = None
        self.__features_test = None
        self.__features_magic_index = {"OOV":0, "PADDING":1}
        self.__classifier = None
        self.__features_transformers = []
        self.__max_length = 0
        self.__batch_size = 0
        self.__allow_labels = None
        self.__oov_vector = None
        self.__padding_vector = None
        self.__nlp_utils = None
        
        
    @property
    def nlp_utils(self):
        """
        """
        return self.__nlp_utils
        
    @nlp_utils.setter
    def nlp_utils(self, a_nlp_utils):
        """
        """
        self.__nlp_utils = a_nlp_utils
        
        
    @property
    def random_seed(self):
        return self.__random_seed
    
    @random_seed.setter
    def random_seed(self, a_random_seed):
        self.__random_seed = a_random_seed
    
    @property
    def training_corpus(self):
        return self.__training_corpus
    
    @training_corpus.setter
    def training_corpus(self, a_training_corpus):
        self.__training_corpus = a_training_corpus
        
        
    @property
    def evaluation_corpus(self):
        return self.__evaluation_corpus
    
    @evaluation_corpus.setter
    def evaluation_corpus(self, a_evaluation_corpus):
        self.__evaluation_corpus = a_evaluation_corpus
        
    @property
    def predictions(self):
        return self.__predictions
    
    @property
    def allow_labels(self):
        return self.__allow_labels
    
    @allow_labels.setter
    def allow_labels(self, a_allow_labels):
        self.__allow_labels = a_allow_labels
    
    def __load_exk_embeddings(self, exk_embeddings_handler):
        
        path = PropertiesManager.get_prop_value(PropertiesNames.EMBEDDINGS_PATH)
        emb_max_words = PropertiesManager.get_prop_value(PropertiesNames.EMBEDDINGS_MAX_WORDS)
        if emb_max_words is not None:
            emb_max_words = int(emb_max_words)
        else:
            emb_max_words = 100000
            
        encoding = PropertiesManager.get_prop_value(PropertiesNames.ENCODING)
        print("Begin: Loading embeddings")
        exk_embeddings_handler.load(path, encoding, ofset=2, max_words=emb_max_words)
        print("End: Loading embeddings")
        
        if self.__oov_vector is None:
            self.__oov_vector = 2 * 0.1 * np_rand(exk_embeddings_handler.get_vector_embedding_dimension()) - 1
        exk_embeddings_handler.set_vector_embedding("_OOV_", self.__features_magic_index["OOV"], self.__oov_vector)
        
        if self.__padding_vector is None:
            self.__padding_vector = 2 * 0.1 * np_rand(exk_embeddings_handler.get_vector_embedding_dimension()) - 1
        exk_embeddings_handler.set_vector_embedding("_PADDING_", self.__features_magic_index["PADDING"], self.__padding_vector)
    
    def __init_random_seed(self):
        np_seed(self.__random_seed)
        tsf_set_random_seed(self.__random_seed)
    
    def __feature_engineering(self, corpus):
        for doc_index in corpus.corpus:
            doc = corpus.get_document(doc_index)
            preparing_text = doc.raw_text
            if not corpus.is_lowercase:
                preparing_text = self.__nlp_utils.normalization_lowercase(preparing_text)
            if PropertiesManager.get_prop_value(PropertiesNames.NORM_USER):
                preparing_text = self.__nlp_utils.normalization_users(preparing_text, "@user")
            preparing_text = self.__nlp_utils.tokenize(preparing_text, a_preserve_case=False, a_reduce_len=True, a_strip_handles=False)
            if PropertiesManager.get_prop_value(PropertiesNames.NORM_STOPPER):
                preparing_text = self.__nlp_utils.stopper(preparing_text, PropertiesManager.get_prop_value(PropertiesNames.LANGUAGE_TRAINING))
            if PropertiesManager.get_prop_value(PropertiesNames.NORM_STEMMER):
                preparing_text = self.__nlp_utils.stemmer(preparing_text, PropertiesManager.get_prop_value(PropertiesNames.LANGUAGE_TRAINING))
            doc.process_text = preparing_text
            
            
        
            
    
    def make_feature_space_training(self, external_knowledge=None):
        
        self.__feature_engineering(self.__training_corpus)
        
        self.__init_random_seed()
        exk_embeddings_handler = external_knowledge["embeddings"]
        self.__load_exk_embeddings(exk_embeddings_handler)
        
        
        self.__max_length = np_median([len(self.__training_corpus.get_document(doc_index).process_text)for doc_index in self.__training_corpus.corpus])
        self.__max_length = int(self.__max_length)
        self.__features_training = []
        own_features_training_append = self.__features_training.append
        for doc_index in self.__training_corpus.corpus:
            doc = self.__training_corpus.get_document(doc_index)
            feature_index = self.__max_length * [self.__features_magic_index["PADDING"]]
            for word_index in range(self.__max_length):
                if word_index < len(doc.process_text):
                    word_emb_index = exk_embeddings_handler.get_word_index(doc.process_text[word_index])
                    if word_emb_index is not None:
                        feature_index[word_index] = word_emb_index
                    else:
                        feature_index[word_index] = self.__features_magic_index["OOV"]
            own_features_training_append(feature_index)
            
        print(self.__features_training[:5])
        self.__features_transformers.append(exk_embeddings_handler)
        
        
    def make_feature_space_evaluation(self, external_knowledge=None):
        
        self.__feature_engineering(self.__evaluation_corpus)
        
        self.__features_test = []
        own_features_evaluation_append = self.__features_test.append
        if external_knowledge is not None and "embeddings_evaluation" in external_knowledge:
            exk_embeddnings_handler = external_knowledge["embeddings_evaluation"]
            self.__load_exk_embeddings(exk_embeddnings_handler)
        else:
            exk_embeddnings_handler = self.__features_transformers[0]
        
        for doc_index in self.__evaluation_corpus.corpus:
            doc = self.__evaluation_corpus.get_document(doc_index)
            features_index = self.__max_length * [self.__features_magic_index["PADDING"]]
            for word_index in range(self.__max_length):
                if word_index < len(doc.process_text):
                    word_emb_index = exk_embeddnings_handler.get_word_index(doc.process_text[word_index])
                    if word_emb_index is not None:
                        features_index[word_index] = word_emb_index
                    else:
                        features_index[word_index] = self.__features_magic_index["OOV"]
            own_features_evaluation_append(features_index)
        print(self.__features_test[:5])
    
    def training(self):
        
        self.__batch_size = int(PropertiesManager.get_prop_value(PropertiesNames.NN_BATCH_SIZE))
        epochs_size = int(PropertiesManager.get_prop_value(PropertiesNames.NN_EPOCH_SIZE))
        
        docs_labels = [self.__training_corpus.get_document(doc_id).sparse_label for doc_id in self.__training_corpus.corpus]
        print(docs_labels)
        exk_embeddings_handler = self.__features_transformers[0]
        x_input = Input(shape=(self.__max_length, ), dtype="float64")
        embeddings_weights = np_array(exk_embeddings_handler.word_embeddings)
        layer_embeddings = Embedding(exk_embeddings_handler.get_number_of_embeddings(),
                                     exk_embeddings_handler.get_vector_embedding_dimension(),
                                     input_length=self.__max_length,
                                     trainable=False,
                                     weights=[embeddings_weights])
        
        x_sequence = layer_embeddings(x_input)
        
        #x_encoding = LSTM(units=128, return_sequences=True)(x_sequence)
        x_encoding = Bidirectional(LSTM(units=256, return_sequences=True))(x_sequence)
        #x_encoding = Dense(64,
        #                   activation='relu',
        #                   kernel_initializer=glorot_uniform(self.__random_seed),
        #                   kernel_regularizer=regularizers.l2(0.0001),
        #                   activity_regularizer=regularizers.l2(0.0001))(x_encoding)
                           
        x_encoding = Dense(128,
                           activation='relu',
                           kernel_initializer=glorot_uniform(self.__random_seed),
                           kernel_regularizer=regularizers.l2(0.0001))(x_encoding)
        x_encoding = Dropout(0.5)(x_encoding)
        #x_encoding = Dense(32,
        #                   activation='relu',
        #                   kernel_initializer=glorot_uniform(self.__random_seed),
        #                   kernel_regularizer=regularizers.l2(0.001),
        #                   activity_regularizer=regularizers.l2(0.0001))(x_encoding)
        x_encoding = Dense(32,
                           activation='relu',
                           kernel_initializer=glorot_uniform(self.__random_seed),
                           kernel_regularizer=regularizers.l2(0.0001))(x_encoding)
                                              
        x_encoding = Dropout(0.5)(x_encoding)
        x_encoding = Flatten()(x_encoding)
        x_logits = Dense(self.__allow_labels.number_of_labels,
                         activation="softmax")(x_encoding)
        
        self.__classifier = Model(x_input, x_logits)
        
        self.__classifier.summary()
        self.__classifier.compile(loss="sparse_categorical_crossentropy",
                         optimizer="adam",
                         metrics=['accuracy'])
        
        early_stopping = EarlyStopping('loss', patience=5, mode='min')
        self.__classifier.fit(x = np_array(self.__features_training),
                     y=np_array(docs_labels),
                     batch_size=self.__batch_size,
                     epochs=epochs_size,
                     shuffle = False,
                     callbacks=[early_stopping],
                     verbose=1) 
           
    
    def evaluation(self):
        self.__predictions = self.__classifier.predict(np_array(self.__features_test), batch_size=self.__batch_size, verbose=1)
        self.__predictions = np_argmax(self.__predictions, axis=1)
    
    
    
        