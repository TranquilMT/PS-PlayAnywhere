# Connection help

Open **Settings → Connection help** in PS PlayAnywhere. Enter the WAN IPv4 address from your home router’s Internet or WAN status page. The app classifies the text on the device and does not save it.

| Router address | What to check |
| --- | --- |
| Shared address | An upstream device is using the shared IPv4 range commonly associated with carrier-grade NAT. Changes on your home router alone cannot open a path through that upstream NAT. |
| Private address | Check whether a second router or ISP gateway sits upstream. If you own both routers, read the WAN address on the device closest to the internet connection. A private address by itself cannot identify who operates the upstream router. |
| Special-use or invalid address | Verify that you copied the router’s WAN IPv4 address rather than its local management address, a hostname or an IPv6 address. |
| Outside common private and shared ranges | IPv4 addressing alone cannot establish whether the console is reachable. Verify a full session from a separate network. |

Pair and start a session on your home network while the console is awake. If the console wakes from rest but streaming fails, record wake and stream setup as separate results. For off-network testing, switch the phone to mobile data or another Wi-Fi network. Record whether pairing, wake, video and controls worked.

The home-network troubleshooting approach was adapted from [corecompiled/ps5-remote-play-anywhere](https://github.com/corecompiled/ps5-remote-play-anywhere). The [MIT license from the submitted archive](third-party/ps5-remote-play-anywhere-LICENSE.txt) is retained here.

## Play over 5G through a home VPN

Pair on home Wi-Fi first and leave the PS5 awake. Turn Wi-Fi off and connect a home VPN that gives your phone access to the PS5’s LAN. Choose Add Console Manually, enter the PS5’s LAN IP under Host, select your existing PS5 under Registered Console, then save and open the entry.

The VPN must route traffic to your home LAN through your router or an always-on device at home. A commercial VPN exit does not provide that route. Use the manual entry because local broadcast discovery may be unavailable across the VPN. Check video, audio and controls while the console is awake. Test wake from Rest Mode separately.

Automatic PSN discovery and off-network connection remain on the roadmap. The PSN Account ID lookup in the app is used for pairing.
