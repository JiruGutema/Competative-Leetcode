/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    i = 0
    for (el in obj){
        i += 1
    }
    return !Boolean(i)
};