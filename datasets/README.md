# Aegis datasets

## ThaiScamBench

Primary Thai-language benchmark for the Aegis scam-detection experiments.

Source: https://github.com/nutthakorn7/ThaiScamBench

Recommended use in Aegis:
- Thai scam / legitimate message classification
- code-switching and obfuscation robustness
- URL-masked evaluation
- domain hold-out evaluation
- continual-learning and concept-drift experiments

The upstream repository is MIT licensed. Keep the original attribution and license when using its code or dataset artifacts.

### Fetch locally

Run:

```bash
bash scripts/fetch_thaiscambench.sh
```

This clones the upstream repository into:

```
external/ThaiScamBench/
```

Do not treat a random train/test split as the only benchmark. For Aegis, prefer temporal or domain hold-out experiments so the model is evaluated on emerging/unseen scam patterns.
