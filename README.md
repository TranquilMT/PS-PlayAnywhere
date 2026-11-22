# PS PlayAnywhere

Unofficial Android PS5 Remote Play client project.

**Status:** Repository initialized; no playable APK has been built or tested.

## Objectives
- Native PS5 streaming over local Wi-Fi and remote networks (4G/5G/external Wi-Fi).
- DualSense and touchscreen controls.
- Remote PSN console discovery and authentication, subject to upstream support.
- Configurable streaming quality and connection diagnostics.

## Implementation plan
Use a verified, Android-compatible open-source Chiaki/chiaki-ng implementation as the native streaming foundation. Verify its repository, license, build instructions, remote PSN functionality, and required Android SDK/NDK versions before importing it. Preserve upstream license notices. A WebView is not a substitute for the native streaming engine.

Proposed Android package ID: `com.tranquil.ps5remoteplay`.

See [ROADMAP.md](ROADMAP.md) for the implementation and verification checklist.

## Release requirements
Every verified release should include a signed APK, full corresponding source archive, SHA-256 checksum, version information and physical-device test results for both local and remote PS5 connections.

Do not commit PSN credentials, tokens, registration keys or signing secrets. This project is not affiliated with Sony Interactive Entertainment.
