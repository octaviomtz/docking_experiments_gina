#%%
!grep ATOM Q8N163/AF-Q8N163-F1-model_v1.pdb > Q8N163/rec.pdb

# %%
!obabel Q8N163/rec.pdb -OQ8N163/rec.pdb

#%%
import pandas as pd
df = pd.read_csv('SMILES_datasets/lung_cancer.csv')
df['smiles'].values[4]

#%%
!obabel -:'CC1=C(/C=C/C(C)=C/C=C/C(C)=C/C(=O)O)C(C)(C)CCC1' -OQ8N163/l3.sdf --gen3D

#%%
!obabel Q8N163/l3.sdf -OQ8N163/l3.pdb

#%%
# !grep 538 Q8N163/AF-Q8N163-F1-model_v1.pdb > Q8N163/lig.pdb

# %%
# %%
import py3Dmol
v = py3Dmol.view()
v.addModel(open(f'Q8N163/rec.pdb').read())
v.setStyle({'cartoon':{},'stick':{'radius':0.15}})
v.addModel(open('Q8N163/l3.pdb').read())
v.setStyle({'model':1},{'stick':{'colorscheme':'greenCarbon'}})
v.zoomTo({'model':1})

# %%
!cat AF-Q8N163-F1-model_v1.pdb

# %%
!./gnina -r Q8N163/rec.pdb -l Q8N163/l3.pdb --autobox_ligand Q8N163/l3.pdb
# %%
!./gnina -r Q8N163/rec_noH.pdb -l Q8N163/l3.pdb --autobox_ligand Q8N163/rec.pdb -o Q8N163/wdocking.sdf.gz --seed 0

# %%
import gzip
v = py3Dmol.view(height=400)
v.addModel(open('Q8N163/rec_noH.pdb').read())
v.setStyle({'cartoon':{},'stick':{'radius':.1}})
v.addModel(open('Q8N163/l3.pdb').read())
v.setStyle({'model':1},{'stick':{'colorscheme':'dimgrayCarbon','radius':.125}})
v.addModelsAsFrames(gzip.open('Q8N163/wdocking.sdf.gz','rt').read())
v.setStyle({'model':2},{'stick':{'colorscheme':'greenCarbon'}})
v.animate({'interval':1000}); v.zoomTo(); v.rotate(90)

# %%
!obabel Q8N163/rec.pdb -d -OQ8N163/rec_noH.pdb
# %%
