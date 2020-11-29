from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    # overwrite the method for signals
    def ready(self):
    	import accounts.signals
