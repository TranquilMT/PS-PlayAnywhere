# PS PlayAnywhere — Roadmap

## Phase 0 — Foundation
- [x] Create public GitHub repository
- [x] Add project scope and roadmap
- [ ] Select and verify Android-compatible upstream Chiaki implementation
- [ ] Verify upstream license and attribution obligations
- [ ] Confirm Android SDK/NDK, CMake/Gradle requirements

## Phase 1 — Native Android client
- [ ] Import native streaming client source with license notices
- [ ] Establish reproducible Android ARM64 build
- [ ] Set app ID `com.tranquil.ps5remoteplay`
- [ ] Brand launcher and application as PS PlayAnywhere
- [ ] Verify local network PS5 pairing and streaming
- [ ] Add DualSense Bluetooth/USB input tests

## Phase 2 — Remote access
- [ ] Implement or retain upstream PSN authentication and console discovery
- [ ] Verify remote wake and connection outside home network
- [ ] Test 4G, 5G, external Wi-Fi and NAT failure cases
- [ ] Add diagnostics without exposing account tokens

## Phase 3 — Experience
- [ ] Touch controls and landscape-first layout
- [ ] Resolution, bitrate and frame-rate options
- [ ] Connection status, recovery and troubleshooting
- [ ] Android lifecycle and background/foreground handling

## Phase 4 — Release
- [ ] CI build workflow for debug APK
- [ ] Secure release signing configuration
- [ ] Smoke test on physical Android device
- [ ] Verify PS5 local and remote streaming
- [ ] Publish APK, source ZIP and SHA-256 checksum
- [ ] Document known limitations

**No checklist item should be marked complete without evidence.**
