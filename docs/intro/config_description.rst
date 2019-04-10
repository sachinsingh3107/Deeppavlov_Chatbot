Configuration files
===================

An NLP pipeline config is a JSON file that contains one required element ``chainer``:

.. code:: python

    {
      "chainer": {
        "in": ["x"],
        "in_y": ["y"],
        "pipe": [
          ...
        ],
        "out": ["y_predicted"]
      }
    }

:class:`~deeppavlov.core.common.chainer.Chainer` is a core concept of DeepPavlov library: chainer builds a pipeline from
heterogeneous components (Rule-Based/ML/DL) and allows to train or infer from pipeline as a whole. Each component in the
pipeline specifies its inputs and outputs as arrays of names, for example: ``"in": ["tokens", "features"]`` and
``"out": ["token_embeddings", "features_embeddings"]`` and you can chain outputs of one components with inputs of other
components:

.. code:: python

    {
      "class_name": "deeppavlov.models.preprocessors.str_lower:StrLower",
      "in": ["x"],
      "out": ["x_lower"]
    },
    {
      "class_name": "nltk_tokenizer",
      "in": ["x_lower"],
      "out": ["x_tokens"]
    },

Each :class:`~deeppavlov.core.models.component.Component` in the pipeline must implement method :meth:`__call__` and has
``class_name`` parameter, which is its registered codename, or full name of any python class in the form of
``"module_name:ClassName"``. It can also have any other parameters which repeat its :meth:`__init__` method arguments.
Default values of :meth:`__init__` arguments will be overridden with the config values during the initialization of a
class instance.

You can reuse components in the pipeline to process different parts of data with the help of ``id`` and ``ref``
parameters:

.. code:: python

    {
      "class_name": "nltk_tokenizer",
      "id": "tokenizer",
      "in": ["x_lower"],
      "out": ["x_tokens"]
    },
    {
      "ref": "tokenizer",
      "in": ["y"],
      "out": ["y_tokens"]
    },


Variables
---------

As of *version 0.1.0* every string value in a configuration file is interpreted
as a `format string <https://docs.python.org/3.6/library/string.html#formatstrings>`__ where fields are evaluated
from ``metadata.variables`` element:

.. code:: python

    {
      "chainer": {
        "in": ["x"],
        "pipe": [
          {
            "class_name": "my_component",
            "in": ["x"],
            "out": ["x"],
            "load_path": "{MY_PATH}/file.obj"
          },
          {
            "in": ["x"],
            "out": ["y_predicted"],
            "config_path": "{CONFIGS_PATH}/classifiers/intents_snips.json"
          }
        ],
        "out": ["y_predicted"]
      },
      "metadata": {
        "variables": {
          "MY_PATH": "/some/path",
          "CONFIGS_PATH": "{DEEPPAVLOV_PATH}/configs"
        }
      }
    }

Variable ``DEEPPAVLOV_PATH`` is always preset to be a path to the ``deeppavlov`` python module.

One can override configuration variables using environment variables with prefix ``DP_``. So environment variable
``DP_VARIABLE_NAME`` will override ``VARIABLE_NAME`` inside a configuration file.

For example, adding ``DP_ROOT_PATH=/my_path/to/large_hard_drive`` will make most configs use this path for downloading and reading  embeddings/models/datasets.

Training
--------

There are two abstract classes for trainable components: :class:`~deeppavlov.core.models.estimator.Estimator`
and :class:`~deeppavlov.core.models.nn_model.NNModel`.

:class:`~deeppavlov.core.models.estimator.Estimator` are fit once on any data with no batching or early stopping,
so it can be safely done at the time of pipeline initialization. :meth:`fit` method has to be implemented for each
:class:`~deeppavlov.core.models.estimator.Estimator`. One example is :class:`~deeppavlov.core.data.vocab.Vocab`.

:class:`~deeppavlov.core.models.nn_model.NNModel` requires more complex training. It can only be trained in a supervised
mode (as opposed to :class:`~deeppavlov.core.models.estimator.Estimator` which can be trained in both supervised and
unsupervised settings). This process takes multiple epochs with periodic validation and logging.
:meth:`~deeppavlov.core.models.nn_model.NNModel.train_on_batch` method has to be implemented for each
:class:`~deeppavlov.core.models.nn_model.NNModel`.

Training is triggered by :func:`~deeppavlov.core.commands.train.train_evaluate_model_from_config` function.


