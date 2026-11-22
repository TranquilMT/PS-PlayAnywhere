#!/usr/bin/env bash
set -euo pipefail

source_dir="${1:?Pass the path to a fresh Chiaki source checkout}"
support_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

git -C "$source_dir" apply "$support_dir/patches/native-archive-checksums.patch"
cp -- "$support_dir/verification-metadata.xml" "$source_dir/android/gradle/verification-metadata.xml"
