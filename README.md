# AWS Redshift Serverless Data Warehouse (Demo)

This project builds a **star‑schema data warehouse** in **Amazon Redshift Serverless** and loads it with song & event log data stored in **S3**.  
All setup is automated with lightweight Python scripts (no GUI wizards after initial cluster creation).

---

## Tech Used
- **Amazon Redshift Serverless** (4 RPUs, `us‑east‑1`)
- **AWS IAM** role with S3 read‑only access
- **AWS S3** public bucket `udacity‑dend` (`us‑west‑2`)
- **Python 3** + `psycopg2‑binary`
- **WSL Ubuntu** as run environment

---

## What It Does

| Stage | Action |
|-------|--------|
| **1 — Infrastructure** | Creates workgroup **`redshift-demo-wg`** + namespace **`redshift-demo-ns`**, publicly accessible, IAM role attached. |
| **2 — Staging** | Two COPY commands load ~500 MB of JSON logs & song data from S3 (cross‑region). |
| **3 — Warehouse** | Builds star schema (`songplays` fact + 4 dims) and inserts ~11 k rows. |
| **4 — Validation** | Row counts verified in Query Editor v2. |
| **5 — Teardown** | Deletes workgroup & namespace to avoid charges (promo credit untouched). |

---

## Project Structure
```text
redshift-dw/
├── create_tables.py      # DDL script
├── etl.py                # COPY + INSERTs
├── sql_queries.py        # All SQL strings
├── dwh.cfg               # Endpoint / creds / IAM ARN
├── .gitignore            # venv/ and *.cfg excluded
├── images/               # screenshots
│   ├── 1. Redshift Role Screenshot.png
│   ├── 2. Set associate IAM role.png
│   ├── 3. Namespace and workgroup available.png
│   ├── 4. Songplay row query.png
│   └── 5. ETL terminal success.png
└── README.md
```

---
## How to Run

``` Bash
# Clone project and set up environment
git clone https://github.com/k-idem/redshift-dw.git
cd redshift-dw
python3 -m venv venv
source venv/bin/activate
pip install psycopg2-binary

# Configure dwh.cfg
# Fill in your Redshift workgroup endpoint, admin password, and IAM role ARN
nano dwh.cfg

# Run the setup and ETL scripts
python create_tables.py
python etl.py
```
---

## Validate the Load

After `python etl.py` finishes:

1. **AWS Console** → **Amazon Redshift**.  
2. Click **Query data** (upper‑right) to open **Query Editor v2**.  
3. In the connect dialog choose:  
   - **Connection type**: *Amazon Redshift Serverless*  
   - **Workgroup**: `redshift-demo-wg`  
   - **Database**: `dev`  
   - **Authentication**: *Federated user* **or** *Database user & password* (`admin` / your password)  
4. Paste and run:

   ```sql
   SELECT COUNT(*) AS songplay_rows FROM songplays;

## Cleanup
Delete the workgroup and namespace from the Serverless dashboard
 (Actions → Delete workgroup → “Also delete namespace”).


---
## Screenshots
* [Redshift IAM Role Created](images/1. Redshift Role Screenshot.png)
* [IAM Role Attached to Namespace](images/iam_role_attached_to_namespace.png)
* [Workgroup and Namespace Available](images/workgroup_namespace_available.png)
* [Songplays Query in Query Editor v2](images/query_editor_songplays.png)
* [ETL Pipeline Success in Terminal](images/terminal_etl_success.png)

---

## Author

Kenneth Idem  
[github.com/k-idem](https://github.com/k-idem)
