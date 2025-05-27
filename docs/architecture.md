# Architecture

1. **core.py**  
   - Initializes Telegram Application  
   - Loads Config  
   - Registers Handlers

2. **handlers/**  
   - Each handler class encapsulates one feature  
   - `register()` binds commands/callbacks

3. **models/**  
   - `NLPModel` wraps GPT  
   - `Storage` interface with SQLite/Redis adapters

4. **keyboards.py**  
   - Factories for InlineKeyboardMarkup

_Data flows_  
User → Telegram API → Handler → Model/Storage → Handler → User
