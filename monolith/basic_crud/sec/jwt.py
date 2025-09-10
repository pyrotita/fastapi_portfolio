from uuid import uuid4

import datetime
import jwt
import os


# <·
SECRET_KEY: str = os.getenv('SECRET_KEY', str(uuid4()))
ALGORITHM_JWT: str = 'HS256'


class JwtHandler:
    def __init__(
        self,
        algorithm: str = ALGORITHM_JWT,
        expire_time_minutes: int = 15,
        secret: str = SECRET_KEY,
    ) -> None:
        self.__expire_time_minutes: int = expire_time_minutes
        self.__algorithm: str = algorithm
        self.__secret: str = secret


    def gen_payload(self, iden_ref: str) -> dict:
        now = datetime.datetime.utcnow()
        expire = datetime.timedelta(
            minutes=self.__expire_time_minutes,
        )

        return {
            'iden': iden_ref,
            'exp': expire,
            'iat': now,
        }


    def create_jwt(self, payload: dict) -> str:
        return jwt.encode(
            algorithm=self.__algorithm,
            key=self.__secret,
            payload=payload,
        )


    def read_jwt(self, token: str):
        try:
            decode_payload = jwt.decode(
                algorithms=[self.__algorithm],
                key=self.__secret,
                jwt=token,
            )

            return decode_payload

        except jwt.ExpiredSignatureError as e:
            print(e)

        except jwt.InvalidTokenError as e:
            print(e)

        except Exception as e:
            print(e)
