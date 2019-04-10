Pre-trained embeddings
============================

ELMo
----

| We are publishing :class:`Russian language ELMo embeddings model <deeppavlov.models.embedders.elmo_embedder.ELMoEmbedder>` for tensorflow-hub and :class:`LM model <deeppavlov.models.elmo.elmo.ELMo>` for training and fine-tuning ELMo as LM model.
| ELMo (Embeddings from Language Models) representations are pre-trained contextual representations from
  large-scale bidirectional language models. See a paper `Deep contextualized word representations
  <https://arxiv.org/abs/1802.05365>`__ for more information about the algorithm and a detailed analysis.

License
~~~~~~~

The pre-trained models are distributed under the `License Apache
2.0 <https://www.apache.org/licenses/LICENSE-2.0>`__.

Downloads
~~~~~~~~~

The models can be downloaded and run by configuration file or tensorflow hub module from:

+--------------------------------------------------------------------+---------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Description                                                        | Dataset parameters                          | Perplexity       | Configuration file and tensorflow hub module                                                                                                                                                                                               |
+====================================================================+=============================================+==================+============================================================================================================================================================================================================================================+
| ELMo on  `Russian Wikipedia <https://ru.wikipedia.org/>`__         | lines = 1M, tokens = 386M, size = 5GB       | 43.692           | `config_file <https://github.com/deepmipt/DeepPavlov/blob/master/deeppavlov/configs/elmo_embedder/elmo_ru_wiki.json>`__, `module_spec <http://files.deeppavlov.ai/deeppavlov_data/elmo_ru-wiki_600k_steps.tar.gz>`__                       |
+--------------------------------------------------------------------+---------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ELMo on  `Russian WMT News <http://www.statmt.org/>`__             | lines = 63M, tokens = 946M, size = 12GB     | 49.876           | `config_file <https://github.com/deepmipt/DeepPavlov/blob/master/deeppavlov/configs/elmo_embedder/elmo_ru_news.json>`__, `module_spec <http://files.deeppavlov.ai/deeppavlov_data/elmo_ru-news_wmt11-16_1.5M_steps.tar.gz>`__              |
+--------------------------------------------------------------------+---------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ELMo on  `Russian Twitter <https://twitter.com/>`__                | lines = 104M, tokens = 810M, size = 8.5GB   | 94.145           | `config_file <https://github.com/deepmipt/DeepPavlov/blob/master/deeppavlov/configs/elmo_embedder/elmo_ru_twitter.json>`__, `module_spec <http://files.deeppavlov.ai/deeppavlov_data/elmo_ru-twitter_2013-01_2018-04_600k_steps.tar.gz>`__ |
+--------------------------------------------------------------------+---------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

fastText
--------

We are publishing pre-trained word vectors for Russian language.
Several models were trained on joint `Russian
Wikipedia <https://ru.wikipedia.org/>`__
and `Lenta.ru <https://lenta.ru/>`__ corpora.
We also introduce one model for Russian conversational language that
was trained on `Russian Twitter <https://twitter.com/>`__ corpus.

All vectors are 300-dimensional. We used fastText skip-gram (see
`Bojanowski et al. (2016) <https://arxiv.org/abs/1607.04606>`__) for
vectors training as well as various preprocessing options (see below).

You can get vectors either in binary or in text (vec) formats both for
fastText and GloVe.

License
~~~~~~~

The pre-trained word vectors are distributed under the `License Apache
2.0 <https://www.apache.org/licenses/LICENSE-2.0>`__.

Downloads
~~~~~~~~~

The pre-trained **fastText skipgram** models can be downloaded from:

+-----------------------+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Domain                | Preprocessing                                           | Vectors                                                                                                                                                                                                                                                                                                                            |
+=======================+=========================================================+====================================================================================================================================================================================================================================================================================================================================+
| Wiki+Lenta            | tokenize (nltk word\_tokenize), lemmatize (pymorphy2)   | `bin <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_wiki_lenta_lemmatize/ft_native_300_ru_wiki_lenta_lemmatize.bin>`__, `vec <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_wiki_lenta_lemmatize/ft_native_300_ru_wiki_lenta_lemmatize.vec>`__                                                                   |
+                       +---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | tokenize (nltk word\_tokenize), lowercasing             | `bin <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_wiki_lenta_lower_case/ft_native_300_ru_wiki_lenta_lower_case.bin>`__, `vec <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_wiki_lenta_lower_case/ft_native_300_ru_wiki_lenta_lower_case.vec>`__                                                               |
+                       +---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | tokenize (nltk wordpunсt\_tokenize)                     | `bin <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_wiki_lenta_nltk_wordpunct_tokenize/ft_native_300_ru_wiki_lenta_nltk_wordpunct_tokenize.bin>`__, `vec <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_wiki_lenta_nltk_wordpunct_tokenize/ft_native_300_ru_wiki_lenta_nltk_wordpunct_tokenize.vec>`__           |
+                       +---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | tokenize (nltk word\_tokenize)                          | `bin <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_wiki_lenta_nltk_word_tokenize/ft_native_300_ru_wiki_lenta_nltk_word_tokenize.bin>`__, `vec <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_wiki_lenta_nltk_word_tokenize/ft_native_300_ru_wiki_lenta_nltk_word_tokenize.vec>`__                               |
+                       +---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | tokenize (nltk word\_tokenize), remove stopwords        | `bin <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_wiki_lenta_remstopwords/ft_native_300_ru_wiki_lenta_remstopwords.bin>`__, `vec <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_wiki_lenta_remstopwords/ft_native_300_ru_wiki_lenta_remstopwords.vec>`__                                                       |
+-----------------------+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Twitter               | tokenize (nltk word\_tokenize)                          | `bin <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_twitter_nltk_word_tokenize.bin>`__, `vec <http://files.deeppavlov.ai/embeddings/ft_native_300_ru_twitter_nltk_word_tokenize.vec>`__                                                                                                                                   |
+-----------------------+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Word vectors training parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These word vectors were trained with following parameters ([...] is for
default value):

fastText (skipgram)
                   

-  lr [0.1]
-  lrUpdateRate [100]
-  dim 300
-  ws [5]
-  epoch [5]
-  neg [5]
-  loss [softmax]
-  pretrainedVectors []
-  saveOutput [0]

