Funkcje czasu:
function text() {
    console.log('Java script Rules')
}
function textInter() {
    console.log('setInterval')
}

setInterval(textInter, 10000)
setTimeout(text, 4000)


Funkcje FunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcje
FunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcjeFunkcje

// Zadanie 2

function countHello(n) {

    if (typeof n !== 'number' || (n < 1 || n > 10)) {
        console.log('Bledny parametr');
        return;
    }

    let i = 1;

    const myInterval = setInterval(function() {
        console.log(`Licznik: ${i}`);

        if (i === n) {
            clearInterval(myInterval);
        }

        i++;
    }, 1000);

}

countHello(3);



// Stoper (JS)

let isPaused = true;
let time = 0;

let intervalID = setInterval(function() {
    if (!isPaused) {
        time++;
        console.log(time);
    }
}, 1000);

document.querySelector('.start').addEventListener('click', function() {
    isPaused = false;
});

document.querySelector('.pause').addEventListener('click', function() {
    isPaused = true;
});

document.querySelector('.stop').addEventListener('click', function() {
    isPaused = true;
    time = 0;
});








function callOtherFunction(nameOfFunction) {
  console.log("Cześć jestem funkcją o nazwie 'callOtherFunction' i wywołuję funkcję, którą ktoś mi wrzucił jako parametr");

  const randomNumber1 = Math.random() * 20;
  const randomNumber2 = Math.random() * 10;
  nameOfFunction(randomNumber1, randomNumber2);
}

callOtherFunction(function (a, b) {
  console.log("Pierwsza liczba:", a);
  console.log("Druga liczba", b);
  console.log("Wynik", a + b);
});



Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe
 Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe Metody tablicowe 

Mutacyjne 

Jest to zbiór metod które modyfikują oryginalną tablicę. 

arr.pop() - usuń i zwróć ostatni element tablicy 

arr.push() – dodaj element do końca tablicy 

arr.reverse() – odwróć całą tablicę 

arr.shift() – usuń i zwróć pierwszy element tablicy 

arr.unshift() – dodaj element na początek tablicy i zwraca nową długość 

arr.splice() – usuń (ew. zamień) i zwróć kawałek tablicy 

arr.sort() – posortuj elementy na podstawie przekazanej funkcji 

Przykłady 

pop() 

Usuń i zwróć ostatni element tablicy 

const array1 = [1, 2, 3, 4]; 
const lastElem = array1.pop(); 
 
console.log(array1); /* [ 1, 2, 3] */ 
console.log(lastElem); /* 4 */ 
 

push() 

Dodaj element do końca tablicy 

const array1 = [1, 2, 3]; 
const newLength = array1.push(5); 
 
console.log(array1); /* [ 1, 2, 3, 5] */ 
console.log(newLength); /* 4 */ 
 

reverse() 

Odwróć całą tablicę 

const array1 = [1, 2, 3];fo 
const newArray = array1.reverse(); 
f 
console.log(array1); /* [3, 2, 1] */ 
console.log(newArray); /* [3, 2, 1] */ 
 

shift() 

Usuń i zwróć pierwszy element tablicy 

const array1 = [2, 3, 12]; 
const firstElem = array1.shift(); 
console.log(array1); /* [3, 12] */ 
console.log(firstElem); /* 2 */ 
 

unshift() 

Dodaj element na początek tablicy i zwraca nową długość 

const array1 = [2, 3, 12]; 
const newLength = array1.unshift(5); 
console.log(array1); /* [5, 2, 3, 12] */ 
console.log(newLength); /* 4 */ 
 

splice() 

Usuń (ew. zamień) i zwróć kawałek tablicy. 

Zacznij od indeksu 2, usuń jeden element i wstaw liczbę 24 oraz ciąg znaków " kot". 

const array1 = [1, 2, 3, 4]; 
 
// 2 to index, 1 to ilość elementów 
array1.splice(2, 1, 24, "kot"); 
console.log(array1); 
// [1, 2, 24, "kot", 4] 
 

Usuń pierwszy element 

const array1 = [1, 2, 3]; 
 
// 0 to index, 1 to ilość elementów 
const firstElem = array1.splice(0, 1); 
console.log(array1); // [2, 3] 
 

Usuń ostatni element 

const array1 = [2, 3]; 
 
// -1 to index (licz od końca), 1 to ilość elementów 
const lastElem = array1.splice(-1, 1); 
console.log(array1); /* [2] */ 
 

sort() 

Posortuj elementy na podstawie przekazanej funkcji. 

const array1 = [23, 2, 3, 1, 34, 8]; 
const array2 = array1.sort(); 
console.log(array2); 
/* [1, 2, 23, 3, 34, 8] */ 
 

Jak widzisz tablica jest posortowana, ale z wykorzystaniem porządku leksykograficznego tzn. cyfry są porządkowane jako ciągi. Od ostatniej do pierwszej. Litery alfabetu występują po cyfrach. Przykład: [1, "a", 5, 11, 7, "c"] - taka tablica zostanie uporządkowana w następujący sposób: [1, 11, 5, 7, "a", "c"]. 

sort(func) 

const array1 = [23, 2, 3, 1, 34, 8]; 
const array2 = array1.sort(function(a, b) { 
return a - b; 
}); 
console.log(array2); 
/* [1, 2, 3, 8, 23, 34] */ 
 

Aby zaradzić temu problemowi, wystarczy do funkcji sort() przekazać parametr w postaci funkcji anonimowej, która sortuje cyfry za pomocą ich porównywania. 

 

 

Dostępowe 

Metody te nie modyfikują oryginalnej tablicy. 

arr.concat() – połącz dwie tablice 

arr.join() – połącz wszystkie elementy tablicy w ciąg znaków, użyj przekazanego argumentu jako separatora. 

arr.slice() – zwróć kawałek tablicy 

arr.indexOf() – pierwsza pozycja szukanego elementu 

arr.lastIndexOf() – ostatnia pozycja szukanego elementu 

arr.includes() - czy element znajduje się w tablicy (true/false) 

Przykłady 

concat() 

Połącz dwie tablice 

const array1 = [1, 2, 3]; 
const array2 = [5, 6]; 
const mergedArrays = array1.concat(array2); 
console.log(mergedArrays); /* [ 1, 2, 3, 5, 6] */ 
 

join() 

Połącz wszystkie elementy tablicy w ciąg znaków, użyj przekazanego argumentu jako separatora. 

const array1 = ["wsiąść", "do", "pociągu"]; 
const text = array1.join(); 
console.log(text); /* wsiąść,do,pociągu */ 
const array1 = ["wsiąść", "do", "pociągu"]; 
const text = array1.join("+"); 
console.log(text); /* wsiąść+do+pociągu */ 
 

slice() 

Zwróć kawałek tablicy. 

const array1 = [1, 2, 3]; 
const restarray1 = array1.slice(0, 2); 
console.log(restarray1); /* [ 1, 2] */ 
 

indexOf() 

Pierwsza pozycja szukanego elementu. 

const array1 = [1, 2, 3]; 
const index = array1.indexOf(2); 
console.log(index); /* 1 */ 
 

lastIndexOf() 

Ostatnia pozycja szukanego elementu. 

const array1 = [1, 2, 3, 1, 3, 3]; 
const index = array1.lastIndexOf(1); 
console.log(index); /* 3 */ 
 

includes() 

Czy element znajduje się w tablicy. 

const array1 = [1, 2, 3, 1, 3, 3]; 
const isNumberThreeInArray = array1.includes(3); 
console.log(isNumberThreeInArray); /* true */ 
 

 

Iteracyjne 

Są to funkcje wyższego rzędu (Higher order functions), czyli przyjmujące inną funkcję jako argument. 

arr.forEach() – wywołaj funkcję dla każdego z elementów 

arr.reduce() – wywołaj funkcję dla każdego z elementów w taki sposób, żeby mieć dostęp do wartości otrzymanej w wyniku wykonania funkcji dla poprzedniego elementu (przydatne przy sumowaniu) 

arr.some() – sprawdź, czy jakikolwiek element spełnia dany warunek 

arr.every() – sprawdź, czy wszystkie elementy spełniają dany warunek 

arr.filter() – wywołaj funkcję dla każdego z elementów tablicy, zwróć nową tablicę zawierającą tylko te elementy, które spełniły ten warunek 

arr.map() – wywołaj funkcję dla każdego z elementów, zwróć nową tablicę ze zmodyfikowanymi elementami 

forEach() 

Wywołaj funkcję dla każdego z elementów 

const array1 = [1, 2, 3]; 
array1.forEach(function(element, index, array) { 
console.log("Element" + element); 
}); 
 

reduce() 

Wywołaj funkcję dla każdego z elementów w taki sposób, żeby mieć dostęp do wartości otrzymanej w wyniku wykonania funkcji dla poprzedniego elementu (przydatne przy sumowaniu). 

const array1 = [1, 2, 3]; 
 
const sum = array1.reduce(function(total, item) { 
return total + item; 
}); 
 
console.log(sum); // 6 
 

some() 

Sprawdź, czy jakikolwiek element spełnia dany warunek. 

const array1 = [1, 2, 3]; 
array1.some(function(element, index, array) { 
return element % 2 !== 0; 
}); 
 

Sprawdź, czy jakikolwiek element jest nieparzysty, zwraca wartość logiczną true lub false. 

every() 

Sprawdź, czy wszystkie elementy spełniają dany warunek. 

const array1 = [1, 2, 3]; 
array1.every(function(element, index, array) { 
return element % 2 === 0; 
}); 
 

Sprawdź, czy wszystkie elementy są parzyste, zwraca wartość logiczną true lub false. 

filter() 

Wywołaj funkcję dla każdego z elementów tablicy, zwróć nową tablicę zawierającą tylko te elementy, które spełniły ten warunek. 

const array1 = [1, 2, 3, 4]; 
const bar = array1.filter(function(element, index, array) { 
return element % 2 === 0; 
}); 
console.log(bar); // [2, 4] 
 

Znajdź tylko elementy parzyste. 

map() 

Wywołaj funkcję dla każdego z elementów, zwróć nową tablicę ze zmodyfikowanymi elementami. 

const array1 = [1, 2, 3, 4]; 
const bar = array1.map(function(element, index, array) { 
return element * 2; 
}); 
console.log(bar); // [2, 4, 6, 8] 
Pomnóż elementy przez dwa. 












// Zadanie 1Zadanie 1 - rozwiązywane z wykładowcą

//Napisz funkcję distFromAverage, która ma przyjmować tylko jeden argument - tablicę. F
//unkcja ta ma zwracać też tablicę. Zwracana tablica powinna mieć w sobie różnicę pomiędzy liczbą z danej komórki a średnią wartością tablicy. Np.
//distFromAverage([1,2,3,4,5,6,7]) => [3,2,1,0,1,2,3] (średnia z tablicy wejściowej to 4)
//distFromAverage([1,1,1,1]) => [0,0,0,0] (średnia z tablicy wejściowej to 1)
//distFromAverage([2,8,3,7]) => [3,3,2,2] (średnia z tablicy wejściowej to 5)

function distFromAverage(arr) {

    const average = arr.reduce(function(acc, next) {
        return acc + next;
    }) / arr.length;

    // const average = arr.reduce((acc, next) => acc + next) / arr.length;

    return arr.map(function(element) {
        return Math.abs(element - average);
    });

    // return arr.map(element => Math.abs(element - average));

}

console.log(distFromAverage([2, 8, 3, 7]));
console.log(distFromAverage([1,2,3,4,5,6,7]));
console.log(distFromAverage([1,1,1,1]))





// Zadanie 2
Stwórz tablicę z listą swoich ulubionych owoców. Następnie:
    Wypisz pierwszy owoc w konsoli.
    Wypisz ostatni owoc w konsoli (skorzystaj z atrybutu length).
    W pętli wypisz wszystkie owoce (skorzystaj z atrybutu length).



let fruitArray = ['cherry', 'banana', 'berry', 'strawberry']

console.log(fruitArray.length);

//fruitArray.reverse()[0] - ostatni element (po odwroceniu tablicy)
//fruitArray.forEach(element => console.log(element)

console.log(fruitArray[0])
console.log(fruitArray[fruitArray.length - 1])

for(let i = 0; i < fruitArray.length; i++){
    console.log(fruitArray[i])
}


// Zadanie 4
Napisz funkcję printTable(array), która przyjmuje tylko jeden parametr - tablicę. 
Następnie przy pomocy odpowiedniej metody tablicowej przeiteruj (przejdź) po każdym elemencie i wypisz każdy z nich w konsoli.



function printTable(array){

    for(let i = 0; i < array.length; i++)
    {
    console.log(array[i]);
    }

}


printTable([2,3,4,10, 'r'])



//Zadanie 5 
Napisz funkcję multiply(array). Funkcja ma przyjmować tylko jeden argument - tablicę. 
Następnie funkcja multiply ma pomnożyć wszystkie liczby znajdujące się w tablicy przy pomocy odpowiedniej metody tablicowej i zwrócić wynik.
multiply([1,2,3,4,5,6,7]) => 5040
multiply([1,1,1,1]) => 1
multiply([2,8,3,7]) => 336




function multiply(array){
   // let summary = 0;
    // for(let i = 0; i < array.length; ++i)
    // {
    //  summary  *= array[i] ;
    // }
    return array.reduce((acc, next) =>{
        return acc * next;
    })
}



console.log(multiply([1,2,3,4,5,6,7]));

multiply([1,1,1,1]);

multiply([2,8,3,7]);





Zadanie 6
Napisz funkcję getEvenAverage, która ma przyjmować tylko jeden argument - tablicę. Funkcja ta ma zwracać średnią wartość parzystych liczb z tej tablicy. 
Dla uproszczenia można założyć, że tablica ma w sobie tylko liczby. Jeśli w tablicy nie ma parzystych liczb niech zwraca null.


