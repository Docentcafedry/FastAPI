from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get_users(): ...


@router.get("/{user_id}")
def get_user(user_id: int): ...


@router.patch("/{user_id}")
def update_product(user_id: int): ...


@router.delete("/{user_id}")
def delete_product(user_id: int): ...
