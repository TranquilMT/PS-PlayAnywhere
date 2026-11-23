# VYNUVO 0.1.13

**All your games. One place.** PS PlayAnywhere takes the VYNUVO name as the Android app expands toward console, PC and cloud streaming.

## Android experience

- The launcher icon, system splash screen, app label and main toolbar use the new VYNUVO identity.
- The launch intro animates the V mark, wordmark and tagline. The home screen follows with a short entrance animation. Android's animation preference controls whether these transitions play.
- The PlayStation console list sits below the platform header. Xbox Cloud Gaming and PC / Steam appear as **Coming soon**, with animated information dialogs that explain the planned integrations. Xbox sign-in, PC pairing and streaming from those platforms are future work.

## PlayStation and GPU features

- The native Chiaki-ng engine remains integrated at the repository's pinned revision. Console registration, discovery and streaming continue through the existing Android flow.
- Paired consoles retain the existing stream options, including per-console resolution and bitrate choices, Display only, and experimental GPU frame generation.
- Frame generation requests a 30 FPS source and aims to present interpolated frames at 60 FPS on the phone. Real-device frame pacing, motion quality and thermal behavior still need physical testing.

## Updating and verification

- Android app ID is `com.tranquil.ps5remoteplay`. This update uses version code 14 and requires the same signing certificate as 0.1.12. Android associates existing pairings and preferences with this package.
- PlayStation pairing, controller input, off-network streaming, and the upgrade flow still need a physical phone and console test for this release.
- The source archive includes the pinned Chiaki-ng tree, its submodules, license notices, and the patches and scripts used to build VYNUVO.

[VYNUVO source and upstream attribution](UPSTREAM.md)
