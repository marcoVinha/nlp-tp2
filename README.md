# Fine tuning BERTimbau on the Mac-Morpho dataset

## Overview

This repo fine tunes a BERTimbau model ([`neuralmind/bert-base-portuguese-cased`](https://huggingface.co/neuralmind/bert-base-portuguese-cased), 110M parameters) in the Mac-Morpho dataset to perform a Parts of Speech Tagging (POS Tagging) task in portuguese.

## Objectives

- Fine tune a model to perform POS Tagging in the Mac-Morpho dataset
- Evaluate the overall performance of the model
- Compare it to the [`lisaterumi/postagger-portuguese`](https://huggingface.co/lisaterumi/postagger-portuguese), which already does that

## Managing requirements

To be able to reproduce the notebook in this repo in a Python environment with the same requirements listed here:
- Install Python 3.10
- Install [uv](https://docs.astral.sh/uv/) to manage the deps
- Run `uv sync`
    - This will create a virtual environment in the `.venv/` dir
    - Use this virtual environment to run any Python code for this project
- Execute the single notebook inside the `notebooks/` directory
