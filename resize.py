from pathlib import Path
from PIL import Image
folder = '/Users/gsole/Library/CloudStorage/OneDrive-Personal/2_Programing/2_Django/between/between_app/static/between_app/images'
new_dimension = (200, 300)
new_subdir = '/smaller/'

def resize(folder, new_dimension, new_subdir):
	"""function to resize a folder full of jpg"""       
	images_folder = Path(folder)    
	for child in images_folder.iterdir():        
            print("Found image:", child)        
            image_path = child.absolute()
            image = Image.open(image_path)        
            resized_image = image.resize(new_dimension)  # could also add Image.ANTIALIAS
             # create if the subdir not exists        
            subdir = images_folder.join(new_subdir)        
            if not subdir.exists():            
                subdir.mkdir(parents=True, exist_ok=True)               
                to_path = subdir.joinpath(child.name)  # join adds the path-separators        
            print("Saving resized to:", to_path)       
            resized_image.save(to_path,'JPEG',quality=90)  # add  'JPEG', quality=90