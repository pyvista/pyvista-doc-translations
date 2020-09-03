sudo apt-get update
sudo apt-get install -y --no-install-recommends python3-setuptools
sudo apt-get install -y --no-install-recommends libgl1-mesa-dev xvfb ffmpeg
sudo apt-get install -y --no-install-recommends python3-venv
(cd pyvista; git fetch origin; git checkout master; git reset --hard origin/master; git branch -a; pip3 install -r ./requirements_docs.txt)
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip setuptools wheel
pip install -r ./requirements.txt
git clone --depth 1 git://github.com/pyvista/gl-ci-helpers.git
source ./gl-ci-helpers/travis/setup_headless_display.sh
rm -rf gl-ci-helpers
pip install -U scipy
pip install -U imageio-ffmpeg
pip install -U matplotlib
pip install -U colorcet
(cd pyvista; make -C docs html -b coverage; make -C docs doctest; make -C docs html)
sh ./locale/update.sh
ls ./pyvista/docs/examples
rm -Rf examples
mv ./pyvista/docs/examples .
ls ./pyvista/docs/images
rm -Rf images
mv ./pyvista/docs/images .

