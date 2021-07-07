from github import Github
import git

try:
    g = Github('{{cookiecutter.github_auth_token}}')

    local_repo = git.Repo.init()

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
    origin = local_repo.create_remote('origin', repo.ssh_url)
    local_repo.index.add(local_repo.untracked_files)
    local_repo.index.commit("Intial Commit By Cookiecutter")
    branch = local_repo.active_branch
    branch.rename("main")
    local_repo.git.push("--set-upstream", origin, 'main')
except:
    print('Repo Creation Failed')