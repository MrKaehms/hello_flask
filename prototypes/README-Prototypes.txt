Use this area to create mockups that can latter be used for the final UI(s).  
Learn to use Bootstrap and some of bootstrap's VSCode extensions for rapid developent.
Let's standardize on Bootstrap 5.  Also, if you create individual javascript files 
or css files, please name them with your initials as part of the filename, and fully 
document so that we can share design ideas. Keep them in the css directory, and the js 
directory.

To do prototyping that can be isolated, please create a subdirectory under the prototypes directory,
with your name, or initials as the subdirectory name.

A couple of good tutorials on getting started with bootstrap and javascript:
https://youtu.be/PNKy60ah5kI
https://youtu.be/_E3HkekndFU

The bootstrap website example page:
https://getbootstrap.com/docs/5.2/examples/


Not sure whether we would have to use something like this or not, since we will probably use turbo-flask, but here is an 
example of how to call python from javascript:

$.ajax({
  type: "POST",
  url: "~/pythoncode.py",
  data: { param: text}
}).done(function( o ) {
   // do something
});

In the above case, the python code might be a method to adjust the motor controller(s).  If so, the param would be the
current speed to set the motors to (for the for/rev method)
See: https://stackoverflow.com/questions/13175510/call-python-function-from-javascript-code






