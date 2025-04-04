import os
import getpass
from pathlib import Path

""" Youtube Downloader """
""" Works on Playlists and Videos with a 1080p limit """

"""   INSTRUCTIONS: THIS IS ONLY FOR FIRST TIME SET-UP  """
"""   1. Create a .txt file in your desired folder entitled 'Links'   """
"""   2. Copy and Paste the links of the videos you want to download into the Links.txt file   """
"""   3. Create a .txt file in your desired folder entitled 'UsedLinks'   """
"""   4. Download and install firefox """
"""   5. Login to your Youtube account on Firefox and then close the browser, this will create the cookies file yt-dlp needs to get around youtube bot detection"""
"""   ONLY USE WITH A VPN AND A THROWAWAY GOOGLE AND YOUTUBE ACCOUNT   """
"""   YOUTUBE WILL BAN YOUR ACCOUNT IF YOU USE THIS TOO MUCH   """

username = getpass.getuser() # Get Username of the user
path = f"C:\\Users\\{username}\\Downloads\\yt-dlp" # Path to Downloads Folder

txtpath1 = Path(f"{path}\\Links.txt") # Path to Links.txt
txtpath2 = Path(f"{path}\\UsedLinks.txt") # Path to UsedLinks.txt

# os.system(f"cd {path}") # Change Directory to Downloads Folder
# os.system("pip install yt-dlp")

if txtpath1.exists(): # Check if the path exists
    pass

elif txtpath1.exists() == False: # If the path does not exist
    with open(f"{txtpath1}", "x") as f:
        f.write("")
        f.close()

if txtpath2.exists(): # Check if the path exists
    pass

elif txtpath2.exists() == False: # If the path does not exist
    with open(f"{txtpath2}", "x") as f:
        f.write("")
        f.close()

with open(txtpath1, "r+") as infile, open(txtpath2, "w+") as outfile:
    lines = infile.readlines()
    usedlinks = outfile.readlines()
    if len(lines) == 0: # If there are no links in the file
        print("No Links in the Links file, please add links to the file and re-run")
    
    else:
        print("Links Found, Continuing...")
        oldlines = []
        for line in lines:
            try:
                os.system(f"yt-dlp.exe --cookies-from-browser firefox --merge-output-format mp4 {line}") # Merge format command allows for automatic mp4 conversion as well as format choosing based on the video which is ideal for lists of different quality videos
                print(f"Downloaded {line}")
                oldlines.append(line) # appends link to the list of used links
                lines.pop(0)

            except Exception as e:
                errorstring = f"Tried Downloading from {line} but failed with {e}" # Appends Link and error caused to old links list
                oldlines.append(errorstring)
                continue

        infile.truncate(0) # Clear the file
        outfile.writelines(f"{oldlines}\n") # Write the old links and/or error messages to the usedlinks file
        
        infile.close()
        outfile.close()