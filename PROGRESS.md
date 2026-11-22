# PS PlayAnywhere — PROGRESS

Last updated: 2026-11-22

## Status legend
- [x] Complete (evidence recorded)
- [ ] Pending
- BLOCKED: prerequisite missing
- EXPERIMENTAL: unverified technique

## Phase 0 — Repository and upstream investigation
- [x] Public repository created: https://github.com/TranquilMT/PS-PlayAnywhere
- [x] README, ROADMAP and .gitignore committed
- [x] Identified primary upstream: https://github.com/chiaki-ng/chiaki-ng
- [x] Confirmed upstream source contains an android/ frontend and lib/ protocol implementation (per contributor guide)
- [x] Located upstream remote PSN documentation: https://github.com/chiaki-ng/chiaki-ng/blob/main/docs/setup/remoteconnection.md
- [x] Inspect upstream Android Gradle build requirements (Java 17, compile SDK 35, NDK 28.2.13676358, CMake 3.22.1); upstream commit still needs pinning
- [ ] Audit all native dependencies before import (upstream COPYING is AGPL-3.0)
- [ ] Select pinned upstream revision
- [ ] Produce first reproducible native Android build (GitHub Actions workflow added, execution unverified)

**Works:** GitHub repository, documentation, and committed baseline Android CI workflow definition.
**Does not work / not verified:** Native app, PS5 pairing, video/audio streaming, PSN login, off-network connection, controllers, interpolation, APK.
**Current blocker:** First CI build has not been verified. Workflow currently checks out upstream main; pin to tested commit before release.

## Phase 1 — Native streaming
- [ ] Import pinned upstream with license notices
- [ ] Compile Android ARM64 client
- [ ] Verify local PS5 registration
- [ ] Verify video/audio streaming and input

## Phase 2 — Remote PSN
- [ ] Verify PSN sign-in flow and secure token handling
- [ ] Verify console discovery, remote wake, IPv4 UDP NAT traversal
- [ ] Test external Wi-Fi and cellular networks
- [ ] Record NAT/network failure handling

## Phase 3 — Video and controls
- [ ] Android MediaCodec hardware decoding
- [ ] 720p/1080p and 30/60 FPS source options as supported
- [ ] Bluetooth/USB DualSense and touchscreen
- [ ] Streaming metrics and reconnect handling

## Phase 4 — Experimental 30-to-60 display interpolation
- [ ] Measure baseline latency, decode time and dropped frames
- [ ] Implement optional GPU motion interpolation prototype
- [ ] Measure artifacts, GPU/battery cost and added latency
- [ ] Provide immediate disable switch and favor native 60 FPS

**Note:** Interpolated 60 FPS is not native 60 FPS gameplay and may increase input latency.

## Phase 5 — UI and release
- [ ] Landscape Android UI
- [ ] Settings and diagnostics
- [ ] CI build and secure signing
- [ ] Signed APK, full source and SHA-256
- [ ] Device tests and release notes

## Evidence log
- 2026-11-22: Inspected upstream android/app/build.gradle and COPYING via GitHub connector; confirmed native Android Gradle/CMake build and AGPL-3.0 license. Added .github/workflows/android-baseline.yml to compile upstream debug APK and upload checksum/commit provenance. No successful build claimed.
- 2026-11-22: Created PROGRESS.md. Verified repository and identified upstream architecture and PSN documentation. No native code or APK shipped.
