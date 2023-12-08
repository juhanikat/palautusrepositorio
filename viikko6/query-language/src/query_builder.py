from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, Or, Not, And


class AllQuery:

    def __init__(self) -> None:
        pass

    def test(self, player):
        return True


class PlaysInQuery:

    def __init__(self, query, team) -> None:
        self.query = query
        self.team = team

    def test(self, player):
        if PlaysIn(self.team).test(player) and self.query.test(player):
            return True


class hasFewerThanQuery:
    def __init__(self, query, value, attr) -> None:
        self.query = query
        self.value = value
        self.attr = attr

    def test(self, player):
        if HasFewerThan(self.value, self.attr).test(player) and self.query.test(player):
            return True


class hasAtLeastQuery:
    def __init__(self, query, value, attr) -> None:
        self.query = query
        self.value = value
        self.attr = attr

    def test(self, player):
        if HasAtLeast(self.value, self.attr).test(player) and self.query.test(player):
            return True


class OrQuery:
    def __init__(self, *queries) -> None:
        self.queries = queries

    def test(self, player):
        for query in self.queries:
            if Or(query).test(player):
                return True
        return False


class QueryBuilder:

    def __init__(self, query=AllQuery()) -> None:
        self.query = query

    def playsIn(self, team):
        return QueryBuilder(PlaysInQuery(self.query, team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(hasAtLeastQuery(self.query, value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(hasFewerThanQuery(self.query, value, attr))

    def oneOf(self, *queries):
        return QueryBuilder(OrQuery(*queries))

    def build(self):
        return self.query
