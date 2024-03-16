#!/usr/bin/env python3

"""
This script adds a list of my repositories from other platforms to the end.
"""

import requests

response = requests.get("https://git.comfycamp.space/api/v1/users/lumin/repos")
data = response.json()

repos = [
    f'[{ repo["name"].title() }]({ repo["html_url"] }) - { repo["description"].lower() }'
    for repo in data
]

with open('template.md', 'r') as f:
    template = f.read()

full_text = (template
    + "\nI have a few projects on Forgejo. Github is not the only place where I post my code."
    + "\n\n- " + "\n- ".join(repos)
    + "\n")

with open('README.md', 'w') as f:
    f.write(full_text)
