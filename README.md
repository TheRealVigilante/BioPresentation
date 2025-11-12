# Does Depression come from our genetics: Bioinformatics Presentation

## Overview

This project investigates whether genetic variation contributes to the risk of depression by combining GWAS summary statistics, SNP-to‐gene mapping and pathway enrichment in a bioinformatics pipeline. The goal is to bridge raw genetic association data with biological pathways, offering insight into the genetic architecture of depression.

## Objectives

* Use summary statistics from a large-scale genome-wide association study (GWAS) of major depressive disorder (MDD).
* Map significant single nucleotide polymorphisms (SNPs) to their nearest genes using genomic coordinates.
* Perform gene set / pathway enrichment analysis to identify biological processes enriched among these genes.
* Interpret the findings to answer: *“Does depression come from our genetics?”*

## Study
The primary dataset for this analysis comes from the Psychiatric Genomics Consortium (PGC) – major depressive disorder (MDD) GWAS summary statistics.
You can access the dataset here:
- [Dataset (PGC MDD2025)](https://figshare.com/articles/dataset/GWAS_summary_statistics_for_major_depression_PGC_MDD2025_/27061255)
- [Paper (PGC MDD2025)](https://www.cell.com/cell/fulltext/S0092-8674(24)01415-6)

Use of this dataset is subject to [Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/)

## Methods

1. **Loading and QC**: Read the .tsv.gz summary statistics file, inspect key fields (CHR, BP, SNP, A1, A2, BETA, SE, PVAL, etc.).
2. **Significant SNP filtering**: Apply genome-wide significance threshold (e.g., p < 5×10⁻⁸) to identify risk SNPs.
3. **SNP → Gene mapping**: Using SNP chromosomal coordinates (CHR, BP) query the Ensembl REST API to retrieve the nearest or overlapping gene symbol.
4. **Gene list generation**: Extract unique gene symbols mapped from significant SNPs.
5. **Pathway enrichment**: Use the g:Profiler (or other enrichment tool) to identify GO terms, KEGG pathways, and biological processes that are statistically over-represented in the gene list.
6. **Interpretation**: Review the enriched pathways and gene set results in the context of neurobiology, synaptic signalling and depression risk.

## Results Summary

* A set of ~13,000 significant SNPs were mapped to nearest genes.
* A non-trivial number of unique genes emerged from the mapping, implicating genomic regions linked to depression risk.
* Pathway enrichment revealed that key processes such as **neuronal development**, **synapse organization**, **neurotransmitter signaling**, and **behavior/learning** were over-represented.
* These findings support a **genetic component** to depression, but do not imply genes alone determine depression risk.

## Interpretation & Conclusion

* Genetic variation matters: the identification of genome-wide significant SNPs and gene associations shows that *some portion* of depression risk is inherited.
* The polygenic nature: Many genes each contribute a small effect, rather than a single “depression gene”.
* Biological plausibility: The enriched pathways pertain to brain structure and function—consistent with depression being a disorder of neuronal circuits and signalling.
* But environment remains critical: While genetics provides susceptibility, factors like life stress, trauma, and environment trigger or modulate risk.

## How to reproduce

1. Place the GWAS summary file in your working directory (e.g., `pgc-mdd2025_summary.tsv.gz`).
2. Run the provided script `map_snps_to_genes.py` to map SNPs → genes (requires internet connection for Ensembl REST API).
3. Run `enrichment_analysis.py` to perform gene set enrichment (requires gprofiler-official Python package).
4. Review the generated outputs: `depression_SNP_gene_all.tsv`, `depression_pathway_enrichment.csv`.
5. Use `plots.ipynb` (Jupyter notebook) to visualize Manhattan plots, gene counts, and top pathways.

## Requirements

* Python 3.8 or higher
* pandas
* requests
* gprofiler-official
* Optional: matplotlib, seaborn for plotting

[1]: https://figshare.com/articles/online_resource/Supplementary_Results_for_GWAS_meta-analysis_of_major_depression_PGC_MDD2025_/27089614?utm_source=chatgpt.com "Supplementary Results for GWAS meta-analysis of major ..."
[2]: https://pgc.unc.edu/for-researchers/download-results/?utm_source=chatgpt.com "Download Results – PGC"
