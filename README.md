## About
I experimented with combinations of simpler embedding models - DistilBERT and TinyBERT- with the original RAT-SQL architecture and its ablated variant - DuoRAT. The experiments conclude that our simpler architectures required significantly lesser training iterations over the dataset to converge close to the original paper’s result. The experiment results also point to the efficacy of DistilBERT and TinyBERT in nearly matching the performance of BERT on external tasks despite significant reduction in complexity.


The RAT and DuoRAT were forked and modified for experiments from their original open-source implementations (see Resources section). For BERT, DistilBERT and TinyBERT, the open-source implementations from https://huggingface.co/ were used.



## Resources
- [Original RAT implementation](https://github.com/microsoft/rat-sql)
- [Original DuoRAT implementtion](https://github.com/ElementAI/duorat)
- [How to run RAT+TinyBERT](RAT_TinyBERT/README.md)
- [How to run RAT+DistilBERT](RAT_DistilBERT/README.md)
- [How to run DuoRAT+TinyBERT](DuoRAT_TinyBERT/README.md)
- [How to run DuoRAT+DistilBERT](DuoRAT_DistilBERT/README.md)
