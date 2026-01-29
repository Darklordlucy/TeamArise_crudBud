# AI Credit Decisioning System - Backend

FastAPI backend for AI-powered credit decisioning with ML-based loan approval predictions.

## Features

- 🤖 **ML Credit Scoring**: KNN classifier for loan approval prediction
- 📊 **Transaction Analysis**: CSV/Excel upload with spending categorization
- 🔐 **JWT Authentication**: Secure user authentication with Supabase
- 🏦 **Bank Integration**: Partner bank statistics and recommendations
- 📈 **Financial Behavior Scoring**: 8-category spending analysis
- 🚀 **FastAPI**: Modern, fast, async API framework

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Update `.env` with your Supabase credentials:
```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_service_key
SUPABASE_ANON_KEY=your_anon_key
```

### 3. Train ML Model
```bash
python scripts/train_model.py
```

### 4. Run Server
```bash
# Development (with auto-reload)
uvicorn app.main:app --reload

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## API Documentation

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/verify` - Verify JWT token

### Loans
- `POST /api/loans/apply` - Submit loan application
- `GET /api/loans/user/{user_id}` - Get user's loans
- `GET /api/loans/{loan_id}` - Get loan details

### Transactions
- `POST /api/transactions/upload` - Upload bank statement
- `GET /api/transactions/analyze/{user_id}` - Get financial behavior

### Banks
- `GET /api/banks/` - Get all banks
- `GET /api/banks/top` - Get top banks
- `GET /api/banks/trusted` - Get trusted banks

### User
- `GET /api/user/me` - Get current user info
- `GET /api/user/financial-behavior/{user_id}` - Get financial behavior

## Example Usage

### Register User
```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepass123",
    "full_name": "John Doe",
    "phone": "9876543210",
    "city_tier": "tier_1"
  }'
```

### Apply for Loan
```bash
curl -X POST http://localhost:8000/api/loans/apply \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "amount_requested": 100000,
    "num_debts": 2,
    "total_debt_amount": 50000,
    "monthly_emis": 5000,
    "total_assets": 200000,
    "monthly_income": 50000,
    "city_tier": "tier_1"
  }'
```

## Testing

```bash
# Run tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=app --cov-report=html
```

## Project Structure

```
credit-decision-backend/
├── app/
│   ├── config/          # Settings & database
│   ├── models/          # Pydantic models
│   ├── routes/          # API endpoints
│   ├── services/        # Business logic
│   ├── db/repositories/ # Database operations
│   ├── ml/              # ML model
│   ├── utils/           # Utilities
│   ├── middleware/      # Auth & error handling
│   └── main.py          # App entry point
├── data/                # Training data
├── scripts/             # Utility scripts
└── tests/               # Tests
```

## Database Schema

See [walkthrough.md](./walkthrough.md) for detailed database schema.

## License

MIT
