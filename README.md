# Klaviyo Proxy API (Flask)

This is a lightweight Flask app that securely connects to the Klaviyo API using your private API key. It exposes simple endpoints like `/metrics` so you can use this proxy to retrieve data for analysis.

## Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/your-username/klaviyo_proxy_api.git
cd klaviyo_proxy_api
```

### 2. Add your Klaviyo API Key

Create a `.env` file:

```bash
echo "KLAVIYO_API_KEY=your_private_klaviyo_key" > .env
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python app.py
```

### 5. Deploy

Deploy this to a service like [Render](https://render.com), [Railway](https://railway.app), or [Fly.io](https://fly.io) with your `.env` added securely.

