from pathlib import Path

import click
import os


@click.group
def main():
    pass


@main.command()
@click.argument('app_name')
def startfullaskapp(app_name):
    """
    create a fullask-rest-framework app.

    app_name
        ├── app_name_api
        │         ├── __init__.py
        │         ├── views.py
        │         ├── models.py
        │         └── schemas.py
        ├── __init__.py
        ├── config.py
        └── tests.py

    :param app_name: app name you want to create.
    :param path: filepath your app will be located.
    :return: None
    """
    app_path = os.getcwd() + "/" + app_name
    Path(app_path).mkdir(parents=True, exist_ok=True)
    with open("__init__.py", 'w') as f:
        f.write(f"# {app_name} created by fullask-rest-framework. write your application factory function here.")
    with open("config.py", 'w') as f:
        f.write(f"# write your models here.")
    with open("tests.py", 'w') as f:
        f.write(f"# write your {app_name} tests here.")
    Path(f"/{app_path}/api").mkdir(parents=True, exist_ok=True)
    with open(f"/{app_path}/api/__init__.py", 'w') as f:
        pass
    with open(f"/{app_path}/api/views.py", 'w') as f:
        pass
    with open(f"/{app_path}/api/models.py", 'w') as f:
        pass
    with open(f"/{app_path}/api/schemas.py", 'w') as f:
        pass



if __name__ == "__main__":
    main()
