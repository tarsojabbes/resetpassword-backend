import datetime
import logging
import os

import ldap
from dotenv import load_dotenv

logging.basicConfig(filename='reset.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# CONFIGURE LDAP_PASS ON .ENV
load_dotenv()

LDAP_SERVER = os.getenv('LDAP_SERVER')
LDAP_DOMAIN = os.getenv('LDAP_DOMAIN')
LDAP_PASS = os.getenv('LDAP_PASS')


def change_pass(user, new_password):
    l = ldap.initialize('ldap://%s' % LDAP_SERVER)
    l.simple_bind_s("cn=admin," + LDAP_DOMAIN, os.getenv('LDAP_PASS'))
    tdn="cn=" + user + ",ou=People," + LDAP_DOMAIN
    mod_attrs = [(ldap.MOD_REPLACE,"userPassword", new_password.encode()),]
    l.modify_s(tdn,mod_attrs)
    log_message = f"User {user} altered LDAP password successfully"
    logging.info(log_message)

if __name__ == "__main__":
    import sys
    change_pass(sys.argv[1], sys.argv[2])
