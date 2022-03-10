from github import Github
import requests
import json
import re
import base64
from pprint import pprint
from pynpm import NPMPackage
import subprocess
import os


g=Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
finalvulpackage = ""
packagedata = ""
packagelockdata = ""

for repo in g.get_user().get_repos():
    if (repo.name.__eq__("bms-push-servicebroker")):
        print("*******", repo.clone_url)
        files = repo.get_contents("")
        print("files ::", files)
        s = repo.get_contents('package.json')
        packagecontent = s.decoded_content
        print("package.json content::", packagecontent)
        s = repo.get_contents('package-lock.json')
        packagelockcontent = s.decoded_content
        print("package-lock .json content ::", packagelockcontent)
        packagedata = json.loads(packagecontent)
        packagelockdata = json.loads(packagelockcontent)

    for issue in repo.get_issues():
      for label in issue.get_labels():
        if (label.name.__eq__("psirt")):
                b = issue.body.replace("<br />", "\n")
                b1 = b.replace("**", "")
                dict_1 = json.dumps(b1)
                b = issue.body.__repr__()
                print("*********PSIRT issue ********", issue)
                start = b.find("Affected Products:")
                end = b.find("Dependent Products")
                substring = b[start:end]
                vulpackage = substring.replace("<br />", "")
                size = len(vulpackage)
                print("vulnerability package::",vulpackage[20:size-2])
                finalvulpackage = vulpackage[20:size-2]

                if finalvulpackage in packagedata:
                    print("found in package.json",packagedata[finalvulpackage])
                else:
                    print("not found in package.json")

                if finalvulpackage in packagelockdata:
                    print("found in package-lock.json", packagelockdata[finalvulpackage])
                else:
                    print("not found in package-lock.json")
