#!/usr/bin/env python3
# Copyright 2021 Canonical Ltd.
# See LICENSE file for licensing details.

import unittest

from charm_bundle_generator import Application, CharmBundle, Relation

TEST_PATH = "tests/unit/lib"


def file_content(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


class TestRenderBundle(unittest.TestCase):
    def test_given_charmhub_charm_when_render_bundle_then_bundle_is_rendered(self):
        rendered_bundle_path = f"{TEST_PATH}/rendered_bundle_charmhub.yaml"
        expected_bundle_path = f"{TEST_PATH}/expected_bundle_charmhub.yaml"

        bundle_description = "My wonderful bundle description"
        bundle_name = "My wonderful bundle name"
        app_1 = Application(name="app-1-name", charm="app-1-charm")
        app_2 = Application(name="app-2-name", charm="app-2-charm")
        app_3 = Application(name="app-3-name", charm="app-3-charm")
        relation_1 = Relation(
            app_1_name=app_1.name,
            app_1_relation_name="banana",
            app_2_name=app_2.name,
            app_2_relation_name="fruit",
        )
        relation_2 = Relation(
            app_1_name=app_2.name,
            app_1_relation_name="pizza",
            app_2_name=app_3.name,
            app_2_relation_name="cheese",
        )
        bundle = CharmBundle(
            description=bundle_description,
            name=bundle_name,
            applications=[
                app_1,
                app_2,
                app_3,
            ],
            relations=[
                relation_1,
                relation_2,
            ],
        )
        bundle.render(output_file=rendered_bundle_path)

        self.assertEqual(file_content(rendered_bundle_path), file_content(expected_bundle_path))