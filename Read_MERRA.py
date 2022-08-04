
import netCDF4


fp = 'insert your file path here'

    
def read_merra(fp):
    NETCDF = { }
    
    nc = netCDF4.Dataset(fp)
    Var = nc.variables
    Keys = Var.keys
    for k in Keys: 
        array = numpy.array(nc[k])
        NETCDF[k] =   numpy.flip(array,axis=0)
        NETCDF['lat'] = ( nc.WesternmostLongitude  , nc.EasternmostLongitude ) 
        NETCDF['lon'] = ( nc.SouthernmostLatitude  , nc.NorthernmostLatitude ) 
        NETCDF['res'] =  { 'x'  : nc.LatitudeResolution  , 'y' = nc.LongitudeResolution }
    return NETCDF
     
