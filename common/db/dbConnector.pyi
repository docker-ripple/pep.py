# I just want type hints.
from typing import Any

class db:
    def __init__(
        self, host: str, user: str, password: str, database: str, initialSize: int
    ) -> None:
        """
        Initialize a new MySQL database helper with multiple workers.
        This class is thread safe.
        :param host: MySQL host
        :param username: MySQL username
        :param password: MySQL password
        :param database: MySQL database name
        :param initialSize: initial pool size
        """
        ...
    def execute(self, query: str, params: tuple = ()) -> None:
        """
        Executes a query
        :param query: query to execute. You can bind parameters with %s
        :param params: parameters list. First element replaces first %s and so on
        """
        ...
    def fetch(self, query: str, params: tuple = (), _all: bool = False) -> Any:
        """
        Fetch a single value from db that matches given query
        :param query: query to execute. You can bind parameters with %s
        :param params: parameters list. First element replaces first %s and so on
        :param _all: fetch one or all values. Used internally. Use fetchAll if you want to fetch all values
        """

        ...
    def fetchAll(self, query: str, params: tuple = ()) -> tuple[dict[str, Any]]:
        """
        Fetch all values from db that matche given query.
        Calls self.fetch with all = True.
        :param query: query to execute. You can bind parameters with %s
        :param params: parameters list. First element replaces first %s and so on
        """

        ...
