/**
 * Created by wangqianjin on 2017/2/17.
 */
function main() {
    var canvas = document.getElementById("example");
    if(!canvas){
        console.log('Faliled to retrieve the <canvas> element');
        return false;
    }

    // Get the renderging context for 2DCG
    var ctx=canvas.getContext('2d');
    //Draw a blue rectangle
    ctx.fillStyle='rgba(0,0,255,1.0)';// set a blue color
    ctx.fillRect(120,10,150,150);//Fill a rectangle with the color
}




































