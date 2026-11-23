#!/usr/bin/env bash
set -euo pipefail

output="$(realpath -m -- "${1:?Pass the destination .tar.gz path}")"
stage="$(mktemp -d)"
trap 'rm -rf -- "$stage"' EXIT
export SOURCE_ARCHIVE_ROOT="$stage"
git archive HEAD | tar -xf - -C "$stage"
git submodule foreach --quiet --recursive '
    destination="$SOURCE_ARCHIVE_ROOT/$displaypath"
    mkdir -p "$destination" &&
    git archive HEAD | tar -xf - -C "$destination"
'
tar -czf "$output" -C "$stage" .
