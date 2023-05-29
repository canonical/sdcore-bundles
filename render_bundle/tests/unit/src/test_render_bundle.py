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
    def test_given_sdcore_when_render_bundle_then_bundle_is_rendered(self):
        rendered_bundle_path = f"{TEST_PATH}/rendered_bundle_sdcore.yaml"
        expected_bundle_path = f"{TEST_PATH}/expected_bundle_sdcore.yaml"
        render_bundle(
            local=False,
            bundle_variant="SDCORE",
            channel="edge",
            output_file=rendered_bundle_path,
        )

        self.assertEqual(file_content(rendered_bundle_path), file_content(expected_bundle_path))

    def test_given_sdcore_local_when_render_bundle_then_bundle_is_rendered(self):
        rendered_bundle_path = f"{TEST_PATH}/rendered_bundle_sdcore_local.yaml"
        expected_bundle_path = f"{TEST_PATH}/expected_bundle_sdcore_local.yaml"
        render_bundle(
            local=True,
            bundle_variant="SDCORE",
            output_file=rendered_bundle_path,
        )

        self.assertEqual(file_content(rendered_bundle_path), file_content(expected_bundle_path))

    def test_given_sdcore_control_plane_when_render_bundle_then_bundle_is_rendered(self):
        rendered_bundle_path = f"{TEST_PATH}/rendered_bundle_sdcore_control_plane.yaml"
        expected_bundle_path = f"{TEST_PATH}/expected_bundle_sdcore_control_plane.yaml"
        render_bundle(
            local=False,
            bundle_variant="SDCORE_CONTROL_PLANE",
            channel="beta",
            output_file=rendered_bundle_path,
        )

        self.assertEqual(file_content(rendered_bundle_path), file_content(expected_bundle_path))

    def test_given_sdcore_control_plane_local_when_render_bundle_then_bundle_is_rendered(self):
        rendered_bundle_path = f"{TEST_PATH}/rendered_bundle_sdcore_control_plane_local.yaml"
        expected_bundle_path = f"{TEST_PATH}/expected_bundle_sdcore_control_plane_local.yaml"
        render_bundle(
            local=True,
            bundle_variant="SDCORE_CONTROL_PLANE",
            output_file=rendered_bundle_path,
        )

        self.assertEqual(file_content(rendered_bundle_path), file_content(expected_bundle_path))

    def test_given_sdcore_user_plane_when_render_bundle_then_bundle_is_rendered(self):
        rendered_bundle_path = f"{TEST_PATH}/rendered_bundle_sdcore_user_plane.yaml"
        expected_bundle_path = f"{TEST_PATH}/expected_bundle_sdcore_user_plane.yaml"
        render_bundle(
            local=False,
            bundle_variant="SDCORE_USER_PLANE",
            channel="beta",
            output_file=rendered_bundle_path,
        )

        self.assertEqual(file_content(rendered_bundle_path), file_content(expected_bundle_path))

    def test_given_sdcore_user_plane_local_when_render_bundle_then_bundle_is_rendered(self):
        rendered_bundle_path = f"{TEST_PATH}/rendered_bundle_sdcore_user_plane_local.yaml"
        expected_bundle_path = f"{TEST_PATH}/expected_bundle_sdcore_user_plane_local.yaml"
        render_bundle(
            local=True,
            bundle_variant="SDCORE_USER_PLANE",
            output_file=rendered_bundle_path,
        )

        self.assertEqual(file_content(rendered_bundle_path), file_content(expected_bundle_path))
