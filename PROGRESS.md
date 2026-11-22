# PS PlayAnywhere — Progress and verification ledger

Updated: 2026-11-22. This file is the authoritative evidence ledger; see [ROADMAP.md](ROADMAP.md) for the full 12-phase task breakdown.

## Current state
**Active:** Phase 0 — Native baseline build.
**Works:** GitHub repository, project documentation, committed GitHub Actions workflow definition.
**Not verified:** CI build success, APK installation, console pairing, video/audio, controllers, PSN authentication, remote connection, frame interpolation.
**Blockers:** Run #4 passed the `protoc` check and reached native compilation, where nanopb failed to import `google.protobuf`. CI now installs the Python runtime for the interpreter used by CMake and tests Takion code generation before Gradle. A successful APK build, resolved dependency audit and physical device tests remain pending.

## Phase gates
| Phase | Name | Status | Evidence / next gate |
| --- | --- | --- | --- |
| 0 | Baseline, licensing and reproducibility | IN PROGRESS | Takion code generation passed locally. CI still needs to verify APK build, debug signature, ARM64 packaging and checksum. |
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

## Verified CI run #4
- [Run #4](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45004670277), job `137153477589`, built commit `c0dc35d`.
- The host compiler and CMake configuration passed. Native ARM64 build failed when `/usr/bin/python3` ran the pinned nanopb generator and raised `ModuleNotFoundError: No module named 'google'`. APK upload was skipped.
- The pinned generator produced both `takion.pb.c` and `takion.pb.h` locally with Python Protobuf 4.25.3 and libprotoc 25.1. The GitHub runner uses the Ubuntu compiler and Python package, which the new CI step exercises against the same schema.

## Verified CI run #3
- https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45004455273 (job 137152820250).
- Observed: checkout, source SHA assertion, Java 17, Android toolchain installation, Gradle wrapper checks **success**.
- Observed: `Build upstream Android debug APK` **failed**: `lib/protobuf/CMakeLists.txt:4: Could not find protoc`. Checksum and upload skipped. Fix committed c0dc35d. No APK produced.

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
1. Verify the next baseline run passes the Takion generator step, and inspect any subsequent native build failure.
2. Record the verified APK's package, ABI, signature and SHA-256 after CI produces it.
3. Finish third-party licensing review, then integrate native source into PS PlayAnywhere.
4. Begin physical-device local pairing tests before claiming remote support.

Do not mark a phase complete based solely on plans, source presence or an unexecuted CI workflow.
