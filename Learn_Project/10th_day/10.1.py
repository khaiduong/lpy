"""
10.1
----
Write a script to list all Github repositories of an user.
For example, user ``hvnsweeting``, use:
https://api.github.com/users/hvnsweeting/repos
Form::
  githubrepos.py username
Libs:
- argparse
- logging
- requests
"""

import requests
import json 
import argparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("--user", dest="user", action="store", type=str, default='reader',
                        help="Github user to request")
args = parser.parse_args()

logger.info('User is: {user}'.format(user = args.user))
if args.user:
    url = "https://api.github.com/users/{user}/repos".format(user=args.user)
    res = requests.get(url)
    logger.debug(res)
    repos = json.loads(res.text)
    names = [repo['name'] for repo in repos]
    logger.info("List of repos is: {names}".format(names = names))
    #print()
else:
    print('Should input github user')