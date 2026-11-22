# Upstream provenance and licensing

## Native streaming baseline
- Project: chiaki-ng
- Repository: https://github.com/chiaki-ng/chiaki-ng
- Pinned revision: `43728af2e639fecb8a7af1cd68c29820a40de973`
- Revision link: https://github.com/chiaki-ng/chiaki-ng/commit/43728af2e639fecb8a7af1cd68c29820a40de973
- Main license: GNU Affero General Public License, version 3 (`COPYING`). Upstream files marked `LicenseRef-AGPL-3.0-only-OpenSSL` refer to the [additional OpenSSL permission](https://github.com/chiaki-ng/chiaki-ng/blob/43728af2e639fecb8a7af1cd68c29820a40de973/LICENSES/AGPL-3.0-only-OpenSSL.txt).
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

These entries come from the pinned source, Android Gradle catalog and CMake files. The resolved Android runtime graph and the packaged native libraries were checked against this inventory.

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
| LLVM C++ runtime | Android NDK r28c, `28.2.13676358` | `libc++_shared.so` | NDK `NOTICE.toolchain` includes libc++ and libc++abi notices. The packaged ARM64 binary matched the NDK copy after stripping unneeded symbols. |

The direct Gradle runtime declarations also include AndroidX Activity, AppCompat, Core, ConstraintLayout, RecyclerView, Preference, Lifecycle and Room, Material Components, Kotlin coroutines and Moshi. Record each resolved runtime component, its source version and notices before distributing a branded APK. The Gradle/KSP compiler plugins, host `protoc` and Python Protobuf are build tools. The baseline config disables desktop Qt, FFmpeg, system Opus and tests. Android decodes Opus through MediaCodec.

Preserve the OpenSSL license and SSLeay notices alongside the upstream permission. The permission text calls for corresponding source to include the used OpenSSL source.

The following SHA-256 values were computed from the archives at the URLs used by the pinned upstream CMake files. Upstream CMake currently fetches these two archives by tag URL.

| Archive | Observed SHA-256 |
| --- | --- |
| json-c `json-c-0.17-20230812.tar.gz` | `024d302a3aadcbf9f78735320a6d5aedf8b77876c8ac8bbb95081ca55054c7eb` |
| miniupnpc `miniupnpc_2_2_8.tar.gz` | `3d0d49f761f09c1321ceb663d1b008825361d7bd242640c60ae467e82642502a` |

### Resolved runtime license evidence

[Run #6](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45005296420) archived the `debugRuntimeClasspath` report used for this audit. The report resolves 89 distinct runtime coordinates. Published POMs declare Apache-2.0 for 87 of them. The remaining two were resolved from primary source:

- `com.google.guava:listenablefuture:1.0`. The [published source JAR](https://repo.maven.apache.org/maven2/com/google/guava/listenablefuture/1.0/listenablefuture-1.0-sources.jar) gives the file-level Apache-2.0 notice.
- `com.google.oboe:oboe:1.10.0`. The [matching source license](https://github.com/google/oboe/blob/1.10.0/LICENSE) is Apache-2.0.

The upstream APK packages three shared libraries in each ABI: `libchiaki-jni.so`, `liboboe.so` and `libc++_shared.so`. ARM64 JNI links to Oboe, the C++ runtime and Android-supplied system libraries. The pinned CMake files identify its statically linked dependencies in the table above. Carry the component notices and corresponding source into the Phase 10 release package.

The build preparation script applies both archive hashes through CMake `URL_HASH`. OpenSSL retains its upstream SHA-256 pin. Gradle strict verification uses the [SHA-256 manifest](../build-support/verification-metadata.xml) for 844 artifacts across 407 coordinates, including Maven metadata. The lock covers the Linux debug and unsigned release build paths.

## Android integration notes

- Android integration uses the pinned `engine/chiaki` submodule and a tracked app identity patch. The patch preserves the Kotlin namespace and JNI bindings and derives the FileProvider authority from the application ID.
- The pinned Android app has discovery, manual console registration and streaming screens. Its native CMake target includes Chiaki's remote hole-punching code, but the Android manifest has no PSN sign-in callback and the Android UI has no PSN authentication flow. Verify Android pairing and streaming first, then wire and test PSN authentication separately.

## Source distribution requirements
The pinned submodule retains the upstream source and license files. The build scripts and tracked patches are part of the corresponding source for the branded app. Preserve copyright and AGPL notices and include the source, build scripts and bundled dependencies in the Phase 10 release package. Never publish signing keys, PSN tokens or user registration secrets.

## Reproducibility status
- [x] Pin upstream Git revision in CI
- [x] Assert checked-out revision matches expected commit
- [x] Record commit in artifact
- [x] Generate and require non-empty SHA256SUMS.txt after build
- [x] Verify GitHub Actions successful run ([run #5](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45005001825))
- [x] Record and independently verify the APK SHA-256 ([PROGRESS.md](../PROGRESS.md))
- [x] Verify baseline dependency licenses against the resolved runtime graph and native dependency inventory
- [x] Enforce the Android Maven artifact and native archive SHA-256 pins during builds
- [x] Rebuild twice and compare reproducibility characteristics ([run #7](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45006004955)). All APK payload entries matched. The signed debug APKs used different runner-generated certificates.
- [ ] Sign and publish a compliant PS PlayAnywhere release

## Limitations
GitHub Actions builds the upstream debug baseline and the PS PlayAnywhere integration APK. Release signing, physical launch, PS5 pairing and PSN connectivity are tracked separately in the roadmap.
