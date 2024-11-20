import pyogrio
import subprocess

pyogrio_gdal_version=pyogrio.__gdal_version_string__
system_gdal_version: str
result = subprocess.run(['dpkg', '-s', 'libgdal-dev'], capture_output=True, text=True, check=True)
for line in result.stdout.splitlines():
    if line.startswith('Version:'):
        system_gdal_version=line.split(':', 1)[1].strip().split('+')[0]
print(f"Pyogrio compiled with Gdal version: {pyogrio_gdal_version}")
print(f"Gdal system version: {system_gdal_version}")
if pyogrio_gdal_version == system_gdal_version:
    print("Version is correct.")
else:
    print("Version is not correct. Pex wasn't built inside environment.")
    exit(1)