function getEvenAverage(array) {

    if (array.every(element => element % 2 === 1)) {
        return null;
    }

    const filteredArray = array.filter(element => element % 2 === 0);

    return filteredArray.reduce((acc, next) => acc + next) / filteredArray.length;

}

console.log(getEvenAverage([1,2,3,4,5,6,7]));
console.log(getEvenAverage([1,1,1,1]));
console.log(getEvenAverage([2,8,3,7,4]));




Zadanie 7
Napisz funkcję sortArray, która ma przyjmować tylko jeden argument - tablicę zawierającą liczby całkowite. Funkcja ta ma zwracać posortowaną rosnąco tablicę. Możesz skorzystać z metod tablicowych.
sortArray([145,11,3,64,4,6,10]) => [3,4,6,10,11,64,145]
// Zadanie 7 Sortowanie

function sortArray(array) {

    return array.sort((a, b) => {
        return a - b;
    });

}

console.log(sortArray([145,11,3,64,4,6,10]));



// Zadanie 8
Napisz funkcję addArrays, która ma przyjmować dwa argumenty - dwie tablice zawierające liczby całkowite. Funkcja ta ma zwracać również tablicę, która będzie wynikiem dodawania każdego elementu o tym samym indeksie. Jeżeli, tablice nie są równe, elementy nadmiarowe są przepisywane do nowej tablicy.
addArrays([4,0,1,3,4], [1,9,6,7,8,17]) => [5,9,7,10,12,17]
addArrays([8,3,22], [1,3,2]) => [9,6,24]
addArrays([2,3,1,5,3,5], [3,1,76,1]) => [5,4,77,6,3,5]


function addArrays(arr1, arr2) {
 
    if (arr1.length > arr2.length) {
        return arr1.map((element, index) => {
            if (arr2[index]) {
                return element + arr2[index];
            } else {
                return element;
            }
        });
    } else {
        return arr2.map((element, index) => {
            if (arr1[index]) {
                return element + arr1[index];
            } else {
                return element;
            }
        })
    }
 
}
 
console.log(addArrays([4,0,1,3,4], [1,9,6,7,8,17]));
console.log(addArrays([8,3,22], [1,3,2]));


// Zadanie 1 DOMOWE
// Napisz funkcję getNumber, która ma przyjmować dwa argumenty: liczbę i tablicę.
//     Funkcja ta ma zwracać wartość true lub false, w zależności od tego czy podana
// liczba znajduje się w tablicy czy nie.
//
// getNumber(2, [33, 54, 2, 1, 4, 100]) => true
// getNumber(5, [33, 54, 2, 1, 4, 100] ) => false

function getNumber1(number, array) {
    console.log(array.includes(number))
}


function getNumber2(number, array) {
    return array.filter(function (element) {
        if (element === number) {
            return true;
        }
    }).length > 0;
}


function getNumber3(number, array) {

   check = array.some(function (element) {
            return element === number ;

    });

   if (check) return true; else return false;
}

console.log("Sposób 1")
getNumber1(2, [33, 54, 2, 1, 4, 100]);
getNumber1(5, [33, 54, 2, 1, 4, 100]);
console.log("Sposób 2")
console.log(getNumber2(2, [33, 54, 2, 1, 4, 100]));
console.log(getNumber2(5, [33, 54, 2, 1, 4, 100]));
console.log("Sposób 3")
console.log(getNumber3(2, [33, 54, 2, 1, 4, 100]));
console.log(getNumber3(5, [33, 54, 2, 1, 4, 100]));
console.log(getNumber3(100, [100, 54, 2, 1, 100]));
console.log(getNumber3(3, [33, 1, 4, 100]));



// Zadanie 2 DOMOWE
// Napisz funkcję addTheSameNumbers, która ma przyjmować dwa argumenty: liczbę i tablicę.
//     Funkcja ta ma zwracać sumę wszystkich elementów tablicy,
//     które są równe liczbie podanej jako pierwszy argument funkcji.
// Jeżeli liczby, podanej jako pierwszy argument funkcji nie ma w tablicy, zwróć null.


function addTheSameNumbers(number, array){

    if (array.includes(number)){


    const newArray = array.filter(function(element, index, array) {
        return element === number;
    });

    const sum = newArray.reduce(function(acc, next) {
        return acc + next;
    });

console.log(sum);
return sum;

} else {
        console.log(null);
        return null;
    }

}

addTheSameNumbers(7, [4, 7, 24, 7, 0, 10]) //=> 14
addTheSameNumbers(9, [33, 54, 2, 1, 9, 100] )// => 9
addTheSameNumbers(0, [33, 0, 2, 0, 9, 0] )// => 0
addTheSameNumbers(43, [6, 0, 2, 2, 3, 46] ) //=> null





 TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE 
  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE averagev TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  
  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE  TABLICE WIELOWYMIAROWE 


Zadanie 1

W pliku js/app.js znajduje się tablica o nazwie multiValueArray.

    Wypisz element znajdujący się w położeniu 3, 2.
    Wypisz długość tablicy znajdującej się w drugim rzędzie.
    Wypisz element znajdujący się w położeniu 4, 2.


const multiValueArray = [
  [2, 3],
  ["Ala", "Ola"],
  [true, false],
  [5, 6, 7, 8],
  [12, 15, 67]
];

console.log(multiValueArray[3][2])
console.log(multiValueArray[1].length)
console.log(multiValueArray[4][2].length)




  Zadanie 2
Napisz funkcje print2DArray, która będzie przyjmować jako argument tablicę dwuwymiarową. Następnie funkcja ma wypisać w konsoli zawartość tej tablicy.


// Zadanie 2 - Tablice wielowymiarowe

function print2DArray(array) {

    array.forEach(row => {
        row.forEach(element => {
            console.log(element);
        });
    });

    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array[i].length; j++) {
            console.log(array[i][j]);
        }
    }

}

print2DArray([
    [1, 2, 3],
    ['a', 'b', 'c'],
    [true, false, true]
])



 OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTYv OBIEKTY
  OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY
   OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY OBIEKTY


Zadanie 1 - rozwiązywane z wykładowcą
Stwórz obiekt country. Dopisz do niego następujące właściwości:
    capital - string,
    population - number,
    president - string,
    ministers - tablica stringów
Wypisz w konsoli wszystkie właściwości.


// Zadanie 1 - Obiekty

const country = {
    capital: 'Warszawa',
    population: 38_000_000,
    president: 'A.Duda',
    ministers: ['a', 'b', 'c'],
};

// console.log(country.capital);

for (const property in country) {
    console.log(country[property]);
}




Zadanie 2 - rozwiązywane z wykładowcą
Stwórz obiekt timeMachine. Dopisz do niego następujące właściwości:

    shape - string,
    model - string,
    run(date, place) - metoda, dzięki której można się przenieść w czasie. Argument date to data, do jakiej chcemy się przenieść, 
    a place to miejsce, do którego chcemy się przenieść. Oba argumenty to stringi.
Wypisz w konsoli wszystkie właściwości i uruchom metodę run.


// Zadanie 2

const timeMachine = {
    shape: 'Trianlge',
    model: 'ZX-15',
    // run(date, place)
    run: function(date, place) {
        console.log(`Przeniosles sie do ${place} i dnia ${date}`)
    },
};

timeMachine.run('2025-04-05', 'Kopenahaga');

for (let property in timeMachine) {
    console.log(timeMachine[property]);
}





Zadanie 4 slownik

Stwórz obiekt person. Dopisz do niego następujące właściwości i metodę:

    name,
    age,
    sayHello() - wypisującą string "hello"

Wypisz właściwości w konsoli, wywołaj metodę.

const person = {

    name: 'John Thaner',
    age: 22,
    sayHello: function(text) {
        console.log(`hello ${text}`)
    }
};

person.sayHello('Jacek')
for (let property in person) {
    console.log(person[property]);
}





Zadanie 5 slownik

Stwórz obiekt, który będzie przetrzymywał Twój ulubiony przepis. Obiekt powinien mieć własność title (string), servings (number) oraz ingredients (tablica stringów).
Dodaj pole ingredients poza ciałem obiektu.
Wypisz w konsoli te wszystkie informacje.

const myReceipt = {

    title: 'Cake',
    servings: 4,

};

myReceipt.ingrendients = (['maka', 'olej', 'owoce']);

for (let property in myReceipt) {
    console.log(myReceipt[property]);
}


Zadanie 6

Do pliku js/app.js przekopiuj poniższy kod:
const spoon = {
  isExist: true

}
const fork = spoon;
fork.isExist  = false;
Następnie sprawdź czy łyżka istnieje. > Tak istnieje
 



 Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this
 Słowo kluczowe this  Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe thisv
  Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this Słowo kluczowe this
 

Zadanie 1 - rozwiązywane z wykładowcą

Stwórz obiekt car, utwórz dla niego odpowiednie właściwości i metody.
Właściwości:

    brand,
    color,
    numberOfKilometers (na początku 0).

Metody:

    printCarinfo() - metoda powinna wypisywać informacje o samochodzie (kolor, markę i liczbę przejechanych kilometrów).
    drive(km) - która dodaje do przejechanych kilometrów podaną wartość. Użyj słowa kluczowego this, żeby odwołać się do obiektu w środku metody.

car.printCarinfo(); => "Czarny Mercedes, 0km"

car.drive(20);

car.printCarinfo(); => "Czerny mercedes, 20km"

Zadanie do samodzielnego wykonania

Do obiektu car z dodaj tablicę z listą dat przeglądów (niech będą to zwykłe napisy).

Dodaj też następujące metody:

    metodę dodającą wpis do tej tablicy,
    metodę zwracającą wszystkie przeglądy samochodu.

Użyj słowa kluczowego this, żeby odwołać się do obiektu w środku metody.


// Zadanie 1 - this

const car = {
    brand: 'Mercedes',
    color: 'black',
    numberOfKilometers: 0,
    printCarInfo() {
        console.log(`
            Marka ${this.brand}
            Kolor ${this.color}
            Liczba kilometrów ${this.numberOfKilometers}
        `)
    },
    drive(km) {
        this.numberOfKilometers += km;
    },
};

car.printCarInfo();
car.drive(20);
car.printCarInfo();


car.servicesDates = ['2020-01-01', '2021-01-01'];

car.addService = function(date) {
    this.servicesDates.push(date);
};

car.servicesList = function() {
    return this.servicesDates;
};

car.addService('2022-05-05');

console.log(car.servicesList());





Zadanie 2

Przeanalizuj kod, który znajduje się w pliku js/app.js.
Jest tam stworzony obiekt calculator, który posiada jedną metodę save(newA,newB). Zadaniem tej metody jest zapisanie dla tego obiektu pod pola a i b dwóch liczb.
Dopisz metody sum oraz multiply, tak aby zwracały sumę oraz iloczyn tych dwóch liczb ustawionych w metodzie save.


const calculator = {
  save: function (newA, newB) {
    this.a = newA;
    this.b = newB;
  },
  sum() {
        return this.a + this.b;
    },
  multiply() {
        return this.a * this.b;
    },
};

calculator.save(2, 3);
console.log(calculator.sum());
console.log(calculator.multiply());





Zadanie 3

Stwórz obiekt stairs.
Niech obiekt posiada pole step, które na początku ustaw na 0.
Dodaj do obiektu również następujące metody:
    up(), która zwiększa schodek o 1 (modyfikuj pole step)
    down(), która zmniejsza schodek o 1 (modyfikuj pole step)
    printStep(), która pokazuje, na którym schodku jesteśmy.

Przykład wywołania:
stairs.up();
stairs.up();
stairs.up();
stairs.down(); 


// Zadanie 3

const stairs = {
  step: 0,
  up: function() {
    this.step++;
  },
  // up() { ... }
  down() {
    this.step--;
  },
  printStep() {
    console.log(this.step);
  }
}

stairs.up();
stairs.up();
stairs.up();
stairs.down();
stairs.printStep() // 2





 Constructor function  Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function
  Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor functionv
   Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function Constructor function




Zadanie 1 - rozwiązywane z wykładowcą

W pliku js/app.js stwórz konstruktor Basket. Na jego bazie stwórz obiekt, który będzie miał następujące pola:

    products - tablica z wszystkimi produktami
    sum - kwota do zapłaty za wszystkie produkty

Do prototypu konstruktora dodaj metody:

    addProduct(name, price), która jako parametry będzie przyjmowała nazwę produktu oraz jego cenę. Cenę podawaj jako typ number, a nazwę jako string. Umieść te dane jako obiekt w tablicy this.products.
    showBasket(), której zadaniem będzie wyświetlenie wszystkich produktów z koszyka wraz ceną, oraz kwotą do zapłaty.

Przykładowe wywołanie:

const aliceBasket = new Basket();

aliceBasket.addProduct("pomidor",10);
aliceBasket.addProduct("arbuz",40);
aliceBasket.showBasket();


const bruceBasket = new Basket();

bruceBasket.addProduct("rice", 10);
bruceBasket.addProduct("grzyby mun",50);
bruceBasket.addProduct("tofu",20);
bruceBasket.showBasket();




Zadanie 2 - rozwiązywane z wykładowcą
W pliku js/app.js możesz znaleźć przykładowy konstruktor dla robota. Konstruktor oczekuje, że podasz tylko imię robota.
Metody dodane są do prototypu funkcji.
Utwórz kilka robotów i poszukaj, czy w napisanym kodzie nie ma błędów.
Sprawdź w konsoli jak wyglądają poszczególne roboty oraz sam konstruktor.

const Robot = function (name) {
  this.name = name;
  this.isFunctional = false;
};

