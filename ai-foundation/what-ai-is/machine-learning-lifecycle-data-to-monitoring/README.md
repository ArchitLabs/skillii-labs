# Machine Learning Lifecycle: Build, Test, Deploy, Monitor

Course: AI Foundation · Section: What AI is, how it began, how it is built

The lab from the SKILLii lesson video *Machine Learning Lifecycle: Build, Test, Deploy, Monitor*. It walks one tiny
model through the whole loop: it makes 100 delivered food orders (distance, and whether each arrived after the
40 minutes the app promises), splits them into 60 to train on and 40 held out, trains the simplest possible model (a
distance from which to predict "late"), tests it on the held-out orders, deploys it as a function the app calls,
monitors it week by week against what really happened, and, when roadworks make every kilometre slower and the
accuracy falls, retrains it on the orders since the change and deploys it again.

The orders are made up by the script from a fixed rule (3 minutes a km, then 4 after the roadworks, plus 5 minutes
of traffic on every third order), so the numbers are the same on every run. The steps follow the lifecycle in the
[AWS Well-Architected Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lifecycle.html)
and in Google Cloud's
[MLOps: Continuous delivery and automation pipelines in machine learning](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning).

| Script | What it shows | Cost to run |
|---|---|---|
| `lifecycle.py` | **Data, split, train, test, deploy, monitor, retrain**: a model that passes its test, loses accuracy when the world changes, and recovers after retraining on recent data | free |

The script uses only Python itself: no library, no network, no key. It creates nothing and leaves nothing to tidy up.

## Run it

```bash
python lifecycle.py
```

## Recorded run

<!-- skillii-kit:run lifecycle -->
Recorded run of `python lifecycle.py` (25 Nov 2026):

```text
data: 60 orders to train, 40 held out
trained: late from 14 km
held-out test: 97.5%
a 12 km order: on time
week 1: 95.0%
week 2: 80.0%  ALERT: below 90%
retrained: late from 11 km
week 5, old model: 80.0%
week 5, new model: 95.0%
a 12 km order: late
```

This lab makes no paid request.
<!-- /skillii-kit:run lifecycle -->
