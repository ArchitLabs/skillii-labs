# 4 Ways AI Learns: Supervised to Self-Supervised

Course: AI Foundation · Section: How a model learns

The lab from the SKILLii lesson video *4 Ways AI Learns: Supervised to Self-Supervised*. What sets the four ways
apart is the signal the model learns from: labelled answers (supervised), no labels at all (unsupervised), a reward
after each action (reinforcement), or targets made from the data itself, such as the next word (self-supervised).
As [Dive into Deep Learning](https://d2l.ai/chapter_introduction/index.html) puts it, self-supervised learning
"manufactures supervisory targets directly from unlabeled data".

| Script | What it shows | Cost to run |
|---|---|---|
| `four_ways.py` | Six made-up parcels and a short dispatch log, learned four ways. Supervised: from six labelled parcels it learns a weight cut and labels two new parcels. Unsupervised: with no labels, two-means clustering finds the same two groups. Reinforcement: with only a reward per try, it learns to send light parcels by bike and heavy ones by van. Self-supervised: it turns the log into (word, next word) pairs and learns which word comes next | free |

The script uses only Python itself: nothing to install, no network, no key. It creates nothing and leaves nothing to
tidy up. The data never changes, so the output is the same on every run. Each line is printed after a half-second
pause, so you can read the output as it arrives.

## Run it

```bash
python four_ways.py
```

## Recorded run

<!-- skillii-kit:run four-ways -->
Recorded run of `python four_ways.py` (26 Nov 2026):

```text
supervised: 6 labelled parcels, learned the cut at 6.5 kg
  new parcel 4 kg -> small
  new parcel 9 kg -> large
unsupervised: no labels, found 2 groups: [1, 2, 3] and [10, 11, 12]
reinforcement: no labels, one reward per try
  parcel 1 kg: bike +2, van +1
  parcel 2 kg: bike +2, van +1
  parcel 3 kg: bike +2, van +1
  parcel 10 kg: bike -5, van +1
  parcel 11 kg: bike -5, van +1
  parcel 12 kg: bike -5, van +1
  learned: bike for [1, 2, 3], van for the rest
self-supervised: 8 pairs made from the log, first parcel -> to
  after parcel: to (3 of 3 times)
  after to: pune (2 of 3 times)
```

This lab makes no paid request.
<!-- /skillii-kit:run four-ways -->
