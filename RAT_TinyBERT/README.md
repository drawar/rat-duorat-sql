# DistilRAT & DistilDuoRAT

This repository contains the code for the DistilRAT and DistilDuoRAT based on the following papers:

- RAT-SQL: ["RAT-SQL: Relation-Aware Schema Encoding and Linking for Text-to-SQL Parsers"](https://arxiv.org/abs/1911.04942) [Code](https://github.com/microsoft/rat-sql)
- DuoRAT: ["DuoRAT: Towards Simpler Text-to-SQL Models"](https://arxiv.org/abs/2010.11119) [Code](https://github.com/ElementAI/duorat)

## Usage

### Step 1: Download third-party datasets & dependencies

Download the datasets: [Spider](https://yale-lily.github.io/spider) and [WikiSQL](https://github.com/salesforce/WikiSQL). In case of Spider, make sure to download the `08/03/2020` version or newer.
Unpack the datasets somewhere outside this project to create the following directory structure:

```
/path/to/data
├── spider
│   ├── database
│   │   └── ...
│   ├── dev.json
│   ├── dev_gold.sql
│   ├── tables.json
│   ├── train_gold.sql
│   ├── train_others.json
│   └── train_spider.json
└── wikisql
    ├── dev.db
    ├── dev.jsonl
    ├── dev.tables.jsonl
    ├── test.db
    ├── test.jsonl
    ├── test.tables.jsonl
    ├── train.db
    ├── train.jsonl
    └── train.tables.jsonl
```

To work with the WikiSQL dataset, clone its evaluation scripts into this project:

```bash
mkdir -p third_party
git clone https://github.com/salesforce/WikiSQL third_party/wikisql
```

### Step 2: Build and run the Docker image

We have provided a `Dockerfile` that sets up the entire environment for you.
It assumes that you mount the datasets downloaded in Step 1 as a volume `/mnt/data` into a running image.
Thus, the environment setup for RAT-SQL is:

```bash
docker build -t ratsql .
docker run --rm -m4g -v /path/to/data:/mnt/data -it ratsql
```

Note that the image requires at least 4 GB of RAM to run preprocessing.
By default, [Docker Desktop for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/) and [Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows) run containers with 2 GB of RAM.
The `-m4g` switch overrides it; alternatively, you can increase the default limit in the Docker Desktop settings.

> If you prefer to set up and run the codebase without Docker, follow the steps in `Dockerfile` one by one.
> Note that this repository requires Python 3.7 or higher and a JVM to run [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/).

### Step 3: Set up tracking

```
docker build -t ratsql . -t [git-user]/ratsql
docker run -p 5000:5000 --rm -m4g -v /path/to/tracking/data:/mnt/data -it [git-user]/ratsql
```

### Step 4: Run the experiments

Every experiment has its own config file in `experiments`.
The pipeline of working with any model version or dataset is:

```bash
python run.py preprocess experiment_config_file  # Step 4a: preprocess the data
python run.py train experiment_config_file       # Step 4b: train a model
python run.py eval experiment_config_file        # Step 4c: evaluate the results
```

List of experiments (using Spider data set)

1. Replica (i.e. RAT + BERT): `experiments/rat-bert-run.jsonnet`
2. RAT + DistilBERT: `experiments/rat-distilbert-run.jsonnet` (distilled from the generic `bert-base-uncased` model pre-trained with MLM objective)
3. RAT + DistilBART: `experiments/rat-distilbart-run.jsonnet` (distilled from the generic `facebook/bart-base` model fine-tuned on the summarization task on the XSUM dataset)
