class Config:
    def __init__(self, env):
        self.base_url = {
            'dev': 'https://dev-env.com',
            'qa': 'https://qa-env.com'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]