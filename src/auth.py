"""
Authentication and User Account Persistence for SURAKSHA AI.

Stores registered users in data/metadata/users.json with secure SHA-256 password hashes.
Supports registration, login validation, password verification, and session persistence.
"""
from __future__ import annotations

import hashlib
import json
import logging
from datetime import datetime
from pathlib import Path

from src import config

logger = logging.getLogger(__name__)

USERS_FILE = config.METADATA_DIR / "users.json"


def _hash_password(password: str) -> str:
    """Hashes password with SHA-256."""
    return hashlib.sha256(password.strip().encode("utf-8")).hexdigest()


def _ensure_users_file():
    """Initializes users.json with seed accounts if it doesn't exist."""
    if not USERS_FILE.exists():
        default_users = {
            "varshini@gmail.com": {
                "name": "Varshini",
                "role": "Citizen / Traveler",
                "user_id": "varshini@gmail.com",
                "password_hash": _hash_password("password123"),
                "created_at": datetime.now().isoformat()
            },
            "admin@suraksha.gov.in": {
                "name": "System Admin",
                "role": "Law Enforcement / Official",
                "user_id": "admin@suraksha.gov.in",
                "password_hash": _hash_password("admin123"),
                "created_at": datetime.now().isoformat()
            }
        }
        try:
            with open(USERS_FILE, "w", encoding="utf-8") as f:
                json.dump(default_users, f, indent=2)
            logger.info("Initialized default users in users.json")
        except Exception as e:
            logger.error(f"Failed to create users.json: {e}")


def load_users() -> dict:
    """Loads all registered users from users.json."""
    _ensure_users_file()
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load users.json: {e}")
        return {}


def register_user(full_name: str, role: str, user_id: str, password: str) -> tuple[bool, str]:
    """Registers a new user and saves to users.json."""
    name_clean = full_name.strip()
    id_clean = user_id.strip().lower()
    pass_clean = password.strip()

    if not name_clean:
        return False, "❌ Full Name is required."
    if not id_clean:
        return False, "❌ Mobile or Email is required."
    if len(pass_clean) < 4:
        return False, "❌ Password must be at least 4 characters long."

    users = load_users()

    if id_clean in users:
        return False, "⚠️ An account with this Email or Mobile already exists. Please switch to the 'Login' tab."

    users[id_clean] = {
        "name": name_clean,
        "role": role,
        "user_id": id_clean,
        "password_hash": _hash_password(pass_clean),
        "created_at": datetime.now().isoformat()
    }

    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2)
        logger.info(f"Registered new user: {id_clean}")
        return True, f"🎉 Account created successfully! Welcome, {name_clean}."
    except Exception as e:
        logger.error(f"Failed to save user to users.json: {e}")
        return False, f"❌ Failed to save user account: {e}"


def authenticate_user(user_id: str, password: str) -> tuple[bool, dict | str]:
    """Validates user credentials against stored accounts."""
    id_clean = user_id.strip().lower()
    pass_clean = password.strip()

    if not id_clean:
        return False, "❌ Please enter your Email or Mobile Number."
    if not pass_clean:
        return False, "❌ Please enter your password."

    users = load_users()

    if id_clean not in users:
        return False, "❌ Account not found. Please click 'Create Account' to register."

    user_data = users[id_clean]
    if user_data.get("password_hash") == _hash_password(pass_clean):
        return True, user_data
    else:
        return False, "❌ Incorrect password. Please check your password and try again."
