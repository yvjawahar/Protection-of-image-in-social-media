# Protection-of-image-in-social-media
Watermarking and Encryption

The idea is to watermark the image and encrypt the watermarked image so when someone tries to download the image it will be in encrypted format and only with the help of key they can download the original image.<br><br>
Select a unique watermark for every image and simply embed on the original image.(embed.py)<br><br>
Encrypt the watermarked image using AES algorithm.Use unique key for every image.(e_d.py)<br><br>
For detection an algorithm namely "Template Matching" is used which calculates coefficient correlation of watermark and watermarked image and based on threshold it selects the highest value and its an indication that watermark is present in the image.(fulldetection.py)<br><br>
Finally,watermark can be attacked by resizing and lightning the watermark image.(attack.py)<br><br>
Using main.py the above mentioned functionalities can be accessed.

