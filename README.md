# Poynting Vectors around a Simple Circuit
In electronic circuits, electrons flow through the wires, but the energy does not. The energy flows through the fields <i>surrounding</i> the wires. The direction of that flow is determined by the <a href="https://en.wikipedia.org/wiki/Poynting_vector">Poynting vector</a>, named after John Henry Poynting. Yes, it's a pun and I love it. Anyway, the operation looks like this:

```math
\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B}
```

where $`\vec{E}`$ is the electric field, $`\vec{B}`$ is the magnetic field, $`\mu_0 = 4 \pi \times 10^{-7}`$ N/A<sup>2</sup> is the vacuum permeability, and $`\vec{S}`$ is the Poytning vector (in the direction of energy flow).

## Necessary Software
The code is done in Python 3.8 using the Visual Python 7 (vpython) package. If you haven't already, install Python then type the following into your command line to add the vpython package:

```
pip install vpython --upgrade
```

## What to Expect
All calcuations are done for when the circuit is in something called the &quot;steady state&quot;, which is when circuit has found an equilbrium (i.e. <i>not</i> immediately after you turn it on). That means the display is static. There is no animating. The program performs the calcuations, displays the objects and arrows, and then stops.

<img src="https://github.com/ScienceAsylum/Poynting-Vector/blob/main/Poynting%20(All).png">

The yellow sphere is supposed to be a light bulb and the blue cylinder is a battery. For the arrows: cyan is the electric field, orange is the magnetic field, and white is the Poynting vector. Strong effects are shown as larger arrows.

## Purpose of the Project
My goal was to confirm the orientation of the Poynting vector given the steady state conditions. You can see from the image above that, while the energy does flow through the field outside the wires, <i>most</i> of the energy is <i>immediately</i> outside the wires. The energy still mostly flows along the wires. I discuss this weird effect in the following videos:

<a href="https://youtu.be/zYRx6Zub3cA"> <img src="https://img.youtube.com/vi/zYRx6Zub3cA/mqdefault.jpg"> </a>
<a href="https://youtu.be/C7tQJ42nGno"> <img src="https://img.youtube.com/vi/C7tQJ42nGno/mqdefault.jpg"> </a>

## License
This code is under the <a href="https://github.com/ScienceAsylum/Poynting-Vector/blob/main/LICENSE">GNU General Public License v3.0</a>.
