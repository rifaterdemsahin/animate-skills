# Tidal Memory

Wind writes on water, and the water forgets it almost at once. **Tidal Memory** is a field of
thousands of particles drifting through layered Perlin noise. Each one leaves a faint stroke,
and the canvas keeps those strokes only as long as the trail-length setting allows. What you see
is not a picture of wind. It is the record of where the wind has been in the last few seconds,
fading steadily into the background.

The algorithm has three parts. A **current**: a flow field built from two octaves of noise, slowly
rotated over time so the field itself drifts like a tide. **Bodies**: particles that inherit the
local angle, move at a speed set by the flow-speed parameter, and take one of three palette colors
from how far they sit from the canvas center, giving warm cores and cool edges. **Forgetting**: each
frame paints a translucent wash over everything. The trail-length setting controls how strong that
wash is, so it decides how much the canvas remembers.

The aim is a careful, slow composition: low alpha, hairline strokes, and no clipping at the edges.
Particles that leave the canvas come back in at a random point, and those points come from the seed,
so every seed gives a reproducible weather system. Changing the seed changes the sea, while the
rules that drive it stay the same.
