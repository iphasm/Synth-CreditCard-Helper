# Railway Deployment Guide

## 1. Project Setup
1.  Log in to [Railway](https://railway.app/).
2.  Click **"New Project"**.
3.  Select **"Deploy from GitHub repo"** and choose `TC-HELPER`.

## 2. Add Database (PostgreSQL)
1.  In your project view, click **"New"** (or right-click).
2.  Select **"Database"** -> **"PostgreSQL"**.
3.  This will automatically create a `DATABASE_URL` variable.

## 3. Environment Variables
Go to your **TC-HELPER Service** -> **Settings** -> **Variables** and add:

| Variable | Value / Description |
| :--- | :--- |
| `PORT` | `8000` (Railway usually sets this, but good to ensure) |
| `DATABASE_URL` | *Reference the Postgres variable* (Type `${{` and select Postgres URL) |
| `GOOGLE_CLIENT_ID` | From Google Cloud Console |
| `GOOGLE_CLIENT_SECRET` | From Google Cloud Console |
| `GOOGLE_REDIRECT_URI` | `https://<YOUR-RAILWAY-URL>.up.railway.app/api/auth/callback` |
| `GOOGLE_CREDENTIALS_JSON` | Parsing the content of `credentials.json` directly. See below. |

### How to get `GOOGLE_CREDENTIALS_JSON`
1.  Download the `credentials.json` file from Google Cloud (Desktop or Web Client).
2.  Open the file in a text editor.
3.  Copy the **entire content** (starts with `{` and ends with `}`).
4.  Paste it as the value for the `GOOGLE_CREDENTIALS_JSON` variable in Railway.

## 4. Google Cloud Console Setup
1.  Go to **APIs & Services** -> **Credentials**.
2.  Add your Railway URL to **Authorized Redirect URIs**:
    -   `https://<YOUR-RAILWAY-URL>.up.railway.app/api/auth/callback`
3.  Enable the **Gmail API**.
