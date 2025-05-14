from app.core.database import database

async def add_funds(user_id: int, amount: float) -> None:
    """Add funds to a user's wallet with transaction logging.

    Args:
        user_id (int): ID of the user.
        amount (float): Amount to add.

    Raises:
        Exception: If database operation fails (handled by caller).
    """
    async with database.transaction():
        # Update wallet balance
        query = """
            UPDATE wallets
            SET balance = balance + :amount
            WHERE user_id = :user_id
        """
        await database.execute(query=query, values={"amount": amount, "user_id": user_id})
        # Log transaction
        query = """
            INSERT INTO wallet_transactions (user_id, amount, type)
            VALUES (:user_id, :amount, 'credit')
        """
        await database.execute(query=query, values={"user_id": user_id, "amount": amount})