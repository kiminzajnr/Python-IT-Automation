# Scale and convert images using Python Imaging Library

This script does the following to a batch of images iteratively:
- Open an image
- Rotate an image
- Resize an image
- Save an image in a specific format in a separate directory

### Usage
To use this script, Download the file containing zipped images using the following CURL request:

```
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie
```  

Unzip the file using the following command:
```
unzip images.zip
```  

The script changes the format of these images to *.jpg* and rotates them *90 degrees* and also changes the size of these pictures from *192 X 192* to *128 X 128*.  

Install `pillow` library using the following command:
```bash
pip3 install pillow
```  

Copy the script to your local computer.  
Now, run the file.  

`./<your_script_name>.py`  

Once this is successful, this should produce images in the right format withing the directory `opt/icons/`  
Note: You might face permission issues in accessing /opt, in this case run the script with `sudo`
