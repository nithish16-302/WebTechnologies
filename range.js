/* exported range */
/* eslint-env browser */
/* eslint no-console:0 */
function range(l,h){
    var arr =new Array();
    var i,j;
    for(i=l,j=0;i<=h;i++,j++){
        arr[j]=i;
    }
    return arr;
}