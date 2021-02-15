import netCDF4 as nc
def nc_dumps(file, unique_id):
    
    with nc.Dataset(file) as ds:
        o = {
            "uri": unique_id        
        }
        dims = {}
        for dim in ds.dimensions.values():
            dims[dim.name] = dim.name
        o["dimensions"] = dims
        o["properties"] = {}
        for prop in ds.variables.values():
            props = {}
            
            ###
            try:
                props["type"] = str(prop.datatype)
            except:                
                pass
            
            ###
            try:
                props["unit"] = prop.units                
            except:                
                pass
            
            ###
            try:
                if list(prop.dimensions):
                    props["shape"] = list(prop.dimensions)
            except:                
                pass
            
            ###
            try:
                if 'standard_name' in prop.ncattrs():                    
                    props["label"] = getattr(prop, 'standard_name')
                else:                    
                    props["label"] = prop.name
            except:
                pass

            ###
            try:
                if 'long_name' in prop.ncattrs():                    
                    props["description"] = getattr(prop, 'long_name')                   
            except:
                pass
            
            
            o["properties"][prop.name] = props

        return o
