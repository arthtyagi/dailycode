'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    const vowels = 'aeiou';
    s = s.split("")

    s.map((i) => {
         if (vowels.indexOf(i) > -1) {
               console.log(i);
         }
         return i;
    }); 

    s.map((i)=> {
        if (vowels.indexOf(i)<0)
        {
            console.log(i);
    }
    return i;
    });
    
    
}

