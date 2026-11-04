# Importando bibliotecas para criptgrafia de senhas
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError

# Instanciando o PasswordHasher do Argon2
ph = PasswordHasher()

# Criptografar a senha
def hash_password(password: str) -> str:
    return ph.hash(password)

# Verificar se as senhas conferem
def verify_password(password_hash: str, password: str) -> bool:
    try:
        return ph.verify(password_hash, password)
    except (VerifyMismatchError, VerificationError):
        return False