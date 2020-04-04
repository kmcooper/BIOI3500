###
#
#
#
# DO NOT FORGET TO ADD IN YOUR HONOR PLEDGE AND PROGRAM DESCRIPTION!
#
#
##
# This program will take a list of symbols and look up the gene ID, taxonomy ID,
# accession numbers (RNA, protein and genomic) and PubMed IDs for symbol.

# Do the imports
import sys        # for reading files, exit, and stuff
import getopt     # for command line arguments
import io         # stuff for opening files (for us at least)
import MySQLdb   # Our database plugin

# Function name: usage()
# Parameters: None
# Return value(s): None
# Description: Displays usage information
def usage():
    print("Usage: ", sys.argv[0]," [-i INFILE] [-o OUTFILE] ")
    print("-i: Specifies the name of the input file. If this option " \
          "is not given, output will be taken from standard input (i.e., the "\
          "keyboard)")
    print("-o: Specifies the name of the output file. If this option is " \
          "not given, output will be sent to standard output (i.e., the " \
          "screen)")

def main():

    # Define our variables
    inFile = ""                 # File to be read, if there is one
    outFile = ""                # Outfile to write to, if there is one
    inFile = sys.stdin          # File name for input; defaults
                                # to standard input
    outFile = sys.stdout        # File name for output; defaults
                                # to standard output
    outputString = ""           # Output string
    symbol = ""                 # Gene symbol
    rnaAccess = ""              # holds our ran accessions
    proAccess = ""              # Holds our protein accessions
    genAccess = ""              # holds our genomic accessions
    pubMeds = ""                # holds our pubmed IDs
    geneID = ""                 # the gene ID for the symbol
    taxID = ""                  # holds the tax id for the symbol

    # Process command-line options
    # e.g., python3 FASTAToTab.py -i input.fna -o output.tab
    #
    # If there are issues, program prints output to std.err, 
    # prints usage and error statements, and exits
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:")
    except getopt.GetoptError as err:
        sys.stdout = sys.stderr
        print(str(err))
        usage()
        sys.exit(2)

    # Parse command line options
    for (opt, arg) in opts:
        if opt == "-i":
            inFile = open(arg, 'r') 
        elif opt == "-o":
            outFile = open(arg, 'w')

    # Get a connection (throws an exception if a connection cannot be made)
    # 
    # You need to connect to your database - mine will not work for you
    conn = MySQLdb.connect(db="kmcooper") 
    
    # Create a cursor to execute queries on the MySQL database
    cursor = conn.cursor()
 
    # Read in first line of file 
    line = inFile.readline()
    while (line):
        # Each line in the file is a gene
        symbol = line.rstrip()
        print("Now processing: " + symbol)

    
        # Here you should write a SELECT query that finds for the gene ID and the
        # Taxonomy ID by searching for the symbol in the GeneInfo table. 
        query = "Your query goes here";
        print("Query for testing on your MySQL database is: ",query)
        
        # Uncomment the line below to execute the query once you have formed it
        #cursor.execute(query)

        # Get results
        rows = ''
        #rows = cursor.fetchall()

        # No results for the gene
        if not rows:
            #You will need to change the line below to match my output
            outFile.write(symbol + "Not found\n")

        # Iterate over the rows (if rows is empty, this loop will be skipped)
        for row in rows:
        
            # Clear the output string and write the symbol to it
            # This corresponds to the line in the Assignment:
            # "
            outputString = symbol + "\t"

            # Get the gene ID and tax ID 
            geneID = str(row[0])
            taxID = str(row[1])

            # Clear the output strings
            rnaAccNos = ""
            pubmedIDs = ""

            # Get all of the RNA accession numbers
            cursor.execute("SELECT DISTINCT (rna_accession) FROM " + \
                           "gene2refseq WHERE gene_id = " + geneID + \
                           " ORDER BY rna_accession ASC;")
            accRows = cursor.fetchall()

            # Iterate over the rows
            for accRow in accRows:
                if ("None" not in str(accRow[0])):
                    rnaAccNos = rnaAccNos + str(accRow[0]) + "|"

            # Remove the last pipe
            rnaAccNos = rnaAccNos[ : -1]
            
            ########################
            # Get all of the pubmed ids
            #
            # You will need to develop the code for grabbing 
            # pubmed IDs below. Use the RNA accession code as a guide
            #
            ###########################
    
            # Get all of the Pubmed IDs with a query
            # Iterate over the rows
            # Remove the last pipe symbol with a slice

            # If after all this processing these items are blank, fill them
            # If they are blank, we need to replace them with a -.
            if not geneID:
                geneID = "-"
            if not taxID:
                taxID = "-"
            if not rnaAccNos:
                rnaAccNos = "-"
            if not pubmedIDs:
                pubmedIDs = "-"

            # Create output string
            outputString = outputString + geneID + "\t" + taxID + "\t" + \
                           rnaAccNos + "\t" + pubmedIDs + "\n"

            # Output
            outFile.write(outputString)

        # Read in next gene symbol
        line = inFile.readline()

    # Close our handles, wherever they point to
    inFile.close()
    outFile.close()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()

