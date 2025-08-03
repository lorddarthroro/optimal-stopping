# 🎯 Optimal Stopping Simulation — The Secretary Problem

Welcome to a simulation of one of the most fascinating puzzles in computer science and behavioral decision-making:  
**Optimal Stopping**, also known as the **Secretary Problem**.

---

## 🧠 The Problem (aka “The 37% Rule”)

You're presented with **n** options — one at a time, in **random order**. These could be job applicants, apartments, or romantic partners.  
After evaluating each option, you must **decide immediately** whether to select it — **no going back**.

Your mission?

> **Pick the single best option overall.**

But here's the catch:  
You **don’t know what’s coming next**, and you can’t recall past choices.  
You can only compare each new candidate to the ones you've already seen.

---

## 📂 This File: `optimal_stopping_no_knowledge.py`

This simulation focuses on the **classical "no-knowledge" model** of optimal stopping.

### ✅ Assumptions:
- You **do not know the distribution** of candidate values.
- You can **only compare relatively** (who's the best *so far*).
- You must **decide in real-time**, without second chances.
- Each candidate is **randomly ordered** and **uniquely ranked**.

This version implements the canonical solution:
- **Observe** the first ~37% of the options without selecting (exploration phase).
- Then **choose the first candidate** who is better than all seen so far.
- If none beat the early frontrunners, select the final candidate by default.

This yields a success rate of about **1/e ≈ 36.8%**, even as `n` grows large.

---

## 🧪 What This Repo Does

- Generates random permutations of unique candidates.
- Applies the optimal stopping rule across **10,000+ trials**.
- Calculates how often it successfully picks the **best** option.
- Lets you adjust `n`, `p`, and number of trials to experiment.

---

## 🔀 Future Versions & Extensions

This file models the **no-knowledge baseline**.  
But life isn't always that strict — sometimes you *do* know a bit more.

### Possible Future Branches:
- `optimal_stopping_with_distribution.py`:  
  Use Bayesian priors or known value distributions to improve strategy.
- `optimal_stopping_with_recall.py`:  
  What if you’re allowed to **recall** past candidates?
- `optimal_stopping_multiple_choices.py`:  
  What if you can pick more than one?
- `optimal_stopping_with_costs.py`:  
  Introduce **switching penalties**, time costs, or noise in evaluation.

Each variant relaxes or changes the original constraints, opening up rich real-world strategy modeling.

---

## 📚 Inspired by: *Algorithms to Live By*

Much of the motivation and insight for this simulation comes from  
> **_Algorithms to Live By_** by **Brian Christian & Tom Griffiths**.

It’s a fantastic book that shows how algorithms like optimal stopping aren’t just theoretical curiosities —  
they’re actually **tools for everyday life**: dating, job hunting, apartment searching, even parking!

---

## 🚀 Try It Yourself

```bash
# Run the simulation with default settings
python optimal_stopping_no_knowledge.py
