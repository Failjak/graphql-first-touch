from ariadne import convert_kwargs_to_snake_case

from .models import Post


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload


def listPosts_resolver(*args, **kwargs):
    try:
        posts = [p.to_dict() for p in Post.query.all()]
        payload = {
            "success": True,
            "posts": posts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
