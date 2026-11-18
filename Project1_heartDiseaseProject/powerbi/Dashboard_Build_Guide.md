# Power BI dashboard: step-by-step build guide

> **The finished dashboard is already in this folder:** `Heart_Disease_Dashboard_final.pbix`. This guide explains how it is designed. Use it to understand the build, or to rebuild the dashboard yourself as practice.

This guide builds a **4-page interactive dashboard** from the cleaned data. Plan on 2–3 hours if you are new to Power BI.

| Page | Purpose | Business problems |
|---|---|---|
| 1. Overview | Headline KPIs and patient profile | 2, 3, 4 |
| 2. Symptoms & tests | How each test separates patients | 5, 6, 7, 8 |
| 3. Risk drivers & tiers | What matters most and who to prioritise | 9, 10 |
| 4. Data quality | What was fixed and why the numbers can be trusted | 1 |

**You need:**
* **Power BI Desktop**, which is free from the Microsoft Store.
* The files in `data/processed/`. To create them, run `notebooks/01_Heart_Disease_Data_Analysis.ipynb` first.

---

## Step 1: Load the data

1. Open Power BI Desktop and go to **Home → Get data → Text/CSV**.
2. Load each of these files from `data/processed/`:
   * `heart_disease_clean.csv` (the main table)
   * `factor_ranking.csv`
   * `data_quality_log.csv`
   * `data_dictionary.csv`
3. In the preview, click **Transform data** to open Power Query and check the column types:

   | Column(s) | Type |
   |---|---|
   | `age`, `resting_bp`, `cholesterol`, `max_heart_rate`, `warning_signs`, `heart_disease`, `sign_*`, `*_order` | Whole number |
   | `st_depression`, `cramers_v`, `rate_gap_pts`, `p_value` | Decimal number |
   | `vessels_blocked` | Whole number (blanks are expected: unknown values) |
   | Everything else | Text |

4. Click **Close & Apply**.

> **Data model:** no relationships are needed. `factor_ranking` and `data_quality_log` are standalone summary tables. In **Model view**, check that Power BI did not auto-create any relationships, and delete any it made.

## Step 2: Apply the theme

Go to **View → Themes → Browse for themes** and choose `powerbi/Heart_Disease_Theme.json`. This applies the project colours:
* Red `#C8102E` = heart disease.
* Slate `#5B7083` = no heart disease.
* A light page background with white cards.

## Step 3: Set up sort order and measures

1. Set **Sort by column** for every banded column. The table is at the end of [`DAX_Measures.md`](DAX_Measures.md).
2. Create the `_Measures` table and every measure listed in [`DAX_Measures.md`](DAX_Measures.md).
3. Set the format of `Disease Rate`, `Overall Disease Rate`, `% Male`, `High Risk Share of Patients`, `High Risk Share of Cases` and `Share of All Cases` to **Percentage**.

## Step 4: Page canvas

1. Go to **Format page → Canvas settings** and choose **16:9 (1280 × 720)**.
2. Add a title bar at the top: **Insert → Shapes → Rectangle**, filled with dark `#3D0B17`.
3. Put a white text box on it, for example "Heart Disease Patient Analysis | Overview".
4. Copy this header onto each page and change the subtitle.

---

## Page 1: Overview

```
┌──────────────────────────────────────────────────────────────────────────┐
│  HEART DISEASE PATIENT ANALYSIS · Overview                    [Selection]│
├──────────┬──────────┬──────────┬──────────┬──────────┬───────────────────┤
│ Patients │ Disease  │ Disease  │ Median   │ % Male   │  SLICERS          │
│   302    │ cases 138│ rate 46% │ age 55.5 │  68%     │  Sex              │
├──────────┴──────────┴──────────┴──────────┴──────────┤  Age group        │
│ Diagnosis split   │ Disease rate by age group        │  Chest-pain type  │
│ (donut)           │ (column + overall line)          │  Risk tier        │
├───────────────────┼──────────────────────────────────┤                   │
│ Disease rate      │ Sex × age group matrix           │                   │
│ by sex (column)   │ (heatmap via conditional format) │                   │
└───────────────────┴──────────────────────────────────┴───────────────────┘
```

| Visual | Type | Fields | Formatting tips |
|---|---|---|---|
| 5 KPI cards | **Card (new)** | `Total Patients`, `Disease Cases`, `Disease Rate`, `Median Age`, `% Male` | Category label below the value; callout 28pt |
| Diagnosis split | **Donut chart** | Legend: `diagnosis`; Values: `Total Patients` | Colours: Heart disease red, No heart disease slate; detail labels = percent |
| Rate by age group | **Line and clustered column** | X: `age_group`; Column: `Disease Rate`; Line: `Overall Disease Rate` | Data labels on; line dashed and grey; Y-axis 0–100% |
| Rate by sex | **Clustered column** | X: `sex`; Y: `Disease Rate` | Data label: `Rate Label` measure |
| Sex × age | **Matrix** | Rows: `sex`; Columns: `age_group`; Values: `Disease Rate` | **Cell elements → Background colour → fx → Gradient**, white to red `#C8102E` |
| Slicers | **Slicer** (tile or dropdown) | `sex`, `age_group`, `chest_pain_type`, `risk_tier` | **Sync slicers** (View → Sync slicers) across pages 1–3 |
| Selection | **Card** | `Selection Title` | Top-right corner of the header |

**Insight text box:** "Almost half of referred patients (46%) have heart disease. Rates climb sharply after 50 and men are twice as affected as women (55% vs 25%)."

---

## Page 2: Symptoms & tests

