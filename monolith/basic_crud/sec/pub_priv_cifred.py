from cryptography.hazmat.primitives.asymmetric import rsa
from typing import NamedTuple

import secrets
import time


class KeysPair(NamedTuple):
    private: str
    public: str


class KeyManager:
    def __init__(
        self,
        key_rotate_minutes: int = 60, # 1 hora
    ) -> None:
        self.__key_rotate_minutes: int = key_rotate_minutes
        self.__key_pairs: dict[str, KeysPair] = {}

        self._current_key = self._generate_key()

        self._generate_new_key_pair()


    def _generate_key(self) -> str:
        now: float = time.time()
        secret: str = secrets.token_hex(4)

        return f'key_{int(now)}_{secret}'


    def _generate_new_key_pair(self) -> None:
        private_key = rsa.generate_private_key()
        raise NotImplementedError('in construction')
