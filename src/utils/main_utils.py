import sys
from typing import Dict, Tuple
import os

import numpy as np
import pandas as pd
import pickle
import yaml
import boto3

from src.constants import *
from src.exception import CustomException
from src.logger import logging

class MainUtils:
    def __init__(self)-> None:
        pass

    def read_yaml_file(self, filename : str)->dict:
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)
            
        except Exception as e:
            raise CustomException(e,sys) from e