```
┌──────────────────────────────────────────────────────────────────────────┐
│  HEART DISEASE PATIENT ANALYSIS · Symptoms & tests                       │
├────────────────────────────────┬─────────────────────────────────────────┤
│ Rate by chest-pain type        │ Stress test: rate by Max HR band        │
│ (bar — Asymptomatic highlight) │ Rate by Exercise angina                 │
├────────────────────────────────┤ Rate by ST depression band              │
│ Imaging: vessels narrowed      │ Rate by ST slope   (4 small multiples)  │
│ Imaging: thallium result       ├─────────────────────────────────────────┤
│                                │ Routine checks: BP / Cholesterol /      │
│                                │ Fasting sugar / Resting ECG             │
└────────────────────────────────┴─────────────────────────────────────────┘
```

| Visual | Type | Fields | Tips |
|---|---|---|---|
| Chest pain | **Clustered bar** | Y: `chest_pain_type`; X: `Disease Rate` | **Bars → Colour → fx → Rules**: red if `Rate vs Overall (pts)` > 0, otherwise slate |
| Stress test (×4) | **Clustered column** | X: `max_hr_band`, `exercise_angina`, `st_depression_band`, `st_slope`; Y: `Disease Rate` | Same size; sync Y-axis 0–100% |
| Imaging (×2) | **Clustered column** | X: `vessels_label` and `thallium_result`; Y: `Disease Rate` | Tooltip: add `Total Patients` |
| Routine checks (×4) | **Clustered column** | X: `bp_category`, `cholesterol_category`, `high_fasting_sugar`, `resting_ecg`; Y: `Disease Rate` | Grey colour (`#A9B8C4`) to show they matter less |
| Scatter (optional) | **Scatter** | X: `age`; Y: `max_heart_rate`; Legend: `diagnosis`; Values: `patient_id` | Shows max heart rate falling with age |

**Insight text box:** "Patients with no chest pain have the highest rate (73%). Stress-test and imaging results separate patients far better than blood pressure, cholesterol or blood sugar."

---

## Page 3: Risk drivers & tiers

```
┌──────────────────────────────────────────────────────────────────────────┐
│  HEART DISEASE PATIENT ANALYSIS · Risk drivers & tiers                   │
├──────────────────────────────────┬───────────────────────────────────────┤
│ Factor ranking (Cramér's V)      │ KPI: High-risk patients 92 (30%)      │
│ horizontal bar, colour = type    │ KPI: Share of cases in High tier 62%  │
│                                  ├───────────────────────────────────────┤
│                                  │ Disease rate by risk tier (column)    │
├──────────────────────────────────┼───────────────────────────────────────┤
│ Disease rate by # warning signs  │ Tier table: patients, cases, rate,    │
│ (column 0–6)                     │ share of all cases                    │
└──────────────────────────────────┴───────────────────────────────────────┘
```

| Visual | Type | Fields | Tips |
|---|---|---|---|
| Factor ranking | **Clustered bar** (from `factor_ranking`) | Y: `factor`; X: `cramers_v` (Don't summarize / Sum); Legend: `test_type` | Sort descending by `cramers_v`; tooltip: `rate_gap_pts`, `significant` |
| KPI cards | **Card** | `High Risk Patients`, `High Risk Share of Patients`, `High Risk Share of Cases` | |
| Rate by tier | **Column** | X: `risk_tier`; Y: `Disease Rate` | Data label `Rate Label` |
| Warning signs | **Column** | X: `warning_signs` (set to *Don't summarize*, axis type *Categorical*); Y: `Disease Rate` | |
| Tier table | **Table** | `risk_tier`, `Total Patients`, `Disease Cases`, `Disease Rate`, `Share of All Cases` | Data bars on `Disease Rate` |

**Insight text box:** "A simple count of six warning signs puts 62% of all disease cases into a High tier that is just 30% of patients. Book High-tier patients for a specialist review within days."

> Important: the factor ranking comes from the full dataset, so it does **not** change with slicers. Say so in a small subtitle: *"Calculated on all 302 patients."*

---

## Page 4: Data quality

| Visual | Type | Fields |
|---|---|---|
| Cards | **Card** | `Total Patients` (302 after cleaning), `Issues Found`, `Unknown Vessel Results`, `Unknown Thallium Results` |
| Issue log | **Table** | `data_quality_log`: `issue`, `rows_affected`, `action`, `note` |
| Data dictionary | **Table** | `data_dictionary`: `column`, `description` |
| Callout | **Text box** | "The raw file's outcome label was reversed (target = 1 meant *no* disease). It was confirmed against the UCI source and corrected before any analysis." |

---

## Step 5: Interactivity and finishing touches

1. **Tooltips:** add `Total Patients` and `Disease Cases` to every chart's tooltip well, so viewers see group sizes.
2. **Edit interactions** (Format → Edit interactions): stop the KPI cards from cross-filtering one another.
3. **Page navigation:** go to **Insert → Buttons → Navigator → Page navigator** and place it in the header.
4. **Alt text:** add alt text to each visual (**Format → General → Alt text**) for accessibility.
5. **Bookmarks (optional):** create "Men 50+" and "Women 50+" bookmarks to tell the screening story.
6. **Check it:** clear all slicers. The cards should show **302 patients, 138 cases and a 46% rate**, matching the notebook.

## Step 6: Save and share

1. Save as `powerbi/Heart_Disease_Dashboard.pbix`.
2. Export screenshots for the README:
   * Export each page with **File → Export → Export to PDF**, or take screenshots.
   * Save them as `images/dashboard_page1.png` to `dashboard_page4.png`.
3. Optional: **Publish** to the Power BI Service and use **File → Embed report → Publish to web** for a public portfolio link. Only do this for public data such as this dataset.
