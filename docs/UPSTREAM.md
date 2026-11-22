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
- Gradle wrapper 8.11.1
- Android Gradle Plugin 8.7.3
- Android compile SDK 35
- Android NDK 28.2.13676358
- CMake 3.22.1
- Native git submodules (including nanopb, jerasure, gf-complete, curl and Oboe).

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
