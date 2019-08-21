function addRow() {
    var table = document.getElementById("table");
    var row = document.createElement("tr");
    var td1 = document.createElement("td");
    var td2 = document.createElement("td");
    var td3 = document.createElement("BUTTON");

    td1.innerHTML = document.getElementById("fname").value;
    td2.innerHTML  = document.getElementById("lname").value;
    td3.innerHTML = "Remove.";
    // td3.onClick = "removeRow()";

    row.appendChild(td1);
    row.appendChild(td2);
    row.appendChild(td3);

    table.children[0].appendChild(row);

    // Clear the fields
    document.getElementById("fname").value = "";
    document.getElementById("lname").value = "";
}

// function removeRow() {
//     var table = document.getElementById("table");

//     table.deleteRow(1);
// }

function removeAllRows() {
    var table = document.getElementById("table");

    while(table.rows.length > 1) {
        table.deleteRow(1);
    }
}

function removeEmptyRows() {
    var table = document.getElementById("table");

    for (var i = 1, row; row = table.rows[i]; i++) {
        var flag = true;

        for (var j = 0, col; col = row.cells[j]; j++) {
            if (col.innerHTML != "") {
                    flag = false;
            }
        }
        if (flag) {
            table.deleteRow(i);
            i = i - 1;
        }
    }
}

document.querySelector("#fname").addEventListener("keyup", event => {
    // Use `.key` instead.
    if(event.key == "Enter") {
        document.querySelector("#nameadd").click(); // Things you want to do.
        event.preventDefault(); // No need to `return false;`.
    }
});

document.querySelector("#lname").addEventListener("keyup", event => {
    // Use `.key` instead.
    if(event.key == "Enter") {
        document.querySelector("#nameadd").click(); // Things you want to do.
        event.preventDefault(); // No need to `return false;`.
    }
});