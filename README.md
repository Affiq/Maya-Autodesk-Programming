<h1> Maya-Autodesk-Programming </h1>
A subset of different scripts that will manipulate the scenes in Maya Autodesk - such as a randomised scene generator, a tornado like scene, a ball projectile animation and a complex object creator.

<h2> DNA Object Generator </h2>

<h3> Usage </h3>
<p> There are a number of parameters that manipulate the model of the DNA. </p>
<ul>
  <li> <b> Input Copy Number: </b> The number of individual strands to produce</li>
  <li> <b> Input Peak: </b> The maximum height/width of the strands</li>
  <li> <b> X Increment: </b> The spacing and distance between each strand.</li>
  <li> <b> Input Wave Length: </b> The overall length of the DNA model in terms of pi (affects rotation)</li>

<h3> Samples </h3>

![DNA1](https://github.com/Affiq/Maya-Autodesk-Programming/blob/main/Images/DNA1.PNG?raw=true)
![DNA2](https://github.com/Affiq/Maya-Autodesk-Programming/blob/main/Images/DoubleCopies.PNG?raw=true)
![DNA1](https://github.com/Affiq/Maya-Autodesk-Programming/blob/main/Images/DoubleWavelength.PNG?raw=true)
![DNA1](https://github.com/Affiq/Maya-Autodesk-Programming/blob/main/Images/ReducedX.PNG?raw=true)

</ul>

<h3> Explanation </h3>
<p>  The main function uses the sin wave (you can see this when we use math.sin). the value of y will equal sin x (y will at most be 1 or -1 in the diagram above
looking at the peaks). The start of the wave, x=0 and y=0. The peak of the wave is at x=~1.6 (pi/2)
and y=1. The middle of the wave is when x=3.14 (pi) and y=0, the bottom peak of the wave is at
x=~4.7 (3pi/2) and y=-1 and then it will return to x=~6.28 (2pi) and y=0.
You will see the valriable or parameter y_factor often – this changes the height of the peak, so if it is
10, the wave will peak at y=10 instead of y=1.
Copy_number is the number of times our function should copy an object and display it in a certain
position.
X_value_increment is the space between each object.
Wavelength is an optional value we use to stretch the wave in the function y=sin(x/wavelength). If
we wanted to make it twice as long, we double wavelength.</p>

<h3> YSinWave function </h3>
<p>
The program first checks if a user has selected one object only. If not, appropriate error messages
are printed out. If so, it will begin the sinwave function. It will loop a certain number of times – the
same number as the amount of copies that the user wants to be made.
In each loop, it will duplicate the originally selected objects. It will then work out the x value (this is
whatever the previous x value was) and also the y value (this will be based on the equation in the
code (y_value = y_factor * math.sin(x_value/wavelength)) before moving the object to its correct x
and y position.

The YCosWave function works in the exact same way except it will use the cos value instead and so
the equation (y_value = y_factor * math.cos(x_value))
The ZSinWave also works in the same way except we do not work out the y values based on cos x –
we make it z= cos x instead and then move it to the appropriate x and z positions.</p>

<h3> BarMaker function</h3>
<p> Program works in a similar way as well – except for the positions, we only move it to its correct x
position – y and z will remain 0 for all the objects. However we create cubes who’s height depend on
the sinx function.
If you use the Ysinwave function and barmaker function with the same values, each bar should have
a sphere at the end of it – it almost looks like a DNA strand but it is missing one side of spheres. </p>

<h3> DNAMaker function</h3>
<p> The DNA maker will use two functions called make strand and makebar – but both essentially use
the Ysinwave function and makebar function. The makestrand function simply creates the same sin
wave – but also rotates this one 180 degrees upside down. It then produces the same sin wave but
with no rotation, so you get two strands without a middle.

![DNA1](https://github.com/Affiq/Maya-Autodesk-Programming/blob/main/Images/Peaks.PNG?raw=true)

The barmaker function then fills out this gap to produce a simple 2d DNA model. </p>

![DNA1](https://github.com/Affiq/Maya-Autodesk-Programming/blob/main/Images/Strands.PNG?raw=true)

<h3> DNAMaker2.0 function </h3>
<p> We then attempt to shade the model with different colours. It uses the exact same code as before to
produce the dna model.
The program finds all objects that starts with “sphere1*”, selects them and then shades them in a
“red” shader/material.
The program then finds all objects that start with “sphere2*”, selects them and then shades them in
a “bloo” shader/material.
The program then finds all objects that start with “bondbar*”, selects them and then shades them in
a “green” shader/material.</p>

<h3> DNAMaker3.0 function </h3>
<p> This essentially twists the gene. If you look at previously created DNA models, a cube with both
spheres at the end will have matching numberings – “strand1sphere3”, “bondbar3” and
“strand2sphere3” all end in the same number.
The twist function uses a for loop starting from bondbar1 and it’s spheres, to rotate it about the x
axis by x_rotate amount.
In the first loop, bondbar1 and its spheres will be rotate by 0. The next loop will select bondbar2 and
rotate it by 15. The next loop will select bondbar3 and rotate it by 30. The next loop will select
bondbar 4 and rotate it by 45 and so forth.
In each loop however, Sphere2 will be rotated to 180+x_rotate degrees so that both spheres are
opposite each other and do not end up in the same spot.
You can compare this to a clock where if one sphere is at 1 o clock (so 30 degrees from the start), the
opposite end must be at 7 o clock (and so 180+30 degrees from the start)</p>

<h2> Scenario Generator </h2>
<p>
The program consists of a few user defined values. The floor is divided into a grid so that there are
essentially square ‘land plots’ for each user defined object. We have a list of string called object list
that contains “empty “, “oil”, “cone” or “crates” that determines what object should be created at
each land plot. A block of code reads the string at each index of the list, and depending on what the
string is, performs the function that either makes crates, makes a cone, makes an oil drum or does
nothing and creates the object at that land plot before moving onto the next land plot.
Dimensionwidth is the area of each landplot, and so the distance between each generated object’s
origin. This ideally should not be reduced as it may cause some objects to collide with each other,
such as a cone fusing with a crate.</p>

<p>
SceneDimensions is the number n, in which the program creates an n x n number of land plots. If it
was 4 for example, the program produces a 4x4 land plot and so 16 land plots.
Firstly, the program starts by determining the minimum number of objects required inside the list
through objectsneeded= SceneDimensions x SceneDimensions. The program then looks at another
set of values (emptyplotnum, oildrumnum, conenum, cratesnum) which specify the ratio in which
the objects should ideally appear. For instance (0,0,1,0) will just generate a scene full of cones while
(2,1,0,0) with roughly 2 empty plots per cone. For each of these values, it will either add “empty”,
“oil”, “cone” or “crates” into a list. (using the previous examples we have a list of
[“cone”,”cone”…”cone”] and a list of [“empty”,”empty”,”cone”,…”empty”,”empty”,”cone”]). Note
that the pattern of how the objects appear is duplicated which is relatively boring – this is why we
use the random.shuffle function to shuffle the order of the list so that the entire pattern of the
object list is now somewhat random. Also note, that the length of the object list may be slightly
bigger than the objectsneeded value which is fine – it simply means some objects in the list won’t be
printed after a certain index. </p>

<h2> Projectile Motion </h2>

<h3> Sphere 1 – Bouncing ball </h3>
<p>The ball will bounce a certain height, and then bounce half the height repeatedly for a certain
number of bounces. </p>

<p> Example of a ball bouncing 3 times for height h and travelling x metres per bounce.
Originally, I tested the ball drop animation with a fixed number of 10 bounces, and experimented
the animation with a different number of frames. I found out that having an average of roughly 40
frames for each bounce made the animation look smooth, and hence this is why we calculate the
number of bounces = (number of frames / 40) so that we roughly get 40 frames per bounce.
We also have 2 other variables that affect the animation, max height (height of the first bounce) and
the x distance travelled per bounce. The z value of the coordinates is always 0 so we do not need to
work this out.
The ball originally starts at the origin (0,0,0).
Then for each bounce, we are interested in the peak of the bounce and then when the ball hits the
floor again.
We work out the coordinate at the peak of the bounce – which is half the current height of the
previous peak of the ball (currenty = currenty / 2) (which is why current height is doubled initially)
and the current x coordinate is the previous x coordinate + x/2 m (currentx = currentx +
(xperbounce/2)).
The coordinate for hitting the floor is then simply calculated as y=0 and current x coordinate is the
previous x coordinate + x/2 m (currentx = currentx + (xperbounce/2)). (note currenty does not
change here as that is only concerned with the ball peak).
The path and object is then created, along with the path animation where the start time (STU) is set
to 0 and the end time (ETU) is set to the number of frames.
</p>

<h3> Sphere 2 – Curved Ball Rolling </h3>
<p>
The ball will do a semicircle(ish) roll around the origin (0,0,0) without intersecting sphere 1. This ball
will roll for the first half of the number of frames. We define the path using 4 nodes with d2 distance
from the origin (0,0,0). In the example below, d2 is set to 3. The following will calculate the list of
coordinates (names as rollordinates) as:
</p>

<p>
(node 1 to node 4 respectively) = [(3,0,3), (-3,0,3), (-3,0,-3), (3,0,-3)]
</p>

<p> From here we create the path (with d = 3 for some form of curvature) and the sphere 2 object
before creating the path animation. In the path animation, the start time is set to 0 and the end time
is set to half the number of frames (etu=totalbouncetime/2) so that it stops halfway through the
main animation. </p>

<h3> Sphere 3 – Straight Diagonal Ball Rolling </h3>
<p>
This ball rolls from where sphere 2 ends to where sphere 3 ends. It starts moving halfway through
the animation until the end of the animation and simply rolls in a straight diagonal path.
We calculate the path simply by obtaining node4 and the last position in coordinates list used for the
ball bouncing. From here we create the path and object as normal, and create the path animation as
start time =(totalbouncetime/2) so it starts halfway through the animation and end time =
totalbouncetime so that both sphere 1 and sphere 3 (this one) meet at the same position at the
same time.
</p>
