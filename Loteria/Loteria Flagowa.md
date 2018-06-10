# Loteria Flagowa

Znaleźliśmy w internecie loterię flagową. W zgodzie z ustawą o grach hazardowych zostanie ona zaraz zablokowana, ale spróbuj przed zamknięciem wyciągnąć z niej flagę.

https://lottery.pwning2016.p4.team/

W zadaniu mamy do czynienia z generatorem liczb losowych. Z w pliku *server.js* widzimy w jaki sposób generowane są liczby.
```javascript
	var seed = new Date().valueOf() & 0xFFFFFFFF;
	var rnd = betterRand(seed)
    var userId = new Buffer(seed.toString()+","+rnd.next().value).toString("base64")
    
    var numbers = Array.from(Array(6)).map(() => Math.floor(rnd.next().value * 89 + 10))
```
Na pierwszy rzut oka wydaje się, że problemem może być uzyskanie dokładnie takiego samego timestampa, jednak możemy odczytać go z *userID* podanego na stronie.

1. Wchodzimy na stronę z loterią.
2. Odczytujemy seed z odkodowanego userID.
3. Wykonujemy taki sam js, jaki wykonuje serwer.
```javascript
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
```
wpisujemy otrzymane liczby i z konsoli wywołujemy funkcję ```submitNumbers()```
