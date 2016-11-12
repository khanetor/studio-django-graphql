import graphene
from records.schema import QueryType as RecordQueryType


class QueryType(
    RecordQueryType,
    graphene.ObjectType):
    pass


schema = graphene.Schema(query=QueryType)
