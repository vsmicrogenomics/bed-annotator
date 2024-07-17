import pandas as pd
import requests

# Function to query Ensembl API for GRCh37
def query_ensembl(chrom, start, end):
    server = "https://grch37.rest.ensembl.org"
    ext = f"/overlap/region/human/{chrom}:{start}-{end}?feature=gene;content-type=application/json"
    headers = {"Content-Type": "application/json"}
    response = requests.get(server + ext, headers=headers)
    
    if not response.ok:
        response.raise_for_status()
    
    return response.json()

# Load BED file
file_path = 'ProbesGL.bed'
bed_data = pd.read_csv(file_path, sep='\t', header=None, names=['chrom', 'start', 'end'])

# Prepare a DataFrame to store annotations
annotations = []

for index, row in bed_data.iterrows():
    chrom = row['chrom'].replace('chr', '')
    start = row['start']
    end = row['end']
    
    if chrom.isdigit() or chrom in ['X', 'Y', 'MT']:
        print(f"Querying for {chrom}:{start}-{end}")
        
        try:
            result = query_ensembl(chrom, start, end)
            
            if result:
                for gene in result:
                    gene_start = gene.get('start')
                    gene_end = gene.get('end')
                    gene_name = gene.get('external_name', 'N/A')  # Safely get the external_name
                    
                    annotations.append([row['chrom'], start, end, gene_start, gene_end, gene_name])
            else:
                annotations.append([row['chrom'], start, end, None, None, None])
        except requests.exceptions.HTTPError as e:
            print(f"HTTPError for {chrom}:{start}-{end}: {e}")
            annotations.append([row['chrom'], start, end, None, None, None])
        except Exception as e:
            print(f"Error for {chrom}:{start}-{end}: {e}")
            annotations.append([row['chrom'], start, end, None, None, None])
    else:
        print(f"Invalid chromosome: {chrom}")
        annotations.append([row['chrom'], start, end, None, None, None])

# Create a DataFrame from annotations
annotated_bed = pd.DataFrame(annotations, columns=['chrom', 'start', 'end', 'gene_start', 'gene_end', 'gene_name'])

# Save the annotated BED file
annotated_bed.to_csv('Annotated_Probe.bed', sep='\t', index=False)
print("Annotated BED file saved as 'Annotated_Probe.bed'.")
