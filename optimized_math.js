for (let i=1; i<=100; i++) {

    if (!(i%2)) {
        console.log(`The number '${i}' is ${!(i%3) ? 'divisible by 6' : 'even'}`);
    } else {
        console.log(`The number '${i}' is ${!(i%3) ? 'divisible by 3' : 'odd'}`);
    }

}