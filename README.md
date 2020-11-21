# LDAP Wrapper for AD Authentication through APIs
--------------------------------------------------

#### Step 1: Install Requirements to Run Application

```bash
$ pip3 install -r requirements.txt
```

##### NOTE: If getting error while installing pyldap follow the step below

```bash
$ sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev -y
```

#### Step 2: Setup Environmental Variables
```bash
$ nano ~/.bashrc
```
Add following Environmental Variables to your .bashrc file
```text
export AUTH_AD_HOST="IP of your AD Server/Host"
export AUTH_AD_PORT="AD Server/Host Port"
export AUTH_AD_DOMAIN="AD Domain"
export AUTH_AD_DN="Search Path in the Tree"
# Details of Bind User 
export AUTH_AD_USERNAME="Username of Bind User"
export AUTH_AD_PASSWORD="Password of Bind User in Base64 encooding"
```
#### Step 3: Run the Python Application
```bash
$ python3 app.py
``` 

----------------------------------

## API Documentation
-------------------
```api
Host: localhost(Default)
Port: 5000(Default)
```

##### Login / Check Credentials / Authenticating User
```api
API: /api/ldap/login
Method: GET
Params:
    - username: Username of User (GS-xxxx)
    - password: Password of User in base64 encoding
```

##### Fetch User Information
```api
API: /api/ldap/details
Method: GET
Params:
    - username: Username of User (GS-xxxx)
```
