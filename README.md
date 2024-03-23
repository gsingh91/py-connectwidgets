# py-connectwidgets


A python equivalent for the
[connectwidgets](https://rstudio.github.io/connectwidgets/) package in
R.

> [!WARNING]
>
> ### This package is experimental!
>
> This is an experimental porting of the R package and is in
> developement. Please do not use it for production workflows.

## Requirements:

- Python\>=3.9
- Access to Posit Connect server to retrieve :
  - Connect server name
  - API Key

## Available functions:

### listing all content

`get_content()` function outputs a dataframe with all content the user
has access to. Columns include content type, ID, deployed date, owner
ID, tags etc.

### tabular output

`rsc_table()` functions produces an itable output for the content
dataframe. Columns include app name, app owners’ name, last updated time
and app content type.