Robot.prototype.sayHi = function (toWho) {
  if (this.isFunctional === true) {
    console.log("Robot " + this.name + " greets " + toWho);
  } else {
    console.log("Robot " + this.name + " is broken");
  }
};

Robot.prototype.changeName = function (newname) {
  console.log("Robot " + this.name + " changes name to " + newname);
  this.name = newname;
};

Robot.prototype.fixIt = function () {
  this.isFunctional = true;
  console.log("Robot " + this.name + " was fixed");
};



Zadanie 3

Stwórz konstruktor Calculator dla przyszłych obiektów. Konstruktor ma nie przyjmować żadnych danych. Każdy nowo stworzony obiekt powinien mieć pustą tablicę, w której będzie trzymać historię wywołanych operacji. Następnie przy pomocy prototypu dodaj następujące metody:

    add(num1, num2) - metoda ma dodać do siebie dwie zmienne i zwrócić wynik. Dodatkowo w tablicy operacji ma zapamiętać napis: "added num1 to num2 got result" (oczywiście z wartościami zmiennych podstawionymi w odpowiednie miejsce).
    multiply(num1, num2) - metoda ma pomnożyć przez siebie dwie zmienne i zwrócić wynik. Dodatkowo w tablicy operacji ma zapamiętać napis: "multiplied num1 with num2 got result" (oczywiście z wartościami zmiennych podstawionymi w odpowiednie miejsce).
    subtract(num1, num2) - metoda ma odjąć od siebie dwie zmienne i zwrócić wynik. Dodatkowo w tablicy operacji ma zapamiętać napis: "subtracted num1 from num2 got result" (oczywiście z wartościami zmiennych podstawionymi w odpowiednie miejsce).
    divide(num1, num2) - metoda ma podzielić przez siebie dwie zmienne i zwrócić wynik. Dodatkowo w tablicy operacji ma zapamiętać napis: "divided num1 by num2 got result" (oczywiście z wartościami zmiennych podstawionymi w odpowiednie miejsce).
    printOperations() - metoda ma wypisać wszystkie operacje zapamiętane w pamięci.
    clearOperations() - metoda ma wyczyścić wszystkie operacje z pamięci.



function Calculator() {
    this.history = [];
    this.result = 0;

    }


Calculator.prototype.add = function (num1, num2) {
    this.result = num1 + num2;
    this.history.push(`added: ${num1} and ${num2} = ${this.result} ` );
    return this.result;
}

Calculator.prototype.multiply = function (num1, num2){
    this.result = num1 * num2;
    this.history.push(`multiplayed: ${num1} and ${num2} = ${this.result} ` );
    return this.result;
}

Calculator.prototype.printOperations = function(){
    this.history.forEach(element => console.log(element));
}
Calculator.prototype.clearOperations = function() {
    console.log("Wyczyszczono")
    this.history = [];

}


const Calculate1 = new Calculator();
Calculate1.add(2, 3);
Calculate1.multiply(2, 3);
Calculate1.printOperations();
Calculate1.clearOperations();
Calculate1.printOperations();
Calculate1.multiply(3, 3);
Calculate1.printOperations();


// Zadanie 1 DOMOWE DZIEN 2
//
// W pliku app.js za pomocą konstruktora stwórz funkcję Tree.
//     Niech funkcja ta ma jedną właściwość type, która będzie przechowywać typ drzewa.
//     Następnie stwórz 2-3 instancje (obiekty) na podstawie konstruktora Tree, będące różnymi drzewami.
// Dopisz do prototypu konstruktora również metodę bloom(), która będzie zwracała tekst "I am blooming".



function Tree(type) {
    this.type = type;
    }
    
Tree.prototype.bloom = function () {
   return  console.log(`${this.type}: I am blooming  `)
}


const Tree1 = new Tree("Wierzba");
Tree1.bloom();

const Tree2 = new Tree("Sosna");
Tree2.bloom();


const Tree3= new Tree("Świerk");
Tree3.bloom();

 


 OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE
  OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE
   OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE OBIEKTOWOSC DZIEDZICZENIE



Zadanie 2
Część 1

Stwórz klasę Duck. Będzie to klasa abstrakcyjna, z której będą dziedziczyć inne kaczki. Stwórz wewnątrz tej klasy konstruktor i metody:

    konstruktor - którego zadaniem będzie ustawienie typu kaczki na "ordinary duck" np. this.type = "ordinary duck"
    sound() - wypisuje "Quack quack"
    swim() - wypisuje "I'm swimming...""
    print() - wypisuje "Looks like ordinary duck". Skorzystaj z ustawienia type do wypisania typu kaczki.

Stwórz obiekt donaldDuck. Wywołaj dla niego wszystkie metody.
Część 2

Na bazie klasy Duck stwórz kolejną o nazwie WildDuck. Nadpisz odpowiednio konstruktor, tak aby podczas wywoływania metody print() typ kaczki zmienił się na "wild". Stwórz obiekt daffyDuck. Wywołaj dla niego wszystkie metody.
Część 3

Na bazie klasy Duck stwórz kolejną o nazwie MallardDuck. Nadpisz odpowiednio konstruktor, tak aby podczas wywoływania metody print() typ kaczki zmienił się na "mallard". Stwórz obiekt daisyDuck. Wywołaj dla niego wszystkie metody.
Część 4

Stworzyłeś klasę Duck. Mogą z niej dziedziczyć wszystkie kaczki. Twoim zadaniem teraz jest dodanie do odpowiedniej klasy metody fly(). Metoda ma wypisywać w konsoli tekst "I'm flying...".
Część 5

Na bazie klasy Duck stwórz kolejną o nazwie RubberDuck. Nadpisz odpowiednio konstruktor, tak aby podczas wywoływania metody print() typ kaczki zmienił się na "rubber". Stwórz obiekt howardTheDuck. Wywołaj dla niego wszystkie metody. Czy widzisz coś niepokojącego?

Twoja gumowa kaczka potrafi latać!

Nadpisz odpowiednio metodę fly() tak, aby po jej wywołaniu w przypadku gumowej kaczki wypisywał się w konsoli tekst "Rubber ducks can't fly!".



class Duck {

  constructor() {
    this.type = "ordinary duck";
  }

   sound() {
    console.log(`Quack quack`);
  }
    swim() {
    console.log(`I'm swimming`);
  }
    print() {
    console.log(`Looks like ${this.type}`);
  }
  fly(){
      console.log(`I'm flying`);
  }

}
const donaldDuck = new Duck();
donaldDuck.swim();
donaldDuck.sound();
donaldDuck.print();

class WildDuck extends Duck {

    constructor() {
    super();

  }
  print() {
        this.type = "wild";
        console.log(`Looks like ${this.type}`);
  }

}


const daffyDuck = new WildDuck();
daffyDuck.swim();
daffyDuck.sound();
daffyDuck.print();
daffyDuck.fly();


class MallardDuck extends Duck {

    constructor() {
    super();

  }
  print() {
        this.type = "mallard";
        console.log(`Looks like ${this.type}`);
  }

}


const daisyDuck = new MallardDuck();
daisyDuck.swim();
daisyDuck.sound();
daisyDuck.print();
daisyDuck.fly();




class RubberDuck extends Duck {

    constructor() {
    super();

  }
  print() {
        this.type = "rubber";
        console.log(`Looks like ${this.type}`);
  }
  fly(){
        console.log(`Rubber ducks can't fly!`);
  }

}

const howardTheDuck = new RubberDuck();
howardTheDuck.swim();
howardTheDuck.sound();
howardTheDuck.print();
howardTheDuck.fly();










Zadanie 3

Na Twojej stronie internetowej masz stworzony formularz, który pozwala dodawać różne rodzaje produktów do listy.
W pliku masz stworzoną klasę Food - jako klasę abstrakcyjną. W konstruktorze klasa ustawia nazwę produktu (name), ilość białka (protein), ilość węglowodanów (carbs) oraz ilość tłuszczu (fat) w produkcie, (W gramach).
Napisz kod dzięki, któremu po wypełnieniu formularza i kliknięciu przycisku "Dodaj", zostaną wykonane następujące czynności:
    nowy produkt zostanie dodany do listy ul o id products,
    zostanie stworzony nowy obiekt na podstawie odpowiedniej klasy dziedziczącej po Food. To znaczy, jeżeli produkt będzie zawierał powyżej 250 kcal zostanie stworzony jako obiekt klasy FastFood. Jeżeli poniżej 250 kcal zostanie stworzony jako obiekt klasy FatFreeFood.
    dodaj stworzony obiekt do tablicy foods i wyświetl ją w konsoli.
Kalorie możesz obliczyć na podstawie następującego wzoru:

1g białka   dostarcza 4 kcal
1g tłuszczu dostarcza 9 kcal
1g węglowodanów dostarcza 4 kcal

Przykład. Po dodaniu produktu hot_dog i wypełnieniu jego danych odżywczych w formularzu, zostanie stworzony obiekt na bazie klasy FastFood np. w następujący sposób: new FastFood('Hot Dog', 10, 4.2, 26), co po przeliczeniu: 10* 4 + 4.2 * 4 + 9 * 26 daje 280.8 kcal.
Na podstawie formularza stwórz kilka obiektów jak poniżej:
new FastFood('Fries', 3.4, 41, 15)
new FastFood('Donut', 4.9, 51, 25)
new FatFreeFood('Greek Yogurt', 10, 3.6, 0.4)
Napisz metodę o nazwie print (w odpowiedniej klasie), która będzie wypisywała informację o produkcie.






const foods = [];
class Food {
  constructor(name, protein, carbs, fat) {
    this.name = name;
    this.protein = protein;
    this.carbs = carbs;
    this.fat = fat;
  }
  print() {
    console.log(`Name: ${this.name}`);
    console.log(`Proteins: ${this.protein}`);
    console.log(`Carbs: ${this.carbs}`);
    console.log(`Fat: ${this.fat}`);
  }
}
// Klasa FastFood
class FastFood extends Food {}
// Klasa FatFreFood
class FatFreeFood extends Food {}
// funkcja obliczająca kalorie
function calcCalories(p, c, f) {
  return p * 4 + c * 4 + f * 9;
}
const form = document.querySelector('form');
form.addEventListener('submit', event => {
  event.preventDefault();
  const name = document.querySelector('#name').value;
  const proteins = document.querySelector('#proteins').value;
  const carbs = document.querySelector('#carbs').value;
  const fat = document.querySelector('#fat').value;
  const newProduct = document.createElement('li');
  // Generowanie nowej instancji klasy FastFood / FatFreeFood
  if (calcCalories(proteins, carbs, fat) > 250) {
    // FastFood
    const fastFood = new FastFood(name, proteins, carbs, fat);
    fastFood.print();
    foods.push(fastFood);
    console.log(fastFood.constructor.name); // nazwa klasy
    console.log(fastFood instanceof FastFood); // true / false
  } else {
    // FatFreeFood
    const fatFreeFood = new FatFreeFood(name, proteins, carbs, fat);
    fatFreeFood.print();
    foods.push(fatFreeFood);
  }
  console.log(foods);
  newProduct.innerText = name;
  document.querySelector('#products').appendChild(newProduct);
  document.querySelector('#name').value = '';
  document.querySelector('#proteins').value = '';
  document.querySelector('#carbs').value = '';
  document.querySelector('#fat').value = '';
})




QUERY SELECTOR OBJECT
 Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementówv
  Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementówvv
   Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementówvv Wyszukiwanie elementów Wyszukiwanie elementówv
    Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów Wyszukiwanie elementów
QUERY SELECTOR OBJECT
// Ściąga QuerySelector 

<img src="http://img.com/image.jpg" /> 
<p class="myClass myAnotherClass" id="myId" data-animation="bounce">To jest akapit</p> 
<h1 class="myClass">To jest nagłowek pierwszego stopnia</h1> 
<ul> 
<li></li> 
<li></li> 
<li></li> 
</ul> 
<span></span> 
<div></div> 

  

document.querySelector('img'); // Wyszukiwanie znacznika tag-u 
document.querySelector('.myClass'); // Wyszukiwanie po klasie 
document.querySelector('#myId'); // Wyszukiwanie po identyfikatorze 

document.querySelector('h1.myClass'); // Wyszukiwanie znacznika h1 z klasą myClass 
document.querySelector('h1 .myClass'); // Wyszukiwanie elementu z klasą myClass w elemencie h1 

<h1> 
<div class="myClass"></div> 
</h1> 

document.querySelector('.myClass.myAnotherClass'); // Wyszukiwanie elementu z klasami myClass myAnotherClass 
document.querySelector('.myClass#myId'); 


<div> 
<p></p> 1  
<img /> 2 
<p></p> 3  
</div> 

document.querySelector('div + p'); // element p bezpośrednio po elemencie div (rodzeństwo) 
 console.log(document.querySelectorAll(('nav.navigation li'))); - wszystkie 
document.querySelector('div > p'); // element p będący bezpośrednim dzieckiem elementu div 


document.querySelector('[src]'); // element z atrybutem src  <div src="bounce">
document.querySelector('[src=jakaswartosc]'); // element z konkretna wartoscia atrybuty 


document.querySelector('div p:nth-child(2)'); // element p bedacy drugim dzieckime elementu div 




Zadanie 1 - rozwiązywane z wykładowcą

    Znajdź pierwszy element h1 na stronie,
    Znajdź element o class title,
    Znajdź element z atrybutem data-animation

Każdy znaleziony element wypisz w konsoli, aby upewnić się, że Twój kod działa.

// Zadanie 1 - Wyszukiwanie elementów
console.log(document.querySelector('h1'));
console.log(document.querySelectorAll('h1')[0]);
console.log(document.querySelector('.title'));
console.log(document.querySelector('[data-animation]')); // <div data-animation="bounce">




Zadanie 2 - rozwiązywane z wykładowcą

