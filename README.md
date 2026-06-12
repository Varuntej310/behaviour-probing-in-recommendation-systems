# Behavioral Probing in Recommendation Systems

This repository contains a PyTorch implementation of SASRec (Self-Attentive Sequential Recommendation), extended with behavioral probing experiments to analyze how models respond to user behavioral signals.

## Quick Start

**To train the SASRec model (e.g., MovieLens 1M):**
```bash
python main.py --dataset=ml-1m --train_dir=default --maxlen=200 --dropout_rate=0.2 --device=cuda
```

**Inference only**
```bash
python main.py --device=cuda --dataset=ml-1m --train_dir=default \
    --state_dict_path=[YOUR_CKPT_PATH] --inference_only=true --maxlen=200
```
(Note: Results may vary slightly due to random negative sampling.)

## Behavioral Probing Experiments

Located in probing.py, these experiments analyze proxy correlation, cold-start signal recovery, behavior-error correlation, and behavioral stratification.

**Minimal probing (SASRec only):**
```bash
python probing.py --dataset ml-1m --model_path ml1m_model.pth
```

**Full analysis (+ shuffled model, MF-SVD baseline):**
```bash
python probing.py --dataset ml-1m --model_path ml1m_model.pth \
    --shuffled_model_path ml1m_shuffled_model.pth \
    --run_mf --run_coldstart --run_behavior_analysis
```

**Supported Datasets**:

datasets are in the data/ folder (format: user_id item_id, space-separated, one per line):

- MovieLens 1M (ml-1m.txt, ml-1m_shuffled.txt)
- Amazon Beauty (Beauty.txt, Beauty_shuffled.txt)
- Steam (Steam.txt, Steam_shuffled.txt)
- Wikipedia (wikipedia.txt, wikipedia_shuffled.txt)

For shuffling the data use `shuffle_seqs.py`

## Acknowledgements & Citation

This codebase utilizes and builds upon the SASRec implementation. Please cite the original paper and PyTorch implementation:

```
@inproceedings{kang2018self,
  title={Self-attentive sequential recommendation},
  author={Kang, Wang-Cheng and McAuley, Julian},
  booktitle={2018 IEEE International Conference on Data Mining (ICDM)},
  pages={197--206},
  year={2018},
  organization={IEEE}
}

@online{huang2020sasrec_pytorch,
  author  = {Zan Huang},
  title   = {SASRec.pytorch},
  year    = {2020},
  url     = {[https://github.com/pmixer/SASRec.pytorch](https://github.com/pmixer/SASRec.pytorch)}
}
```
