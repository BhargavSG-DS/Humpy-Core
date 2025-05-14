from fastapi import FastAPI
from app.core.database import connect, disconnect
from app.api.v1.endpoints import auth, users, products, orders, subscriptions, wallet, payments

# Initialize FastAPI app
app = FastAPI(
    title="D2C E-commerce API",
    description="API for daily milk subscriptions and organic farm goods",
    version="1.0.0"
)

# Startup event to connect to the database
@app.on_event("startup")
async def startup():
    """Connect to the database on application startup."""
    await connect()

# Shutdown event to disconnect from the database
@app.on_event("shutdown")
async def shutdown():
    """Disconnect from the database on application shutdown."""
    await disconnect()

# Include API routers with versioned prefix
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(orders.router, prefix="/api/v1/orders", tags=["orders"])
app.include_router(subscriptions.router, prefix="/api/v1/subscriptions", tags=["subscriptions"])
app.include_router(wallet.router, prefix="/api/v1/wallet", tags=["wallet"])
app.include_router(payments.router, prefix="/api/v1/payments", tags=["payments"])