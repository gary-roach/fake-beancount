You are a highly proficient Python engineer and TUI developer. Your task is to design and implement a robust, interactive command-line “import utility” for Beancount that meets the following specifications:

1. **Environment & Dependencies**  
   - Language: Python 3.13  
   - TUI framework: Textual
   - Data handling: beancount.core.data + beancount.parser.printer for formatting; JSON for session persistence  

2. **Overall Workflow**  
   a. **Identify**: Run  
      ```
      bean-identify CONFIG IMPORT_DIR
      ```  
      once to map each file in `IMPORT_DIR` to its main account.  
   b. **Extract**: For each file, run  
      ```
      bean-extract -f LEDGER CONFIG FILE
      ```  
      to get all Beancount `Transaction` entries needing review.  
   c. **Review & Edit**: Present one transaction at a time in a Textual UI. Allow navigation with ←/→ keys. Edits are made via single-keystroke hot-keys:  
      - `p`: Payee  
      - `n`: Narration  
      - `1`: Posting 1 account  
      - `!`: Posting 1 amount  
      - `2`: Posting 2 account  
      - `@`: Posting 2 amount  
      Each hot-key opens a small modal (`ModalScreen` + `Input`). When the user presses Enter, a callback updates the in-memory transaction and immediately re-renders the view.  

3. **Session Persistence**  
   - Store the list of transactions and current index in a JSON side-car (`.import-session.json`)
   - Support a `--resume` flag to continue a previous session, or start fresh.  

4. **Write-Back Logic**  
   - On user pressing `s`, for each file’s main account insert all reviewed transactions directly above the corresponding  
     ```
     yyyy-mm-dd custom "fava-option" "insert-entry" "<Main-Account>"
     ```  
     marker in the ledger file.  
   - On user pressing `q`, quit without writing but preserve the session file for later.  

Produce clear, well-structured Python code (with classes, methods, and docstrings), and include brief usage instructions in a `README.md`. Ensure the utility is user-friendly, robust to errors, and easy to extend.```
