# example-package

## Setup
With PDM installed:
```bash
pdm sync
```

## Testing
The following command will run a test against each file of the dataset
```bash
pdm run pytest -v
```

The following command will run a test against the specific file that is currently included inside the repository.
```bash
pdm run pytest -v 'tests/test_sotab_cpa.py::test_cpa_small[Event_ohiocreditunions.org_September2020_CPA.json.gz]'
```

At times, it can be useful to have pytest print the variables available at the time of failure.
These can be shown by appending `-l` or `--showlocals` to one of the above commands.
