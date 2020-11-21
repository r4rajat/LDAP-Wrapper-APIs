from ldap_api import retrieve_user_details, ldap_connection
from configurations import AUTH_AD_HOST, AUTH_AD_PORT, AUTH_AD_DOMAIN
from services import decode
from flask_restful import Resource
from flask import make_response, request
import json
import http


class UserDetails(Resource):
    def options(self):
        return make_response(json.dumps({}), http.HTTPStatus.OK)

    def get(self):
        try:
            username = request.args.get('username')
            user_details = retrieve_user_details(username=username)
            return make_response(json.dumps({
                "data": user_details
            }), http.HTTPStatus.OK)

        except Exception as e:
            return make_response(json.dumps({
                "error": str(e)
            }), http.HTTPStatus.BAD_REQUEST)


class Login(Resource):
    def options(self):
        return make_response(json.dumps({}), http.HTTPStatus.OK)

    def get(self):
        try:
            username = request.args.get('username')
            password = decode(request.args.get('password'))
            ldap_connection(
                host=AUTH_AD_HOST,
                port=AUTH_AD_PORT,
                domain=AUTH_AD_DOMAIN,
                username=username,
                password=password
            )
            user_details = retrieve_user_details(username=username)
            return make_response(json.dumps({
                'message': "Login Successful",
                'data': user_details
            }), http.HTTPStatus.OK)

        except Exception as e:
            return make_response(json.dumps({
                "error": str(e)
            }), http.HTTPStatus.BAD_REQUEST)
