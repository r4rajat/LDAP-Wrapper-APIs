from configurations import app, api, APP_HOST, APP_PORT, APP_RELOAD
from ldap_api.LDAP import UserDetails, Login

api.add_resource(Login, '/api/ldap/login')
api.add_resource(UserDetails, '/api/ldap/details')

if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT, debug=APP_RELOAD)
