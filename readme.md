# Fake Bean Utilities Installation

These stubs let you test the Beancount import utility without installing Beancount or maintaining a real ledger. You’ll create lightweight “wrappers” named `bean-identify` and `bean-extract`, place them in a folder on your `PATH`, and point your import tool at that directory.

---

## 1. Create a stubs folder

Choose or create a folder to hold your wrappers. For example:

- **Windows**: `%USERPROFILE%\bean-stubs`  
- **macOS/Linux**: `~/bean-stubs`

---

## 2. Add the Python stub scripts

Copy the provided stub scripts into that folder as:

- `fake_bean_identify.py`  
- `fake_bean_extract.py`

*(See the stub contents in this repo.)*

---

## 3. Create executable wrappers

### Windows (PowerShell / CMD)

In `%USERPROFILE%\bean-stubs`, create:

**bean-identify.cmd**
```cmd
@echo off
py "%~dp0fake_bean_identify.py" %*
```

**bean-extract.cmd**
```cmd
@echo off
py "%~dp0fake_bean_extract.py" %*
```

### macOS / Linux (Bash)

In `~/bean-stubs`, create:

**bean-identify**
```bash
#!/usr/bin/env bash
python3 "$HOME/bean-stubs/fake_bean_identify.py" "$@"
```

**bean-extract**
```bash
#!/usr/bin/env bash
python3 "$HOME/bean-stubs/fake_bean_extract.py" "$@"
```

Then make them executable:
```bash
chmod +x ~/bean-stubs/bean-identify ~/bean-stubs/bean-extract
```

---

## 4. Add the folder to your PATH

### Windows

Open PowerShell and run:
```powershell
[Environment]::SetEnvironmentVariable(
  "Path",
  "$env:Path;%USERPROFILE%\bean-stubs",
  "User"
)
```
Then close and reopen your terminal.

### macOS / Linux

Append to your shell profile (`~/.bash_profile`, `~/.zshrc`, etc.):
```bash
export PATH="$HOME/bean-stubs:$PATH"
```
Reload your profile:
```bash
source ~/.bash_profile    # or ~/.zshrc, etc.
```

---

## 5. Verify

```bash
bean-identify --help
bean-extract --help
```

You should see usage messages from the stubs. Your import utility will now call these fake tools for testing without a real Beancount install.
