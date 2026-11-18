# DAX measures

Create these measures in Power BI Desktop. Use **Modeling → New measure**, or right-click the table → **New measure**. Put them all in a dedicated **`_Measures`** table, made with **Home → Enter data** (one empty column, named `_Measures`). That keeps them together and easy to find.

The table names assume you loaded the CSV files under these names:
* `heart_disease_clean`
* `factor_ranking`
* `data_quality_log`
* `data_dictionary`

---

## 1. Core KPIs

```DAX
Total Patients = COUNTROWS ( heart_disease_clean )
```

```DAX
Disease Cases = SUM ( heart_disease_clean[heart_disease] )
```

```DAX
No Disease Cases = [Total Patients] - [Disease Cases]
```

```DAX
Disease Rate = DIVIDE ( [Disease Cases], [Total Patients] )
```
Format: **Percentage, 0 decimals**.

```DAX
Overall Disease Rate =
CALCULATE ( [Disease Rate], REMOVEFILTERS ( heart_disease_clean ) )
```
This is the reference value for every chart. It ignores slicers and the chart's own grouping.

```DAX
Rate vs Overall (pts) = ( [Disease Rate] - [Overall Disease Rate] ) * 100
```
Format: **Decimal, 1 place**. Use it for conditional formatting: red above 0, slate below.

---

## 2. Patient profile

```DAX
Median Age = MEDIAN ( heart_disease_clean[age] )
```

```DAX
% Male =
DIVIDE (
    CALCULATE ( [Total Patients], heart_disease_clean[sex] = "Male" ),
    [Total Patients]
)
```

```DAX
% Female = 1 - [% Male]
```

```DAX
Avg Max Heart Rate = AVERAGE ( heart_disease_clean[max_heart_rate] )
```

```DAX
Avg Cholesterol = AVERAGE ( heart_disease_clean[cholesterol] )
```

```DAX
Avg Resting BP = AVERAGE ( heart_disease_clean[resting_bp] )
```

---

## 3. Risk segmentation (Business Problem 10)

```DAX
High Risk Patients =
CALCULATE ( [Total Patients], heart_disease_clean[risk_tier] = "High" )
```

```DAX
High Risk Share of Patients = DIVIDE ( [High Risk Patients], [Total Patients] )
```

```DAX
High Risk Share of Cases =
DIVIDE (
    CALCULATE ( [Disease Cases], heart_disease_clean[risk_tier] = "High" ),
    [Disease Cases]
)
```
This is the headline insight: *the High tier holds 62% of all cases in 30% of patients.*

```DAX
Share of All Cases =
DIVIDE (
    [Disease Cases],
    CALCULATE ( [Disease Cases], REMOVEFILTERS ( heart_disease_clean[risk_tier] ) )
)
```
Put it in a table next to `risk_tier` to show each tier's share of all disease cases.

```DAX
Avg Warning Signs = AVERAGE ( heart_disease_clean[warning_signs] )
```

---

## 4. Labels and titles

```DAX
Rate Label =
FORMAT ( [Disease Rate], "0%" ) & "  (n=" & [Total Patients] & ")"
```
Use it as a custom data label: **Data labels → Value → Field → Rate Label**. It shows the rate and the group size together.

```DAX
Selection Title =
VAR _sex = IF ( ISFILTERED ( heart_disease_clean[sex] ), SELECTEDVALUE ( heart_disease_clean[sex], "Mixed" ), "All patients" )
VAR _age = IF ( ISFILTERED ( heart_disease_clean[age_group] ), " · Age " & SELECTEDVALUE ( heart_disease_clean[age_group], "multiple groups" ), "" )
RETURN _sex & _age & " · " & FORMAT ( [Total Patients], "0" ) & " patients"
```
Use it in a card, or as a dynamic title (**Title → fx**), so viewers always know which filters are active.

```DAX
Key Insight =
"Disease rate " & FORMAT ( [Disease Rate], "0%" ) &
" vs overall " & FORMAT ( [Overall Disease Rate], "0%" )
```

---

## 5. Data quality page

```DAX
Issues Found = COUNTROWS ( data_quality_log )
```

```DAX
Unknown Vessel Results =
CALCULATE ( [Total Patients], heart_disease_clean[vessels_label] = "Unknown" )
```

```DAX
Unknown Thallium Results =
CALCULATE ( [Total Patients], heart_disease_clean[thallium_result] = "Unknown" )
```

---

## Sort order setup (do this once)

Power BI sorts text alphabetically by default, which would put "70+" before "Under 40". Fix it for each column below:

1. In **Table view**, select the column.
2. Go to **Column tools → Sort by column**.
3. Pick the matching `_order` column.

| Column | Sort by |
|---|---|
| `age_group` | `age_group_order` |
| `bp_category` | `bp_category_order` |
| `cholesterol_category` | `cholesterol_category_order` |
| `max_hr_band` | `max_hr_band_order` |
| `st_depression_band` | `st_depression_band_order` |
| `chest_pain_type` | `chest_pain_type_order` |
| `resting_ecg` | `resting_ecg_order` |
| `st_slope` | `st_slope_order` |
| `thallium_result` | `thallium_result_order` |
| `risk_tier` | `risk_tier_order` |

In the `factor_ranking` table, sort `factor` by `rank`.
