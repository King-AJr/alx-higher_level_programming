#!/usr/bin/node

exports.esrever = function(list) {
    let length = list.length;
    const array = [];
    let j = 0;

    for (let i = length - 1; i >= 0; i--) {
        array[j] = list[i];
        j++
    }

    return array;
}