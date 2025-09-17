from typing import (
    NamedTuple,
    Generic,
    TypeVar,
    Any
)


#<·
T = TypeVar('T', bound=Any)
E = TypeVar('E', bound=str)


class Result(NamedTuple, Generic[T, E]):
    ok: bool
    error: Any | E = None
    value: Any | T = None


    def is_ok(self) -> bool:
        return self.ok


    def is_err(self) -> bool:
        return not self.ok


    def __str__(self) -> str:
        return f'Ok(\n\tvalue={self.value}\n)' if self.ok else f'Err(\n\terror={self.error}\n)'


    def expect(self, message: str) -> None:
        return print(f'Expect {message} -> {self.__str__()}')


def Ok(value: T = None) -> Result[T, E]:
    return Result(ok=True, value=value)


def Err(error: E) -> Result[T, E]:
    return Result(ok=False, error=error)
