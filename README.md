# BED File Annotator

This script annotates a BED file with gene information using the Ensembl REST API. It is specifically designed to work with human genome build GRCh37 (hg19).

## Prerequisites

- Python 3.7 or higher
- pandas
- requests

You can install the required Python packages using pip:

```sh
pip install pandas requests


## Usage
Clone the repository:

git clone https://github.com/vsmicrogenomics/bed-annotator.git
cd bed-annotator

Place your BED file (e.g., Probe.bed) in the same directory as the script.

Run the script:
python bed-annotator.py

The annotated BED file (Annotated_Probe.bed) will be generated in the same directory.

Example
Input BED file (Probe.bed):
chr1    10292379    10292499
chr1    10308880    10309000
chr1    10316282    10316402

Output Annotated BED file (Annotated_Probe.bed):
chrom   start       end         gene_start  gene_end    gene_name
chr1    10292379    10292499    10270863.0  10441661.0  KIF1B
chr1    10308880    10309000    10270863.0  10441661.0  KIF1B
chr1    10316282    10316402    10270863.0  10441661.0  KIF1B

## Script Details
The script reads a BED file, queries the Ensembl REST API for gene information, and writes the annotations back to a new BED file. The following information is added to each region in the BED file:

Gene start position
Gene end position
Gene name



## Acknowledgments
This script uses the Ensembl REST API to retrieve gene annotations. We thank the Ensembl team for providing this valuable resource.

## Citation

If you use this script for your research, please consider citing it as follows:
Sharma, V. (2024). bed-annotator.py [Python script]. Retrieved from https://github.com/vsmicrogenomics/bed-annotator
