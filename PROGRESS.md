# PS PlayAnywhere — Progress and verification ledger

Updated: 2026-11-22. This file is the authoritative evidence ledger; see [ROADMAP.md](ROADMAP.md) for the full 12-phase task breakdown.

## Current state
**Active:** Phase 1 — Android source integration.
**Verified:** Phase 0 dependency checksum enforcement, pinned source checkout, branded ARM64 debug build, and 16 KB APK and ARM64 ELF alignment.
**Open in Phase 1:** Install and launch the branded debug app on physical Android 16 hardware.
**Release:** The signed PS PlayAnywhere APK is a Phase 10 deliverable. Device installation, console pairing, PSN and remote play have yet to be tested.

## Phase gates
| Phase | Name | Status | Evidence / next gate |
| --- | --- | --- | --- |
| 0 | Baseline, licensing and reproducibility | COMPLETE | Baseline license audit, repeatable APK payload and strict dependency checksum validation passed. |
| 1 | Android source integration | COMPLETE | The user confirmed that 0.1.1 launches on their Android 16 phone. |
| 2 | Local console streaming | NOT STARTED | 15-minute gameplay test |
| 3 | PSN login and discovery | NOT STARTED | Real-account authentication test |
| 4 | Remote NAT traversal | NOT STARTED | Two external network tests |
| 5 | Video and latency | NOT STARTED | Sustained native 60 FPS measurement |
| 6 | Audio and input | NOT STARTED | Controller and audio tests |
| 7 | 30→60 interpolation | EXPERIMENTAL | Android build and device benchmarks |
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

## Phase 1 Android integration

- A physical Android 16 launch of 0.1.0 crashed. Source inspection found two relative CoordinatorLayout behavior names that resolve against the branded package ID. Version 0.1.1 uses fully qualified Chiaki class names. The local build and all 19 unit tests passed, and APK inspection confirmed both packaged references. Physical retest is pending.

- Added **Settings → Connection help** from the uploaded Remote Play guide. The app gives pairing, rest-mode and off-network troubleshooting guidance and classifies an optional router WAN IPv4 locally. All 19 unit tests passed locally, including the new address boundary cases. The [clean CI build and test run](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45010228669) passed. The downloaded APK matched its recorded SHA-256 `9db912e9ddc877fb1e9cc1ad4b23296539c6945d8d89932366ffd2ce7169dc24`. All 12 packaged native libraries matched the prior integration build byte for byte.

- Verified a fresh recursive checkout of `engine/chiaki` at the audited commit with the eight matching nested gitlinks and both upstream license files.
- Applied the PS PlayAnywhere identity patch. Gradle built version `0.1.0` (version code `1`) as `com.tranquil.ps5remoteplay`. APK inspection verified the label, launcher icon and matching FileProvider authority. The existing Kotlin/JNI namespace is preserved.
- A clean build from the recursive checkout passed all 42 Gradle tasks with the final checksum lock. Its ARM64-only debug APK SHA-256 is `ccf54bdc6596dc5e7c89a0b73ff2e669f9d01877797fe4211c8274b456e9bd52`. The debug signature verified, and the APK passed its 16 KB ZIP alignment check. All LOAD segments in the three packaged ARM64 shared libraries reported `0x4000` alignment.
- The [Android integration CI run](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45009457492) passed from a clean runner. The downloaded APK matched its recorded SHA-256 `3a8a709f6c82ad14fa1b232aa9bae94db320241c53c1465aa96fd4e3995fdf9e`. Its package ID, version, debug signature and 16 KB ARM64 alignment were independently verified again after download.
- ADB listed no connected devices. The physical install and launch gate stays open.

## Phase 0 checksum verification