Wypisz w konsoli:

    Ile na stronie znajduje się elementów div (jest ich 20),
    Ile na stronie znajduje się elementów o klasie offers (jest ich 12),
    Ile na stronie znajduje się elementów, które posiadają atrybut href (jest ich 13).



// Zadanie 2
console.log(document.querySelectorAll('div').length);
console.log(document.querySelectorAll('.offers').length);
console.log(document.querySelectorAll('[href]').length);





Zadanie 3

Wyszukaj na stronie następujące elementy i zapisz je do odpowiednio nazwanych zmiennych:
    Element o id home (na dwa sposoby).
    Pierwszy element li posiadający atrybut data-direction.
    Pierwszy element o klasie block.
Pamiętaj, żeby za każdym razem sprawdzić, czy wczytałeś odpowiedni element. Pamiętaj, żeby używać funkcji, które wyszukują tylko jeden element.


console.log(document.querySelector('#home'));
console.log(document.getElementById('home'));

console.log(document.querySelector('li[data-direction]'));
console.log(document.querySelector('.block'));




Zadanie 4

Wyszukaj na stronie następujące elementy i zapisz je do odpowiednio nazwanych zmiennych:
    Wszystkie elementy li znajdujące się w tagu nav z klasą navigation.
    Wszystkie paragrafy należące do wszystkich elementów div.
    Wszystkie divy znajdujące się w tagu article.
Pamiętaj, żeby za każdym razem sprawdzić, czy wczytałeś odpowiednie elementy. Pamiętaj, żeby używać funkcji, które wyszukują wiele elementów. Za każdym razem wypisz w konsoli, ile znalazłeś elementów.

console.log(document.querySelectorAll(('nav.navigation  li')));
console.log(document.querySelectorAll('div p'));
console.log(document.querySelectorAll('article div'));






Zadanie 5
    Wyszukaj na stronie i zapisz do odpowiednio nazwanej zmiennej tag article o klasie first.
    W kolejnym etapie:
    wypisz w konsoli, ile elementów h2 znajduje się w tym tagu.
Pamiętaj, żeby za każdym razem sprawdzić, czy wczytałeś odpowiednie elementy.



console.log(document.querySelectorAll(('article.first')));
console.log(document.querySelectorAll('h2').length);

const results = document.querySelectorAll(('article.first'));
console.log(results.querySelectorAll('h2').length);







Atrybuty elementu
Po co szukamy elementów na stronie?

Kiedy już znajdziemy element na stronie możemy z nim zrobić wiele rzeczy np. pobrać listę jego klas; 
zmodyfikować nazwę klas; zmienić tekst, który wyświetla; zmienić style; pobrać zbiór dataset itd.

Obok kilka przykładów atrybutów, które możemy pobierać lub modyfikować.
Przykładowe atrybuty

    classList – zwraca pseudotablicę klas HTML,
    className – zwraca lub ustawia nazwy klas HTML jako ciąg znaków,
    id – zwraca lub ustawia Id HTML jako ciąg znaków,
    innerText – zwraca/ustawia tekst znajdujący się w tagu (bez zagnieżdżonych tagów),
    tagName – zwraca nazwę tagu,
    dataset – zwraca obiekt dataset.


 ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTYv
 ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTYv
 ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY ELEMENTY

Atrybuty elementu - przykład
Kod HTML

<a href="www.google.com" class="bar" id="glink" data-foo="1">
  <h1>Google</h1>
</a>

Kod JavaScript

const link = document.querySelector('#glink');
link.className; /* "bar" */
link.id;        /* "glink" */
link.innerText; /* "Google" */
link.tagName;   /* "A" – nazwa zwracana jest wielkimi literami */
link.dataset;   /* { foo: "1" } */

https://developer.mozilla.org/en-US/docs/Web/API/Element


// Zadanie 1 - rozwiązywane z wykładowcą
//
//     Stwórz funkcję getDataInfo(elements), do której przekaż jako argument zmienną links (pamiętaj o tym, że jest to pseudotablica)
//     stwórz w funkcji nową tablicę i wypełnij ją wartościami pobranymi z atrybutu data każdego elementu li
//     zwróć tą tablicę.


// Elementy - Zadanie 1

const links = document.querySelector(".links").querySelectorAll("li");
console.log(links); // wypisze kazdy selektor li
function getDataInfo(elements) {

    const colorsArray = [];

    elements.forEach(element => {
        colorsArray.push(element.dataset.color);
        console.log(element.dataset.color); // wypisze z petli przypisane kolory z data-color
    });

    return colorsArray;
}

console.log(getDataInfo(links));


//DRUGIE ROZWIAZANIE:


const links = document.querySelector(".links").querySelectorAll("li");
const link2 = document.querySelector(".links").getElementsByTagName("li");
Array.from(links).map(link => console.log(link));
[...links].map(link => console.log(link));
// for (let link in links) {
//     console.log(link);
// }
for (let link of links) {
    console.log(link);
}
console.log('---');
// for (let link in link2) {
//     console.log(link);
// }
for (let link of link2) {
    console.log(link);
}
link2.forEach(link => {
    console.log(link);
})

// Zadanie 2
//
// Przeanalizuj kod HTML i JavaScript. W pliku js/app.js jest przygotowane kilka zmiennych,
//     w których zapisane są wyszukane elementy DOM.
// Wypisz w konsoli wszystkie te zmienne. Sprawdź, które z nich to pseudotablice.
// W przypadku pseudotablic przeiteruj (używając np. pętli for). Wypisz nazwę tagu oraz klasy dla każdego elementu.

const home = document.getElementById("home");
const ban = document.querySelector(".ban");

console.log("home");
console.log(home);
console.log("ban");
console.log(ban);




console.log("someBlocks");
const someBlocks = document.querySelectorAll(".block");
console.log(someBlocks); // pseudo tablica

//NIE ZROBIONE

console.log("listElements");
const listElements = document.querySelector(".links").querySelectorAll("li");
console.log(listElements);// pseudo tablica

//NIE ZROBIONE






console.log("CHILDREN");

const children = document.querySelector(".offers").querySelectorAll("div, h2, p");
console.log(children); // pseudo tablica





    children.forEach(element => {
        console.log(element.tagName);
        console.log(element.className);
    });




// Zadanie 3
//
// Wypisz w konsoli wartość innerText dla elementów zmiennej blocks.
//     Następnie ustaw wartość innerText na "Nowa wartość diva o klasie blocks".

   <div class="blocks">
      <div class="block">
        <a href="#">Start</a>
        <a href="#">About</a>
      </div>
      <div class="block">
        <a href="#">Service</a>
        <a href="#">Portfolio</a>
      </div>
      <div class="block">
        <a href="#">Blog</a>
        <a href="#">Contact</a>
      </div>
    </div>



const blocks = document.querySelectorAll(".block");

blocks.forEach(block => {
    console.log(block.innerText); //Start Abaout i tak dalej
 //moze byc rowniez: innerHTML
    block.innerText = 'Nowa wartosc diva o klasie blocks';
    console.log(block.innerText); //'Nowa wartosc diva o klasie blocks';
});








// Zadanie 4
//
//     Znajdź na stronie element o class superFooter
//     Stwórz funkcję getId(element), do której przekaż jako argument znaleziony element
//     pobierz w funkcji nazwę id elementu i zwróć ją

const superFooter = document.querySelector('.superFooter');

function getId(element) {
    return element.id;
}

console.log(getId(superFooter));









// Zadanie 5
//
//     Stwórz funkcję getTags(elements), do której przekaż jako argument zmienną childElements (pamiętaj o tym, że jest to pseudotablica)
//     stwórz w funkcji nową tablicę i wypełnij ją nazwami tagów pobranymi z elementów znajdujących się w childElements
//     zwróć tą tablicę.
 <div class="offers">
          <div class="brilant icons"></div>

          <h2>Clean and morn</h2>

          <p>
            Fusce return pretium lorem semper nulla.
            ra. Fusce return prm lorem sem
          </p>
        </div>
        <div class="offers">
          <div class="cup icons"></div>

          <h2>Easy to use</h2>

          <p>
            Fusce return pretium lorem semper nulla.
            ra. Fusce return pretium .m lor
          </p>
        </div>
        <div class="offers">
          <div class="phone icons"></div>

          <h2>Fully Responsive</h2>

          <p>
            Fusce return pretium lorem semper nulla.
            ra. Fusce return pretium .m lor
          </p>
        </div>


const childElements = document.querySelector(".offers").querySelectorAll("div, h2, p");

function getTags(elements) {
    const tagNames = [];

    elements.forEach(element => {
        tagNames.push(element.tagName);
    });

    return tagNames;
}

console.log(getTags(childElements));








// Zadanie 6
//
//     Stwórz funkcję getClassInfo(element), do której przekaż jako argument zmienną banner
//     zwróć tablicę z listą klas, pobraną z przekazanego do funkcji argumentu.


const banner = document.querySelector(".ban");


function getClassInfo(element) {
    return element.classList;
}

console.log(getClassInfo(banner));


 WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH 
  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH 
   WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH  WIECEJ O ELEMENTACH 

CLASSLIST className

Mamy taki element:
HTML:

<div id="myDiv" class="class1 class2"></div>

JavaScript:

const myDiv = document.getElementById("myDiv");

Możemy łatwo wczytać jego wszystkie klasy:

console.log(myDiv.classList);
/* ["class1", "class2"] - pseudotablica */
console.log(myDiv.className);
/* "class1 class2" - ciąg znaków */




    el.hasAttribute(attrName) – sprawdza, czy element ma podany atrybut. W odpowiedzi dostajemy wartość logiczną.

    link.hasAttribute("href");
    /* true */



    el.getAttribute(attrName) – zwraca wartość podanego atrybutu.

    link.getAttribute("href");
    /* "www.google.com" */

    
    el.removeAttribute(attrName) – usuwa podany atrybut.

    link.removeAttribute("href");
    link.hasAttribute("href");
    /* false */

    el.setAttribute(attrName, attrValue) – nastawia wartość podanego atrybutu.

    link.setAttribute("href", "www.something.com");
    link.hasAttribute("href");
    /* true */
    link.getAttribute("href");
    /* "www.something.com" */




Pobieranie i modyfikacja styli CSS

    Obiekt style przechowuje wszystkie wartości jako ciągi znaków.
    Tak samo będą one nam zwracane i tak powinniśmy je nastawiać.
    Obiekt style "widzi" tylko style ustawione za pomocą JavaScript, nie widzi styli CSS.
    Ustawiając właściwości CSS należy stosować zapis camelCase.

Aktualną wartość stylu możemy wczytać:

element.style.backgroundColor;



Albo nastawić nową wartość:

element.style.backgroundColor = "blue";






// Zadanie 1 - Wiecej o elementach
// Zadanie 1 - rozwiązywane z wykładowcą
//
// Zmodyfikuj listę w sekcji .exercise w następujący sposób:
//
//     Nastaw kolor tła co drugiego elementu listy na szary (#9e9e9e),
//     Nastaw piątemu elementowi listy klasę big,
//     Nastaw co trzeciemu elementowi podkreślenie.

const listElements = document.querySelectorAll('li');

for (let i = 0; i < listElements.length; i++) {

    if (i % 2 === 0) {
        listElements[i].style.backgroundColor = '#9e9e9e';
    }

    if (i === 4) {
        listElements[i].classList.add('big');
        // listElements[i].className = listElements[i].className + ' big';
    }

    if (i % 3 === 0) {
        listElements[i].style.textDecoration = 'underline';
    }

}






// Zadanie 2
//
// Na stronie są trzy obrazki z ikonami najpopularniejszych przeglądarek internetowych. Niestety zarówno obrazki, jak i linki prowadzące do ich stron zawierają błędy. Napisz kod JavaScript, który wprowadzi następujące zmiany:
//
//     Poprawi elementy tak, żeby do każdej przeglądarki było podpięte odpowiednie logo (obrazek jest nastawiany za pomocą background-image).
//     Poprawi linki tak, żeby każdy miał poprawny opis i atrybut href.
//     Poprawi szerokość elementu o klasie chrome (powinno być 100px).


const browsers = document.querySelectorAll('.card');
// [chrome, edge, firefox]

// Chrome

const chromeBrowser = browsers[0];
// szerokosc obrazu tla
chromeBrowser.querySelector('.chrome').style.width = '100px';
// tekst linku
chromeBrowser.querySelector('a').innerText = 'Chrome';

// Edge

const edgeBrowser = browsers[1];
// logo
edgeBrowser.querySelector('.edge').style.backgroundImage = 'url(img/edge.jpg)';
// link
edgeBrowser.querySelector('a').setAttribute('href', 'http://edge.com');


// Firefox

const firefoxBrowser = browsers[2];

firefoxBrowser.querySelector('.firefox').style.backgroundImage = 'url(img/firefox.jpg)';
firefoxBrowser.querySelector('a').innerText = 'Firefox';
firefoxBrowser.querySelector('a').setAttribute('href', 'http://firefox.com');






// Zadanie 3
//
// Na stronie jest lista, w której musisz wpisać swoje imię i nazwisko, swój ulubiony kolor i potrawę.
//
//     Wyszukaj odpowiednie elementy (spany) i zapisz je do zmiennych.
//     Za pomocą innerText wypełnij w nich odpowiednie informacje.


const nameVal = document.querySelector('#name');
const favColorVal = document.querySelector('#fav_color');
const favMealVal = document.querySelector('#fav_meal');

nameVal.innerText = 'JacekRogowski';
favColorVal.innerText = 'Brąz';
favMealVal.innerText = 'Pizza';






