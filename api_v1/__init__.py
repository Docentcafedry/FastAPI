__all__ = ("user_router", "product_router")


from api_v1.users.views import router as user_router
from api_v1.products.views import router as product_router
