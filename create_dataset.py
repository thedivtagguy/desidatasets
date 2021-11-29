def create_dataset(current_path):
    """
    This function creates a new dataset in the datasets folder.
    """


    while True:
        dataset_name = input("Name: ")
        if dataset_name == "":
            print("Please enter a valid dataset name")
        else:
            break

    while True:
        dataset_description = input("Description: ")
        if dataset_description == "":
            print("Please enter a valid dataset description")
        else:
            break

    while True:
        dataset_date = input("Date: ")
        # Validate date format YYYY-MM-DD
        if dataset_date == "":
            print("Please enter a valid date")
        else:
            break

    while True:
        dataset_source_name = input("Source Name: ")
        if dataset_source_name == "":
            print("Please enter a valid source")
        else:
            break

    while True:
        dataset_source = input("Source: ")
        if dataset_source == "":
            print("Please enter a valid source")
        else:
            break

    while True:
        dataset_license = input("License: ")
        if dataset_license not in licenses:
            print("Please enter a valid license")
        else:
            break

    while True:
        # Show list of categories and ask user to choose based on index
        print("\nChoose a category")
        for i, category in enumerate(category_list):
            print(f"{i}: {category}")
        category_index = input("Category: ")
        dataset_category = category_list[int(category_index)]
        if category_index == "":
            print("Please enter a valid category")
        else:
            break

    while True:
       # Show list of subcategories and ask user to choose based on index
        print("\nChoose a subcategory")
        # Go to the category folder and get list of subcategories
        subcategories = get_folders(os.path.join(
            current_path, category_list[int(category_index)]))
        for i, subcategory in enumerate(subcategories):
            print(f"{i}: {subcategory}")
        subcategory_index = input("Subcategory: ")
        dataset_about = subcategories[int(subcategory_index)]
        if subcategory_index == "":
            print("Please enter a valid subcategory")
        else:
            break

    dataset_columns = []
    while True:
        column_name = input("Column name: ")
        column_type = input("Column type: ")
        column_description = input("Column description: ")
        dataset_columns.append([column_name, column_type, column_description])
        if input("Add another column? (y/n) ") == "n":
            break

    # Create citation for dataset
    dataset_citation = "{dataset_source_name} ({dataset_date}). '{dataset_name}', {dataset_url}. Retrieved from {dataset_source} \n".format(
        dataset_source_name=dataset_source_name,
        dataset_date=dataset_date,
        dataset_name=dataset_name,
        dataset_category=dataset_category,
        dataset_source=dataset_source,
        dataset_url=base_url.format(
            category=dataset_category,
            subcategory=dataset_about,
            url=slugify(dataset_name)
        )
    )

    # Create a markdown table from the dataset columns
    markdown_table_from_dataset_columns = "| Column Name | Column Type | Column Description |\n| ----------- | ----------- | --------------- |\n"
    for column in dataset_columns:
        markdown_table_from_dataset_columns += "| " + \
            column[0] + " | " + column[1] + " | " + column[2] + " |\n"

    # Create ID for dataset
    dataset_id = "dd" + "_" + dataset_name + "_" + dataset_date
    dataset_id = slugify(dataset_id)

    # Change into the dataset folder
    os.chdir(dataset_category + "/" + dataset_about)
    # Create dataset folder
    os.mkdir(dataset_id)
    os.chdir(dataset_id)

    # Create a YAML file with the dataset information
    with open("DESCRIPTION.yaml", "w") as f:
        f.write("--- \n")
        f.write("id: " + dataset_id + "\n")
        f.write("name: " + dataset_name + "\n")
        f.write("description: " + dataset_description + "\n")
        f.write("date: " + dataset_date + "\n")
        f.write("source_name: " + dataset_source_name + "\n")
        f.write("source: " + dataset_source + "\n")
        f.write("license: " + dataset_license + "\n")
        f.write("columns:\n")
        for column in dataset_columns:
            f.write("- col_name: " + column[0] + "\n")
            f.write("  col_type: " + column[1] + "\n")
            f.write("  col_description: " + column[2] + "\n")
        f.write("--- \n")

    # Create a README file with the dataset information
    with open("README.md", "w") as f:
        f.write(README_TEMPLATE.format(dataset_name=dataset_name,
                                       data_description=dataset_description,
                                       markdown_table_from_dataset_columns=markdown_table_from_dataset_columns,
                                       dataset_category=dataset_category,
                                       dataset_about=dataset_about,
                                       dataset_id=dataset_id,
                                       dataset_citation=dataset_citation,
                                       dataset_source=dataset_source_name,
                                       dataset_license=dataset_license,
                                       category=dataset_category,
                                       subcategory=dataset_about))

        # Switch back to current_path
        os.chdir(current_path)

if __name__ == "__main__":
    import os
    from slugify import slugify

    current_path = os.getcwd()

    # Switch to /datasets
    os.chdir("./datasets")
    # List out possible licenses
    licenses = [
        "CC0",
        "CC BY",
        "CC BY-SA",
        "CC BY-ND",
        "CC BY-NC",
        "CC BY-NC-SA",
        "CC BY-NC-ND",
    ]


    category_list = [
        "categories",
        "cities",
        "states"
    ]

    base_url = "https://github.com/thedivtagguy/desidatasets/tree/master/datasets/{category}/{subcategory}/{url}"
    # Function to find names of folders in a directory
    def get_folders(path):
        folders = []
        for folder in os.listdir(path):
            if os.path.isdir(os.path.join(path, folder)):
                folders.append(folder)
        return folders


    README_TEMPLATE = """
    # {dataset_name}
    #### {category} > {subcategory}

    {data_description}

    ## Download

    Install the `desidata` package using CRAN and then call the `download_data()` function:
    ```r
    library(desidata)
    download_data(name = "{dataset_id}")
    ```

    ## Data Dictionary 

    {markdown_table_from_dataset_columns}

    # Source
    This dataset is sourced from {dataset_source}

    # License
    {dataset_license}

    ## Cite This Dataset
    {dataset_citation}


    `desidata for R`

    """

    # Function to take in user input about the dataset
    # Get current path

    create_dataset(current_path)