// Zadanie 4
//
// Na stronie jest proste menu. Zarówno kod HTML, jak i CSS jest już do niego przygotowany.
//     Niestety ktoś zapomniał dodać odpowiednie klasy do odpowiednich elementów.
//
//     Wyszukaj element ul w sekcji .exercise i dodaj mu klasę menu.
//     Wyszukaj wszystkie elementy li w sekcji .exercise i dodaj im klasę menuElement (użyj do tego pętli). Uważaj,
//     żeby nie wykasować klasy selected.
//     Zauważ, że jeden z elementów ma czerwony kolor tła. Jest to spowodowane tym, że ma klasę error. Zabierz mu ją (najlepiej,
//     jeżeli zabierzesz tę klasę wszystkim elementom, które ją mają).
 

document.querySelector('.exercise ul').classList.add('menu');

document.querySelectorAll('.exercise li').forEach(element => {
  element.classList.add('menuElement');

  if (element.classList.contains('error')) {
    element.classList.remove('error');
  }
})



// Zadanie 5
//
// Dodaj do każdego elementu listy w sekcji .exercise, atrybut data-id przyjmujący kolejne liczby całkowite (zaczynając od 1).

document.querySelector('.exercise li').forEach((element, index) => {
  element.dataset.id = index + 1;
  // element.setAttribute('data-id', index + 1);
})


// Zadanie 2 DOMOWE Zadanie 2 DOMOWEZadanie 2 DOMOWE Zadanie 2 DOMOWE Zadanie 2 DOMOWE Zadanie 2 DOMOWE
//
// Do każdego podpunktu stwórz odpowiednią funkcję o nazwie podanej w treści zadania.


console.log("PODPUNKT 1:");

// Podpunkt 1. Pobranie informacji z atrybutu data
//     znajdź element o id menu,
const menu = document.getElementById('menu');
console.log(menu)

//     stwórz funkcję getDataInfo(element) do której przekaż, jako argument, znaleziony element,
//     stwórz w funkcji nową tablicę i wypełnij ją wartościami pobranymi z atrybutu data-info każdego elementu li.





const data = document.querySelectorAll('li[data-info]');
console.log(data)

function getDataInfo(element){
  arrayDInfo = [];
    element.forEach(el => {

 arrayDInfo.push(el.dataset.info)
    //console.log(el.innerText)
    })

    return arrayDInfo;

}

console.log(getDataInfo(data));




console.log("BARDZIEJ PRADZIWY SPOSOB:");
//     Zauważ, że elementy li to dzieci elementu o id menu.
//     zwróć tę tablicę.

//const data1 = document.querySelectorAll('[data-info] > li');
const data1 =  document.querySelector("#menu").querySelectorAll("li");
console.log(data1)


function getDataInfo1(element){
  arrayDInfo = [];
    element.forEach(el => {

 arrayDInfo.push(el.dataset.info)

    })

    return arrayDInfo;

}
console.log(getDataInfo1(data1));


 

// Podpunkt 2. Szukanie elementu po id
//
//     Znajdź element o id main-container.
//     stwórz funkcję getElementClass(element) do której przekaż, jako argument, znaleziony element.
//     zwróć tablicę złożoną z nazw klas tego elementu.

console.log("PODPUNKT 2:");
const mainId = document.getElementById('main-container');
  arrayDInfo = [];
function getDataInfo2(element){
 arrayDInfo.push(element.className)
    return arrayDInfo;

}
console.log(getDataInfo2(mainId));


console.log("PODPUNKT 3:");
//Podpunkt 3. Szukanie elementu po klasie
//
//     Znajdź element o klasie pink-color.
//     stwórz funkcję getElementText(element) do której przekaż, jako argument, znalezione elementy.
//     zwróć z funkcji tekst, znajdujący się w tym elemencie.


const classColor  = document.querySelector('.pink-color')
console.log(classColor);



function getElementText(element){

    return element.innerText;

}
console.log(getElementText(classColor));


console.log("PODPUNKT 4:");
//Podpunkt 4. Szukanie elementu po klasie
//
//     Znajdź elementy o klasie images.
//     stwórz funkcję getElementAlt(element) do której przekaż, jako argument, znalezione elementy.
//     stwórz w funkcji tablicę i wypełnij ją wartościami pobranymi z atrybutu alt obrazków.
//     Pobierz te atrybuty z przekazanych jako argument elementów.
const classImages  = document.querySelectorAll('.images')
console.log(classImages)

function getDataAlt(element){
  arrayDInfo = [];
    element.forEach(el => {

 arrayDInfo.push(el.alt)
    //console.log(el.innerText)
    })

    return arrayDInfo;

}

console.log(getDataAlt(classImages));


// Podpunkt 5. Szukanie elementu po klasie
//
//     Znajdź elementy o klasie my-link.
//     stwórz funkcję getElementHref(element) do której przekaż, jako argument, znalezione elementy.
//     stwórz w funkcji tablicę i wypełnij ją wartościami pobranymi z atrybutu href linków.
//     Pobierz te atrybuty z przekazanych jako argument elementów.
console.log("PODPUNKT 5:");

const classLink  = document.querySelectorAll('.my-link')
console.log(classLink)

function getDataHref(element){
  arrayDInfo = [];
    element.forEach(el => {

 arrayDInfo.push(el.href)

    })

    return arrayDInfo;

}

console.log(getDataHref(classLink));


 ZDARZENIAPROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW ZDARZENIA PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW 
 ZDARZENIAPROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW  ZDARZENIAPROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW 
  ZDARZENIAPROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW ZDARZENIA PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW 
  ZDARZENIA PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW  ZDARZENIA PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW  PROPAGACJA ELEMENTOW 
ZDARZENIA



// document.querySelector("button").addEventListener("click", function (e) {
//   alert("huraaa");
//   console.log(e.currentTarget);
//   console.log(e.target);
// });

// document.querySelectorAll("span")[0].addEventListener("click", function (e) {
//   console.log("nacisnieto span 1");
//   e.stopPropagation();
// });

// document.querySelectorAll("span")[1].addEventListener("click", function (e) {
//   console.log("nacisnieto span 2");
//   e.stopPropagation();
// });

document.querySelector("#box1").addEventListener("click", function (event) {
  console.log("Box 1");
  console.log(event.target);
  console.log(event.currentTarget);
  event.stopPropagation();
});

document.querySelector("#box2").addEventListener("click", function (event) {
  console.log("Box 2");
});

document.querySelector("#box3").addEventListener("click", function (event) {
  console.log("Box 3");
});

document.querySelector("#box4").addEventListener("click", function (event) {
  console.log("Box 4");
});

document.querySelector("#box4").addEventListener("click", function (event) {
  console.log("Box 4 - 2");
});

HTML:
<!DOCTYPE html>
<html>
  <head>
    <title>Parcel Sandbox</title>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="./styles.css" />
  </head>

  <body>

            <div id="box1">
                Box 1
                <div id="box2">
                    Box 2
                    <div id="box3">
                        Box 3
                    </div>
                    <div id="box4">
                        Box 4
                    </div>
                <div>
            </div>

    <!-- <button>
      <span class="color1">Te</span>
      <span class="color2">xt</span>
    </button> -->

    <script src="src/index.js"></script>
  </body>
</html>




CSS:
#box1 {
  border: 5px solid black;
  width: 500px;
  margin: 10px;
}

#box2 {
  border: 2px solid orange;
  width: 80%;
  margin: 10px;
}

#box3 {
  border: 2px solid blue;
  width: 80%;
  margin: 10px;
}

#box4 {
  border: 2px solid red;
  width: 80%;
  margin: 10px;
}

button {
  width: 200px;
  height: 125px;
  font-size: 36px;
}

.color1 {
  color: red;
}

.color2 {
  color: yellow;
}


https://codesandbox.io/s/trusting-architecture-93fuv?file=/src/styles.css 





ZDARZENIA Zadania 1-10 ZDARZENIA Zadania 1-10 ZDARZENIA Zadania 1-10 ZDARZENIA Zadania 1-10
ZDARZENIA Zadania 1-10 ZDARZENIA Zadania 1-10 ZDARZENIA Zadania 1-10 ZDARZENIA Zadania 1-10
 


// Zadanie 1 - rozwiązywane z wykładowcą
//
// Uruchom stronę index.html. Na stronie znajdują się dwa elementy o klasach parent i children Stwórz event, który po
// najechaniu na element parent pokaże element children. Zauważ, że element children ma ustawiony display: none w css. Stwórz drugi event,
//     który po zjechaniu z elementów schowa z powrotem element children. Pamiętaj o tym, aby nie chować wszystkich elementów naraz.




const parents = document.querySelectorAll('.parent');

parents.forEach(parent => {
    parent.addEventListener('mouseover', function(event) {
        event.currentTarget.querySelector('.children').style.display = 'block';
    });

    parent.addEventListener('mouseout', function(event) {
        event.currentTarget.querySelector('.children').style.display = 'none';
    });
})




// Zadanie 2
//
// Uruchom stronę przygotowaną dla zadania. Sprawdź w konsoli, czy są jakieś błędy. Następnie:
//
//     Przenieś tag <script> do sekcji <head>. Zobacz, co się zmieniło w działaniu skryptu. Spróbuj to wytłumaczyć.
//     Stwórz event DOMContentLoaded dla elementu document i przenieś kod do środka tego eventu. Czy poprawiło to sytuację?
//     Przenieś znowu tag <script> na koniec pliku - czy jest jakaś różnica?


document.addEventListener('DOMContentLoaded', function (event){
const menu = document.querySelector("#menu");
const paragraf = document.querySelector("p");

menu.classList.add("menu");
paragraf.innerHTML = "A to jest paragraf w zadaniu 2";

})

// ??ODPOWIEDZ JAKA JEST ROZNICA:
//Zdarzenie DOMContentLoaded jest uruchamiane, gdy dokument został całkowicie 
//załadowany i przeanalizowany, 
//bez oczekiwania na zakończenie ładowania arkuszy stylów, obrazów i 
//podramek (zdarzenia ładowania można użyć do wykrycia w pełni załadowanej strony).




// Zadanie 3
//
// Uruchom stronę przygotowaną dla zadania. Na stronie znajduje się przycisk.
//     Podepnij do niego event, który po kliknięciu spowoduje, że w konsoli wyświetli się napis "Hura! Działa!".

const buttonHurraClick = document.querySelector('.container');


buttonHurraClick.addEventListener("click", function (event) {
  console.log("Hurra działa!!!");

});






// Zadanie 4
//
// Uruchom stronę przygotowaną dla zadania. Na stronie znajdują się trzy przyciski i jeden licznik.
//     Napisz jeden wspólny event dla wszystkich przycisków, który spowoduje,
//     że po kliknięciu w przycisk licznik zwiększy wartość o jeden.

let counter = 0;

document.querySelectorAll('.btn').forEach(element =>{
    element.addEventListener('click', function(event){
        counter += 1;
        document.querySelector('.counter').innerText = counter

    })



})
// Zadanie 4

// const counter = document.querySelector('.counter');
//
// document.querySelectorAll('button').forEach(button => {
//
//     button.addEventListener('click', () => {
//         counter.innerText = Number(counter.innerText) + 1;
//     });
//
// });





// Zadanie 5
//
// Uruchom stronę przygotowaną dla zadania. Na stronie znajdują się trzy przyciski i trzy liczniki (elementy span o klasie counter).
// Do każdego przycisku dopisz event, który spowoduje, że po kliknięciu w przycisk przypisany do niego licznik zwiększy swoją wartość o jeden.

let counter = 0;

document.querySelectorAll('button').forEach(element =>{
    element.addEventListener('click', function(event){

event.target.parentElement.querySelector('span').innerText = Number(event.target.parentElement.querySelector('span').innerText) + 1;

    });



});




// Zadanie 6
//
// Uruchom stronę przygotowaną dla zadania. Na stronie znajdują się trzy elementy div.
//     Napisz jeden wspólny event dla nich wszystkich, który będzie zmieniał
// kolor tła tylko w klikniętym divie. Użyj do tego słowa kluczowego this.
//
// Hint: Żeby uzyskać losowy kolor użyj poniższego kodu:
//
// const randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);

document.querySelectorAll('.box').forEach(box => {

    box.addEventListener('click', function() {
        const randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
        this.style.background = randomColor;
    });

});


// Zadanie 7
//
// Uruchom stronę przygotowaną dla zadania. Na stronie znajduje się jeden element div. Napisz dla niego event,
//     który będzie wypisywał położenie kursora myszy w chwili, gdy znajduje się nad tym elementem.
//     Wyszukaj zarówno położenie kursora globalne
// (czyli odległość od górnego lewego rogu okna), jak i lokalne (czyli odległość od lewego górnego rogu elementu).



const box = document.querySelector('#box');

const gX = document.querySelector('#globalX');
const gY = document.querySelector('#globalY');
const lX = document.querySelector('#localX');
const lY = document.querySelector('#localY');

box.addEventListener('mousemove', (event) => {

    // Globalnie

    gX.innerText = `${event.clientX} px`;
    gY.innerText = `${event.clientY} px`;

    // Lokalnie

    lX.innerText = `${event.offsetX} px`;
    lY.innerText = `${event.offsetY} px`;
})




// Zadanie 8
//
// Uruchom stronę przygotowaną dla zadania. Na stronie znajdują się zagnieżdżone elementy.
//     Do każdego dopisane są eventy. Użyj metod stopPropagation i stopImmediatePropagation,  aby:
//
//     Wywoływały się eventy dla elementu pierwszego i drugiego, a nie wywoływał się event dla elementu trzeciego.
//     Wywoływały się wszystkie eventy dla elementu czwartego i pierwszy event dla elementu piątego.
//DOdac: e.stopPropagation();


<main class="container">
  <div id="element3" class="element">
    Element 3
    <div id="element2" class="element">
      Element 2
      <div id="element1" class="element">
        Element 1
      </div>
    </div>
  </div>


