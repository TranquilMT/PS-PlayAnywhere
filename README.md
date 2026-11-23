# VYNUVO

**All your games. One place.**

VYNUVO is an open-source Android streaming hub, formerly PS PlayAnywhere.

| Platform | Status |
| --- | --- |
| PlayStation Remote Play | Native streaming through the pinned Chiaki-ng engine |
| Xbox Cloud Gaming | Coming soon |
| PC / Steam streaming | Coming soon |

See the [0.1.13 release notes](docs/RELEASE-0.1.13.md) for the rebrand, Android update compatibility, and device verification status.

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
bash android/apply-integration.sh engine/chiaki
export SOURCE_DATE_EPOCH="$(git -C engine/chiaki show -s --format=%ct HEAD)"
gradle -p engine/chiaki/android :app:assembleDebug --dependency-verification strict
```

The package ID is `com.tranquil.ps5remoteplay`. The current development version is `0.1.13` with version code `14`.

See [ROADMAP.md](ROADMAP.md) for the implementation and verification checklist.

## Connection help

Open **Settings → Connection help** for home pairing, rest-mode wake and off-network testing. The optional WAN IPv4 check identifies common upstream NAT configurations entirely on the device. See the [connection guide](docs/CONNECTION_HELP.md) for interpreting results.

## Release requirements
Every verified release should include a signed APK, full corresponding source archive, SHA-256 checksum, version information and physical-device test results for both local and remote PS5 connections.

Do not commit PSN credentials, tokens, registration keys or signing secrets. This project is not affiliated with Sony Interactive Entertainment.
