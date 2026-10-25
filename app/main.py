import logging
import os
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger("checkout-api")

app = FastAPI(
    title="Enterprise Checkout API",
    description="A portfolio demo for cloud architecture validation.",
    version="1.0.0",
)


class CartItem(BaseModel):
    sku: str = Field(min_length=1, max_length=50)
    quantity: int = Field(gt=0, le=100)


class CheckoutRequest(BaseModel):
    items: list[CartItem]
    simulate_failure: bool = False


@app.get("/")
def root():
    return {
        "service": "checkout-api",
        "version": app.version,
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "checkout-api",
        "environment": os.getenv("APP_ENVIRONMENT", "local"),
    }


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.post("/checkout")
def checkout(request: CheckoutRequest):
    if not request.items:
        raise HTTPException(
            status_code=400,
            detail="At least one cart item is required.",
        )

    if request.simulate_failure:
        logger.warning("Simulated checkout dependency failure")
        raise HTTPException(
            status_code=503,
            detail="Simulated temporary checkout dependency failure.",
        )

    order_id = f"demo-{uuid4().hex[:12]}"

    logger.info(
        "Checkout simulation accepted order_id=%s item_count=%s",
        order_id,
        len(request.items),
    )

    return {
        "status": "accepted",
        "mode": "simulation",
        "order_id": order_id,
        "item_count": len(request.items),
        "message": "Demo only; no payment or persistent order was created.",
    }
