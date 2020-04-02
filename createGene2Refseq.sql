CREATE TABLE gene2refseq (
        tax_id INTEGER NOT NULL,
        gene_id INTEGER NOT NULL,
        status TEXT,
        rna_accession TEXT,
        rna_gi INTEGER,
        protein_accession TEXT,
        protein_gi INTEGER,
        genomic_dna_accession TEXT,
        genomic_dna_gi INTEGER,
        genomic_start INTEGER,
        genomic_end INTEGER,
        orientation TEXT,
        assembly TEXT,
	      mature_peptide_accession TEXT,
	      mature_peptide_gi INTEGER,
        default_gene_symbol TEXT
);