Train config
~~~~~~~~~~~~

:class:`~deeppavlov.core.models.estimator.Estimator` s that are trained should also have ``fit_on`` parameter which
contains a list of input parameter names. An :class:`~deeppavlov.core.models.nn_model.NNModel` should have the ``in_y``
parameter which contains a list of ground truth answer names. For example:

.. code:: python

    [
      {
        "id": "classes_vocab",
        "class_name": "default_vocab",
        "fit_on": ["y"],
        "level": "token",
        "save_path": "vocabs/classes.dict",
        "load_path": "vocabs/classes.dict"
      },
      {
        "in": ["x"],
        "in_y": ["y"],
        "out": ["y_predicted"],
        "class_name": "intent_model",
        "save_path": "classifiers/intent_cnn",
        "load_path": "classifiers/intent_cnn",
        "classes_vocab": {
          "ref": "classes_vocab"
        }
      }
    ]

The config for training the pipeline should have three additional elements: ``dataset_reader``, ``dataset_iterator``
and ``train``:

.. code:: python

    {
      "dataset_reader": {
        "class_name": ...,
        ...
      },
      "dataset_iterator": {
        "class_name": ...,
        ...
      },
      "chainer": {
        ...
      },
      "train": {
        ...
      }
    }


Simplified version of training pipeline contains two elements: ``dataset`` and ``train``. The ``dataset`` element
currently can be used for train from classification data in ``csv`` and ``json`` formats. You can find complete examples
of how to use simplified training pipeline in
:config:`intents_sample_csv.json <classifiers/intents_sample_csv.json>` and
:config:`intents_sample_json.json <classifiers/intents_sample_json.json>` config files.


Train Parameters
~~~~~~~~~~~~~~~~

``train`` element can contain a ``class_name`` parameter that references a trainer class (default value is
:class:`nn_trainer <deeppavlov.core.trainers.NNTrainer>`). All other parameters will be passed as keyword arguments
to the trainer class's constructor.

Metrics
_______

.. code:: python

    "train": {
      "class_name": "nn_trainer",
      "metrics": [
        "f1",
        {
          "name": "accuracy",
          "inputs": ["y", "y_labels"]
        },
        {
          "name": "roc_auc",
          "inputs": ["y", "y_probabilities"]
        }
      ],
      ...
    }

| The first metric in the list is used for early stopping.
|
| Each metric can be described as a JSON object with ``name`` and ``inputs`` properties, where ``name``
  is a registered name of a metric function and ``inputs`` is a list of parameter names from chainer's
  inner memory that will be passed to the metric function.
|
| If a metric is described as a single string, this string is interpreted as a registered name.
|
| Default value for ``inputs`` parameter is a concatenation of chainer's ``in_y`` and ``out`` parameters.


DatasetReader
~~~~~~~~~~~~~

:class:`~deeppavlov.core.dara.dataset_reader.DatasetReader` class reads data and returns it in a specified format.
A concrete :class:`DatasetReader` class should be inherited from this base class and registered with a codename:


.. code:: python

    from deeppavlov.core.common.registry import register
    from deeppavlov.core.data.dataset_reader import DatasetReader

    @register('dstc2_datasetreader')
    class DSTC2DatasetReader(DatasetReader):


DataLearningIterator and DataFittingIterator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:class:`~deeppavlov.core.data.data_learning_iterator.DataLearningIterator` forms the sets of data ('train', 'valid',
'test') needed for training/inference and divides them into batches. A concrete :class:`DataLearningIterator` class
should be registered and can be inherited from :class:`deeppavlov.data.data_learning_iterator.DataLearningIterator`
class. This is a base class and can be used as a :class:`DataLearningIterator` as well.

:class:`~deeppavlov.core.data.data_fitting_iterator.DataFittingIterator` iterates over provided dataset without
train/valid/test splitting and is useful for :class:`~deeppavlov.core.models.estimator.Estimator` s that do not require
training.


Inference
---------

All components inherited from :class:`~deeppavlov.core.models.component.Component` abstract class can be used for
inference. The :meth:`__call__` method should return standard output of a component. For example, a `tokenizer`
should return `tokens`, a `NER recognizer` should return `recognized entities`, a `bot` should return an `utterance`.
A particular format of returned data should be defined in :meth:`__call__`.

Inference is triggered by :func:`~deeppavlov.core.commands.infer.interact_model` function. There is no need in a
separate JSON for inference.
