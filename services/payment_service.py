import razorpay
from config import Config

client = razorpay.Client(
    auth=(
        Config.RAZORPAY_KEY_ID,
        Config.RAZORPAY_KEY_SECRET
    )
)


def create_payment(amount):

    payment = client.order.create({
        "amount": amount * 100,   # Razorpay expects amount in paise
        "currency": "INR",
        "payment_capture": 1
    })

    return payment