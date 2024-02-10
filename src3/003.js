myArray = [1, 2, 3]

function doubleMyArray(my_array){
    for (let i = 0; i < my_array.length; i++) {
        my_array[i] *= 2
    }
    return my_array
}

console.log(myArray)
console.log(doubleMyArray(myArray))
console.log(myArray)