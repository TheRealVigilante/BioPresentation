import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "pgc-mdd2025_no23andMe_div_v3-49-46-01.tsv.gz"

# ----------------------------------------------------
# 1. Define expected columns manually (based on PGC MDD GWAS schema)
# ----------------------------------------------------
column_names = [
    "CHR",        # Chromosome
    "BP",         # Base-pair position
    "SNP",        # rsID
    "A1",         # Effect allele
    "A2",         # Other allele
    "BETA",       # Effect size
    "SE",         # Standard error
    "PVAL",       # p-value
    "FRQ_A1",     # Frequency of A1 in cases
    "FRQ_U",      # Frequency in controls
    "INFO",       # Imputation info
    "N",          # Sample size or effective N
    "NMISS",      # Missing count
    "N_TOTAL",    # Total samples
    "QC",         # QC flag
    "GENPOS",     # Genetic position
    "RSQ"         # Imputation R² or similar
]

# Load with manual headers
df = pd.read_csv(
    file_path,
    sep='\t',
    compression='gzip',
    names=column_names,
    comment='#',
    header=None,
    low_memory=False
)

print(f"✅ Loaded {len(df):,} variants with proper headers.")
print(df.head())

# ----------------------------------------------------
# 2. Filter significant SNPs (p < 5e-8)
# ----------------------------------------------------
sig_threshold = 5e-8
significant_snps = df[df['PVAL'] < sig_threshold].copy()

print(f"\n🧬 Significant SNPs (p < {sig_threshold}): {len(significant_snps):,}")

# ----------------------------------------------------
# 3. (Optional) Manhattan plot
# ----------------------------------------------------
df['-log10(P)'] = -np.log10(df['PVAL'])
plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=df.sample(min(500000, len(df))),  # sample for faster plotting
    x='BP',
    y='-log10(P)',
    hue='CHR',
    palette='tab20',
    s=5,
    linewidth=0
)
plt.axhline(-np.log10(sig_threshold), color='red', linestyle='--', label='Genome-wide significance')
plt.legend()
plt.title('Manhattan Plot - Depression GWAS (PGC MDD)')
plt.xlabel('Chromosome Position (BP)')
plt.ylabel('-log10(p-value)')
plt.tight_layout()
plt.show()

# ----------------------------------------------------
# 4. Save significant SNPs
# ----------------------------------------------------
significant_snps.to_csv("significant_snps_depression.tsv", sep='\t', index=False)
print("\n💾 Saved significant SNPs to 'significant_snps_depression.tsv'")
