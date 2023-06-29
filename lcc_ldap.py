import os

from dotenv import load_dotenv
import ldap
import datetime
import logging

logging.basicConfig(filename='reset.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# CONFIGURE LDAP_PASS ON .ENV
load_dotenv()

def change_pass(user, new_password):
    domain = "dc=lcc,dc=ufcg,dc=edu,dc=br"
    server = '150.165.42.41'
    l = ldap.initialize('ldap://%s' % server)
    l.simple_bind_s("cn=admin," + domain, os.getenv('LDAP_PASS'))
    tdn="cn=" + user + ",ou=People," + domain
    mod_attrs = [(ldap.MOD_REPLACE,"userPassword", new_password.encode()),]
    l.modify_s(tdn,mod_attrs)
    log_message = f"User {user} altered LDAP password successfully"
    logging.info(log_message)

if __name__ == "__main__":
    import sys
    change_pass(sys.argv[1], sys.argv[2])