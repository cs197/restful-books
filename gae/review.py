

from google.appengine.ext import ndb


class Review(ndb.Model):
    """A model for representing an Amazon review."""
    product_id = ndb.StringProperty(indexed=True)
    member_id = ndb.StringProperty(indexed=True)
    time = ndb.DateTimeProperty(indexed=False)
    rating = ndb.FloatProperty(indexed=False)
    summary = ndb.StringProperty(indexed=False)
    text = ndb.TextProperty(indexed=False)


def reviews_for_product(product_id):
    q = Review.query().filter(Review.product_id == product_id)
    count = q.count()
    to_fetch = count if count < 10 else 10
    print("Found " + str(count) + " reviews for product " + product_id + ", returning " + str(to_fetch))
    reviews = q.fetch(to_fetch)
    return reviews


def reviews_for_member(member_id):
    q = Review.query().filter(Review.member_id == member_id)
    count = q.count()
    to_fetch = count if count < 10 else 10
    print("Found " + str(count) + " reviews for member " + member_id + ", returning " + str(to_fetch))
    reviews = q.fetch(to_fetch)
    return reviews