document.querySelector("#element1").addEventListener("click", function (e) {
  console.log("Event in #element1 fired!");
});

document.querySelector("#element2").addEventListener("click", function (e) {
  console.log("Event in #element2 fired!");
  e.stopPropagation();
});

document.querySelector("#element3").addEventListener("click", function (e) {
  console.log("Event in #element3 fired!");
});

document.querySelector("#element4").addEventListener("click", function (e) {
  console.log("Event in #element4 fired!");
});

document.querySelector("#element5").addEventListener("click", function (e) {
  console.log("Event in #element5 fired!");
  e.stopPropagation();
});

document.querySelector("#element5").addEventListener("click", function (e) {
  console.log("Second event in #element5 fired!");
});



// Zadanie 9
//
// Uruchom stronę przygotowaną dla zadania. Na stronie znajdują się dwa elementy, które pokazują wielkość okna.
//     Dopisz event do okna (element window), który spowoduje, że elementy te będą pokazywały poprawne wartości
// (innerWidth, innerHeight) nawet po przeskalowaniu okna (resize).


const windowWidth = document.querySelector('#windowWidth');
const windowHeight = document.querySelector('#windowHeight');

windowWidth.innerText = `${window.innerWidth} px`;
windowHeight.innerText = `${window.innerHeight} px`;

window.addEventListener('resize', function(event) {

    windowWidth.innerText = `${window.innerWidth} px`;
    windowHeight.innerText = `${window.innerHeight} px`;
})




// Zadanie 10
//
// Uruchom stronę przygotowaną dla zadania. Prześledź dokładnie kod i przeczytaj komentarze.
//     Skoncentruj się na każdej linijce kodu. Zastanów się nad taką sytuacją:
//     Potrzebujesz użyć elementu o id b wewnątrz funkcji innerFuncOne, żeby zmienić mu kolor. Jak to zrobisz?
//     Odpowiedź umieść w komentarzu.

const a = document.getElementById("a");
const b = document.getElementById("b");

// Tutaj this wskazuje na obiekt document (Ponieważ kontext wywołania funkcji
// addEventListener to właśnie document)
console.log("obiekt document: ", this);

a.addEventListener("click", function (event) {
  // Tutaj this wskazuje na element DOM o id a
  console.log("a: ", this);
});

b.addEventListener("click", function (event) {
  // Tutaj this wskazuje na element DOM o id b
  console.log("b: ", this);


  function innerFuncOne() {
    // Tutaj this wskazuje na element Window, bo funkcja została
    //wywołana bez żadnego kontekstu.
    console.log("innerFuncOne: ", this);
  }

  innerFuncOne();

});


 DOM PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE
  PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE
   PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE PORUSZANIE SIE PO DRZEWIE

// Zadanie 1 - rozwiązywane z wykładowcą
//
// Znajdź i zapisz do zmiennych następujące elementy:
//
//     Element o klasie first -> jego pierwsze dziecko -> jego trzecie dziecko.
//     Element o id second -> jego rodzic -> jego czwarte dziecko.
//     Element o atrybucie data-ex nastawionym na wartość third -> jego dziadek -> jego ostatnie dziecko ->
//     jego pierwsze dziecko -> jego środkowe dziecko (żeby otrzymać środkowy element, podziel liczbę dzieci przez dwa i zaokrąglij w dół).
//     Div o klasie forth -> jego rodzic -> jego pierwsze dziecko o tagu article -> jego drugie dziecko o tagu <p>.
//
// Wszystkie te elementy mają atrybut data-answer nastawiony na numer zadania, dla którego są odpowiedzią.

const first = document.querySelector('.first').children[0].children[2];
console.log(first.dataset.answer);

const second = document.querySelector('#second').parentElement.children[3];
console.log(second.dataset.answer);

const helper = document.querySelector('[data-ex="third"]').parentElement.parentElement.lastElementChild.firstElementChild;

const third = helper.children[Math.floor(helper.children.length / 2)];
console.log(third.dataset.answer);

const forth = document.querySelector('.forth').parentElement.querySelector('article').querySelectorAll('p')[1];
console.log(forth.dataset.answer);




// Zadanie 2 - rozwiązywane z wykładowcą
//
// W pliku znajduje się kilka przycisków (są to odpowiednio ostylowane linki). Po kliknięciu w którykolwiek z nich -
// element, który znajduje się bezpośrednio po nim, powinien zniknąć (jeżeli był widoczny) lub się pojawić (jeżeli był niewidoczny). R
// ozwiązanie musi spełniać następujące założenia:
//
//     Na wszystkie przyciski musi być założony ten sam event.
//     Następny element ma być wyszukiwany zależnie od położenia this.
//     Kod musi działać poprawnie i nie generować błędów (pamiętaj o sprawdzeniu, czy następny element nie równa się null).

document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function(event) {

        // event.target === this;

        if (this.previousElementSibling !== null) {

            if (this.previousElementSibling.style.display === 'none') {
                this.previousElementSibling.style.display = 'block';
            } else {
                this.previousElementSibling.style.display = 'none';
            }

        }

    })
})





// Zadanie 3
//
// W pliku znajduje się kilka przycisków (są to odpowiednio ostylowane linki).
// Po kliknięciu w którykolwiek z nich jego rodzic ma zmienić kolor tła (na losowy).
// Rozwiązanie musi spełniać następujące założenia:
//
//     Na wszystkie przyciski musi być założony ten sam event.
//     Rodzic ma być wyszukiwany zależnie od położenia this.
//     Kolor tła musi być losowy.
//
// Hint: Żeby uzyskać losowy kolor, użyj poniższego kodu:
//
// const randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);

document.querySelectorAll('.btn').forEach(element => {
    element.addEventListener('click', function() {
 
        this.parentElement.style.background = "#" + Math.floor(Math.random()*16777215).toString(16);
 
    })
})





 TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW 
  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  
   TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW  TWORZENIE ELEMENTOW 



// Tworzenie, klonowanie, usuwanie

// Tworzenie nowych elementów
const newHeading = document.createElement('h1');
newHeading.innerText = 'My new heading';
newHeading.classList.add('heading-class');
// Klonowanie elementów
<div class="myClass">
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
    </ul>
    <h1 class="heading-class">My new heading</h1>
</div>

document.querySelector('.myClass').appendChild(newHeading);
document.querySelector('.myClass').prepend(newHeading);
// prepend- doda jako pierwsze dziecko

const newDiv = document.querySelector('div').cloneNode(false);

document.querySelector('.myClass').insertBefore(newHeading, document.querySelector('ul li'));
// replaceChild
document.querySelector('.myClass').replaceChild(newHeading, document.querySelector('ul'));

const myElement = document.querySelector('#myId');
myElement.parentElement.removeChild(myElement);

myElement.remove();

document.querySelector('.myClass').parentElement.removeChild(document.querySelector('.myClass'));
document.querySelector('.myClass').remove();






// Zadanie 1 - rozwiązywane z wykładowcą
//
// Na stronie znajduje się tabela z zamówieniami. Przy każdym zamówieniu znajduje się przycisk, który służy do usuwania tego zamówienia.
//     Dopisz do niego odpowiedni event, który spowoduje, że dane zamówienie zniknie z tablicy.
//     Spróbuj zrobić to w taki sposób, żeby wszystkie przyciski korzystały z tego samego eventu (użyj this).


// Zadanie 1
<body>

<main class="container">
  <table class="table" id="orders">
    <thead>
    <tr>
      <th>
        Numer zamówienia
      </th>
      <th>
        Przedmiot
      </th>
      <th>
        Ilość
      </th>
      <th>Akcja</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td>
        74761
      </td>
      <td>
        Komputer
      </td>
      <td>
        10
      </td>
      <td>
        <a href="#" class="btn btn-danger deleteBtn">Usuń przedmiot</a>
      </td>
    </tr>
    <tr>
      <td>
        12532
      </td>
      <td>
        Klawiatura
      </td>
      <td>
        40
      </td>
      <td>
        <a href="#" class="btn btn-danger deleteBtn">Usuń przedmiot</a>
      </td>
    </tr>
    </tbody>
  </table>

</main>
</body>

document.querySelectorAll('.deleteBtn').forEach(button => {
    button.addEventListener('click', function() {

        this.parentElement.parentElement.remove();

        // Przed ES6
        // this.parentElement.parentElement.removechild(this.parentElement.parentElement);

    })
})





// Zadanie 2
//
// Na stronie znajduje się przycisk. Musisz dopisać do niego event
// w taki sposób, żeby po kliknięciu w niego został usunięty ze strony.
<body>

<main class="container">
  <button id="remove" class="btn btn-danger btn-lg btn-block mt-4">Usuń mnie!</button>
</main>

</body>




const remove = document.querySelector('#remove')
    remove.addEventListener('click', function() {

        this.remove();
//lub     event.target.remove();
// 
//     // event.target.parentElement.removeChild(event.target);
            })






// Zadanie 3
//
// Na stronie przypisanej do zadania znajduje się lista i przycisk. Dopisz odpowiednie eventy do nich w taki sposób,
//     żeby po kliknięciu w przycisk dodał się nowy element do listy.
//     Element powinien mieć w sobie informacje na temat tego, ile elementów jest w liście w chwili jego dodania.



const addElement = document.querySelector('#add')


let counter = 1;
    addElement.addEventListener('click', function(event) {

    const newHeading = document.createElement('ul');
    counter ++;
    newHeading.innerText = `Element ` + counter;
    event.target.parentElement.parentElement.querySelector('ul').appendChild(newHeading);
    document.querySelector('.list-group-item').innerText = 'Element 1 - w chwili dodania było ' + counter-1 +' elementów'


            })



//Marceli dokładniej:

// Zadanie 3

const button = document.querySelector('#add');

button.addEventListener('click', (e) => {

    const list = document.querySelector('#menu');

    // Klonowanie

    // const listElement = document.querySelector('.list-group-item').cloneNode(true);

    // Tworzenie od "0"

    const listElement = document.createElement('li');
    listElement.className = 'list-group-item';
    // listElement.classList.add('list-group-item');

    listElement.innerText = `Element ${list.children.length + 1} - w chwili dodania było ${list.children.length} elementów`;

    list.appendChild(listElement);
})






    // Zadanie 4
//
// Na stronie znajduje się tabela z informacjami na temat zamówień (z dwoma już wprowadzonymi zamówieniami).
// Poniżej znajduje się formularz do wypełnienia nowego zamówienia.
//     Napisz event, który pobierze informacje z inputów (el.value) i wprowadzi nowy wpis do tabeli.

 

{/* <tr>
    <td>
    74761
    </td>
    <td>
    Komputer
    </td>
    <td>
    10
    </td>
</tr> */}

const button = document.querySelector('#add');

button.addEventListener('click', (e) => {

    const orderId = document.querySelector('#orderId').value;
    const item = document.querySelector('#item').value;
    const quantity = document.querySelector('#quantity').value;

    const newRow = document.createElement('tr');

    const orderTd = document.createElement('td');
    orderTd.innerText = orderId;

    const itemTd = document.createElement('td');
    itemTd.innerText = item;

    const quantityTd = document.createElement('td');
    quantityTd.innerText = quantity;

    newRow.appendChild(orderTd);
    newRow.appendChild(itemTd);
    newRow.appendChild(quantityTd);

    document.querySelector('tbody').appendChild(newRow);

    document.querySelector('#orderId').value = '';

})






// Zadanie 5
//
// Na stronie znajduje się lista z wpisami i przycisk. Napisz taki event,
//     żeby po kliknięciu w przycisk z listy zostały usunięte wszystkie jej dzieci.
//     Element ul#list powinien pozostać na stronie.
 
const button = document.querySelector('#remove');

const list = document.querySelector('#list');

button.addEventListener('click', (e) => {

    const listWithoutChilds = list.cloneNode(false);

    document.querySelector('.container').replaceChild(listWithoutChilds, list);

    // for (let i = list.children.length - 1; i >= 0; i--) {
    //     list.children[i].remove();
    // }

    // Array.from(list.children).forEach(child => {
    //     child.remove();
    // })

})




// Zadanie 6
//
// Na stronie znajdują się dwie listy. Każdy z wpisów jest "klikalny".
// Napisz taki kod JavaScript, żeby po kliknięciu danego elementu listy, został on przeniesiony na drugą listę.
// Pamiętaj, że element może być przenoszony wiele razy (np. z listy 1 do listy 2, a potem z powrotem do listy 1).

const list1 = document.querySelector('#list1');
const list2 = document.querySelector('#list2');

document.querySelectorAll('a').forEach(element => {

    element.addEventListener('click', (event) => {

        if (event.currentTarget.parentElement.id === 'list1') {
            // do list2
            list2.appendChild(event.currentTarget);
        } else {
            // do list1
            list1.appendChild(event.currentTarget);
        }

    })

})





 FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE
  FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE
   FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE FORMULARZE







// Zadanie 1 - rozwiązywane z wykładowcą
// Przy rozwiązywaniu tego zadania pamiętaj, aby teksty wypisywane w elementach #error-message i #success-message były identyczne jak w treści zadania. Elementy te mają nadane klasy d-none które je ukrywają. Należy tę klasę usunąć aby pokazać odpowiednie pole.
// Na stronie znajduje się formularz rejestracyjny. Napisz walidację tego formularza w taki sposób, żeby informacja o sukcesie pojawiła się tylko i wyłącznie wtedy, kiedy spełnione zostaną następujące warunki:
//
//     Email zawiera w sobie @.
//         Jeżeli warunek nie jest spełniony, wypisz w polu #error-message informację: Email musi posiadać znak @,
//     Imię jest dłuższe niż 2 znaki.
//         Jeżeli warunek nie jest spełniony, wypisz w polu #error-message informację: Twoje imię jest za krótkie,
//     Nazwisko jest dłuższe niż 2 znaki.
//         Jeżeli warunek nie jest spełniony, wypisz w polu #error-message informację: Twoje nazwisko jest za krótkie,
//     Hasło i hasło drugie są identyczne, ale nie puste.
//         Jeżeli warunek nie jest spełniony, wypisz w polu #error-message informację: Hasła nie są takie same lub puste,
//     Checkbox musi być zaznaczony.
//         Jeżeli warunek nie jest spełniony, wypisz w polu #error-message informację: Musisz zaakceptować warunki.
//
// Jeżeli walidacja przebiegła poprawnie, wpisz w polu #success-message informację: Formularz wysłany!.
// Zadanie 1 - Formularza

