# Script Description
This python script creates a matplotlib heatmap of orthologues from an [orthologuedb](http://www.pathogenomics.sfu.ca/ortholugedb/?page=matrix-setup) generated table of inter-species orthologues

## Usage

``` python ortho_heatmap.py --orthologue_csv dowloaded_orthologues.csv --locus_tag b00004 (locus tag of genes to compare seperated by a space if multiple. However not more than 10 at once) --out_plot heat_plot.pdf (user supplied name of created plot) ```

## Note
 The locus tag ID should come from the reference genome. 
