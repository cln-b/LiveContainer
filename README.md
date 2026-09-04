<div align="center">
   <img width="217" height="217" src="./screenshots/livecontainer_icon.png" alt="Logo">
</div>
   

<div align="center">
  <h1><b>LiveContainer</b></h1>
  <p><i>An app launcher that runs iOS apps without actually installing them! </i></p>
</div>
<h6 align="center">

Crowdin Project: [![Crowdin](https://badges.crowdin.net/livecontainer/localized.svg)](https://crowdin.com/project/livecontainer) &nbsp;| &nbsp; Documentation:[liveconainer.github.io](https://livecontainer.github.io/docs/intro)

# LiveContainer

- Fork of LiveContainer built with SideStore Nightly.

> [!CAUTION]
> **Important Notice Regarding Third-Party Builds of LiveContainer**
>
> We have recently noticed the appearance of certain closed-source third-party builds of LiveContainer. Please be aware that all your apps are installed within LiveContainer, which means these third-party builds **have full access to your data, including sensitive information such as keychain items and login credentials**. 
> 
> Furthermore, please note that we do not provide any support for issues of these third-party builds.


# Installation
**LiveContainer comes with a standalone version and a version with built-in SideStore. [Please read the install guide here](https://livecontainer.github.io/docs/installation)**

If you encounter any issue please [read our FAQ here](https://livecontainer.github.io/docs/faq)

### LiveContainer+SideStore
<table>
<tr>
<th colspan="2">
Nightly
</th>
</tr>
<tr>
<td>
<a href="https://stikstore.app/altdirect/?url=https://github.com/cln-b/LiveContainer/releases/download/latest/apps_nightly.json&exclude=livecontainer" target="_blank">
   <img src="https://raw.githubusercontent.com/StikStore/altdirect/refs/heads/main/assets/png/AltSource_Blue.png" alt="Add AltSource" width="200"/>
</a>
</td>
<td>
<a href="https://github.com/cln-b/LiveContainer/releases/download/latest/LiveContainer.ipa" target="_blank">
   <img src="https://raw.githubusercontent.com/StikStore/altdirect/refs/heads/main/assets/png/Download_Blue.png" alt="Download .ipa" width="200"/>
</a>
</td>
</tr>
</table>


## License
[GNU Affero General Public License v3.0](https://github.com/LiveContainer/LiveContainer/blob/main/LICENSE)

## Credits
- [xpn's blogpost: Restoring Dyld Memory Loading](https://blog.xpnsec.com/restoring-dyld-memory-loading)
- [LinusHenze's CFastFind](https://github.com/pinauten/PatchfinderUtils/blob/master/Sources/CFastFind/CFastFind.c): [MIT license](https://github.com/pinauten/PatchfinderUtils/blob/master/LICENSE)
- [litehook](https://github.com/opa334/litehook): [MIT license](https://github.com/opa334/litehook/blob/main/LICENSE)
- @haxi0 & @m1337v for icon
- @Vishram1123 for the initial shortcut implementation.
- @hugeBlack for SwiftUI contribution
- @Staubgeborener for automatic AltStore/SideStore source updater
- @fkunn1326 for improved app hiding
- @slds1 for dynamic color feature
- @Vishram1123 for iOS 26+ JIT Script Support
- @StephenDev0 for AltStore source support
