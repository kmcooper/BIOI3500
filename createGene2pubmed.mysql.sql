CREATE TABLE gene2pubmed (
    tax_id          int,            -- The unique identifier provided by NCBI 
                                    -- Taxonomy for the species or 
                                    -- strain/isolate
    gene_id         int,            -- The unique identifier for the gene
    pubmed_id       int             -- The unique identifier in PubMed for a 
                                    -- citation
);
