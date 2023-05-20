#!/usr/bin/env python3
# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Generates any charm bundle from user provided Application and Relation objects."""

from typing import Optional

from jinja2 import Template
from pydantic import BaseModel


def write_to_file(file: str, content: str):
    """Writes content to a file.

    Args:
        file: File name
        content: File content
    """
    with open(file, "w") as f:
        f.write(content)


class Resource(BaseModel):
    """Pydantic model describing a charm application resource."""

    name: str
    value: str


class Application(BaseModel):
    """Pydantic model describing a charm application."""

    name: str
    charm: str
    resources: Optional[list[Resource]] = None
    scale: int = 1
    trust: bool = False
    channel: Optional[str] = None


class Relation(BaseModel):
    """Pydantic model describing a charm relation."""

    app_1_name: str
    app_1_relation_name: str
    app_2_name: str
    app_2_relation_name: str


class CharmBundle:
    """Class describing a charm bundle."""

    def __init__(
        self,
        name: str,
        description: str,
        applications: list[Application],
        relations: Optional[list[Relation]],
        bundle: str = "kubernetes",
    ):
        self.name = name
        self.description = description
        self.bundle = bundle
        self.applications = applications
        self.relations = relations

    def render(self, output_file: str):
        """Renders charm bundle using jinja2 templating.

        Args:
            output_file: Output file
        """
        with open("lib/bundle.yaml.j2") as file:
            template = Template(file.read())
        content = template.render(
            bundle=self.bundle,
            name=self.name,
            description=self.description,
            applications=self.applications,
            relations=self.relations,
        )
        write_to_file(content=content, file=output_file)
