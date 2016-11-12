import graphene
from .models import Album


class TagType(graphene.ObjectType):
    name = graphene.String()


class TrackType(graphene.ObjectType):
    name = graphene.String()
    duration = graphene.String()


class AlbumType(graphene.ObjectType):
    name = graphene.String()
    date = graphene.types.datetime.DateTime()
    tracks = graphene.List(
        TrackType
    )
    tags = graphene.List(
        TagType
    )

    def resolve_tracks(self, args, context, info):
        return self.track_set.all()

    def resolve_tags(self, args, context, info):
        return self.tags.all()


class QueryType(graphene.AbstractType):
    album = graphene.Field(
        AlbumType,
        id=graphene.Int()
    )

    albums = graphene.List(
        AlbumType
    )

    def resolve_album(self, args, context, info):
        id = args.get('id')
        return Album.objects.get(pk=id)

    def resolve_albums(self, args, context, info):
        return Album.objects.all()
