# Data cleaning notes – Laptop Lifecycle: 2026 Refresh Programme Analysis

Source: `data/raw/laptop_lifecycle.csv`. Cleaning code: `notebooks/Project5_LaptopLifecycle_Analysis_final.ipynb`, sections 2–3.

## Anonymisation (done before publishing)
Names, emails, employee IDs, serial numbers, asset tags and tracking numbers are replaced with consistent fake values (`EMP0001`, `User 0001`, `user0001@example.com`, ...). Names typed into free-text cells are replaced with `Person X`. Locations, dates and statuses are real, and every typo and spacing problem is kept so the cleaning steps still have something to fix.

## What validation found
* **3 blank rows** at the bottom (one holds only a stray `1` in Reminder) are removed.
* **2 users are listed twice.** For one, the second row is an almost empty re-entry with a different location. For the other, it repeats the user with a different new asset tag and tracking number. The first record of each is kept.
* **Yes/no values are typed many ways:** `Yes`/`yes`/`YES`, `Updated`/`updated` and the typo `Upated`, plus stray values like `Check`, `Out`, `hello` and `ANA`. They are standardised to True/False; the stray values count as "not confirmed".
* **Dates have no year and come in five formats** (`29-Jul`, `19-Jun-26`, `June 17`, `8/19/2026`, `July 29th`). One keyed date is an Excel serial number (`46191`) and one is the word `No`. All are converted to 2026 dates, except `No`.
* **Tracking column problems:** 5 cells hold text instead of a tracking number (`King`, and a person's name). One tracking number is reused for **25 users in 6 different cities**, which can't be one shipment, so it is likely a copy-down error. In the old-laptop column, one cell holds a tracking number instead of Yes/No.
* **28 new host names skip the `LT` part** (e.g. `KST-SD…` instead of `KST-LTSD…`), and 23 new host names and 31 new serials have stray spaces. That will break exact matches in other systems, which is exactly what the Secure Boot project ran into.
* **The `Teams` column is completely empty.**

## Cleaning steps
1. Read with `encoding="cp1252"`, because the file was saved from Excel on Windows.
2. Strip stray spaces from column names (`New Serial `, `Reminder `).
3. Drop the 3 blank rows and keep the first record for each of the 2 users listed twice (518 users).
4. Turn each step into a True/False flag: trimmed, lower-cased, and counted as done only for yes / updated / upated / received / 1.
5. Count tracking columns only when they hold a real 12-digit number.
6. Read five date formats and add the missing year (2026); convert the Excel serial `46191`; leave `No` empty.
7. Derive the province from the location, including the home-based (WFH) entries.
8. Save the result to `data/processed/laptop_lifecycle_clean.csv`.
