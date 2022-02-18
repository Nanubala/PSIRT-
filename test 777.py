from github import Github
import requests
import json
import re
from pprint import pprint

access_token = ""

g = Github(access_token)
for repo in g.get_user().get_repos():
    print("repo name is ::", repo)

    content = repo.get_contents("")
    print("content ::", content)
    for issue in repo.get_issues():
        # print("issue name is ::", issue)

        for label in issue.get_labels():
            # print("*********issue having label********",label.name)
            if (label.name.__eq__("psirt")):
                b=issue.body.replace("<br />", "")
                b1=b.replace("**","")
                dict_1 = json.dumps(b1)
                b = issue.body.__repr__()
                a = re.search('Affected Products:', b)
                print("*********PSIRT issue********", issue)
                start = b.find("Affected Products:")
                end = b.find("Dependent Products")
                substring = b[start:end]
                print(substring.replace("<br />", ""))
