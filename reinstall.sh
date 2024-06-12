rm dist -rf
python3 setup.py sdist bdist_wheel
cd dist
pip3 uninstall leafleter -y
pip3 install --user *.whl
cd ..
python3 -m unittest
python3 example.py
# twine upload dist/* # to upload to PyPi
