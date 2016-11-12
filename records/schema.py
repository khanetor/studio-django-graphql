import graphene
from graphene import relay
import graphene_django
from graphene_django import filter

from .models import Album, Track, HashTag


class TagType(graphene_django.DjangoObjectType):
    class Meta:
        model = HashTag
        interfaces = (relay.Node,)


class TrackNode(graphene_django.DjangoObjectType):
    duration = graphene.String()  # Should be removed once Graphene is updated

    class Meta:
        model = Track
        interfaces = (relay.Node,)


class AlbumNode(graphene_django.DjangoObjectType):
    class Meta:
        model = Album
        interfaces = (relay.Node,)


class QueryType(graphene.AbstractType):
    album = relay.Node.Field(AlbumNode)
    albums = filter.DjangoFilterConnectionField(AlbumNode)
    track = relay.Node.Field(TrackNode)
    tracks = filter.DjangoFilterConnectionField(TrackNode)
