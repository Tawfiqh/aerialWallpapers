#!/bin/bash

mkdir resources;
cd resources;

# Download tvOS13 wallpapers
curl https://sylvan.apple.com/Aerials/resources-13.tar > resources.tar && tar xopf resources.tar && mv entries.json tvOS13.json && rm -rf TVIdleScreenStrings.bundle; rm resources.tar

# Download tvOS12 wallpapers
curl https://sylvan.apple.com/Aerials/resources.tar > resources.tar    && tar xopf resources.tar && mv entries.json tvOS12.json && rm -rf TVIdleScreenStrings.bundle; rm resources.tar;

# Download tvOS11 wallpapers
curl https://sylvan.apple.com/Aerials/2x/entries.json > tvos11.json;

# Download tvOS10 wallpapers
curl http://a1.phobos.apple.com/us/r1000/000/Features/atv/AutumnResources/videos/entries.json > tvos10.json
