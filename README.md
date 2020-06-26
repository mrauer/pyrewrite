# PyRewrite
Tool for standardizing and optimizing photos.

### Available Commands
    pyrewrite set <PATH>
	pyrewrite rename
	pyrewrite compress <QUALITY>

### Example

Let's suppose you have a photos directory located at `Dropbox/photos/20180921`

First you need to set the path of the directory you would like to optimize:

`pyrewrite set Dropbox/photos/20180921`

If successful, you can see the path set by typing the command `pyrewrite`, as well as all the commands available.

Then you can rename the file. This will lowercase the name and replace all the special characters. Only `.jpg` files are supported at this point:

`pyrewrite rename`

You can then compress the images in the directory by setting the image quality:

`pyrewrite compress 75`

### Contribute

You can contribute to the project by developing new features, fixing bugs, submitting ideas or writing unit tests.

Submit a ticket at https://github.com/mrauer/pyrewrite/issues
