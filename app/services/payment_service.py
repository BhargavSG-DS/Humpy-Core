import razorpay
from app.core.config import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

async def create_payment_order(amount: int, currency: str = "INR") -> dict:
    """Create a payment order with Razorpay.

    Args:
        amount (int): Amount in smallest currency unit (e.g., paise for INR).
        currency (str): Currency code (default: INR).

    Returns:
        dict: Razorpay order details.
    """
    data = {
        "amount": amount,
        "currency": currency,
        "receipt": f"order_{int(amount)}_{int(datetime.now().timestamp())}"
    }
    return client.order.create(data=data)