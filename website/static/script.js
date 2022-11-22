var clicked = false;
function toggle() {
    if ((document.getElementById("Input").innerHTML = "Ilokano"))
        if (!clicked) {
        clicked = true;
        document.getElementById("Input").innerHTML = "Tagalog";
        } else {
        clicked = false;
        document.getElementById("Input").innerHTML = "Ilokano";
        }
    if ((document.getElementById("Input").innerHTML = "Tagalog")) {
        if (!clicked) {
        clicked = true;
        document.getElementById("Input").innerHTML = "Ilokano";
        } else {
        clicked = false;
        document.getElementById("Input").innerHTML = "Tagalog";
        }
    }

    if ((document.getElementById("Output").innerHTML = "Tagalog"))
        if (!clicked) {
        clicked = true;
        document.getElementById("Output").innerHTML = "Ilokano";
        } else {
        clicked = false;
        document.getElementById("Output").innerHTML = "Tagalog";
        }
    else if ((document.getElementById("Output").innerHTML = "Ilokano")) {
        if (!clicked) {
        clicked = true;
        document.getElementById("Output").innerHTML = "Tagalog";
        } else {
        clicked = false;
        document.getElementById("Output").innerHTML = "Ilokano";
        }
    }
}