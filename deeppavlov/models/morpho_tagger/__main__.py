import argparse

from deeppavlov.core.common.file import find_config
from deeppavlov.download import deep_download
from deeppavlov.models.morpho_tagger.common import predict_with_model

parser = argparse.ArgumentParser()
parser.add_argument("config_path", help="path to file with prediction configuration")
parser.add_argument("-d", "--download", action="store_true", help="download model components")

if __name__ == "__main__":
    args = parser.parse_args()
    config_path = find_config(args.config_path)
    if args.download:
        deep_download(config_path)
    predict_with_model(config_path)
