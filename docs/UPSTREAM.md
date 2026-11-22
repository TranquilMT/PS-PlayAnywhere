# Upstream provenance and licensing

## Native streaming baseline
- Project: chiaki-ng
- Repository: https://github.com/chiaki-ng/chiaki-ng
- Pinned revision: `43728af2e639fecb8a7af1cd68c29820a40de973`
- Revision link: https://github.com/chiaki-ng/chiaki-ng/commit/43728af2e639fecb8a7af1cd68c29820a40de973
- Main license: GNU Affero General Public License, version 3 (`COPYING`).
- Android frontend: `android/`, with native CMake project in the root.

## Build dependencies observed
- JDK 17
- Gradle distribution 8.11.1, with published SHA-256 checked before use. The pinned upstream wrapper targets 8.11.1 but its JAR identifies itself as Gradle 4.6, so CI invokes the verified distribution directly.
- Android Gradle Plugin 8.7.3
- Android compile SDK 35
- Android NDK 28.2.13676358
- CMake 3.22.1
- Native git submodules (including nanopb, jerasure, gf-complete, curl and Oboe).

## Android dependency inventory

These entries come from the pinned source, Android Gradle catalog and CMake files. The resolved Android runtime dependency graph and the contents of the built APK still need to be checked against this inventory.

| Dependency | Revision or version | Role in the Android baseline | License evidence |
| --- | --- | --- | --- |
| nanopb | `160d4f09e5fabb2b66aa2dea32d4f38ace2c4b3f` | Takion code generation and native serialization | [LICENSE.txt](https://github.com/nanopb/nanopb/blob/160d4f09e5fabb2b66aa2dea32d4f38ace2c4b3f/LICENSE.txt), zlib |
| Jerasure | `505ccb4bc69eee8d7ea40a6089a056b99671134f` | Native forward error correction | [COPYING](https://github.com/streetpea/jerasure/blob/505ccb4bc69eee8d7ea40a6089a056b99671134f/COPYING), BSD 3-Clause |
| GF-Complete | `fa54a4670a5705c84abf6c24b92b0cd479625478` | Finite-field arithmetic for Jerasure | [COPYING](https://github.com/streetpea/gf-complete/blob/fa54a4670a5705c84abf6c24b92b0cd479625478/COPYING), BSD 3-Clause |
| curl | `75a2079d5c28debb2eaa848ca9430f1fe0d7844c` | Native HTTP and WebSocket client | [COPYING](https://github.com/curl/curl/blob/75a2079d5c28debb2eaa848ca9430f1fe0d7844c/COPYING), curl license |
| Oboe | Maven AAR `1.10.0` | Native audio output via Prefab | [1.10.0 LICENSE](https://github.com/google/oboe/blob/1.10.0/LICENSE), Apache-2.0. The checked-out Oboe gitlink is separate from the AAR dependency. |
| OpenSSL | `1.1.1w` with an upstream SHA-256 pin | Native TLS and cryptography | [LICENSE](https://github.com/openssl/openssl/blob/OpenSSL_1_1_1w/LICENSE), OpenSSL and original SSLeay terms |
| json-c | `0.17-20230812` tag archive | Native JSON | [COPYING](https://github.com/json-c/json-c/blob/json-c-0.17-20230812/COPYING), MIT |
| miniupnpc | `2.2.8` tag archive | Native UPnP client | [LICENSE](https://github.com/miniupnp/miniupnp/blob/miniupnpc_2_2_8/LICENSE), BSD 3-Clause |

The direct Gradle runtime declarations also include AndroidX Activity, AppCompat, Core, ConstraintLayout, RecyclerView, Preference, Lifecycle and Room, Material Components, Kotlin coroutines and Moshi. Record each resolved runtime component, its source version and notices before distributing a branded APK. The Gradle/KSP compiler plugins, host `protoc` and Python Protobuf are build tools. The baseline config disables desktop Qt, FFmpeg, system Opus and tests. Android decodes Opus through MediaCodec.

The release audit remains open for transitive Gradle dependencies, bundled NDK runtimes, archive hashes for json-c and miniupnpc, and review of the OpenSSL terms alongside the app's license and linkage.

## Android integration notes

- Preserve the upstream Kotlin namespace and JNI bindings when setting the new application ID. Change the manifest FileProvider authority to use `${applicationId}` and update the matching runtime lookup in the same patch.
- The pinned Android app has discovery, manual console registration and streaming screens. Its native CMake target includes Chiaki's remote hole-punching code, but the Android manifest has no PSN sign-in callback and the Android UI has no PSN authentication flow. Verify Android pairing and streaming first, then wire and test PSN authentication separately.

## Source distribution requirements
The first workflow builds upstream source without modifying it. It does **not** yet produce a PS PlayAnywhere branded APK. When distributing a modified app, preserve copyright and AGPL notices and provide the complete corresponding source and build scripts. Review all bundled third-party licenses before publishing a release. Never publish signing keys, PSN tokens or user registration secrets.

## Reproducibility status
- [x] Pin upstream Git revision in CI
- [x] Assert checked-out revision matches expected commit
- [x] Record commit in artifact
- [x] Generate and require non-empty SHA256SUMS.txt after build
- [ ] Verify GitHub Actions successful run
- [ ] Record APK SHA-256 from a real run
- [ ] Verify full dependency licenses and hashes
- [ ] Rebuild twice and compare reproducibility characteristics
- [ ] Sign and publish a compliant PS PlayAnywhere release

## Limitations
GitHub Actions is currently configured for an upstream *debug baseline*. A debug APK is not a production-signed release. Build success and functional PS5/PSN support require independent verification.
