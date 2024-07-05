import xarray as xr

r = 'huss_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca_ERA.nc'

ds = xr.open_dataset(r)

print(ds)