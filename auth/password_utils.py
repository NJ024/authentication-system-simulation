import hashlib


def hash_password(password):
    """Returns SHA-256 hashed version of a password."""
    return hashlib.sha256(password.encode()).hexdigest()


def check_password_strength(password):
    """Evaluates password strength based on length and character mix."""
    if len(password) < 4:
        return "Weak"
    elif any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
        return "Strong"
    return "Moderate"
