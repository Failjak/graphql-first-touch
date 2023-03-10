from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, \
    ObjectType, MutationType
from ariadne.explorer.playground import PLAYGROUND_HTML
from flask import request, jsonify

from api import app
from api.models import Post

# from api.queries import listPosts_resolver, getPost_resolver

query: ObjectType = ObjectType("Query")
# mutation = MutationType()


# query.set_field("listPosts", listPosts_resolver)
# query.set_field("getPost", getPost_resolver)


# @mutation.field("add_place")
# def add_place(_, info, title, description):
#     place = Post(title=title, description=description)
#     place.save()
#     return place.to_json()


@query.field("posts")
def listPosts_resolver(obj, info):
    # try:
    #     posts = [post.to_dict() for post in Post.query.all()]
    #     print(posts)
    #     payload = {
    #         "success": True,
    #         "posts": posts
    #     }
    # except Exception as error:
    #     payload = {
    #         "success": False,
    #         "errors": [str(error)]
    #     }
    return {"id": 1, "title": "Paris", "description": "The city of lights", "country": "France", "created_at": 12312}


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        # debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)



class Contact(models.Model):
   first_name = models.CharField(max_length=150)
   last_name = models.CharField(max_length=150)
   phone = models.CharField(max_length=150)
   email = models.CharField(max_length=150, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)


def test_contact_create():
   contact = Contact(first_name="John", last_name="Doe", phone="123456789")
   contact.save()
   assert contact.first_name == "John"
   assert contact.last_name == "Doe"
   assert contact.phone == "123456789"
   assert contact.email == ""
   assert contact.created_at is not None