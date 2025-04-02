# Python Backend Setup

1. Create and activate a virtual environment:
   - Windows (PowerShell):
     ```
     python -m venv .venv
     .venv\Scripts\Activate
     ```

2. Install dependencies:
`pip install -r requirements.txt`

RUN `pip freeze > requirements.txt ` to update after each `pip install`

3. Run the FastAPI server (if applicable):
`uvicorn main:app --reload`
