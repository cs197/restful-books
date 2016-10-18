
import webapp2

import json

from review import reviews_for_product

from product import Product


class AverageRatingsHandler(webapp2.RequestHandler):

    def post(self):

        # Part I of October 18th's homework goes here.
        # What this method should do is calculate the average rating for the product
        # specified in the payload. That will involve fetching all the ratings for the product,
        # and then summing the individual ratings up and dividing by the total number.
        # Finally you will need to get the Product object from the datastore (see product.py),
        # and update the average rating (or if there is no Product object, make it first).

        payload_string = self.request.body
        payload_dict = json.loads(payload_string)
        product_id = payload_dict["product_id"]
        reviews = reviews_for_product(product_id)
        reviews_len = len(reviews)

        if reviews_len == 0:
            print("No reviews for product with product_id " + product_id + ", returning.")
            return

        rating_accumulator = 0.0

        for review in reviews:
            rating_accumulator += review.rating

        average_rating = rating_accumulator / reviews_len

        product = Product(id=product_id)
        product.average_rating = average_rating
        product.put()

        # October 25th's homework (over the midterm break) is to continue understanding what Professor Ng in his free
        # Coursera course tells us about recommender systems. The URLs for the lectures we are watching is:
        #
        # Recommender Systems Lectures (Week 9 of Ng's Course)
        # ====================================================

        # Problem Formulation (7 minutes):
        #
        #   * https://www.coursera.org/learn/machine-learning/lecture/Rhg6r/problem-formulation
        #
        # Content-Based Recommendations (14 minutes):
        #
        #   * https://www.coursera.org/learn/machine-learning/lecture/uG59z/content-based-recommendations
        #
        # Collaborative Filtering (10 minutes):
        #
        #   * https://www.coursera.org/learn/machine-learning/lecture/2WoBV/collaborative-filtering
        #
        # Collaborative Filtering Algorithm (8 minutes):
        #
        #   * https://www.coursera.org/learn/machine-learning/lecture/f26nH/collaborative-filtering-algorithm
        #

        #  I am unclear so far how critical it is to study the remaining two lectures of Week 9:
        #
        # Vectorization - Low Rank Matrix Factorization (8 minutes):
        #
        #   * https://www.coursera.org/learn/machine-learning/lecture/CEXN0/vectorization-low-rank-matrix-factorization
        #
        # Implementation Detail - Mean Normalization (8 minutes):
        #
        #   * https://www.coursera.org/learn/machine-learning/lecture/Adk8G/implementational-detail-mean-normalization
        #

app = webapp2.WSGIApplication([
    webapp2.Route(r'/_ah/queue/average-ratings', handler=AverageRatingsHandler, name='average-ratings-for-product'),
])
