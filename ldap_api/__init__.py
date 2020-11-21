import ldap
from configurations import AUTH_AD_HOST, AUTH_AD_PORT, AUTH_AD_DOMAIN, AUTH_AD_DN, AUTH_AD_USERNAME, AUTH_AD_PASSWORD, \
    LOGGER


def retrieve_user_details(username):
    try:
        username = str(username).upper()
        connection = ldap_connection(
            host=AUTH_AD_HOST,
            port=AUTH_AD_PORT,
            domain=AUTH_AD_DOMAIN,
            username=AUTH_AD_USERNAME,
            password=AUTH_AD_PASSWORD
        )
        attributes = ["distinguishedName", "description", 'name', 'SamAccountName', 'givenName', 'manager', 'mail',
                      'gs-Project']
        ad_filter = "(&(objectclass=user))"
        ldap_result_id = connection.search(AUTH_AD_DN, ldap.SCOPE_SUBTREE, ad_filter, attributes)
        result_set = []
        user_detail = {}
        while 1:
            result_type, result_data = connection.result(ldap_result_id, 0)
            if not result_data or 'user_email' in user_detail:
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)
                    for result in result_data:
                        temp_dict = result[1]
                        sam_account_name = temp_dict['sAMAccountName'][0].decode()
                        if sam_account_name == username:
                            user_detail['user_full_name'] = temp_dict['name'][0].decode()
                            user_detail['manager'] = temp_dict['manager'][0].decode().split(',')[0].split('=')[1]
                            user_detail['user_email'] = temp_dict['mail'][0].decode()
                            user_detail['project'] = temp_dict['gs-Project'][0].decode()
        user_detail['username'] = username
        return user_detail

    except Exception as e:
        LOGGER.exception("Exception Occurred " + str(e))
        raise Exception(e)


def ldap_connection(host, port, domain, username, password):
    try:

        domain_user = domain + "\\" + username  # create user with domain\username
        ldap_conn = 'ldap://' + str(host) + ':' + str(int(port))  # ldap connection string
        ldap_conn = ldap_conn.replace(" ", "")
        connection = ldap.initialize(ldap_conn)  # connection object of ldap
        connection.protocol_version = 3  # specify the version
        connection.set_option(ldap.OPT_REFERRALS, 0)
        connection.simple_bind_s(domain_user, password)  # connect to ldap
        print(connection.whoami_s())
        return connection

    except Exception as e:
        e = str(e) + "(" + host + ")"  # modify error message and add host details.
        raise Exception(e)
