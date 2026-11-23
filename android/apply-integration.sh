#!/usr/bin/env bash
set -euo pipefail

source_dir="${1:?Pass the path to a fresh Chiaki source checkout}"
patch_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/patches" && pwd)"
git -C "$source_dir" apply \
    "$patch_dir/playanywhere-identity.patch" \
    "$patch_dir/connection-help.patch" \
    "$patch_dir/psn-account-lookup.patch" \
    "$patch_dir/stream-controls.patch"
git -C "$source_dir" apply "$patch_dir/vynuvo-branding.patch"
git -C "$source_dir" apply "$patch_dir/vynuvo-motion.patch"
