CREATE TABLE geneinfo (
    tax_id          int,            -- The unique identifier provided by NCBI
                                    -- Taxonomy for the species or
                                    -- strain/isolate
    gene_id         int,            -- The unique identifier for the gene
    symbol          varchar(255),   -- The default symbol for the gene
    locusTag        varchar(255),   -- The LocusTag value
    synonyms        varchar(255),   -- Bar-delimited set of unofficial symbols 
                                    -- for the gene
    dbxrefs         varchar(255),   -- Bar delimited set of identifiers in other
                                    -- databases for this gene; in the form
                                    -- database:value
    chromosome      varchar(255),   -- The chromosome on which this
                                    -- gene is placed.  For mitochondrial
                                    -- genomes, the value 'MT' is used.
    map_location    varchar(255),   -- The map location for this gene
    description     varchar(255),   -- Descriptive name of the gene
    type_of_gene    varchar(255),   -- Type assigned to the gene; one of 
                                    -- unknown, tRNA, rRNA, snRNA, scRNA,
                                    -- snoRNA, protein-coding, pseudo,
                                    -- transposon, miscRNA, ncRNA or other
    nom_symbol      varchar(255),   -- When not '-', indicates that this symbol
                                    -- is from a nomeclature authority
                                    -- is from a nomeclature authority
    fullname        varchar(255),   -- When not '-', indicates that this full 
                                    -- name if from a nomenclature authority
    nom_status      char(255),      -- When not '-', indicates the status of the
                                    -- name of the nomenclature authority (0 for
                                    -- official, I for iterim)
    other_desig     varchar(255),   -- Pipe-delimited set of some alternate
                                    -- descriptions that have been assigned to a
                                    -- GeneID; '-' indicates that none is being
                                    -- reported
    mod_date   int                  -- The last date a gene record was updated,
                                    -- in YYYYMMDD format
);
