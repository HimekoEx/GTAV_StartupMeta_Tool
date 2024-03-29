import git


class AboutUtils:

    @staticmethod
    def get_latest_git_tag() -> str:
        """
        获取最新的`git tag`

        :return: 最新的`git tag`
        """
        repo = git.Repo(search_parent_directories=True)
        tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
        latest_tag = tags[-1].name
        return latest_tag

    @staticmethod
    def get_latest_commit_hex() -> str:
        """
        获取最新的`git commit`的前8位`hex`

        :return: 最新的`git commit`的前8位`hex`
        """
        repo = git.Repo(search_parent_directories=True)
        latest_commit = repo.head.commit
        return latest_commit.hexsha[:8]

    @staticmethod
    def get_static_version() -> str:
        """
        获取静态版本号

        :return: 静态版本号
        """
        return 'v1.2.0'
