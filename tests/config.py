class Config:
    def __init__(self, env):

        SUPPORTED_ENVS = ['dev', 'qa']

        if env.lower() not in SUPPORTED_ENVS:
            # here we can implement our own exception
            raise Exception(f'{env} is not supported')

        self.base_url = {
            "dev": "https://dev-env.com", 
            "qa": "https://qa-env.com"
        }[env]

        self.app_port = {
            "dev": 8080, "qa": 80
        }[env]
