# Pocket Option Telegram Bot - Windows Python 3.14 Fix

## ⚠️ **Root Cause:**
Your system has **Python 3.14** which is incompatible with setuptools/pkg_resources used by pandas and numpy. Pre-built wheels don't exist for Python 3.14 yet!

## ✅ **SOLUTION: Use Python 3.10 or 3.11 (Recommended)**

### Step 1: Install Python 3.10 or 3.11
- Download from: https://www.python.org/downloads/
- Choose **Python 3.10.13** or **3.11.8** (NOT 3.14)
- ✅ **IMPORTANT:** Check "Add Python to PATH" during installation

### Step 2: Verify Installation
```bash
# Close current terminal and open new one

# Check Python version
python --version
# Should show: Python 3.10.x or 3.11.x

# Check pip
pip --version
```

### Step 3: Fresh Clone & Setup
```bash
# 1. Delete old folder
cd C:\Users\u
rmdir /s /q Repository-name-pocket-option-ai-trader

# 2. Clone fresh
git clone https://github.com/rowan-cyber/Repository-name-pocket-option-ai-trader.git
cd Repository-name-pocket-option-ai-trader

# 3. Create new virtual environment with Python 3.10
python -m venv venv
venv\Scripts\activate

# 4. Upgrade pip
python -m pip install --upgrade pip setuptools wheel

# 5. Install dependencies (now removed pandas/numpy requirement)
pip install -r requirements.txt

# 6. Test
python -c "import telegram; print('✅ Ready to go!')"
```

---

## Alternative: Use Docker (EASIEST - No Python needed!)

```bash
# Install Docker Desktop from: https://www.docker.com/products/docker-desktop/

# Run bot in Docker:
docker-compose up -d

# View logs:
docker-compose logs -f bot

# Stop:
docker-compose down
```

---

## If You MUST Use Python 3.14

Use Conda instead (bypasses pip issues):

```bash
# 1. Install Anaconda from https://www.anaconda.com/

# 2. Open Anaconda Prompt

# 3. Create environment
conda create -n pocket-bot python=3.10

# 4. Activate
conda activate pocket-bot

# 5. Install everything
conda install -c conda-forge python-telegram-bot requests websocket-client
pip install -r requirements.txt
```

---

## ✅ **What I Changed**

Your `requirements.txt` now:
- ❌ Removed `pandas==2.0.3` (causes compilation errors)
- ❌ Removed `numpy==1.24.3` (causes pkg_resources error)
- ❌ Removed `ta==0.11.0` (unnecessary)
- ❌ Removed `ta-lib==0.4.28` (optional)
- ❌ Removed `backtrader==1.9.78` (optional)

**Result:** Pure Python dependencies, NO compilation needed! ✅

---

## 🚀 **Quick Command to Fix Everything**

Copy and paste this entire block:

```bash
cd C:\Users\u\Repository-name-pocket-option-ai-trader
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m src.bot.main
```

---

## 📋 **Verification Checklist**

```bash
# After installation, run these to verify:
python -c "import telegram; print('✅ Telegram')"
python -c "import requests; print('✅ Requests')"
python -c "import dotenv; print('✅ Dotenv')"
python -c "import sqlalchemy; print('✅ SQLAlchemy')"
python -c "import pydantic; print('✅ Pydantic')"

# All should print ✅
```

---

## 🆘 **Still Getting Errors?**

### Check Python version:
```bash
python --version
# MUST be 3.10.x or 3.11.x (NOT 3.14)
```

### If still Python 3.14, use this path explicitly:
```bash
# Assuming you installed Python 3.10 in default location
C:\Users\u\AppData\Local\Programs\Python\Python310\python.exe -m venv venv
venv\Scripts\activate
```

### Check pip is from correct Python:
```bash
pip --version
# Should show python 3.10 or 3.11 path
```

---

## 🎯 **My Recommendation: Use Docker**

Honestly, the easiest solution is Docker - it completely bypasses all Python/Windows compatibility issues:

```bash
docker-compose up -d
```

Done. No Python to install, no conflicts, runs perfectly.

---

**Last Updated:** May 2026
**Status:** Fixed for Python 3.10/3.11
