export PYTHONPATH=
apt install openbabel
MINICONDA_INSTALLER_SCRIPT=Miniconda3-py37_4.10.3-Linux-x86_64.sh
MINICONDA_PREFIX=/usr/local
wget https://repo.continuum.io/miniconda/$MINICONDA_INSTALLER_SCRIPT
chmod +x $MINICONDA_INSTALLER_SCRIPT
./$MINICONDA_INSTALLER_SCRIPT -b -f -p $MINICONDA_PREFIX
conda install --channel defaults conda python=3.7 --yes
conda update --channel defaults --all --yes
python3 -c 'import sys;_ = (sys.path.append("/usr/local/lib/python3.7/site-packages"))'
conda install -q -y -c conda-forge openbabel
# pip install py3Dmol
conda install -c conda-forge py3dmol -y
wget https://downloads.sourceforge.net/project/smina/smina.static
wget https://github.com/gnina/gnina/releases/download/v1.0.1/gnina
chmod +x gnina
./gnina