#!/usr/bin/env python3
# Copyright 2021 Canonical Ltd.
# See LICENSE file for licensing details.

import unittest

from render_bundle import render_bundle

TEST_PATH = "tests/unit/src"


def file_content(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


class TestRenderBundle(unittest.TestCase):
    def test_given_sdcore_up_when_render_bundle_then_bundle_is_rendered(self):
        rendered_bundle_path = f"{TEST_PATH}/rendered_bundle_sdcore_up.yaml"
        expected_bundle_path = f"{TEST_PATH}/expected_bundle_sdcore_up.yaml"
        render_bundle(
            local=False,
            bundle_variant="SDCORE_UP",
            output_file=rendered_bundle_path,
        )

        self.assertEqual(file_content(rendered_bundle_path), file_content(expected_bundle_path))

    def test_given_sdcore_up_local_when_render_bundle_then_bundle_is_rendered(self):
        rendered_bundle_path = f"{TEST_PATH}/rendered_bundle_sdcore_up_local.yaml"
        expected_bundle_path = f"{TEST_PATH}/expected_bundle_sdcore_up_local.yaml"
        render_bundle(
            local=True,
            bundle_variant="SDCORE_UP",
            output_file=rendered_bundle_path,
        )

        self.assertEqual(file_content(rendered_bundle_path), file_content(expected_bundle_path))
