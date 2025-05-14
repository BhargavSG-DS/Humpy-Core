# Humpy Farms Core System

Humpy Farms Core System is a modular backend platform designed to manage core business operations for Humpy Farms, including user management, products, orders, payments, subscriptions, and more. The system is built with scalability and maintainability in mind, leveraging modern Python frameworks and best practices.

## Features

- **User Management:** Registration, authentication, roles, and permissions.
- **Product Catalog:** CRUD operations for products and inventory.
- **Order Processing:** Order creation, tracking, and management.
- **Payments:** Secure payment processing and wallet management.
- **Subscriptions:** Recurring subscription handling.
- **Pro-Membership:** Humpy Pro Membership handling. 
- **Customer Management:** Customer profiles and history.
- **API Versioning:** Organized API endpoints for future scalability.

## Project Structure

```
app/
  main.py                # Application entry point
  api/                   # API versioning and endpoints
    v1/
      endpoints/         # RESTful endpoints (auth, customers, orders, etc.)
core/
  config.py              # Configuration and environment settings
  database.py            # Database connection and ORM setup
  security.py            # Security utilities (auth, JWT, etc.)
  utils.py               # Utility functions
models/                  # SQLAlchemy models for all entities
schemas/                 # Pydantic schemas for request/response validation
services/                # Business logic and service layer
tests/                   # Unit and integration tests
requirements.txt         # Python dependencies
migrations/              # Database migration scripts
```

## Getting Started

### Prerequisites

- Python 3.9+
- pip (Python package manager)
- (Optional) Virtual environment tool (venv, virtualenv, etc.)

### Installation

1. **Clone the repository:**
   ```powershell
   git clone https://github.com/yourusername/humpy-core.git
   cd humpy-core
   ```

2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy `.env.example` to `.env` and update values as needed.

5. **Run database migrations:**
   ```powershell
   # Example using Alembic (if configured)
   alembic upgrade head
   ```

6. **Start the application:**
   ```powershell
   uvicorn app.main:app --reload
   ```

### Running Tests

```powershell
pytest
```

## API Documentation

Once the server is running, access the interactive API docs at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License.
