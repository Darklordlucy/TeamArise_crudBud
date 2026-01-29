from app.utils.security import hash_password, verify_password, create_access_token
from app.db.repositories.user_repository import user_repository
from fastapi import HTTPException, status
from typing import Dict

class AuthService:
    async def register_user(self, user_data: Dict) -> Dict:
        """Register a new user"""
        # Check if user exists
        existing_user = await user_repository.get_user_by_email(user_data['email'])
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Hash password
        hashed_password = hash_password(user_data.pop('password'))
        user_data['password_hash'] = hashed_password
        
        # Create user
        user = await user_repository.create_user(user_data)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create user"
            )
        
        # Generate token
        access_token = create_access_token(data={"sub": user['email'], "user_id": user['id']})
        
        # Remove password hash from response
        user.pop('password_hash', None)
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": user
        }
    
    async def login_user(self, email: str, password: str) -> Dict:
        """Login user"""
        # Get user
        user = await user_repository.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Verify password
        if not verify_password(password, user['password_hash']):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Generate token
        access_token = create_access_token(data={"sub": user['email'], "user_id": user['id']})
        
        # Remove password hash
        user.pop('password_hash', None)
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": user
        }

auth_service = AuthService()
