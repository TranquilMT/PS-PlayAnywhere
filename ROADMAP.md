# VYNUVO Roadmap

Each phase has an exit gate. A feature is complete only when build output, test evidence, or device logs prove it. Status is recorded in [PROGRESS.md](PROGRESS.md).

## 0. Baseline, licensing and reproducibility
- [x] Create repository, roadmap and progress log
- [x] Inspect upstream Android Gradle and CMake configuration
- [x] Identify upstream AGPL-3.0 license and required submodules
- [x] Add initial native baseline GitHub Actions build workflow
- [x] Verify first CI result and capture failure logs (runs #2–4 diagnosed in PROGRESS.md)
- [x] Pass upstream debug packaging, signature and ARM64 checks in CI ([run #5](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45005001825))
- [x] Pin upstream to a specific source commit and assert its identity in CI
- [x] Complete third-party license audit for the upstream baseline (see [UPSTREAM.md](docs/UPSTREAM.md))
- [x] Compare independent upstream builds and document differences ([run #7](https://github.com/TranquilMT/PS-PlayAnywhere/actions/runs/45006004955))
- [x] Enforce the remaining Maven and native archive SHA-256 pins in the Android build

The Phase 0 build artifact is an upstream Chiaki debug reference used to verify the toolchain. The signed PS PlayAnywhere release APK is tracked in Phase 10.

**Exit:** Verify the pinned upstream Android build and finish the Phase 0 license and reproducibility checks before starting Phase 1.

## 1. Android source integration
- [x] Choose pinned submodule integration
- [x] Import complete corresponding source and preserve notices
- [x] Set app ID and versionCode/versionName without breaking updates
- [x] Set application label and launcher icon
- [x] Compile ARM64-v8a debug APK
- [x] Verify 16 KB ZIP and ARM64 ELF segment alignment
- [x] Add in-app connection help and offline WAN IPv4 classification
- [x] Verify installation and launch on physical Android 16 hardware (0.1.1 user-confirmed)
**Exit:** Branded native app launches on a physical device.

## 2. Console registration and local streaming
- [ ] PS5 registration with user-provided pairing code
- [ ] Local discovery and manual IP fallback
- [ ] Persist registration securely
- [ ] Test H.264/H.265 video and audio
- [ ] Verify video orientation, aspect ratio and decoding
- [ ] Handle suspend/resume and connection teardown
**Exit:** 15-minute local gameplay session without crash or audio loss.

## 3. PSN login and remote discovery
- [ ] Review Android-compatible PSN auth flow and OAuth redirect handling
- [ ] Avoid embedded credential capture; use browser-based sign-in
- [ ] Protect tokens at rest and redact logs
- [ ] Fetch registered consoles and display clear error states
- [ ] Implement token expiry, reauth and logout
**Exit:** Authenticated discovery on a real PSN account without credential leakage.

## 4. Remote connection and NAT traversal
- [ ] Reuse proven upstream UDP hole punching logic
- [ ] Verify PS5 remote wake from Rest Mode
- [ ] Test external Wi-Fi, 4G, 5G and tethering
- [ ] Diagnose CGNAT, symmetric NAT, IPv6-only and firewall failures
- [ ] Offer documented manual connection fallback where feasible
- [ ] Retry with bounded backoff and user-visible status
**Exit:** Remote play succeeds on two different off-network connections.

## 5. Video pipeline and latency
- [x] Select and preview the requested PS5 resolution, source FPS and target bitrate before streaming
- [ ] MediaCodec hardware decode with supported codecs
- [ ] Configurable resolution, bitrate and source frame rate
- [ ] Optimize buffering and frame pacing
- [ ] Detect dropped/late frames and decoder resets
- [ ] Measure glass-to-glass latency and input-to-photon latency
- [ ] Avoid unnecessary frame copies and thermal overload
**Exit:** Sustained playable native 60 FPS stream where console/game/network support it.

## 6. Audio and input
- [ ] Low-latency audio output and A/V sync
- [ ] DualSense Bluetooth and USB mappings
- [ ] Touchpad, triggers, vibration support where platform allows
- [ ] Touch overlay and remappable controls
- [ ] Input focus, disconnection and reconnect handling
- [ ] Verify Display only mode with Remote Play on a second PS5 account and the DualSense connected to the console on the main account
**Exit:** Full controller test checklist passes during a remote session.

## 7. Experimental 30 → 60 FPS display interpolation
- [ ] Establish baseline 30 FPS input and latency measurements
- [x] Route decoded frames to a GPU-readable SurfaceTexture while retaining the direct SurfaceView path
- [x] Estimate motion between adjacent frames and synthesize one midpoint frame per pair on the phone
- [ ] Pace real and generated frames at 16.7 ms intervals for a steady 30 FPS source and verify each generated frame is distinct
- [ ] Compare GPU Vulkan/OpenGL ES implementations
- [x] Verify shader output against a known midpoint for a synthetic camera pan
- [ ] Test UI/HUD ghosting, camera pans and fast motion
- [ ] Record extra frame latency, battery use and thermal cost
- [x] Add off/on toggle, default off, and automatic fallback
**Exit:** Objective benefit without unacceptable input delay; otherwise retain as experimental.

## 8. Product UI and accessibility
- [ ] Console dashboard, pairing and connection flow
- [ ] Landscape gameplay screen and in-session settings
- [ ] Clear connectivity and quality indicators
- [ ] Accessibility labels, scaling and readable errors
- [ ] Localized text architecture
**Exit:** Usable onboarding without developer tools.

## 9. Reliability and security
- [ ] Network switching Wi-Fi ↔ cellular
- [ ] Android foreground/background behavior
- [ ] Secrets and permissions review
- [ ] Crash diagnostics without personal data
- [ ] Long-session memory, battery and thermal tests
**Exit:** Documented reliability and security test report.

## 10. Build, signing and releases
- [ ] Debug CI passes reproducibly
- [ ] Permanent signing key stored securely (never in repository)
- [ ] Signed release APK with stable package/version increments
- [ ] Source archive, license notices, SHA-256 checksum
- [ ] Install-over-previous-version regression
- [ ] Publish GitHub release and changelog
**Exit:** Downloadable verified signed APK with matching source.

## 11. Device acceptance
- [ ] PS5 local pairing
- [ ] External Wi-Fi remote play
- [ ] Cellular remote play
- [ ] DualSense and touch
- [ ] 30 FPS and native 60 FPS modes
- [ ] Optional interpolation benchmark
- [ ] Connection recovery and 30-minute soak test
**Exit:** Physical device acceptance report with known limitations.

## Known technical constraints
- PSN-assisted hole punching is IPv4 dependent according to upstream documentation.
- Some NAT combinations will not support automatic traversal.
- A 30 FPS source cannot gain real gameplay updates from frame interpolation.
- Interpolation adds compute cost and may increase latency.
- Upstream AGPL-3.0 obligations must be preserved.

## Platform expansion

- [x] Show Xbox Cloud Gaming and PC / Steam as Coming soon in the Android hub.
- [ ] Implement and test Xbox Cloud Gaming authentication, controller input and playback.
- [ ] Select a PC streaming protocol and validate host pairing, controller input and Steam game launches.
- [ ] Verify the rebrand on a physical Android device, including upgrading from 0.1.12 and opening an existing PlayStation pairing.

- [x] Add registration, account lookup and stream connection feedback driven by app state.
- [ ] Verify reconnect, PIN prompts and reduced motion on a physical Android device.
