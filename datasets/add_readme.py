import os

readme_template = """
# {name} datasets

## Description
This category contains datasets related to {name}.

## Usage

Install the `desidata` package using CRAN:
```r
install.packages("desidata")
```
Access datasets in this category by using the following command:
```r
library(desidata)
get_datasets(within = {main_category}, about = {name})
```

`desidata 📦 for R`
"""

# Delete the readme file if it exists
for folder in os.listdir(os.getcwd()):
    if os.path.isdir(folder):
        for subfolder in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, subfolder)):
                if os.path.exists(os.path.join(folder, subfolder, 'README.md')):
                    os.remove(os.path.join(folder, subfolder, 'README.md'))

# Add empty README.md to all subdirectories
for folder in os.listdir(os.getcwd()):
    if os.path.isdir(folder):
        for subfolder in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, subfolder)):
                with open(os.path.join(folder, subfolder, 'README.md'), 'w') as f:
                    f.write('')

# Add README.md readme_template to all folders
for folder in os.listdir(os.getcwd()):
    if os.path.isdir(folder):
        for subfolder in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, subfolder)):
                if os.path.exists(os.path.join(folder, subfolder, 'README.md')):
                    with open(os.path.join(folder, subfolder, 'README.md'), 'r') as f:
                        read_template = f.read()
                    with open(os.path.join(folder, subfolder, 'README.md'), 'w') as f:
                        f.write(readme_template.format(name = subfolder, main_category = folder))
