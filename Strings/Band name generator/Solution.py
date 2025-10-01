def band_name_generator(name):
    if(name[0]==name[-1]):
        return (name+name[1:]).capitalize()
    else:
        return (f"The {name.capitalize()}") 
