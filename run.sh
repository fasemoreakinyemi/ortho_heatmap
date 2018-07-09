#!/usr/bin/bash

main(){
#	single_locus_plot
	multiple_locus_plot
}

single_locus_plot(){
python \
	ortho_heatmap.py \
	--orthologue_csv ./orthologueList.csv \
	--locus_tag b0004 \
	--out_plot single_locus_plot.pdf
}

multiple_locus_plot(){
python \
	ortho_heatmap.py \
	--orthologue_csv ./orthologueList.csv \
       --locus_tag b001 b0005 b0033 b0026 b0094 b0024 b0025 b0026 b0030 b0031 b0032 b0034 b0114 b0149 b0150 b0156 b0210 b0211 b0456 \
	--out_plot multiple_locus_plot.pdf
}
main
