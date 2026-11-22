# PS PlayAnywhere — Progress and verification ledger

Updated: 2026-11-22. This file is the authoritative evidence ledger; see [ROADMAP.md](ROADMAP.md) for the full 12-phase task breakdown.

## Current state
**Active:** Phase 0 — Baseline, licensing and reproducibility.
**Verified:** The pinned upstream Chiaki source compiles on GitHub Actions. The archived debug APK's signature, ARM64 libraries and SHA-256 were verified independently after download.
**Open in Phase 0:** Third-party license audit and comparison of independent builds. Phase 1 starts after these checklist items are complete.
**Release:** The signed PS PlayAnywhere APK is a Phase 10 deliverable. Device installation, console pairing, PSN and remote play have yet to be tested.

## Phase gates
| Phase | Name | Status | Evidence / next gate |
| --- | --- | --- | --- |
| 0 | Baseline, licensing and reproducibility | IN PROGRESS | Run #5 passed. Finish the dependency license audit and independent rebuild comparison. |
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

## Verified CI run #5
- [Run #5](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45005001825), job `137154496486`, built upstream Chiaki `43728af2e639fecb8a7af1cd68c29820a40de973`.
- The Protocol Buffers preflight, native Gradle build, APK checks and artifact upload passed. The upstream debug package was `com.metallic.chiaki` version `1.10.1` (version code `12`).
- SHA-256 of the APK: `4d9ec2f8f5e641cbc8226fd80689834a03e4f657d9541890a7d612656f6501e0`. The downloaded APK matched this digest, passed APK Signature Scheme v2 verification and contained ARM64 builds of Chiaki JNI, Oboe and the C++ runtime.
- [Run #6](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45005296420) passed the Gradle distribution checksum check and is rebuilding the same upstream revision with the runtime dependency report enabled.

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
1. Check run #6 and audit the resolved third-party dependencies against the packaged files.
2. Compare independent upstream builds and record any differences between their APK contents and signatures.
3. Complete Phase 0 before starting Android source integration in Phase 1.

Do not mark a phase complete based solely on plans, source presence or an unexecuted CI workflow.
