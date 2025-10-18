# Dynamic Profile API (Stage 0)

This project is a simple RESTful API built with Django as part of the HNG Backend Stage 0 task. It exposes a single `GET` endpoint that returns a static user profile, the current UTC timestamp, and a random cat fact fetched live from an external API.

The API is rate-limited to protect against abuse and is deployed on Railway.

**Live Endpoint:** [**https://web-production-9f847.up.railway.app/me**](https://web-production-9f847.up.railway.app/me)

---

## Features

* **`GET /me` Endpoint:** Returns a JSON object with profile data.
* **Dynamic Data:** Integrates with the [Cat Fact API](https://catfact.ninja/fact) to fetch a new fact on every request.
* **Dynamic Timestamp:** Returns the current server time in UTC ISO 8601 format.
* **Rate Limiting:** Implements IP-based rate limiting (`10 requests/minute`) using `django-ratelimit` to protect the endpoint.
* **Production Ready:** Configured for production deployment using `gunicorn` and environment variables.

### Example Response

```json
{
  "status": "success",
  "user": {
    "email": "your-email@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T20:45:01.123456+00:00",
  "fact": "A cat can jump up to five times its own height in a single bound."
}
```

-----

## Technologies Used

  * **Backend:** [Python](https://www.python.org/) / [Django](https://www.djangoproject.com/)
  * **External API:** [requests](https://pypi.org/project/requests/)
  * **Rate Limiting:** [django-ratelimit](https://pypi.org/project/django-ratelimit/)
  * **Environment Variables:** [python-decouple](https://pypi.org/project/python-decouple/)
  * **WSGI Server:** [gunicorn](https://gunicorn.org/)
  * **Database (for rate-limiting):** [PostgreSQL](https://www.postgresql.org/) (via `dj-database-url` and `psycopg2-binary`)

-----

## Instructions to Run Locally

### 1. Prerequisites

  * Python 3.12.1
  * Git

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/dynamic_profile_project.git
cd dynamic_profile_project
```

### 3. Set Up a Virtual Environment

It is highly recommended to use a virtual environment.

```bash
# Create the environment
python -m venv venv

# Activate it
# On Windows:
.env\Scriptsctivate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies

Install all required packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the root of the project (`dynamic_profile_project/` folder, next to `manage.py`). This file is used for local configuration.

```env
# --- .env file ---

# Set to True for local development
DEBUG=True

# A random string for Django's security
SECRET_KEY=local-secret-key-for-testing

# Your local hosts
ALLOWED_HOSTS=127.0.0.1,localhost

# Your personal info
USER_EMAIL=your-email@example.com
USER_NAME=Your Full Name
USER_STACK= Your preferred backend stack

# Cat Fact API Url
CAT_FACT_API_URL=https://catfact.ninja/fact
```

### 6. Run Migrations

This will create the local `db.sqlite3` file and set up the necessary tables for Django and the rate-limiting package.

```bash
python manage.py migrate
```

### 7. Run the Server

Run the local development server.

```bash
python manage.py runserver
```

The API will be available at **http://127.0.0.1:8000/me/**.

-----

## Environment Variables Needed

These variables are required for the application to run, especially in a production environment like Railway.

| Variable | Description | Example |
| :--- | :--- | :--- |
| `SECRET_KEY` | A strong, unique secret key for Django. | `django-insecure-a_b_c123...` |
| `DEBUG` | Set to `False` in production. | `False` |
| `ALLOWED_HOSTS` | Comma-separated list of domains that can serve the site. | `web-production-9f847.up.railway.app,localhost` |
| `USER_EMAIL` | Your email to be displayed in the API response. | `my-email@gmail.com` |
| `USER_NAME` | Your full name for the API response. | `Ayoigbala Soares` |
| `USER_STACK` | Your backend stack for the API response. | `Python/Django` |
| `CAT_FACT_API_URL` | The cat fact api url | `https://catfact.ninja/fact` |
