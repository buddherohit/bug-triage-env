# 🚀 Bug Triage OpenEnv Environment

A real-world reinforcement learning environment where AI agents learn to triage software bug reports by assigning priority, team ownership, and suggested fixes.

Built for **OpenEnv Hackathon – Round 1**

---
# 📌 Overview

Bug triage is a common real-world software engineering task. This environment simulates bug triage workflow where an AI agent learns to:

* Assign priority to bugs
* Assign responsible team
* Suggest potential fixes

The environment follows the **OpenEnv standard** with:

* `step()`
* `reset()`
* `state()`

---

# 🎯 Tasks

This environment contains **3 tasks**:

### 🟢 Task 1 — Easy

Assign **priority** to bug

Example:

Input:

```
App crashes when clicking login
```

Expected Output:

```
High
```

---

### 🟡 Task 2 — Medium

Assign **team ownership**

Input:

```
Login button UI broken
```

Expected Output:

```
Frontend
```

---

### 🔴 Task 3 — Hard

Suggest **solution**

Input:

```
Null pointer exception in auth module
```

Expected Output:

```
Add null check
```

---

# 🧠 Environment API

The environment implements standard OpenEnv interface:

### reset()

Resets environment

Returns:

```
Initial observation
```

---

### step(action)

Takes action and returns:

```
observation, reward, done, info
```

---

### state()

Returns current state

---

# 🏆 Reward Function

| Condition      | Reward |
| -------------- | ------ |
| Correct Answer | 1.0    |
| Partial Match  | 0.5    |
| Some Progress  | 0.2    |
| Incorrect      | -0.2   |

---

# 📁 Project Structure

```
bug-triage-env/
│
├── environment.py
├── tasks.py
├── grader.py
├── reward.py
├── inference.py
├── openenv.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone repository

```
git clone <repo-url>
cd bug-triage-env
```

Install dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Run Environment

Run baseline inference

```
python inference.py
```

---

# 📊 Example Output

```
[START]
[STEP]
Reward: 1.0
[STEP]
Reward: 1.0
[STEP]
Reward: 1.0
[END] Final Score: 1.0
```

---

# 🐳 Docker

Build container

```
docker build -t bug-triage-env .
```

Run container

```
docker run bug-triage-env
```

---

# 🚀 HuggingFace Deployment

This environment is deployed using HuggingFace Spaces with Docker.

Requirements:

* Dockerfile
* inference.py
* openenv.yaml

---

# 📈 Baseline Score

| Task   | Score |
| ------ | ----- |
| Easy   | 1.0   |
| Medium | 1.0   |
| Hard   | 1.0   |

Final Score: **1.0**

---

# 🎯 Features

* Real world task simulation
* 3 difficulty levels
* Reward shaping
* Baseline inference
* Docker support
* OpenEnv compatible

---

# 🛠 Tech Stack

* Python
* OpenEnv
* Docker
* HuggingFace Spaces

---

# 👨‍💻 Author

**Rohit Buddhe**
Computer Engineering Student

---

# 📄 License

MIT License

---

# ⭐ Submission

OpenEnv Hackathon Round 1 Submission

---
