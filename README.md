# Olist Brazilian E-Commerce Data Analysis

## Project Overview

Analyzed the Olist Brazilian e-commerce dataset using Python and Pandas, focusing on dataset quality, relational joins, order-level financial aggregation, and reconciliation of recorded item and payment amounts.

## Problem Statement

E-commerce datasets contain multiple related tables with different row-level grains. Directly joining order items and payments can duplicate records and inflate financial totals. The analysis investigates these relationships and validates order-level results.

## Objectives

- Inspect nine related e-commerce datasets.
- Validate order identifiers and required financial columns.
- Aggregate order items and payments before joining.
- Prevent financial double counting.
- Investigate unmatched orders and missing payment records.

## Technologies Used

- Python
- Pandas
- Jupyter Notebook
- JSON

## Project Structure

- data/
- notebooks/
- reports/
- sql/
- src/

## Dataset or Input Sources

- Olist, Brazilian E-Commerce Public Dataset by Olist, Kaggle: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce (source dataset license: CC BY-NC-SA 4.0).


## Environment and Prerequisites

Locally tested with Python 3.14, Pandas 3.0.6, Jupyter Notebook Classic and the registered 'Python (Olist Data Engineering)' kernel. The analysis was tested locally; a completely independent environment reproduction has not yet been verified.

## Installation and Setup

Obtain the nine Olist CSV datasets and place them in `data/raw/`. Select the Python kernel associated with your configured environment.

## How to Run

Open `notebooks/01_olist_data_exploration_publication_v2.ipynb` in Jupyter Notebook Classic. This is the published notebook containing saved results from a verified local execution. Download the source datasets and configure your environment before re-running it.

## Methodology and Implementation

Loaded CSV datasets into Pandas DataFrames, identified table grain and relationship keys, aggregated order items and payments by order_id, performed validated left joins, and compared aggregated financial totals against their original source DataFrames.

## Testing and Validation

- Row-count and primary-key uniqueness assertions.
- Required-column and numeric-data-type checks.
- One-to-one merge validation.
- Financial-total reconciliation with a 0.01 tolerance.
- Order-status investigation of unmatched records.

## Results and Key Findings

- Validated 99,441 unique order-level financial rows. (Evidence: Jupyter Pandas validation confirmed that len(order_financials) == len(orders) == 99441 and order_financials.order_id is unique.)
- Reconciled recorded item prices totaling R$13,591,643.70. (Evidence: Aggregated item_price_total matched the original order_items.price sum within 0.01.)
- Reconciled recorded payments totaling R$16,008,872.12. (Evidence: Aggregated payment_total matched the original payments.payment_value sum within 0.01.)
- Identified 775 orders without matching item records. (Evidence: Left-join analysis identified 603 unavailable, 164 canceled, 5 created, 2 invoiced, and 1 shipped order without matching item records.)
- Identified one delivered order without a matching payment record. (Evidence: The unmatched delivered order contained three item records, R$134.97 in item prices, and R$8.49 in freight, with payment_total missing.)
- Successfully executed the corrected 212-cell Olist notebook from a fresh kernel with 116 executed code cells and zero recorded errors. (Evidence: The publication V2 notebook was validated with nbformat. Execution counts confirmed 116 completed code cells and zero error outputs. Financial validation messages and totals were reproduced.)


## Limitations

- The notebook underlying publication V2 completed clean-kernel execution in the local Olist environment using nine source CSV datasets. Reproduction elsewhere requires obtaining the datasets and configuring the required Python environment.
- Financial amounts represent recorded item prices and payments, not necessarily recognized revenue or profit.
- Missing payment records do not establish that an order was unpaid.
- Unmatched relationships require business-context review.
- Source datasets remain outside the portfolio staging repository.

## Future Improvements

- Add an automated clean-kernel execution test to the project validation workflow.
- Add reproducible analytical reports.
- Expand order-status and delivery-performance analysis.
- Improve automated testing and documentation for future releases.

## GitHub and Portfolio Presentation

Published repository: https://github.com/essoun/olist-ecommerce-analysis

## Acknowledgments and Data Attribution

- Olist, Brazilian E-Commerce Public Dataset by Olist, Kaggle: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce (source dataset license: CC BY-NC-SA 4.0).

## License

A license for the original project code has not yet been selected. The source dataset has separate licensing terms.

---

## Reproducing the Published Analysis

The verified portfolio notebook is:

`notebooks/01_olist_data_exploration_publication_v2.ipynb`

### Environment setup

Use Python 3.14 and create a virtual environment.

Run these commands from the repository root:

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `python -m pip install -r requirements.txt`

Install or launch a compatible Jupyter Notebook application.
Select the environment's Python kernel.

### Obtain the dataset

Download the Brazilian E-Commerce Public Dataset by Olist:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Extract the nine original CSV files into `data/raw/`.

Validate the extracted files using:

`python src/validate_olist_files_portable_v2.py`

The original ZIP archive is optional.

The original datasets are not included in this repository.
A local symbolic link was used during development,
but a normal `data/raw/` directory can be used instead.

### Execute the analysis

Start Jupyter from the repository root, open the
publication notebook, and select the appropriate kernel.

Run the notebook from the beginning.

Saved outputs document a previously verified execution.
Re-execution may produce environment-dependent differences.
