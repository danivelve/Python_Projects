# Data cleaning notes – UPS Monitoring Non-Compliance Audit

Source: `data/raw/apc_ups_sites.csv`. Cleaning code: `notebooks/Project6_NonCompliance_Analysis_final.ipynb`, sections 2–3.

## Anonymisation (done before publishing)
People's names (site contacts and technicians mentioned in the notes), internal IP addresses and UPS serial numbers are replaced with placeholders (`Person A`, `10.x.x.x`, fake serials). Sites, statuses, brands and model numbers are real.

## What validation found
* **The last row is a "total" row** (55 / 70), not a UPS. It is removed, leaving **71 UPS records at 52 sites**.
* **Two columns share the name "APC Connected"**: one has a hidden trailing space and holds Yes/No, the other holds a count. They are renamed `Connected_YesNo` and `Connected_Count`.
* **Item numbers:** 2 rows have no item number, and item `61` is used for 4 different UPS units at Weston.
* **The same status is spelt different ways** (`No Netwk Port` / `No Ntwk Port`, `Smart NtwkPort ` with a trailing space). They are standardised. 2 rows have no status.
* **Brand typo:** `APS` appears 17 times and is clearly APC (the model codes are APC's). It is corrected.
* **Values in the wrong column:** 3 Model Number cells hold an IP address, a technician's note or "unable to locate the data sheet" instead of a model code.
* **4 site codes are written in full** (`Blackfoot`, `EDMUNDSTON`, `SAULT STE MARIE`, `Yarmouth`) instead of 3 letters. They are shortened.
* **An empty column** at the end of the sheet is dropped.

## Cleaning steps
1. Read with `encoding="cp1252"` (saved from Excel on Windows).
2. Drop the `total` row at the bottom of the sheet.
3. Rename the two `APC Connected` columns (one has a hidden trailing space) **before** trimming column names, then drop the empty last column.
4. Trim every text value; merge `No Ntwk Port` into `No Netwk Port`; rename `Smart NtwkPort` to `Smart Netwk Port`; mark missing status as `Not recorded`.
5. Correct the brand typo `APS` to `APC`, and shorten the 4 site codes written in full.
6. Flag compliance (`Status == Online`) and map each non-compliant status to a reason and a fix.
7. Save the result to `data/processed/ups_sites_clean.csv`.
