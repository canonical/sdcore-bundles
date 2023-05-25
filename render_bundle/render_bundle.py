#!/usr/bin/env python3
# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.


"""Python script to generate one of the potential SD-Core bundle variants."""

import argparse
import enum
from typing import Optional

from bundles import SDCoreUserPlane


class SDCoreBundleVariant(enum.Enum):
    """Possible bundles to generate."""

    SDCORE_USER_PLANE = SDCoreUserPlane


def _parse_args() -> tuple[bool, str, str, str]:
    """Parses user provided arguments.

    Returns:
        local (bool): Whether to generate a bundle for local charms (instead of charmhub)
        bundle_variant (str): SD-Core bundle to generate
        channel(str): Charmhub channel. Only use when "local" is set to False.
        output_file (str): Directory and file name where bundle will be generated.
    """
    parser = argparse.ArgumentParser(description="Render jinja2 bundle template from cli args.")
    parser.add_argument(
        "--local",
        action=argparse.BooleanOptionalAction,
        help="Use local path for charms (instead of Charmhub)",
        required=False,
        default=False,
    )
    parser.add_argument(
        "--bundle_variant",
        type=str,
        help="SDCORE bundle type.",
        required=True,
        choices=["SDCORE_USER_PLANE"],
    )
    parser.add_argument(
        "--channel",
        type=str,
        help="Output file",
        choices=["edge", "beta", "candidate", "stable"],
        required=False,
        default="edge",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        help="Output file",
        required=False,
        default="bundle.yaml",
    )
    bundle_args, _ = parser.parse_known_args()
    return (
        bundle_args.local,
        bundle_args.bundle_variant,
        bundle_args.channel,
        bundle_args.output_file,
    )


def render_bundle(
    local: bool,
    bundle_variant: str,
    output_file: str,
    channel: Optional[str] = None,
):
    """Generates a SD-Core bundle variant.

    Args:
        local: Whether to use local charms (instead of charmhub).
        bundle_variant: Bundle variant (ex. SDCORE_USER_PLANE)
        channel: Charmhub channel
        output_file: Output file path and directory (ex. `my/path/bundle.yaml`)
    """
    bundle_variant_type = SDCoreBundleVariant[bundle_variant]
    bundle = bundle_variant_type.value(local=local, channel=channel)
    bundle.render_to_file(output_file=output_file)


def main():
    """Generates one of the SDCORE charm bundles based on user provided bundle type."""
    local, bundle_variant, channel, output_file = _parse_args()
    render_bundle(
        local=local,
        bundle_variant=bundle_variant,
        channel=channel,
        output_file=output_file,
    )


if __name__ == "__main__":
    main()
