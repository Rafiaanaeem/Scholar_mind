```markdown
# ScholarMind

**ScholarMind** is an enterprise-ready, AI-powered academic research assistant designed to streamline topic discovery, generate structured literature review foundations, and manage research artifacts. Built with a modular Python architecture, it leverages high-speed inference via the Groq API (Llama 3), secure native authentication, local SQLite persistence, and dynamic document generation (PDF/DOCX).

---

## 🌟 Key Features

* **💡 AI Topic Discovery:** Instant generation of 5 trending academic research topics based on any field of study, powered by Groq LPUs.
* **📄 Research Package Generation:** Produces structured research foundations containing Executive Summaries, Research Questions, Literature Review Focus areas, Methodologies, and Future Directions.
* **🔐 Secure Authentication & RBAC:** Native user registration and login utilizing `bcrypt` password hashing with Role-Based Access Control (`Admin` vs. `User`).
* **📥 Multi-Format Export:** In-memory generation and download of research documents in both PDF (`reportlab`) and Word (`python-docx`) formats.
* **📜 Local History Tracking:** SQLite-backed persistence storing user query logs and research documents, with automatic UTC-to-Local timezone conversions for accurate timestamping.
* **👑 Admin Dashboard:** Administrative view for system auditing and account creation monitoring.

---

## 🛠️ Tech Stack

| Component | Technology / Library | Purpose |
| :--- | :--- | :--- |
| **Frontend UI** | Streamlit | Reactive web application interface |
| **AI LLM Engine** | Groq API (`llama3-8b-8192`) | Rapid research text and topic generation |
| **Security** | `bcrypt` | Native password hashing & verification |
| **Database** | SQLite3 | Local persistent storage for users & history |
| **Document Export** | `reportlab`, `python-docx` | PDF and DOCX file creation |
| **Environment** | `python-dotenv` | Secure API key and secret management |

---

## 📂 Project Structure

```text
scholarmind/
│
├── config/
│   └── settings.py
├── database/
│   └── db_manager.py
├── services/
│   ├── ai_service.py
│   ├── auth_service.py
│   └── export_service.py
├── ui/
│   ├── admin_page.py
│   ├── auth_page.py
│   ├── components.py
│   └── research_page.py
├── utils/
│   ├── logger.py
│   └── time_utils.py
├── .env
├── .gitignore
├── app.py
├── requirements.txt
└── README.md

```

---

## 🚀 Quick Start & Installation

### Prerequisites

* Python 3.10 or higher
* A free [Groq Cloud API Key](https://console.groq.com/)

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/ScholarMind.git](https://github.com/your-username/ScholarMind.git)
cd ScholarMind

```

### 2. Set Up a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure Environment Variables

Create a `.env` file in the root directory by copying `.env.example`:

```bash
cp .env.example .env

```

Open `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
GROQ_MODEL=llama3-8b-8192

```

### 5. Launch the Application

```bash
streamlit run app.py

```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🔄 How It Works

```text
Field of Study
      ↓
AI Topic Discovery
      ↓
Select Research Topic
      ↓
Generate Research Package
      ↓
Save to Research History
      ↓
Export as PDF / DOCX / Markdown

```

---

## 🧪 Usage & Testing Guide

1. **Create Account:** Navigate to the **Register** tab and create a new account.
2. **Admin Setup:** To grant an account `Admin` privileges, directly modify the `role` column in `database/scholarmind.db` or initialize an admin user via `db_manager.py`.
3. **Discover Topics:** Enter a field of study (e.g., *Quantum Machine Learning*) in the **Research Workspace** and click **Discover Topics**.
4. **Generate Package:** Select a topic and click **Generate Research Package** to output the full document.
5. **Export & Review:** Download the generated output as PDF/DOCX or visit **Research History** to view saved logs stamped in your local timezone.

---

## 🔒 Security Best Practices

* **Secrets Isolation:** All API keys and session identifiers are stored in `.env` and excluded from version control via `.gitignore`.
* **Password Hashing:** Passwords are salted and hashed using `bcrypt` prior to database insertion. Raw passwords are never stored.
* **SQL Injection Prevention:** All database operations utilize parameterized queries (`?` placeholders).

---

## 👩‍💻 Author

**Rafia Naeem**

*Bachelor of Computer Science*

```

```