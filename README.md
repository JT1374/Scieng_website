# SciEng Website

This is a Django-based web application it has

---

## Local Development Setup (venv)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd 06-031-Capstone-Project-Consolidation
   ```

2. **Create and activate a virtual environment**
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python scieng_website/manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python scieng_website/manage.py runserver
   ```

6. **Access the app**
   Open your browser and go to [http://localhost:8000](http://localhost:8000)

---

## Notes

- **Do not commit secrets** (such as passwords or API keys) to public repositories.
- If your project requires secrets, create a `.env` file or use environment variables. Document how to set these up here if needed.
- For production, set `DEBUG = False` and update `ALLOWED_HOSTS` in `scieng_website/scieng_website/settings.py`.

---

## Documentation

- Project documentation can be found in the `docs/` directory.
- It was made using sphinx.