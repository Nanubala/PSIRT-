
from github import Github 
import warnings
import zipfile
import io
import json
from .base import VulnersApiBase, ParamError, validate_params
from .base import Endpoint, String, Integer, Dict, List, Tuple, Const, ResultSet

access_token = "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"

g = Github(access_token)


for repo in g.get_user().get_repos():
    print("repo name is ::", repo)
    for issue in repo.get_issues():
        #print("issue name is ::", issue)
        a = issue.title
        #print("*********issue having title********",a)
        for label in issue.get_labels():
         # print("*********issue having label********",label.name)
          if(label.name.__eq__("psirt") ) :
             print("========issue having body=======")
            
          
    for branch in repo.get_branches():
        print("&&&&&branch name&&&&&&",branch)
    
        