const errorMsg = document.querySelector('#error-message');
const successMsg = document.querySelector('#success-message');

document.querySelector('form').addEventListener('submit', (event) => {

    event.preventDefault();

    // Jedna po drugiej
    // const emailValue = document.querySelector('#email').value;

    const formFields = event.currentTarget.elements;

    function showError(msg) {
        errorMsg.innerText = msg;
        errorMsg.classList.remove('d-none');
    }

    // alternatywnie formField.email.value...
    if (!formFields[0].value.includes('@')) {
        showError('Email musi posiadać znak @');
    } else if (formFields[1].value.length <= 2) {
        showError('Twoje imię jest za krótkie');
    } else if (formFields[2].value.length <= 2) {
        showError('Twoje nazwisko jest za krótkie');
    } else if (formFields[3].value === '' || formFields[3].value !== formFields[4].value) {
        showError('Hasła nie są takie same lub puste');
    } else if (formFields[5].checked === false) {
        showError('Musisz zaakceptować warunki');
    } else {
        errorMsg.classList.add('d-none');

        successMsg.innerText = 'Formularz wyslany';
        successMsg.classList.remove('d-none');
    }

})




// Zadanie 2
//
// Na stronie znajduje się formularz do zamówienia. Jest w nim sekcja odpowiedzialna za wystawienie faktury.
// Napisz kod JavaScript, który spowoduje, że sekcja ta jest widoczna tylko
// i wyłącznie wtedy, kiedy zaznaczony jest checkbox "Chcę otrzymać fakturę".
// Ma to również działać przy starcie strony: sekcja z danymi do faktury powinna być ukryta!

const invoiceData = document.querySelector('#invoiceData');
invoiceData.style.display = 'none';

const checkbox = document.querySelector('#invoice');

checkbox.addEventListener('change', (event) => {

    if (event.target.checked) {
        invoiceData.style.display = 'block';
    } else {
        invoiceData.style.display = 'none';
    }

})


// Zadanie 3
//
// Na stronie znajduje się select i trzy obrazki. Każdy z obrazków jest przypisany do jednego z wyborów w selekcie.
//     Napisz kod javaScript w taki sposób, żeby widoczny był tylko ten obrazek, który został wybrany.
// Na start powinien być wyświetlony obrazek Windows. Następnie po wyborze innego i zatwierdzeniu przyciskiem Zatwierdź zmień wyświetlany obrazek.
 
const images = document.querySelectorAll('img');

// 0 - Windows
// 1 - MacOS
// 2 - Ubuntu

images[1].style.display = 'none';
images[2].style.display = 'none';

function hideAll() {
    images[0].style.display = 'none';
    images[1].style.display = 'none';
    images[2].style.display = 'none';
}

document.querySelector('button').addEventListener('click', (event) => {

    event.preventDefault();

    const selectedValue = document.querySelector('select').value;

    if (selectedValue === 'Windows') {
        hideAll();
        images[0].style.display = 'block';
    } else if (selectedValue === 'MacOS') {
        hideAll();
        images[1].style.display = 'block';
    } else {
        hideAll();
        images[2].style.display = 'block';
    }

})




// Zadanie 4
//
// Na stronie znajduje się tabela z wynikami w lokalnych mistrzostwach piłkarskich. Poniżej znajduje się formularz, który wypełniają wszyscy sędziowie po ukończonych rozgrywkach.
// Napisz kod JavaScript w taki sposób, żeby po wybraniu odpowiednich drużyn nastąpiła walidacja:
//     Obie drużyny muszą być różne.
//     Liczba goli powinna być nieujemna.
// Jeżeli formularz zostanie zweryfikowany poprawnie, odpowiednia informacja o wyniku spotkania powinna pojawić się w tabeli jako kolejny wiersz.
 
document.querySelector('button').addEventListener('click', (event) => {

    event.preventDefault();

    const formElements = document.querySelector('form').elements;

    // <tr>
    //   <td>Drużyna 1</td>
    //   <td>Drużyna 2</td>
    //   <td>Wynik:</td>
    // </tr>

    if (formElements[0].value === '' || formElements[2].value === '') {
        alert('error');
        return;
    }

    if (formElements[1].value < 0 || formElements[3].value < 0) {
        alert('error');
        return;
    }

    const newTr = document.createElement('tr');

    const team1 = document.createElement('td');
    team1.innerText = formElements[0].value;
    const team2 = document.createElement('td');
    team2.innerText = formElements[2].value;
    const result = document.createElement('td');
    result.innerText = `${formElements[1].value} - ${formElements[3].value}`;

    newTr.appendChild(team1);
    newTr.appendChild(team2);
    newTr.appendChild(result);

    document.querySelector('tbody').appendChild(newTr);

})


// Walidacja karty kredytowej - dodatkowe
//
// Zadanie polega na walidacji kart kredytowych wpisywanych w formularz na stronie.
//     Walidacja ma następować w czasie rzeczywistym (czyli po wprowadzeniu każdej cyfry).
// W elemencie #type znajdują się trzy elementy reprezentujące odpowiednie firmy obsługujące karty kredytowe.
//     Powinna być wyświetlona tylko ikona tego rodzaju karty której numer wpisujemy w polu obok, jak tylko jest możliwe jej ustalenie
// Poprawność karty ma być pokazana po wpisaniu odpowiedniej liczby cyfr - zmiana koloru ikony na zieloną.
// Zasady rozpoznawania kart:
//
//     Karty Visa zaczynają się od cyfry 4.
//     Karty Mastercard zaczynają się od cyfry 5.
//     Karty American Express zaczynają się od cyfry 3. Następną cyfrą musi być 4 lub 7.
//
// Zasady walidacji kart:
//
//     Karty Visa mają od 13 do 16 cyfr.
//     Karty Mastercard mają równo 16 cyfr.
//     Karty American Express mają równo 15 cyfr.
//
// Zasady walidacji kart są uproszczone (nie powinniście ich stosować w rzeczywistych projektach).
// Jeżeli chcesz poznać prawdziwe zasady walidacji kart kredytowych, to są one opisane tutaj: https://en.wikipedia.org/wiki/Bank_card_number, https://en.wikipedia.org/wiki/Luhn_algorithm.
// Zadanie dodatkowe

// Zasady rozpoznawania kart:
// Karty Visa zaczynają się od cyfry 4.
// Karty Mastercard zaczynają się od cyfry 5.
// Karty American Express zaczynają się od cyfry 3. Następną cyfrą musi być 4 lub 7.
// Zasady walidacji kart:
// Karty Visa mają od 13 do 16 cyfr.
// Karty Mastercard mają równo 16 cyfr.
// Karty American Express mają równo 15 cyfr.

function hideIcons() {
    document.querySelector('#visa-icon').style.display = 'none';
    document.querySelector('#amex-icon').style.display = 'none';
    document.querySelector('#mastercard-icon').style.display = 'none';
}

function colorizeIcon(selector) {
    document.querySelector(selector).style.color = 'green';
}

function uncolorizeIcons() {
    document.querySelector('#visa-icon').style.color = 'dimgray';
    document.querySelector('#amex-icon').style.color = 'dimgray';
    document.querySelector('#mastercard-icon').style.color = 'dimgray';
}

hideIcons();

const input = document.querySelector('#cardNumber');

input.addEventListener('input', (event) => {

    const firstChar = event.target.value[0];
    const secondChar = event.target.value[1];

    if (firstChar === '4') {
        // Visa
        document.querySelector('#visa-icon').style.display = 'block';
        if (event.target.value.length >= 13 && event.target.value.length <= 16) {
            colorizeIcon('#visa-icon');
        } else {
            uncolorizeIcons();
        }
    } else if (firstChar === '5') {
        // Mastercard
        document.querySelector('#mastercard-icon').style.display = 'block';
        if (event.target.value.length === 16) {
            colorizeIcon('#mastercard-icon');
        } else {
            uncolorizeIcons();
        }
    } else if (firstChar === '3' && (secondChar === '4' || secondChar === '7')) {
        // American Express
        document.querySelector('#amex-icon').style.display = 'block';
        if (event.target.value.length === 15) {
            colorizeIcon('#amex-icon');
        } else {
            uncolorizeIcons();
        }
    } else {
        hideIcons();
    }

});






 SLIDER  SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER
  SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER
   SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER SLIDER

// Slider
//
// Twoim zadaniem jest stworzenie prostego slidera. Realizacja podzielona jest na punkty.
// Pamiętaj, żeby trzymać się dokładnie ich treści i wykonywać je po kolei.
// Punkt 1
//
// Zapoznaj się z kodem HTML i CSS dodanym do zadania. Do zrobienia slidera zazwyczaj
// używany odpowiednio ostylowanej listy, w której znajdują się obrazki.
// Lista zazwyczaj spełnia następujące zależności:
//
//     Nie ma żadnych styli.
//     Ma szerokość i wysokość odpowiednią do wyświetlenia jednego obrazka.
//     Wszystkie obrazki mają tę samą szerokość i wysokość.
//     Wszystkie obrazki poza jednym są niewidoczne.
//
// Dodaj w odpowiednie miejsce klasę slider w kodzie HTML. ?? Odpowiedz:<div class="slider">??

// Punkt 2
// Przygotuj do pracy plik app.js. Następnie znajdź następujące elementy i zapisz je do zmiennych:
//
//     Guzik next.
//     Guzik prev.
//     Wszystkie elementy listy (zapisz do tablicy).

 document.querySelector('div').classList.add('slider');

const prevPicture = document.querySelector('#prevPicture')
const nextPicture = document.querySelector('#nextPicture')

const pictures = document.querySelectorAll('li')


let picturesArray = []


//Filling pictures index into array
pictures.forEach(function (picture ){


    picturesArray.push(picture)

    console.log(picture) // no matter check
    console.log(picture.src)  // no matter check

})



// Dodaj też zmienną liczbową, która będzie określała indeks obrazka, który jest aktualnie widoczny (na początku będzie to pierwszy obrazek - czyli zmienna będzie wskazywała na indeks 0).
//
// Wypisz zmienne w konsoli, żeby upewnić się, czy zawierają poprawne dane.
// Punkt 3
console.log("TABLICA:")  // no matter check
console.log(picturesArray) // no matter check
console.log("FOTA nr 2:") // no matter check
console.log(picturesArray[1]) // no matter check




// const newVisibleClass = document.createElement('.visible');
// document.querySelector('img').appendChild(newVisibleClass);

// Po dodaniu klasy slider zniknęły nam wszystkie obrazki. Dodaj do zerowego elementu naszej listy klasę visible.
// Użyj odpowiednich zmiennych:
//
//     tablicy z elementami listy,
//     zmiennej, która określa widoczny element. Po wejściu na stronę pierwszy obrazek powinien być widoczny.
picturesArray[0].classList.add('visible'); // make picture [0] visible
// console.log(picturesArray[0].classList)
// Punkt 4
//
// Dodaj do guzików eventy reagujące na kliknięcie. Na początku mają tylko wypisywać w konsoli informacje o kliknięciu.


// Punkt 5
//
// W evencie odpowiadającym za pokazanie następnego obrazka wykonaj następujące czynności:
//
//     Zabierz obecnie widocznemu obrazkowi klasę visible.
//     Zwiększ zmienną trzymającą indeks obrazka, który jest aktualnie widoczny o jeden.
//     Dodaj obrazkowi, który powinien być widoczny, klasę visible. Użyj odpowiednich zmiennych (czyli tablicy z elementami listy oraz zmiennej, która określa, który element jest widoczny).
//
// Punkt 6
//
// Wykonaj czynności w evencie dla guzika pokazującego poprzedni obrazek analogicznie do punktu 5.
// Punkt 7
//
// Sprawdź, jak działa Twoja strona. Widzisz jakieś problemy związane ze sliderem? Napisz.
// Punkt 8
//
// W poprzednim punkcie powinieneś zauważyć, że po wielokrotnym naciśnięciu guzika do przodu (albo do tyłu) obrazki znikają ze strony. Dzieje się tak dlatego, że zmienna określająca numer widocznego obrazka przyjmuje niepoprawną wartość (mniejszą od zera lub większą niż liczba elementów w naszej tablicy). Jak temu zaradzić? W eventach dodaj if-a, który sprawdzi, czy wartość nie wyszła poza zakres. Jeżeli tak się stało, to program ma nastawić poprawną wartość:
//
//     liczbą jest ujemna -> ostatni element,
//     liczba równa się liczbie elementów lub jest większa -> 0.


const nextButton = document.querySelector('#nextPicture');

console.log("dlugosc tablicy :" + picturesArray.length)
let index = 0;

nextButton.addEventListener('click', event => {
    picturesArray[index].classList.remove('visible');
    index++;
console.log(index) // no matter check



    if (index === picturesArray.length)  {

index = 0
picturesArray[index].classList.add('visible');

    } else {

        picturesArray[index].classList.add('visible');
        picturesArray[index-1].classList.remove('visible');
    }

})

//PRevious Button will show previous picture, after reach index -1
// and below will show latest available picture

