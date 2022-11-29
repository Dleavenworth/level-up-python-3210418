import zipfile
import os

def zip_all(to_zip, exts, output_file):
    with zipfile.ZipFile(output_file, "w") as z:
        for file in os.listdir(to_zip):
            for ext in exts:
                if os.path.join(to_zip, file).endswith(ext):
                    z.write(os.path.join(to_zip, file))
    if os.path.exists(output_file):
        print("Zip file created")
    else:
        print("Zip file not created")


zip_all("src/14 Build a Zip Archive/my_stuff",
        [".jpg", ".png", ".txt"], "src/14 Build a Zip Archive/my_stuff.zip")
