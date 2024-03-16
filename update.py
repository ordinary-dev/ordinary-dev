#!/usr/bin/env python3

"""
This script adds a list of my repositories from other platforms to the end.
"""

import requests


def format_name(src: str) -> str:
    return src[0].title() + src[1:]


def format_description(src: str) -> str:
    src = src[0].lower() + src[1:]
    if not src.endswith('.'):
        src += '.'
    return src


def gen_markdown(name: str, url: str, description: str) -> str:
    return f'[{ format_name(name) }]({ url }) - { format_description(description) }'


response = requests.get("https://git.comfycamp.space/api/v1/users/lumin/repos")
data = response.json()

repos = [gen_markdown(repo["name"], repo["html_url"], repo["description"]) for repo in data]

with open('template.md', 'r') as f:
    template = f.read()

full_text = (template
    + "\nI have a few projects on Forgejo. Github is not the only place where I post my code."
    + "\n\n- " + "\n- ".join(repos)
    + "\n")

with open('README.md', 'w') as f:
    f.write(full_text)
