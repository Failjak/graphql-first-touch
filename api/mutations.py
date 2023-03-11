from datetime import date

from ariadne import convert_kwargs_to_snake_case

from api.models import Post


@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description):
    try:
        post = Post(
            title=title, description=description, created_at=date.today()
        )
        post.save()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload
