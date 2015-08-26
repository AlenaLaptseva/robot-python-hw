from CmpUtils import CmpUtils
import requests
import json
from random import randint
from string import ascii_lowercase, ascii_uppercase, digits

class APIUserLib(CmpUtils):

    def create_user(self, host, port, username, password, login, user_password, email, firstName, lastName, accountId,
                    enabled=None, accountAdmin=None, liteUser=None, engageUser=None, company=None, jobTitle=None,
                    collaborateLogin=None, autoRefreshEnabled=None, autoRefreshInterval=None, phone=None, address1=None,
                    address2 =None, country=None, state=None, zip=None):

        """Executes the create user method of the User API Service
        The Create User method allows creating a user account with specified parameters.
        It returns the userId on successful creation, fails when the requested user is not created.


        Example:
        | ${userID}=  | create user | qaserver10 | 18081 | admin | admin | user1 | user1 | user@clarabridge.com | John | Smith | <accountId> | enabled=true |

        """

        url = self._get_url('http://{host}:{port}/mobile/rest/users', host, port)
        headers = {'Content-Type': 'application/json'}
        payload = {
            'login': login,
            'password': user_password,
            'email': email,
            'firstName': firstName,
            'lastName': lastName,
            'enabled': enabled,
            'accountAdmin': accountAdmin,
            'liteUser': liteUser,
            'engageUser': engageUser,
            'accountId': accountId,
            'company': company,
            'jobTitle': jobTitle,
            'phone': phone,
            'address1': address1,
            'address2': address2,
            'country': country,
            'state': state,
            'zip': zip,
            'collaborateLogin': collaborateLogin,
            'autoRefreshEnabled': autoRefreshEnabled,
            'autoRefreshInterval': autoRefreshInterval
        }

        r = requests.put(url, data=json.dumps(payload), auth=(username,password), headers=headers)

        if r.status_code == 201:
            resp = r.json()
            return resp["userId"]

        raise Exception("Error Code, %i %s" % (r.status_code, r.text))

    def delete_user(self, host, port, username, password, userId):
        """
        The Delete User method allows deleting a user by specified userId

        Example:
        | ${status}=  | delete user | qaserver10 | 18081 | admin | admin | $(userId) |

        """
        url = self._get_url('http://{host}:{port}/mobile/rest/users/', host, port)
        url = url + str(userId)

        r = requests.delete(url, auth=(username, password))

        if r.status_code == 202:
            resp = r.json()
            return resp["status"]

        raise Exception("Error Code, %i %s" % (r.status_code, r.text))

