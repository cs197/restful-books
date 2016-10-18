

from google.appengine.ext import ndb


class Product(ndb.Model):
    """A model for representing an Amazon product."""
    average_rating = ndb.FloatProperty(indexed=False)
