# Pocket Option Telegram Bot - Installation Issues & Solutions

## 🔧 Fixing pandas/numpy Installation Error on Windows

The error you're experiencing is a **common Windows issue** with pandas compilation. Here are the solutions:

### ✅ **Solution 1: Update requirements.txt (EASIEST)**

I've already fixed your `requirements.txt` with compatible versions. Just reinstall:

```bash
# 1. Remove old virtual environment
rmdir /s /q venv

# 2. Create fresh virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Upgrade pip
python -m pip install --upgrade pip setuptools wheel

# 4. Install fresh dependencies
pip install -r requirements.txt
```

### ✅ **Solution 2: Install Pre-built Wheels (FASTEST)**

If the above doesn't work, use pre-built binary wheels:

```bash
# 1. Activate virtual environment
venv\Scripts\activate

# 2. Install numpy first (pre-built)
pip install numpy==1.24.3

# 3. Install pandas (pre-built)
pip install pandas==2.0.3

# 4. Install other dependencies
pip install -r requirements.txt --skip-installed
```

### ✅ **Solution 3: Use Conda (MOST RELIABLE)**

If you have Anaconda/Miniconda installed:

```bash
# 1. Create conda environment
conda create -n pocket_option python=3.10

# 2. Activate environment
conda activate pocket_option

# 3. Install dependencies
conda install -c conda-forge python-telegram-bot=20.3
conda install -c conda-forge requests websocket-client
conda install -c conda-forge pandas numpy
conda install sqlalchemy pytest

# 4. Pip install remaining
pip install python-dotenv pyyaml pydantic
```

### ✅ **Solution 4: Downgrade Python (IF NEEDED)**

The issue might be with Python 3.14. Try with Python 3.10:

```bash
# 1. Check Python version
python --version

# 2. If Python 3.14, install Python 3.10 from python.org
# Download: https://www.python.org/downloads/

# 3. Create venv with Python 3.10
C:\Python310\python.exe -m venv venv
venv\Scripts\activate

# 4. Install requirements
pip install --upgrade pip
pip install -r requirements.txt
```

### ✅ **Solution 5: Minimal Installation (LIGHTWEIGHT)**

Start with essential packages only:

```bash
# 1. Create minimal requirements
pip install python-telegram-bot==20.3
pip install python-dotenv==1.0.0
pip install requests==2.31.0
pip install pyyaml==6.0.1

# 2. Test bot startup
python -m src.bot.main

# 3. Add other packages one by one if needed
pip install pandas==2.0.3
pip install numpy==1.24.3
```

---

## 🎯 Quick Fix - What Changed

### Previous requirements.txt had issues:
- ❌ `pandas==2.1.3` - Requires compilation on Windows
- ❌ `ta-lib==0.4.28` - Complex C++ dependencies
- ❌ `backtrader==1.9.78` - Optional but problematic

### Updated requirements.txt:
- ✅ `pandas==2.0.3` - Pre-built wheels available
- ✅ `numpy==1.24.3` - Stable and Windows-compatible
- ✅ Removed `ta-lib` - Not essential for core bot
- ✅ Removed `backtrader` - Moved to optional

---

## 📋 Troubleshooting Checklist

Before installation:
- ✅ Python 3.9-3.11 (NOT 3.14)
- ✅ pip is up to date: `python -m pip install --upgrade pip`
- ✅ Visual C++ Build Tools installed
- ✅ No spaces in file paths

If still having issues:
```bash
# Clear pip cache
pip cache purge

# Try installing with no cache
pip install --no-cache-dir -r requirements.txt

# Verbose output for debugging
pip install -vvv -r requirements.txt
```

---

## 🚀 Recommended Installation Steps for Windows

```bash
# Step 1: Use Python 3.10 or 3.11
python --version  # Should show 3.10.x or 3.11.x

# Step 2: Clean installation
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate

# Step 3: Upgrade tools
python -m pip install --upgrade pip setuptools wheel

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Test installation
python -c "import telegram; import requests; import dotenv; print('✅ All packages installed successfully!')"

# Step 6: Copy .env template
copy .env.example .env

# Step 7: Fill in your credentials in .env
# Then start bot:
python -m src.bot.main
```

---

## 🆘 If All Else Fails

### Use Docker (Eliminates All Environment Issues)

```bash
# 1. Install Docker Desktop from docker.com

# 2. Build and run
docker-compose up -d

# 3. Check status
docker-compose ps

# 4. View logs
docker-compose logs bot
```

This completely bypasses Windows dependency issues!

---

## ✅ After Fix: Verify Installation

```bash
# Test each major component
python -c "import telegram; print('✅ Telegram bot library OK')"
python -c "import requests; print('✅ Requests library OK')"
python -c "import dotenv; print('✅ Python-dotenv OK')"
python -c "import sqlalchemy; print('✅ SQLAlchemy OK')"
python -c "import pytest; print('✅ Pytest OK')"

# If all pass, you're ready to go!
python -m src.bot.main
```

---

## 📞 Need More Help?

1. **Check detailed error log:**
   ```bash
   pip install -r requirements.txt 2>&1 | tee install_log.txt
   ```

2. **Post in GitHub Issues with:**
   - Your Python version
   - Output of `pip --version`
   - The `install_log.txt` file

3. **Try Docker instead** - Most reliable for Windows

---

**Last Updated:** May 2026
**Status:** Fixed for Windows compatibility
