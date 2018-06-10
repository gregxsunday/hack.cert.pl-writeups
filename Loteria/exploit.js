<script>
function* betterRand(seed) {
  var m = 25, a = 11, c = 17, z = seed || 3;
  for(;;) yield (z=(a*z+c)%m)/m;
}

var seed = -463477979;
var rnd = betterRand(seed);
document.write(rnd.next().value + "<br>");

for(var i=0; i<6; i++)
	document.write(Math.floor(rnd.next().value * 89 + 10) + ',')
</script>
