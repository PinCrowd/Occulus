
# Occulus: The Pincrowd Haar Classifier Build Tools

### Building the classifiers:

```
git clone git@github.com:PinCrowd/Occulus.git
cd Occulus
# Edit the build.xml selecting the desired options
ant
#return in 6 days and play
```


Generally select a single sample image indicative of the pins to be scanned. It is expected that this will entail a rather standard perspective within all allies with the exception of lighting and background color.

1. Crop the selected image covering the pin head (two lines on neck to the top of the pin) keeping all parts of the pin within the selection and ensuring the not select more extraneous whitespace than necessary.
2. Utilizing the `opencv_createsamples` utility generate a minimum of 5000 samples the utilizing the command [1].
3. Once the output vector has been generated make a quick visual inspection of the generated samples using the `-show` option [2].
4. Upon satisfactory sample generation create the haar classification using the `opencv_haartraining` command [3].
5. To finalize the hair cascade utilize the tool `convert_cascade`, this tool will render the requisite XML file that will be implemented for image recognition. [4].

# References
1. `opencv_createsamples -img images/positive.png -vec pincrowd.vec -maxxangle 0.03 -maxyangle 0 -maxzangle 0.03 -maxidev 100 -bgcolor 0 -bgthresh 0 -w 25 -h 45 -num 5000 -show`
2. `opencv_createsamples -vec pincrowd.vec -show -w 25 -h 45`
3. `opencv_haartraining -data haar -vec pincrowd.vec -bg negatives.txt -nstages 20 -mem 2000 -mode ALL -w 25 -h 45`
4. `convert_cascade --size="25x45" haar pincrowd.xml`

# Resouces
 - [http://note.sonots.com/SciSoftware/haartraining.html#w0a08ab4]
 - [http://note.sonots.com/SciSoftware/haartraining/document.html]
 - [http://achuwilson.wordpress.com/2011/07/01/create-your-own-haar-classifier-for-detecting-objects-in-opencv/]
