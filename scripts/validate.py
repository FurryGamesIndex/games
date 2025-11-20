#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# usage: <schema file> <yaml file to validate>

from jsonschema import validate
from ruamel.yaml import YAML

yaml = YAML(typ="safe")
import sys

with open(sys.argv[1]) as f:
    schema = yaml.load(f)

with open(sys.argv[2]) as f:
    instance = yaml.load(f)

validate(instance, schema)
