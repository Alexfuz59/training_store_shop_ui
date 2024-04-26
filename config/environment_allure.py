import platform


class EnvironmentAllure:

    environment = {'OC': platform.platform(),
                   'Python': platform.python_version(),
                   'Allure_version': '2.23.1'
                   }

    @staticmethod
    def create_environment(browser, env=environment):
        with open('environment.properties', 'w', encoding='utf-8') as file:
            for key, value in env.items():
                file.write(f'{key}: {value}' + '\n')
            file.write(f'Browser: {browser.browser_type.name}' + '\n')
            file.write(f'Browser_version: {browser.version}' + '\n')
