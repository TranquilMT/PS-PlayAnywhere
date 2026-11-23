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
git -C "$source_dir" apply "$patch_dir/vynuvo-platform-hub.patch"
git -C "$source_dir" apply "$patch_dir/vynuvo-xbox.patch"
git -C "$source_dir" apply "$patch_dir/vynuvo-embedded-xbox.patch"
upstream="$patch_dir/../../engine/better-xcloud"
assets="$source_dir/android/app/src/main/assets"
(cd "$upstream" && echo '2293b470bae29cd099162e5a28d77fbd532bf75bea9930e7eb5417ff5714db94  dist/better-xcloud.user.js' | sha256sum --check)
mkdir -p "$assets"
cp "$upstream/dist/better-xcloud.user.js" "$assets/"
cp "$upstream/LICENSE" "$assets/Better-xCloud-LICENSE.txt"
metadata="$source_dir/android/gradle/verification-metadata.xml"
if [[ -f "$metadata" ]]; then
    sed -i "/^   <components>$/r $patch_dir/../xbox-gradle-checksums.xml" "$metadata"
fi