- CMake enforces SHA-256 for json-c and miniupnpc alongside the original OpenSSL pin. Tests accepted both authentic archives and rejected altered copies.
- The committed Gradle lock covers 844 artifacts across 407 coordinates. Both local debug and unsigned release tasks passed strict verification. A deliberately changed Android Gradle Plugin digest stopped Gradle at classpath verification.
- [Run #8](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45008670005) exposed two missing JUnit BOM metadata files. [Run #9](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45008905556) exposed a missing coroutines BOM POM. Their Maven Central SHA-256 values were independently checked and added.
- The reference job in [run #10](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45009204264) passed with the completed lock on a clean GitHub runner. Its downloaded APK matched the recorded SHA-256, and its 1,061 payload entries matched the previously verified upstream baseline. The repeat job received HTTP 403 while downloading Gradle.

## Verified CI run #7

- [Run #7](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45006004955) passed on two clean runners. The reference and repeat runner compiled the same pinned upstream source with the commit timestamp passed to OpenSSL.
- Downloaded and independently compared both upstream debug APKs. All 1,061 APK entries matched byte for byte. The per-entry SHA-256 manifests also matched. Their shared manifest SHA-256 is `8e346efd7aa4dcfb56637b89367a4b9239c69382bcffe86a5eb0d005c8bc882f`.
- The signed debug APKs had different SHA-256 values and different debug signing certificates. Both signatures verified. The resolved dependency reports differed only in the elapsed Gradle command time.

## Verified CI run #6
- [Run #6](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45005296420), job `137155454047`, built the same upstream revision using the checksum-verified Gradle distribution. The APK checksum `23a721f3461bf297f6dd1434a5948ce45dda79e6e3ae6b742cec5a5d59fbe152` matched after download.
- Compared with run #5, 1,057 APK entries matched and four changed. All four changed files were `libchiaki-jni.so`, one per ABI. The ARM64 comparison showed a different OpenSSL build timestamp and ELF build ID. The two APKs also had different debug signing certificates.
- The baseline audit matched all 89 resolved Gradle runtime coordinates to license evidence and identified the packaged native libraries. See [UPSTREAM.md](docs/UPSTREAM.md).
- The workflow subsequently set `SOURCE_DATE_EPOCH` from the pinned upstream commit and scheduled the two clean builds verified in run #7.

## Verified local upstream build

- Downloaded and used Temurin 17.0.21+9, the checksum-verified Gradle 8.11.1 distribution, Android platform 35, NDK r28c and CMake 3.22.1. The local Gradle run used the workspace proxy and a local Protobuf compiler wrapper. The GitHub builds use the Ubuntu Protobuf packages.
- The unmodified upstream checkout passed `:app:assembleDebug`. The output matched the expected upstream package ID, included ARM64, ARMv7, x86 and x86-64, passed APK signature v2 verification and passed the APK ZIP alignment check. SHA-256: `3857306553212d33c5b8c91c407a5046ec44855e2ad688e6e6ba2cee61063318`.

## Verified CI run #5
- [Run #5](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45005001825), job `137154496486`, built upstream Chiaki `43728af2e639fecb8a7af1cd68c29820a40de973`.
- The Protocol Buffers preflight, native Gradle build, APK checks and artifact upload passed. The upstream debug package was `com.metallic.chiaki` version `1.10.1` (version code `12`).
- SHA-256 of the APK: `4d9ec2f8f5e641cbc8226fd80689834a03e4f657d9541890a7d612656f6501e0`. The downloaded APK matched this digest, passed APK Signature Scheme v2 verification and contained ARM64 builds of Chiaki JNI, Oboe and the C++ runtime.

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

## PS5 registration

- 0.1.3 uses the same visible button style for the sign-in and paste actions. The change addresses the missing paste label reported on Android 16. Device retest is pending.

- 0.1.2 adds PlayStation sign-in from the registration screen, validates the pasted Sony return link against the current attempt, and fills the Account ID without the public lookup site. Live PSN sign-in and PS5 pairing still need a device test.

## Physical device retest

- The user confirmed that 0.1.1 launches and reached the PS5 registration screen. Pairing is pending entry of the PSN Account ID.

## Streaming controls

- User reported that pairing and streaming work but controls did not respond. The app now routes input from the selected touch overlay, dispatches joystick motion at the activity boundary, and sends digital trigger changes immediately. Phone retest is pending.

## Display only and 30 → 60 FPS

- The in-stream Display only switch hides the touch overlays, releases held phone controls and suppresses phone controller updates while video and audio continue. Direct DualSense play on the PS5 requires a physical test with a separate Remote Play account.
- The in-stream 30 → 60 frame generation switch enables an experimental OpenGL ES renderer. It estimates motion between consecutive decoded frames and renders a midpoint for roughly 30 FPS input. The switch defaults to off and the direct video path remains available. Display cadence, added latency, motion artifacts and thermal cost need device testing.

## Next actions (strict order)
1. Complete local PS5 registration using the PSN Account ID and console pairing code.
2. Verify local streaming in Phase 2.

Do not mark a phase complete based solely on plans, source presence or an unexecuted CI workflow.
