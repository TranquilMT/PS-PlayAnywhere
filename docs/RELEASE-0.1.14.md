# VYNUVO 0.1.14 · Android preview

## Identity and motion

The launcher, toolbar and loading screens share a new folded V in violet and mint. On a fresh launch the mark turns into place, the wordmark and tagline rise, and a mint underline expands before the console hub appears. Settings, registration, manual console entry and streaming options have short entrance transitions. Custom motion respects Android’s animator setting.

## Loading and connection feedback

- Starting a PlayStation stream displays the VYNUVO connection screen while Chiaki reports that it is connecting. It clears as soon as the session connects, requests a PIN or reports an error. Reconnecting uses the same screen.
- Pairing displays a labeled progress indicator alongside the registration log. Success, failure and duplicate registrations use the existing result flow.
- PSN account lookup shows “Retrieving account ID…” while the request runs. The paste action returns when it completes.

## Updating

The APK uses Android package `com.tranquil.ps5remoteplay`, version code 15 and the existing VYNUVO signing identity. Xbox Cloud Gaming and PC / Steam remain Coming soon. Physical-device checks for the visual transitions, in-place upgrade and live console streaming are pending.
