#%%
from chembl_webresource_client.new_client import new_client
import pandas as pd
from tqdm import tqdm
from rdkit import Chem
from rdkit.Chem import Draw

# %%
drug_indication = new_client.drug_indication
molecules = new_client.molecule

lung_cancer_ind = drug_indication.filter(efo_term__icontains="LUNG CARCINOMA")
lung_cancer_mols = molecules.filter(
    molecule_chembl_id__in=[x['molecule_chembl_id'] for x in lung_cancer_ind])
len(lung_cancer_mols)

# %%
ids = []
smiles = []
for i in tqdm(lung_cancer_mols):
    if i['molecule_structures'] is not None and type(i['molecule_chembl_id']) is not None:
        ids.append(i['molecule_chembl_id'])
        smiles.append(i['molecule_structures']['canonical_smiles'])
len(ids), len(smiles)

# %%
df = pd.DataFrame(list(zip(ids, smiles)), columns=['ids', 'smiles'])
df.to_csv('SMILES_datasets/lung_cancer.csv', index=False)


# %% =====================================
molecule = new_client.molecule
no_violations = molecule.filter(molecule_properties__num_ro5_violations=0)
len(no_violations)

# %%
ids = []
smiles = []
for i in tqdm(no_violations):
    if i['molecule_structures'] is not None and type(i['molecule_chembl_id']) is not None:
        ids.append(i['molecule_chembl_id'])
        smiles.append(i['molecule_structures']['canonical_smiles'])
len(ids), len(smiles)
# %%
type(no_violations)
# %%
dict(no_violations)
# %%
no_violations._get_data()
# %%
df = pd.DataFrame(list(zip(ids, smiles)), columns=['ids', 'smiles'])
df.to_csv('SMILES_datasets/no_rule_of_five.csv', index=False)

# %%
mol = Chem.MolFromSmiles(df['smiles'].values[0])
Draw.MolToImage(mol)
# %%
