import os
from pathlib import Path
import click
from click import BadParameter
from jinja2 import Template

from typing import Final

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def write_file_from_template(
    template_path: str,
    template_variables: dict,
    output_directory: str,
) -> None:
    template = Template(open(template_path).read())
    rendered = template.render(template_variables)
    created_filename = template_path.split("/")[-1][:-9]
    output_path = os.path.join(output_directory, created_filename)
    with open(output_path, "w+") as f:
        f.write(rendered)


@click.group
def main():
    pass


@main.command()
@click.argument("project_name", type=click.STRING, required=True)
@click.argument("path", type=click.Path(exists=True), default=".", required=True)
def startproject(project_name: str, path: str) -> None:
    """
    Create a new Project Files at this given path and project name.

    :param project_name: project name.
    :param path: project root path.
    :return: None
    """

    project_template_path: Final[str] = os.path.abspath(
        os.path.join(ROOT_DIR, "project_template")
    )
    selected_path_by_user: Final[str] = os.path.abspath(os.path.join(Path.cwd(), path))

    if Path(path).is_dir():
        # make project root package.
        project_path = Path(selected_path_by_user + "/" + project_name)
        try:
            project_path.mkdir(parents=True)
        except FileExistsError:
            raise BadParameter(
                f"The folder name with {project_name} already exists.",
                param_hint="[PROJECT_NAME]",
            )
        project_path.joinpath("__init__.py").touch()
        # make config package with template files.
        config_path = project_path.joinpath("./config")
        config_path.mkdir(parents=True)
        for path, subdirs, files in os.walk(project_template_path):
            for name in files:
                write_file_from_template(
                    os.path.join(path, name),
                    {"project_name": project_name},
                    str(config_path),
                )

    else:
        raise BadParameter(
            f"{os.path.abspath(os.path.join(Path.cwd(), path))} is a file, not directory.",
            param_hint="[PATH]",
        )


if __name__ == "__main__":
    main()
