from mongoengine import CASCADE, PULL
from .owl import Owl
from .rating import Rating
from .user import User

#add in all the delete rules now to avoid circular dependency
Owl.register_delete_rule(Rating, 'owl', CASCADE)
Owl.register_delete_rule(User, 'review_owls', PULL)
User.register_delete_rule(Rating, 'user', CASCADE)
Rating.register_delete_rule(Owl, 'ratings', PULL)
Rating.register_delete_rule(User, 'ratings', PULL)

__all__ = ['Owl', 'Rating', 'User']