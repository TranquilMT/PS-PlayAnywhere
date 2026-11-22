# PS PlayAnywhere — Progress and verification ledger

Updated: 2026-11-22. This file is the authoritative evidence ledger; see [ROADMAP.md](ROADMAP.md) for the full 12-phase task breakdown.

## Current state
**Active:** Phase 0 — Native baseline build.
**Works:** GitHub repository, project documentation, committed GitHub Actions workflow definition.
**Not verified:** CI build success, APK installation, console pairing, video/audio, controllers, PSN authentication, remote connection, frame interpolation.
**Blockers:** Both initial CI runs failed at Android SDK setup, before native compilation. Fix committed in a40cad2; its new run must be checked. Native third-party licenses and physical device tests remain pending.

## Phase gates
| Phase | Name | Status | Evidence / next gate |
| --- | --- | --- | --- |
| 0 | Baseline, licensing and reproducibility | IN PROGRESS | Source pinned; CI provenance checks committed; first two runs failed in SDK setup; fix pending verification |
| 1 | Android source integration | NOT STARTED | Branded native APK installs |
| 2 | Local console streaming | NOT STARTED | 15-minute gameplay test |
| 3 | PSN login and discovery | NOT STARTED | Real-account authentication test |
| 4 | Remote NAT traversal | NOT STARTED | Two external network tests |
| 5 | Video and latency | NOT STARTED | Sustained native 60 FPS measurement |
| 6 | Audio and input | NOT STARTED | Controller and audio tests |
| 7 | 30→60 interpolation | NOT STARTED | Latency/artifact benchmark |
| 8 | UI and accessibility | NOT STARTED | Onboarding acceptance |
| 9 | Reliability and security | NOT STARTED | Security and soak test |
| 10 | Build, signing and releases | NOT STARTED | Signed APK, source, checksum |
| 11 | Device acceptance | NOT STARTED | Physical device report |

## Verified upstream facts
- Pinned commit: `43728af2e639fecb8a7af1cd68c29820a40de973`; source and license inventory: `docs/UPSTREAM.md`.
- Source: https://github.com/chiaki-ng/chiaki-ng
- Android entry point: `android/app/build.gradle`, using Java 17, Android compileSdk 35, NDK 28.2.13676358 and CMake 3.22.1.
- Gradle wrapper: 8.11.1; Android Gradle Plugin: 8.7.3.
- Native source is compiled through root `CMakeLists.txt`; upstream has git submodules.
- Upstream COPYING contains GNU AGPL v3.
- Remote PSN setup docs state IPv4-only and warn that some NAT types cannot hole punch.

## Verified CI failures
- Run #1: failed (2026-11-22).
- Run #2: https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45004276383 — **failure**, job 137152274427.
- Job log: `android-actions/setup-android@v3` invokes `sdkmanager tools`, which fails with `Warning: Failed to find package 'tools'`; native compilation step was skipped.
- Fix commit `a40cad20cbbe2c9e286b439f4b0af8d8660c0858`: remove failing setup action; use preinstalled SDK manager to install exact platform/build-tools/CMake/NDK packages. Result not yet verified.

## Change log
- 2026-11-22: Pinned upstream Chiaki revision in workflow and added exact commit assertion, Gradle wrapper presence check and nonempty SHA-256 manifest check.
- 2026-11-22: Created docs/UPSTREAM.md with source provenance, toolchain versions, licensing and reproducibility limitations.
- 2026-11-22: Added README, ROADMAP, .gitignore and PROGRESS.md.
- 2026-11-22: Committed `.github/workflows/android-baseline.yml` to attempt an upstream native debug build and archive checksum/provenance.
- 2026-11-22: Audited upstream Android Gradle, wrapper, submodule list, COPYING and remote connectivity documentation.
- 2026-11-22: Expanded roadmap to 12 gated engineering phases and updated evidence ledger.

## Next actions (strict order)
1. Inspect GitHub Actions baseline build run and diagnose errors; workflow was updated to trigger on push.
2. Fix any native build failures and record successful artifact SHA-256.
3. Finish third-party licensing review, then integrate native source into PS PlayAnywhere.
4. Begin physical-device local pairing tests before claiming remote support.

Do not mark a phase complete based solely on plans, source presence or an unexecuted CI workflow.
