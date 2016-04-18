from flask.ext.login import current_user
from flask import Blueprint, jsonify

from resource_alchemy import (
    RestResource,
    Field,
    FullAuthorization,
    resource_route)

from .models import User

color_schemer_api = Blueprint('api', __name__)


class UserResource(RestResource):

    email = Field()

    class meta:
        model = User
        authorization = FullAuthorization
        results_per_page = 500

    @resource_route(methods=['GET'])
    def me(cls):
        return jsonify(cls.serialize(current_user))


UserResource.register_api(color_schemer_api)
