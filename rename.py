import os, glob, sys, re
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from termcolor import colored

def rename(input_dir, name_prefix="", start_num=0):
    print("Renaming files in directory: " + input_dir)
    
    files = glob.glob(os.path.join(input_dir, "*.png"))
    print("Found " + str(len(files)) + " file(s)")
    
    image_id = start_num
    for file in files:
        basename = os.path.basename(file)
        root, ext = os.path.splitext(basename)
        
        if root.endswith("_c") or root.endswith("_censored"):
            continue
        
        seed_re = re.search(r"s-(\d+)", root)
        seed = seed_re.group()[2:]
        
        prompt = root[:seed_re.start()]
        # print("{} / {}".format(prompt, seed))
        
        is_complete_prompt = prompt.endswith(", ")
        # print(is_complete_prompt)
        if not is_complete_prompt:
            msg = "{}: The prompt was too long!".format(image_id)
            print(colored(msg, "yellow"))
        
        img = Image.open(file)
        metadata = PngInfo()
        metadata.add_text("prompt", prompt)
        metadata.add_text("seed", seed)
        
        dir_name = os.path.dirname(file)
        new_filename = str(image_id).zfill(6) + ext
        if len(name_prefix) > 0:
            new_filename = name_prefix + "_" + new_filename
        
        new_filepath = os.path.join(dir_name, new_filename)
        img.save(new_filepath, pnginfo=metadata)
        
        if os.path.exists(new_filepath):
            print("{}: Renamed {} to {} successfully.".format(image_id, basename, new_filename))
            os.remove(file)
        
        image_id += 1

def main():
    print("Enter the target directory:")
    input_dir = input()
    print("Enter the filename prefix (If you don't need prefix, leave this blank):")
    name_prefix = input()
    rename(input_dir, name_prefix)

if __name__ == '__main__':
    main()