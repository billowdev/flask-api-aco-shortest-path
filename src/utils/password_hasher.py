import argon2
from src.config.common_config import SECRET_KEY

def password_hasher(password):
	hasher = argon2.PasswordHasher(
		time_cost=16,
		memory_cost=2**14,
		parallelism=4,
		hash_len=32,
		salt_len=16,
		encoding='utf-8',
		type=argon2.Type.ID,
	)
	hash = hasher.hash(password)
	return hash


def verify_password(hash, password):
	hasher = argon2.PasswordHasher()
	try:
		hasher.verify(hash, password)
		return True
	except argon2.exceptions.VerifyMismatchError:
		return False