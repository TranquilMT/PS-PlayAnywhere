# PS PlayAnywhere

Unofficial Android PS5 Remote Play client project.

**Status.** Phase 1 Android integration is in progress. The branded debug build compiles and passes package checks. Physical Android 16 installation and launch are pending.

## Objectives
- Native PS5 streaming over local Wi-Fi and remote networks (4G/5G/external Wi-Fi).
- DualSense and touchscreen controls.
- Remote PSN console discovery and authentication, subject to upstream support.
- Configurable streaming quality and connection diagnostics.

## Android source
The native streaming engine lives at `engine/chiaki`, a submodule pinned to the audited Chiaki revision. Clone with `--recurse-submodules`, or initialize it with `git submodule update --init --recursive`.

Use JDK 17, Gradle 8.11.1, Android SDK 35, CMake 3.22.1, NDK r28c, `protoc` and Python Protobuf. From the root of a fresh checkout, prepare and build with:

```bash
bash build-support/apply-dependency-pins.sh engine/chiaki
git -C engine/chiaki apply "$PWD/android/patches/playanywhere-identity.patch"
export SOURCE_DATE_EPOCH="$(git -C engine/chiaki show -s --format=%ct HEAD)"
gradle -p engine/chiaki/android :app:assembleDebug --dependency-verification strict
```

The package ID is `com.tranquil.ps5remoteplay`. The initial version is `0.1.0` with version code `1`.

See [ROADMAP.md](ROADMAP.md) for the implementation and verification checklist.

## Release requirements
Every verified release should include a signed APK, full corresponding source archive, SHA-256 checksum, version information and physical-device test results for both local and remote PS5 connections.

Do not commit PSN credentials, tokens, registration keys or signing secrets. This project is not affiliated with Sony Interactive Entertainment.
