# Data cleaning notes – Secure Boot Rollout: GP1 Coverage Check

Source: `data/raw/secure_boot_devices.csv`, `data/raw/laptop_refresh_new_hosts.csv`. Cleaning code: `notebooks/Project4_SecureBoot_Analysis_final.ipynb`, sections 2–3.

## Anonymisation (done before publishing)
Serial numbers inside host names are replaced with consistent fake codes. The site code and the 2-letter series prefix are kept, and the same real serial always gets the same fake one, also in the Laptop Lifecycle project, so the cross-check still works.

## What validation found
* **The file is a working sheet, not a table:** there are two note rows on top, the lists sit side by side, and column H holds a hand-made list. Each list is read separately.
* **Devices in scope: 73, GP1 members: 69.** No duplicates within either list, and no stray spaces or lower-case names, so an exact host-name match is safe.
* **One host name breaks the naming pattern:** `SAU-LT-PF59121C` has an extra dash. It still matches between the two lists.
* **The side list in column H has 6 entries for 4 devices** (2 are repeated).
* **The manual flag (column E) is blank for 1 device**, and it says `NOT ON GP1` 5 times while the lookup (column F) finds only 4 missing.

## Cleaning steps
1. Read the sheet with `header=None`, because the first two rows are notes, not headers.
2. Split the side-by-side columns into separate lists and drop empty cells.
3. Trim spaces before matching (none were found, but the check is cheap).
4. Extract the site code (first 3 letters) and hardware series (`LT-?` followed by 2 letters) from each host name.
5. Reconcile with an exact `isin()` match in both directions, then compare the result with the manual flag, the lookup and the side list.
