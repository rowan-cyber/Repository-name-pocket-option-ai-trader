# Pocket Option Telegram Bot - Assign Python Version to Project

## 🎯 **Quick Setup with Existing Python Versions**

Since you have all Python versions installed, here's how to assign Python 3.10 or 3.11 to your project:

---

## **Windows Command Prompt / PowerShell**

### Step 1: Find Your Python Installation Paths
```bash
# Open Command Prompt and run:
where python
# Lists all Python installations

# Or check each version:
where python3.10
where python3.11
where python3.12
```

You'll see paths like:
- `C:\Python310\python.exe`
- `C:\Python311\python.exe`
- `C:\Python314\python.exe`

### Step 2: Use Python 3.10 or 3.11 for Your Project

```bash
# Navigate to project
cd C:\Users\u\Repository-name-pocket-option-ai-trader

# DELETE old virtual environment
rmdir /s /q venv

# CREATE virtual environment with Python 3.10
C:\Python310\python.exe -m venv venv

# ACTIVATE virtual environment
venv\Scripts\activate

# Verify correct Python is active
python --version
# Should show: Python 3.10.x
```

### Step 3: Install Dependencies
```bash
# Upgrade pip first
python -m pip install --upgrade pip setuptools wheel

# Install requirements
pip install -r requirements.txt

# Verify installation
python -c "import telegram; print('✅ Ready!')"
```

### Step 4: Start the Bot
```bash
# Make sure venv is activated
venv\Scripts\activate

# Copy .env template if not done
copy .env.example .env

# Fill in your credentials in .env:
# TELEGRAM_BOT_TOKEN=your_token
# POCKET_OPTION_EMAIL=your_email
# POCKET_OPTION_PASSWORD=your_password

# Run the bot
python -m src.bot.main
```

---

## **VSCode Setup (Recommended)**

### Step 1: Select Python Interpreter in VSCode
```
1. Open VSCode in your project folder
2. Press Ctrl + Shift + P
3. Type: "Python: Select Interpreter"
4. Choose: ".\venv\Scripts\python.exe"
5. Or manually add from: C:\Python310\python.exe
```

### Step 2: Configure VSCode Settings
Create `.vscode\settings.json`:
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": true
    }
}
```

### Step 3: Create Launch Configuration
Create `.vscode\launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Pocket Option Bot",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/src/bot/main.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}
```

### Step 4: Run from VSCode
- Press F5 to start bot
- Logs appear in integrated terminal

---

## **PyCharm Setup (Alternative)**

### Step 1: Open Project
1. File → Open → Select your project folder

### Step 2: Configure Interpreter
1. File → Settings → Project → Python Interpreter
2. Click gear icon → Add
3. Select "Existing Environment"
4. Browse to: `C:\Python310\python.exe`
5. Click OK

### Step 3: Create Run Configuration
1. Run → Edit Configurations
2. Click + → Python
3. Set:
   - Script path: `src/bot/main.py`
   - Working directory: Your project folder
   - Python interpreter: The one you just added
4. Click OK

### Step 4: Run
- Press Shift+F10 to start bot

---

## **Command Line - Full Setup from Scratch**

Copy and paste this entire block into Command Prompt:

```bash
cd C:\Users\u\Repository-name-pocket-option-ai-trader
rmdir /s /q venv 2>nul
C:\Python310\python.exe -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
echo Installation complete! Now fill in .env and run: python -m src.bot.main
```

---

## **Verify Correct Python is Active**

```bash
# Check which Python you're using
venv\Scripts\activate
python --version
# MUST show: Python 3.10.x or 3.11.x (NOT 3.14)

# Check pip is from correct Python
pip --version
# Should show path to venv\Scripts\python.exe
```

---

## **If You Accidentally Used Python 3.14**

```bash
# Check
python --version
# If shows Python 3.14.x, DELETE and recreate:

deactivate
rmdir /s /q venv

# Use Python 3.10 explicitly
C:\Python310\python.exe -m venv venv
venv\Scripts\activate
python --version
# Now should show Python 3.10.x ✅
```

---

## **Setting Default Python Version (Optional)**

If you want Python 3.10 as default system-wide:

### Windows Registry Method:
```
1. Win + R
2. Type: regedit
3. Navigate: HKEY_LOCAL_MACHINE\SOFTWARE\Python\PythonCore\3.10\InstallPath
4. Copy the path
5. Add to Windows PATH environment variable
```

Or use Windows Settings:
```
1. Settings → System → About → Advanced system settings
2. Environment Variables → Path
3. Move C:\Python310 to top of the list
```

---

## **Quick Reference: All Python Versions**

```bash
# List installed versions
dir C:\Python*

# Use specific version
C:\Python39\python.exe -m venv venv   # Python 3.9
C:\Python310\python.exe -m venv venv  # Python 3.10 ✅ RECOMMENDED
C:\Python311\python.exe -m venv venv  # Python 3.11 ✅ RECOMMENDED
C:\Python312\python.exe -m venv venv  # Python 3.12
C:\Python313\python.exe -m venv venv  # Python 3.13
C:\Python314\python.exe -m venv venv  # Python 3.14 ❌ PROBLEMATIC
```

---

## **🚀 Fastest Way to Get Running**

1. **Open Command Prompt**
2. **Copy and paste:**
```bash
cd C:\Users\u\Repository-name-pocket-option-ai-trader && rmdir /s /q venv 2>nul & C:\Python310\python.exe -m venv venv & venv\Scripts\activate & python -m pip install --upgrade pip & pip install -r requirements.txt & echo ✅ READY! Now edit .env and run: python -m src.bot.main
```
3. **Fill in `.env` with your credentials**
4. **Run:** `python -m src.bot.main`

---

## **Troubleshooting**

### "python command not found"
```bash
# Use full path
C:\Python310\python.exe --version
```

### "pip install fails"
```bash
# Make sure venv is activated
venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Try again
pip install -r requirements.txt
```

### "Wrong Python version still active"
```bash
# Deactivate and recreate
deactivate
rmdir /s /q venv
C:\Python310\python.exe -m venv venv
venv\Scripts\activate
```

---

**Last Updated:** May 2026
**Recommended Version:** Python 3.10 or 3.11
**Status:** Ready to use!
