# Studio (Django graphene example)

This is a demo of how to use graphql with [Django](https://github.com/django/django) ORM, using [Graphene](https://github.com/graphql-python/graphene/).

#### Dependencies:
- `Django==1.10.3`
- `graphene[django]==1.0.2`

#### Setup
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py loaddata records`
- `python manage.py runserver`

Notice that graphene module is loaded, and a schema is specified in settings.
```python
INSTALLED_APPS = [
    # ...
    'graphene_django',
    # apps
]

GRAPHENE = {
    'SCHEMA': 'records.schema.schema'
}
```

After setting up, you can browse to `http://localhost:8000/graphql/` to try out the graph APIs.

Sample graph query:
```
{
  album(id: 1) {
    name
    date
    tags {
      name
    }
    tracks {
      name
      duration
    }
  }
  
  albums {
    name
    date
    tags {
      name
    }
  }
}
```

#### Concerns
- Performance might not be as optimized as traditional rest API, because there might be multiple queries issues when
querying nested related objects.
- There are other way to integrate Django models with GraphQL Type, but I found them not working with
Django 1.10 at the moment.
