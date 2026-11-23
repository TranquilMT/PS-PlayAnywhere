# VYNUVO 0.1.17 • In-app Xbox player

Tap Xbox Cloud Gaming in the hub to open Microsoft's cloud library directly in VYNUVO. Sign-in, game selection and the streaming page use the same embedded Android WebView. Xbox access still depends on your Microsoft account, region and game entitlements.

- The APK includes redphx’s full open-source Better xCloud 6.7.13 userscript. VYNUVO loads it at document start on the supported Xbox play and sign-in callback routes. The Android companion and browser extension are no longer needed.
- Better xCloud provides its own on-page settings on compatible pages. Its support for the newer play.xbox.com preview differs from the classic www.xbox.com/play experience. The new site can load in the player, but this release applies the enhancements only on the upstream-supported site.
- The player remembers its web sign-in and preferences. Full screen hides the VYNUVO toolbar and system bars. Android Back exits full screen, then navigates web history. Hub closes the player.
- Loading progress and a connection retry action are built into the player. An older Android System WebView without document-start support displays an update message.
- The Android host is VYNUVO’s own implementation. Upstream Android companion-only integrations such as native mouse capture and native vibration are outside this build. Voice chat is not enabled.
- PlayStation retains the native Chiaki engine. PC / Steam remains Coming soon.
- Version code 18 retains the original package and update certificate. The full source archive includes the pinned Better xCloud sources and MIT notices. Signed-in gameplay, latency and controller behavior still require device verification.
