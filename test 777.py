from github import Github

import vulners

access_token = "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"

g = Github(access_token)
vulners_api = vulners.VulnersApi(api_key="7P1T6UORMX8PR0C38RYJA0L7NUZTQTDR0VM7OH9GCA4H2NYUYK0QPQEII533ZL9H")
sw_results = vulners_api.get_bulletin("CVE-2022-0355")
scan  = vulners_api.find_exploit_all("CVE")
print("========vulnarabilities=======",scan)
results = vulners_api.get_software_vulnerabilities("CVE", "1.3")
vulnerabilities_list = [results[key] for key in results if key not in ("info", "blog", "bugbounty")]
print("========vulnerabilities_list=======",vulnerabilities_list)
references = vulners_api.get_bulletin_references("CVE-2022-0355")
print("========get_bulletin_references=======",references)
for repo in g.get_user().get_repos():
    print("repo name is ::", repo)
    for issue in repo.get_issues():
        # print("issue name is ::", issue)
        a = issue.title
        print("*********issue having title********",a)

        for label in issue.get_labels():
            # print("*********issue having label********",label.name)
            if (label.name.__eq__("psirt")):
                print("========issue having body=======")

    for branch in repo.get_branches():
        print("&&&&&branch name&&&&&&", branch)
