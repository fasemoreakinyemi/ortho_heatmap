import argparse
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--orthologue_csv")
parser.add_argument("--locus_tag", nargs="+")
parser.add_argument("--out_plot")
args = parser.parse_args()

species_list = []
species_header = []

file = pd.read_csv(args.orthologue_csv)
num_species = np.arange(5, len(file.columns), 3)
print('The reference genome is from:', " ".join(file.columns[0].split()[0:2]))
print('The crossed genome(s) is/are from:')
for i in num_species:
    species_header.append(file.columns[i])
    species_list.append(" ".join(file.columns[i].split()[0:2]))
print(species_list)
species_header.insert(0,file.columns[1])
new_df = file[species_header]
wanted = new_df[new_df[new_df.columns[0]].isin(args.locus_tag)]
gene_list = wanted[wanted.columns[0]].tolist()
pre_transformed_table = wanted
transformed_table = pre_transformed_table.replace(['SSD', 'Borderline-SSD', 'Non-SSD', 'SimNSSD', 'RBB', 'N/A'], [5,4,3,2,1,0])
ortho_genes = pd.DataFrame(transformed_table.loc[:, transformed_table.columns[1]:])
fig, ax = plt.subplots(figsize=(10,10))
im = ax.imshow(ortho_genes.astype('float'))
ax.set_xticks(np.arange(len(species_list)))
ax.set_yticks(np.arange(len(gene_list)))
ax.set_xticklabels(species_list)
ax.set_yticklabels(gene_list)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
cbar = plt.colorbar(im) 
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_ylabel('Strength of orthologue prediction', rotation=270)

ax.set_ylabel('Locus tag (%s)' % " ".join(file.columns[0].split()[0:2]))
ax.set_title("Orthologue comparison")
plt.savefig(args.out_plot)
