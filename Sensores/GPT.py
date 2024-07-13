from goes2go.data import goes_timerange

from datetime import datetime
import pandas as pd

## Dates may be specified as datetime, pandas datetimes, or string dates
## that pandas can interpret.

## Specify start/end time with datetime object
# start = datetime(2021, 1, 1, 0, 30)
# end = datetime(2021, 1, 1, 1, 30)

## Specify start/end time as a panda-parsable string
start = "2019-01-01 00:00"
end = "2019-02-01 00:00"

df = goes_timerange(start, end, satellite="goes16", product="ABI-L2-LSTF", return_as="xarray", download=False)
print(df)