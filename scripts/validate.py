#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# usage: <schema file> <yaml file to validate>

from jsonschema import validate
import yaml
import sys

with open(sys.argv[1]) as f:
    schema = yaml.safe_load(f)

with open(sys.argv[2]) as f:
    instance = yaml.safe_load(f)

validate(instance, schema)
