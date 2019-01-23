/* exported move */
/* eslint-env browser */
/* eslint no-console:0 */
function move(arr,l,h){
    var temp =arr[l];
    arr[l] = arr[h];
    arr[h] = temp;
    return arr;
}