const prevButton = document.querySelector('#prevPicture');

console.log("dlugosc tablicy :" + picturesArray.length)


prevButton.addEventListener('click', event => {

    console.log(index) // no matter check
picturesArray[index].classList.remove('visible');
index --;
console.log(index) // no matter check

if (index <= -1){
console.log(index) // no matter check

    index = picturesArray.length -1;
    picturesArray[index].classList.add('visible');

} else {
    picturesArray[index].classList.add('visible');
}



})







Obsługa REST API

Wstęp do warsztatu wyjaśnia czym ogólnie jest API. Pora omówić to konkrete API, z którego nasza aplikacja będzie korzystać. Tabela poniżej pokazuje jakie funkcjonalności oferuje nam backend, pozostała część artykułu szczegółowo omawia sposób użycia niektórych z nich.
Dostępne adresy
Adres   Metoda  Opis    Struktura danych wysyłanych
/api/tasks  GET     Pobieranie zadań    
/api/tasks  POST    Dodawanie zadania do wykonania  {title: "", description: "", status: ""}
/api/tasks/:id  PUT     Aktualizowanie zadania do wykonania     {title: "", description: "", status: ""}
/api/tasks/:id  DELETE  Usuwanie zadania    
/api/tasks/:id/operations   GET     Pobieranie zadania wraz z operacjami    
/api/tasks/:id/operations   POST    Dodawanie operacji do zadania   {description: "", timeSpent: 0}
/api/operations/:id     GET     Pobieranie pojedynczej operacji     
/api/operations/:id     PUT     Aktualizowanie pojedynczej operacji     {description: "", timeSpent: 0}
/api/operations/:id     DELETE  Usuwanie operacji   


 FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE  
  FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE  
   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE  
    FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE   FETCH  PROMISE  
  

// Fetch sciaga

const myObject = {
    name: 'Marceli',
    age: 31,
};

fetch('URL', {
    method: 'GET', // POST, PATCH, PUT, DELETE (default: GET)
    headers: {
        'Autorization': 'Bearer XXXYYYZZZ'
    },
    body: JSON.stringify(myObject)
})
.then(resp => resp.json) // resp.text()
.then(data => {
    console.log(data);
})
.catch(error => {
    console.error(error);
});








// Zadanie 1 - rozwiązywane z wykładowcą
//
// Stworzysz teraz aplikację do pobierania informacji na temat książki o danym numerze isbn.
// W pliku index.html masz przygotowany formularz.
// Podepnij do niego zdarzenie, aby w momencie zatwierdzania formularza wysłał zapytanie do API o książkę o danym numerze isbn.
// Wykorzystaj do tego fetch() i wykonaj zapytanie na adres otwartego API:
//     https://www.googleapis.com/books/v1/volumes?q=isbn:{numerISBN}
// gdzie zamiast numerISBN pobrany z formularza
// Otrzymasz w odpowiedzi JSON, a z niego obiekt, w którym interesuje Cię tablica pod kluczem items, a w niej pierwszy element - obiekt z informacją o książce.
// Po pobraniu tych danych utwórz za pomocą JavaScript element h2
// z tytułem (jest w tym obiekcie pod kluczem volumeInfo.title i wstaw go do elementu o klasie .book-info.
// Przetestuj formularz np. dla isbn = 0747532699

// Zadanie 1

document.querySelector('form').addEventListener('submit', (event) => {

    event.preventDefault();

    const input = document.querySelector('input').value;

    fetch(`https://www.googleapis.com/books/v1/volumes?q=isbn:${input}`)
        .then(resp => resp.json())
        .then(data => {
            // console.log(data);
            // console.log(data.items[0].volumeInfo.title);

            const newHeading = document.createElement('h2');
            newHeading.innerText = data.items[0].volumeInfo.title;

            newHeading.className = 'volumeInfo title';

            document.querySelector('.book-info').appendChild(newHeading);
        })
        .catch(error => {
            console.error(error);
        });

})


// Zadanie 2
//
// Zadanie polega na wczytaniu danych z adresu: https://pokeapi.co/api/v2/pokemon i wyświetlenie ich nazw w kolejnych li.
// Przydatne informacje:
//
//     użyj odpowiedniej metody HTTP, jeśli jest potrzebna,
//     użyj odpowiednich metod informujących użytkownika o statusie żądania (metody then(), catch()),
//     sprawdź w konsoli, jak wyglądają wczytywane dane, czy jest to tablica, string, JSON?
//     jeśli dane zostaną poprawnie wczytane, w pętli utwórz elementy li do którego wstawisz nazwę pokemona i li wstawisz do ul
//
// Dla chętnych
//
// API zwraca nam tylko określoną ilość pokemonów +
// linki do API aby pobrać poprzednią / następną póle. Dorób paginację i pobieranie kolejnych pokemonów.


fetch('https://pokeapi.co/api/v2/pokemon')
    .then(resp => resp.json())
    .then(data => {

        console.log(data);

        const list = document.querySelector('.list');

        data.results.forEach((pokemon, index) => {

            const pokemonElement = document.createElement('li');
            pokemonElement.innerText = pokemon.name.toUpperCase();

            const pokemonImage = document.createElement('img');
            pokemonImage.setAttribute('src', `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${index + 1}.png`)

            pokemonElement.appendChild(pokemonImage);

            list.appendChild(pokemonElement);

        })

    })


// POPRAWIONA Z NEXTPAGE


// Zadanie 2 - wersja rozszerzona

getData('https://pokeapi.co/api/v2/pokemon');

function getData(url) {

    const listClone = document.querySelector('.list');
    document.querySelector('body').replaceChild(listClone.cloneNode(false), listClone);

    if (document.querySelector('.prevPage')) {
        document.querySelector('.prevPage').remove();
    }

    fetch(url)
        .then(response => {
            return response.json();
        })
        .then(data => {
            console.log(data);

            const list = document.querySelector('.list');

            data.results.forEach((pokemon) => {
                const pokeElement = document.createElement('li');
                const pokeImg = document.createElement('img');

                pokeElement.innerText = pokemon.name.toUpperCase();
                const pokeIndex = pokemon.url.split('/');
                pokeImg.setAttribute('src', `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokeIndex[pokeIndex.length - 2]}.png`);

                pokeElement.appendChild(pokeImg);
                list.appendChild(pokeElement);
            });

            if (data.previous !== null) {
                if (document.querySelector('.prevPage')) {
                    document.querySelector('.prevPage').remove();
                }

                const prevPageElem = document.createElement('a');
                prevPageElem.classList.add('prevPage');
                prevPageElem.innerText = 'Prev page';

                prevPageElem.addEventListener('click', function (event) {
                    event.preventDefault();
                    getData(data.previous);
                });

                document.querySelector('body').prepend(prevPageElem);
            }

            if (data.next !== null) {
                if (document.querySelector('.nextPage')) {
                    document.querySelector('.nextPage').remove();
                }

                const nextPageElem = document.createElement('a');
                nextPageElem.classList.add('nextPage');
                nextPageElem.innerText = 'Next page';

                nextPageElem.addEventListener('click', function (event) {
                    event.preventDefault();
                    getData(data.next);
                });

                document.querySelector('body').prepend(nextPageElem);
            }

        })
        .catch(error => {
            console.error(error);
        })
}






// Zadanie 3
// Pod adresem https://fer-api.coderslab.pl/v1/holidays jest przechowywana baza świąt państwowych różnych krajów. Aby z niej skorzystać należy przesłać specjalny klucz (key): e92601251-c0a2-4s63-v73f-54041195480f. API wymaga również podania kodu kraju (country). Do dyspozycji mamy trzy:
//
//     Polska (PL)
//     Wielka Brytania (GB)
//     Stany Zjednoczone (US)
//
// Zasób    Metoda  Dane    Opis
// /holidays    GET     key, country    Pobranie świąt w danym kraju
// Za pomocą funkcji fetch() wczytaj do elementu ul wszystkie daty świąt (jako elementy li). Aby poprawnie wczytać dane w funkcji fetch()
// trzeba w odpowiedni sposób skonstruować adres URL naszego żądania, np.: https://fer-api.coderslab.pl/v1/holidays?key=e92601251-c0a2-4s63-v73f-54041195480f&country=PL.
//
// Każdą nazwę święta wczytaj do elementu li jako element h3.holiday-name, a jego datę wczytaj do elementu li jako element date.holiday-date.
// Podpowiedzi:
//     Wczytaj dane i zobacz w konsoli jak wyglądają, pozwoli Ci to ustalić czego należy użyć, aby dostać się do nazw i dat świąt. Możesz tutaj wykorzystać też zakładkę Network.
//
// Dodatkowe
// Dorób na stronie formularz, który zawiera element select w którym będzie można wybrać z którego kraju mają pojawiać się święta. Wybór jakiegoś elementu option ma spowodować
// ponowne wysłanie zapytania i utworzenie na nowo elementów listy. Domyślnie wybraną opcją ma być PL.
// Dane pochodzą z serwisu: https://holidayapi.com.


// Zadanie 3

fetch('https://fer-api.coderslab.pl/v1/holidays?key=e92601251-c0a2-4s63-v73f-54041195480f&country=PL')
.then(resp => resp.json())
.then(data => {

    console.log(data);

    data.holidays.forEach(holiday => {

        const holidayLi = document.createElement('li');

        const holidayH3 = document.createElement('h3');
        holidayH3.className = 'holiday-name';
        const holidayDate = document.createElement('date');
        holidayDate.className = 'holiday-date';

        holidayH3.innerText = holiday.name;
        holidayDate.innerText = holiday.date;

        holidayLi.appendChild(holidayDate);
        holidayLi.appendChild(holidayH3);

        document.querySelector('body').appendChild(holidayLi);

    })

})




// Zadanie 1
//
// Na stronie znajduje się formularz do zamówienia pizzy. W formularzu znajduje się pole z
// checkboxami, w którym użytkownik może wybrać sobie dodatki.
//
// Cena każdego z dodatków jest trzymana w atrybucie data-price.
//
// Napisz takie eventy, żeby po zaznaczeniu checkboxa wyświetlała się poprawna kwota
// zamówienia oraz po wysłaniu formularza wewnątrz elementu order-info wyświetliła się
// następująca informacja: "Do zapłaty: [odpowiednia kwota]", gdzie [odpowiednia kwota] to
// wartość zamówienia (cena za dodatki + 35zł podstawy za pizze). Pamiętaj o tym, że kliknięcie
// w przycisk wywołuje domyślną akcję przeładowania strony. Zablokuj tą akcję, aby móc zobaczyć
// wpisaną informację do elementu order-info.
//
// Zwróć uwagę na dwa specjalne przyciski:
//
//     Wyczyść - powinien odznaczyć wszystkie opcje,
//     Wszystkie dodatki - powinien zaznaczyć wszystkie opcje


const priceInner = document.querySelector('#price')
const checkboxes = document.querySelectorAll('[type=checkbox]');
const checkboxOne = document.querySelector('.form-check-input');
//const checkbox = document.querySelectorAll('dataset');
 console.log(checkboxes)
let sumOfAdditions = 0;
const pizzaCost = Number(35) ;



//EVENT CHANGE BOX AND SUM OF PRODUCTS
console.log("EVENT CHANGE BOX:")
// Use Array.forEach to add an event listener to each checkbox.
checkboxes.forEach(function(check) {


  check.addEventListener('change', function() {


    enabledSettings =
      Array.from(checkboxes) // Convert checkboxes to an array to use filter and map.
      .filter(i => i.checked) // Use Array.filter to remove unchecked checkboxes.
      .map(i => i.dataset.price) // Use Array.map to extract only the checkbox values from the array of objects.




    console.log("Checked:" + enabledSettings)

        //SUMA DODATKÓW
    sumOfAdditions = enabledSettings.reduce(function(total, item) {
    return Number(total) + Number(item);
    });

    const priceInner = document.querySelector('#price')
      priceInner.innerText = parseFloat(sumOfAdditions).toFixed( 2 ); //Parse float
    console.log(`Suma dodatków: ${sumOfAdditions}`)



  })





       //SUBMIT BUTTON
const form = document.querySelector('form');
const orderInfo = document.querySelector('.order-info');


form.addEventListener('submit', event => {
  event.preventDefault();
orderInfo.innerText = `Do zapłaty: ${parseFloat(sumOfAdditions).toFixed( 2 )} zł za dodatki  + ${pizzaCost} zł za podstawę  pizzy
 Razem: ` + parseFloat(sumOfAdditions+pizzaCost).toFixed( 2 );
})



    //FILL CHECKBOXES BUTTON
  const fillButton = document.querySelector('.btn-group').children[0];


fillButton.addEventListener('click', event => {
checkboxes.forEach(function(check) {

    enabledSettings =
     Array.from(checkboxes) // Convert checkboxes to an array to use filter and map.
      .filter(i => i.checked = true)
        .map(i => i.dataset.price)

 sumOfAdditions = enabledSettings.reduce(function(total, item) {
    return Number(total) + Number(item);
    });

    //const priceInner = document.querySelector('#price')
      priceInner.innerText = parseFloat(sumOfAdditions).toFixed( 2 ); //Parse float
    console.log(`Suma dodatków: ${sumOfAdditions}`)
})


})

//CLEAN CHECKBOXES BUTTON

  const cleanButton = document.querySelector('.btn-group').children[1];
//const priceInner = document.querySelector('#price')


cleanButton.addEventListener('click', event => {
checkboxes.forEach(function(check) {

     Array.from(checkboxes) // Convert checkboxes to an array to use filter and map.
      .filter(i => i.checked = false)

    //CLEANING PRICE ADDITIONS
        sumOfAdditions = 0;
     priceInner.innerText = parseFloat(sumOfAdditions).toFixed( 2 ); //Parse float
})


})




});




