#!/usr/bin/env bash
set -euo pipefail

apk="${1:?Pass the Android APK to verify}"
sdk="${ANDROID_HOME:?Set ANDROID_HOME before verifying alignment}"
"$sdk/build-tools/35.0.0/zipalign" -c -P 16 4 "$apk"

scratch="$(mktemp -d)"
trap 'rm -rf -- "$scratch"' EXIT
unzip -q "$apk" 'lib/arm64-v8a/*.so' -d "$scratch"
readelf="$sdk/ndk/28.2.13676358/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-readelf"
for library in "$scratch"/lib/arm64-v8a/*.so; do
    printf '%s\n' "${library##*/}"
    "$readelf" --program-headers --wide "$library" |
        awk '/^[[:space:]]*LOAD / { count++; print $NF } END { exit !count }' |
        while IFS= read -r alignment; do
            if ! [[ "$alignment" =~ ^0x[[:xdigit:]]+$ ]] || (( alignment < 16384 )); then
                printf 'Invalid ARM64 LOAD segment alignment: %s\n' "$alignment" >&2
                exit 1
            fi
            printf 'LOAD segment alignment: %s\n' "$alignment"
        done
done
