with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="Mountain_Scott_ds12",
    version="1.0",
    author="Mountain Scott",
    author_email="mountainscott@yahoo.com",
    description="Helper functions for splitting and adding columns to dataframes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Elswayre/Ray_lambda_ds12",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)