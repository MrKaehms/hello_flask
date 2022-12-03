Examples folder is where you might add sample code and examples directly from the internet.
Try to reference the source article or repo for anything included here.  Include examples as 
complete sub directories!


======
Added "flask-video-streaming" example code.

Here are a couple of articles related to this code:

https://blog.miguelgrinberg.com/post/video-streaming-with-flask
https://blog.miguelgrinberg.com/post/flask-video-streaming-revisited


Note that the code uses multiple camera routines that can be swapped
in and out.  The default routine fakes the stream by just cycling through
3 sample images.  Once you have the basic flask script tunning, you can
change which camera routine to use.

If you download the repositorise directly from the article, they will
have their own git metadata, so cannot be directly added to an existing
git repo, such as this hello_flask repo. (It took me a while to figure out
what was going on with my own hello_flask local repository)
