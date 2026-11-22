# PS PlayAnywhere — Progress and verification ledger

Updated: 2026-11-22. This file is the authoritative evidence ledger; see [ROADMAP.md](ROADMAP.md) for the full 12-phase task breakdown.

## Current state
**Active:** Phase 0 — Native baseline build.
**Works:** GitHub repository, project documentation, committed GitHub Actions workflow definition.
**Not verified:** CI build success, APK installation, console pairing, video/audio, controllers, PSN authentication, remote connection, frame interpolation.
**Blockers:** First build result has not been inspected; upstream revision is not pinned; physical PS5/Android testing is still required.

## Phase gates
| Phase | Name | Status | Evidence / next gate |
| --- | --- | --- | --- |
| 0 | Baseline, licensing and reproducibility | IN PROGRESS | Android Gradle inspected; CI workflow committed; successful run missing |
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
- Source: https://github.com/chiaki-ng/chiaki-ng
- Android entry point: `android/app/build.gradle`, using Java 17, Android compileSdk 35, NDK 28.2.13676358 and CMake 3.22.1.
- Gradle wrapper: 8.11.1; Android Gradle Plugin: 8.7.3.
- Native source is compiled through root `CMakeLists.txt`; upstream has git submodules.
- Upstream COPYING contains GNU AGPL v3.
- Remote PSN setup docs state IPv4-only and warn that some NAT types cannot hole punch.

## Change log
- 2026-11-22: Added README, ROADMAP, .gitignore and PROGRESS.md.
- 2026-11-22: Committed `.github/workflows/android-baseline.yml` to attempt an upstream native debug build and archive checksum/provenance.
- 2026-11-22: Audited upstream Android Gradle, wrapper, submodule list, COPYING and remote connectivity documentation.
- 2026-11-22: Expanded roadmap to 12 gated engineering phases and updated evidence ledger.

## Next actions (strict order)
1. Inspect GitHub Actions baseline build run and diagnose errors.
2. Pin upstream commit and update CI to use it.
3. Build successfully, record SHA-256, then integrate native source into PS PlayAnywhere.
4. Begin physical-device local pairing tests before claiming remote support.

Do not mark a phase complete based solely on plans, source presence or an unexecuted CI workflow.
