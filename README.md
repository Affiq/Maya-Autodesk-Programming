# Maya-Autodesk-Programming
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

The barmaker function then fills out this gap to produce a simple 2d DNA model. </p>

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
