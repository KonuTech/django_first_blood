from abc import ABC, abstractmethod
from dataclasses import dataclass
from faker import Faker

faker = Faker("pl_PL")


@dataclass
class Post:
    id: int
    title: str
    content: str


class IPostService(ABC):

    @abstractmethod
    def list() -> list[Post]:
        pass


class FakePostService(IPostService):
    id = 1

    def list() -> list[Post]:
        n = 25
        return [FakePostService._create_post() for _ in range(n)]

    @classmethod
    def _create_post(cls) -> Post:

        post = Post(
            id=cls.id,
            title=faker.text(30),
            content=faker.text(500)
        )

        cls.id += 1
        return post