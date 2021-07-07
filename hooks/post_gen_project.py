from github import Github

g = Github('{{cookiecutter.github_auth_token}}')
organization = g.get_organization('{{cookiecutter.github_organization}}')
repo = organization.create_repo(
    '{{cookiecutter.remote_repo_name}}',
    allow_rebase_merge=True,
    auto_init=False,
    description="",
    has_issues=True,
    has_projects=False,
    has_wiki=False,
    private=True,
)

repo.git.add(all=True)
repo.index.commit("Intial Commit By Cookiecutter")
origin = repo.remote(name='origin')
origin.push()