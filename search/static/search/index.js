function showTable(checkConcentrated) {
    document.querySelectorAll('table').forEach (table => {
        table.style.display = 'none';
    
    })

    if (checkConcentrated) {
        document.querySelector("#concentrated").style.display = "inline-block"
    }else{
        document.querySelector("#detailed").style.display = "inline-block"
    }
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("checkConcentrated").checked = false;
    document.querySelector("#checkConcentrated").onchange = function() {
        let checkConcentrated = document.getElementById("checkConcentrated");
        if (checkConcentrated.checked == true) {
            showTable(true)
        }else{
            showTable(false)
        }
}
 })


